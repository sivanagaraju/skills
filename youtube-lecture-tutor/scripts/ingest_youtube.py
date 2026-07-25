#!/usr/bin/env python3
"""
Ingest a YouTube lecture into a per-video study folder (no Vertex).

Creates:
  <out>/
    raw/info.json, captions, optional video
    TRANSCRIPT.md
    metadata.json
    screenshots/   (if video + opencv available)

Usage:
  python ingest_youtube.py --url "https://www.youtube.com/watch?v=..." \\
      --out "path/to/04-Lec01-slug" --playlist-index 4

Requires: pip install yt-dlp
Optional: opencv-python for frames; ffmpeg for merge (not required for captions)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.check_call(cmd)


def parse_vtt_to_paragraphs(vtt_path: Path, gap_sec: float = 25.0) -> list[tuple[float, str]]:
    """Deduplicate rolling YouTube auto-captions into timed paragraphs."""
    text = vtt_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    time_re = re.compile(r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})\s*-->")
    tag_re = re.compile(r"<[^>]+>")

    def to_sec(h, m, s, ms):
        return h * 3600 + m * 60 + s + ms / 1000.0

    def new_words(prev: str, curr: str) -> str:
        if not prev:
            return curr
        if curr.startswith(prev):
            return curr[len(prev) :].strip()
        pw, cw = prev.split(), curr.split()
        for k in range(min(len(pw), len(cw)), 0, -1):
            if pw[-k:] == cw[:k]:
                return " ".join(cw[k:])
        if curr in prev:
            return ""
        return curr

    cues: list[tuple[float, str]] = []
    i = 0
    while i < len(lines):
        m = time_re.search(lines[i])
        if m:
            start = to_sec(*map(int, m.groups()))
            i += 1
            parts = []
            while i < len(lines) and lines[i].strip() and "-->" not in lines[i]:
                t = tag_re.sub("", lines[i]).replace("&nbsp;", " ").strip()
                t = re.sub(r"<\d{2}:\d{2}:\d{2}\.\d{3}>", "", t)
                if t:
                    parts.append(t)
                i += 1
            blob = re.sub(r"\s+", " ", " ".join(parts)).strip()
            if blob:
                cues.append((start, blob))
        else:
            i += 1

    stream: list[tuple[float, str]] = []
    prev = ""
    for start, full in cues:
        nw = new_words(prev, full)
        if nw:
            stream.append((start, nw))
        prev = full

    paras: list[tuple[float, str]] = []
    buf: list[str] = []
    buf_start: float | None = None
    for start, words in stream:
        if buf_start is None:
            buf_start = start
        buf.append(words)
        if start - buf_start >= gap_sec:
            para = re.sub(r"\s+", " ", " ".join(buf)).strip()
            if para:
                paras.append((buf_start, para))
            buf, buf_start = [], None
    if buf and buf_start is not None:
        para = re.sub(r"\s+", " ", " ".join(buf)).strip()
        if para:
            paras.append((buf_start, para))
    return paras


def write_transcript(out: Path, meta: dict, paras: list[tuple[float, str]]) -> None:
    lines = [
        f"# Transcript — {meta.get('title', 'Lecture')}",
        "",
        f"> **Source:** {meta.get('url', '')}  ",
        f"> **Channel:** {meta.get('channel', '')}  ",
        f"> **Duration:** ~{int((meta.get('duration_seconds') or 0) / 60)} min  ",
        "> **Note:** Auto-captions cleaned lightly. Minor ASR errors possible.",
        "",
        "---",
        "",
    ]
    for start, para in paras:
        mm, ss = int(start // 60), int(start % 60)
        lines.append(f"**[{mm:02d}:{ss:02d}]** {para}")
        lines.append("")
    (out / "TRANSCRIPT.md").write_text("\n".join(lines), encoding="utf-8")


def slugify_title(title: str) -> str:
    s = re.sub(r"[^\w\-]+", "-", (title or "ch").lower()).strip("-")
    return (s or "ch")[:48]


# Synthetic segment length when YouTube has no chapters (seconds).
# ~6 min slices → ~1 composite each; stops the "one full-video panel reused on every topic" failure.
SYNTHETIC_SEGMENT_SEC = 360.0  # 6 minutes


def _range_from_dict(ch: dict, default_end: float, index: int) -> tuple[float, float, str]:
    start = float(ch.get("start_time") if ch.get("start_time") is not None else ch.get("start") or 0)
    end_raw = ch.get("end_time") if ch.get("end_time") is not None else ch.get("end")
    end = float(end_raw) if end_raw is not None else default_end
    title = str(ch.get("title") or ch.get("slug") or f"seg{index:02d}")
    return (start, max(end, start + 1.0), slugify_title(title))


def synthetic_ranges(duration: float) -> list[tuple[float, float, str]]:
    """
    When the video has no chapters, slice time into ~6 min windows.
    Each window gets one 2×2 composite (4 frames). A 48-min lecture → ~8 panels
    instead of a single "full" range capped at 3 panels.
    """
    if duration <= 0:
        return [(0.0, 1.0, "full")]
    if duration <= SYNTHETIC_SEGMENT_SEC * 1.25:
        # Short video: one range is fine; still denser frame count via frames_per_chapter
        return [(0.0, duration, "full")]
    ranges: list[tuple[float, float, str]] = []
    t = 0.0
    i = 1
    while t < duration - 0.5:
        end = min(t + SYNTHETIC_SEGMENT_SEC, duration)
        # Absorb a tiny leftover tail into the last segment
        if duration - end < 120.0 and end < duration:
            end = duration
        ranges.append((t, end, f"seg{i:02d}"))
        t = end
        i += 1
        if end >= duration:
            break
    return ranges


def chapter_ranges(
    chapters: list[dict] | None,
    duration: float,
    *,
    source_label: str | None = None,
) -> tuple[list[tuple[float, float, str]], str]:
    """
    Return ((start, end, slug), …) and a source tag:
      topic-ranges | youtube-chapters | description | synthetic
    Priority: caller-supplied topic/chapter list > synthetic time slices.
    Never collapse a long video to a single "full" range (that starves NOTES of panels).
    """
    if chapters:
        sorted_ch = sorted(
            chapters, key=lambda c: float(c.get("start_time") or c.get("start") or 0)
        )
        ranges: list[tuple[float, float, str]] = []
        for i, ch in enumerate(sorted_ch):
            if ch.get("end_time") is not None or ch.get("end") is not None:
                start, end, slug = _range_from_dict(ch, duration, i + 1)
            else:
                start = float(ch.get("start_time") or ch.get("start") or 0)
                end = (
                    float(sorted_ch[i + 1].get("start_time") or sorted_ch[i + 1].get("start") or duration)
                    if i + 1 < len(sorted_ch)
                    else duration
                )
                slug = slugify_title(str(ch.get("title") or ch.get("slug") or f"ch{i+1}"))
                start, end, slug = start, max(end, start + 1.0), slug
            ranges.append((start, end, slug))
        return ranges, (source_label or "chapters")
    return synthetic_ranges(duration), "synthetic"


def load_frame_range_sources(out: Path, chapters: list[dict] | None) -> tuple[list[dict] | None, str]:
    """
    Prefer agent-written topic time map for frame extraction.
      raw/topic-ranges.json  — after topic planning (best: one panel band per topic)
      chapters / description — YouTube chapters
      else synthetic slices
    topic-ranges.json items: {start_time|start, end_time|end?, title|slug}
    """
    topic_path = out / "raw" / "topic-ranges.json"
    if topic_path.exists():
        try:
            data = json.loads(topic_path.read_text(encoding="utf-8"))
            if isinstance(data, list) and data:
                print(f"frame ranges: using raw/topic-ranges.json ({len(data)} slices)")
                return data, "topic-ranges"
            if isinstance(data, dict) and data.get("ranges"):
                ranges = data["ranges"]
                print(f"frame ranges: using raw/topic-ranges.json ({len(ranges)} slices)")
                return ranges, "topic-ranges"
        except (json.JSONDecodeError, OSError) as e:
            print(f"WARNING: could not read topic-ranges.json: {e}")
    if chapters:
        return chapters, "youtube-chapters"
    return None, "synthetic"


def frames_per_chapter(dur_sec: float, *, range_source: str = "chapters") -> int:
    """
    How many raw frames to capture inside one range.
    Short: 4 (→ 1 composite of 4)
    Medium: 8 (→ 2 composites)
    Long: 12 (→ 3 composites)

    Synthetic ~6 min slices: always 4 frames → 1 panel (density comes from many slices).
    Topic-range slices: 4 if short, 8 if topic ≥8 min (long topics may get 2 panels).
    """
    if range_source == "synthetic":
        return 4
    mins = dur_sec / 60.0
    if range_source == "topic-ranges":
        if mins < 8:
            return 4
        if mins < 18:
            return 8
        return 12
    if mins < 5:
        return 4
    if mins < 15:
        return 8
    return 12


def sample_times_in_range(start: float, end: float, n: int) -> list[float]:
    """Even samples inside (start, end), inset 8% from edges so slides are up."""
    span = max(end - start, 1.0)
    lo = start + 0.08 * span
    hi = end - 0.08 * span
    if hi <= lo:
        return [start + span * 0.5]
    if n == 1:
        return [(lo + hi) / 2]
    return [lo + (hi - lo) * i / (n - 1) for i in range(n)]


def make_composite_2x2(
    image_paths: list[Path],
    out_path: Path,
    labels: list[str] | None = None,
    cell_w: int = 640,
    cell_h: int = 360,
) -> bool:
    """Combine up to 4 images into one 2x2 grid with optional time labels."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow not installed; skip composites (pip install pillow)")
        return False
    if not image_paths:
        return False
    paths = image_paths[:4]
    while len(paths) < 4:
        paths.append(paths[-1])  # pad by repeating last if odd count
    tiles = []
    for i, p in enumerate(paths):
        im = Image.open(p).convert("RGB")
        im = im.resize((cell_w, cell_h), Image.Resampling.LANCZOS)
        draw = ImageDraw.Draw(im)
        label = (labels[i] if labels and i < len(labels) else p.stem)[:48]
        # dark bar + text for readability
        draw.rectangle([0, cell_h - 28, cell_w, cell_h], fill=(0, 0, 0))
        try:
            font = ImageFont.load_default()
        except Exception:
            font = None
        draw.text((8, cell_h - 22), label, fill=(255, 255, 255), font=font)
        tiles.append(im)
    canvas = Image.new("RGB", (cell_w * 2, cell_h * 2), (20, 20, 20))
    canvas.paste(tiles[0], (0, 0))
    canvas.paste(tiles[1], (cell_w, 0))
    canvas.paste(tiles[2], (0, cell_h))
    canvas.paste(tiles[3], (cell_w, cell_h))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path, quality=90)
    return True


def _clear_shot_dirs(raw_dir: Path, comp_dir: Path, shots: Path) -> None:
    """Remove previous tiles/composites so re-extract does not leave stale panels."""
    for d in (raw_dir, comp_dir):
        if d.is_dir():
            for p in d.glob("*.png"):
                try:
                    p.unlink()
                except OSError:
                    pass
        d.mkdir(parents=True, exist_ok=True)
    # top-level convenience aliases of composites
    for p in shots.glob("*.png"):
        try:
            p.unlink()
        except OSError:
            pass


def extract_frames(
    video: Path,
    shots: Path,
    duration: float,
    count: int | None = None,
    chapters: list[dict] | None = None,
    range_source: str = "chapters",
) -> None:
    """
    Capture MANY frames per time range, then build 2x2 composite images for NOTES.

    Policy:
      - Prefer raw/topic-ranges.json (topic map) when present
      - Else YouTube chapters / description timestamps
      - Else synthetic ~6 min slices (never one "full" range for a long lecture)
      - Each range: 4 / 8 / 12 raw frames by length → 1 / 2 / 3 composites of 4
      - Raw tiles: screenshots/raw/…
      - Composites: screenshots/composites/chXX-slug-panelN.png
      - Re-extract wipes prior pngs so NOTES assignment is not mixed with stale panels
    """
    try:
        import cv2  # type: ignore
    except ImportError:
        print("opencv not installed; skip frames (pip install opencv-python)")
        return

    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        print("could not open video for frames")
        return
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    shots.mkdir(parents=True, exist_ok=True)
    raw_dir = shots / "raw"
    comp_dir = shots / "composites"
    _clear_shot_dirs(raw_dir, comp_dir, shots)

    ranges, src = chapter_ranges(chapters, duration, source_label=range_source)
    range_source = src
    # optional global cap via --frame-count (total raw tiles approx)
    global_cap = count

    all_raw: list[dict] = []
    all_composites: list[dict] = []
    raw_index = 0

    print(
        f"frame plan: ranges={len(ranges)} source={range_source} "
        f"duration={duration:.0f}s (multi-frame + 2x2 composites)"
    )

    for ci, (start, end, slug) in enumerate(ranges, 1):
        ch_dur = end - start
        n = frames_per_chapter(ch_dur, range_source=range_source)
        if global_cap is not None:
            # scale per-range share roughly by duration
            share = max(4, int(round(global_cap * (ch_dur / max(duration, 1.0)))))
            n = min(n, max(4, share - (share % 4) or 4))
            n = min(12, max(4, n))
        times = sample_times_in_range(start, end, n)
        chapter_paths: list[Path] = []
        chapter_labels: list[str] = []
        tile_seconds: list[float] = []
        for sec in times:
            sec = max(0.0, min(float(sec), max(duration - 1.0, 0.0)))
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(sec * fps))
            ok, frame = cap.read()
            if not ok:
                print(f"frame skip t={sec:.0f}s")
                continue
            raw_index += 1
            mm, ss = int(sec // 60), int(sec % 60)
            fname = f"{raw_index:03d}-ch{ci:02d}-{slug}-t{int(sec):04d}s.png"
            path = raw_dir / fname
            cv2.imwrite(str(path), frame)
            chapter_paths.append(path)
            chapter_labels.append(f"ch{ci} {mm:02d}:{ss:02d}")
            tile_seconds.append(round(sec, 1))
            all_raw.append(
                {
                    "file": f"raw/{fname}",
                    "seconds": round(sec, 1),
                    "chapter": ci,
                    "slug": slug,
                    "label": f"{mm:02d}:{ss:02d}",
                    "range_start": round(start, 1),
                    "range_end": round(end, 1),
                }
            )
            print("raw", fname)

        # group into composites of 4
        for panel_i in range(0, len(chapter_paths), 4):
            chunk = chapter_paths[panel_i : panel_i + 4]
            labs = chapter_labels[panel_i : panel_i + 4]
            secs = tile_seconds[panel_i : panel_i + 4]
            if not chunk:
                continue
            panel_n = panel_i // 4 + 1
            n_panels = (len(chapter_paths) + 3) // 4
            comp_name = f"ch{ci:02d}-{slug}-panel{panel_n}of{n_panels}.png"
            comp_path = comp_dir / comp_name
            if make_composite_2x2(chunk, comp_path, labs):
                t0 = secs[0] if secs else start
                t1 = secs[-1] if secs else end
                all_composites.append(
                    {
                        "file": f"composites/{comp_name}",
                        "chapter": ci,
                        "slug": slug,
                        "panel": panel_n,
                        "panels_in_chapter": n_panels,
                        "tiles": [p.name for p in chunk],
                        "labels": labs,
                        "tile_seconds": secs,
                        "time_start": t0,
                        "time_end": t1,
                        "range_start": round(start, 1),
                        "range_end": round(end, 1),
                    }
                )
                print("composite", comp_name)

    cap.release()

    # also keep top-level convenience copies of composites for simple embeds
    for c in all_composites:
        src_path = shots / c["file"]
        if src_path.exists():
            alias = shots / Path(c["file"]).name
            try:
                alias.write_bytes(src_path.read_bytes())
            except OSError:
                pass

    manifest = {
        "duration_seconds": duration,
        "range_source": range_source,
        "range_count": len(ranges),
        "policy": (
            "per-range multi-frame → 2x2 composites; "
            "prefer topic-ranges.json; else chapters; else synthetic ~6min slices"
        ),
        "frames_per_range_rule": {
            "synthetic": "4 frames (1 panel) per ~6min slice",
            "topic-ranges": "4 / 8 / 12 by topic length",
            "chapters": "<5min:4 · 5-15min:8 · >=15min:12",
            "composites": "ceil(frames/4) panels per range",
        },
        "ranges": [
            {"index": i, "start": s, "end": e, "slug": slug}
            for i, (s, e, slug) in enumerate(ranges, 1)
        ],
        "raw_count": len(all_raw),
        "composite_count": len(all_composites),
        "raw": all_raw,
        "composites": all_composites,
        "notes_embed_hint": (
            "Assign each composite to ONE topic whose MM:SS overlaps "
            "time_start–time_end (or range_start–range_end). "
            "Never reuse the same composite path on multiple topics. "
            "If composite_count < topic_count, write raw/topic-ranges.json and re-run --frames-only."
        ),
    }
    (shots / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(
        f"done frames: raw={len(all_raw)} composites={len(all_composites)} "
        f"source={range_source} → see screenshots/manifest.json"
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--url",
        default="",
        help="YouTube URL (required unless --frames-only)",
    )
    ap.add_argument("--out", required=True, help="Video package folder")
    ap.add_argument("--playlist-index", type=int, default=None)
    ap.add_argument("--download-video", action="store_true", help="Also download video for frames")
    ap.add_argument("--no-frames", action="store_true")
    ap.add_argument(
        "--frame-count",
        type=int,
        default=None,
        help="Optional soft cap on total raw tiles (default: per-range policy)",
    )
    ap.add_argument(
        "--frames-only",
        action="store_true",
        help="Only (re)extract frames/composites from existing raw/lecture.*; skip yt-dlp download. "
        "Uses raw/topic-ranges.json if present, else chapters, else synthetic ~6min slices.",
    )
    args = ap.parse_args()

    out = Path(args.out)
    raw = out / "raw"
    shots = out / "screenshots"
    raw.mkdir(parents=True, exist_ok=True)

    # Always target a single video (playlist URLs otherwise poison metadata/captions).
    video_url = (args.url or "").split("&")[0] if args.url and "watch?v=" in args.url else (args.url or "")

    chapters: list[dict] = []
    meta: dict = {}

    if args.frames_only:
        # Reuse local metadata / chapters / video; prefer topic-ranges.json when present
        meta_path = out / "metadata.json"
        if meta_path.exists():
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        ch_path = raw / "chapters.json"
        if ch_path.exists():
            chapters = json.loads(ch_path.read_text(encoding="utf-8"))
        info_path = raw / "info.json"
        if not chapters and info_path.exists():
            try:
                info = json.loads(info_path.read_text(encoding="utf-8"))
                chapters = info.get("chapters") or []
            except json.JSONDecodeError:
                pass
        duration = float(meta.get("duration_seconds") or 0)
        if not duration and info_path.exists():
            try:
                info = json.loads(info_path.read_text(encoding="utf-8"))
                duration = float(info.get("duration") or 0)
            except json.JSONDecodeError:
                duration = 0
        vids = (
            list(raw.glob("lecture*.mp4"))
            + list(raw.glob("lecture*.webm"))
            + list(raw.glob("lecture*.mkv"))
        )
        if not vids or not duration:
            raise SystemExit(
                "--frames-only needs raw/lecture.* and duration in metadata.json/info.json"
            )
        if not args.no_frames:
            range_list, range_src = load_frame_range_sources(out, chapters if chapters else None)
            extract_frames(
                vids[0],
                shots,
                duration,
                count=args.frame_count,
                chapters=range_list,
                range_source=range_src,
            )
        print("done frames-only:", out)
        return

    if not args.url:
        raise SystemExit("--url is required unless --frames-only")

    # metadata JSON
    info_path = raw / "info.json"
    run(
        [
            sys.executable,
            "-m",
            "yt_dlp",
            "-J",
            "--skip-download",
            "--no-playlist",
            video_url,
        ]
    )
    # yt-dlp -J prints to stdout — re-run capture
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "yt_dlp",
            "-J",
            "--skip-download",
            "--no-update",
            "--no-playlist",
            video_url,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0:
        print(proc.stderr)
        raise SystemExit("yt-dlp metadata failed")
    data = json.loads(proc.stdout[proc.stdout.find("{") :])
    # Keep full metadata on disk (truncated info broke chapter recovery earlier)
    info_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    chapters = data.get("chapters") or []
    if not chapters:
        # Fallback: parse "HH:MM:SS Title" lines from description (common on long courses)
        desc = data.get("description") or ""
        for m in re.finditer(
            r"(?m)^(\d{1,2}):(\d{2}):(\d{2})\s+(.+)$", desc
        ):
            h, mi, s, title = m.groups()
            chapters.append(
                {
                    "start_time": int(h) * 3600 + int(mi) * 60 + int(s),
                    "title": title.strip(),
                }
            )
        if chapters:
            print(f"chapters: parsed {len(chapters)} from description timestamps")
    meta = {
        "title": data.get("title"),
        "video_id": data.get("id"),
        "url": video_url,
        "duration_seconds": data.get("duration"),
        "channel": data.get("channel") or data.get("uploader"),
        "description": (data.get("description") or "")[:800],
        "playlist_index": args.playlist_index,
        "chapter_count": len(chapters) if chapters else 0,
    }
    (out / "metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    if chapters:
        (raw / "chapters.json").write_text(
            json.dumps(chapters, indent=2), encoding="utf-8"
        )
        print(f"chapters: {len(chapters)} (multi-frame + composites per chapter)")

    # captions
    cap_base = raw / "captions"
    run(
        [
            sys.executable,
            "-m",
            "yt_dlp",
            "--write-auto-sub",
            "--sub-lang",
            "en",
            "--sub-format",
            "vtt",
            "--skip-download",
            "--no-update",
            "--no-playlist",
            "-o",
            str(cap_base),
            video_url,
        ]
    )
    vtts = list(raw.glob("captions*.vtt")) + list(raw.glob("*.en.vtt"))
    if not vtts:
        print("WARNING: no captions found")
    else:
        paras = parse_vtt_to_paragraphs(vtts[0])
        timed = "\n\n".join(
            f"[{int(s//60):02d}:{int(s%60):02d}] {p}" for s, p in paras
        )
        (raw / "captions.en.timed.txt").write_text(timed, encoding="utf-8")
        write_transcript(out, meta, paras)
        print("transcript paragraphs", len(paras))

    if args.download_video:
        run(
            [
                sys.executable,
                "-m",
                "yt_dlp",
                "-f",
                "bv*[height<=720]/b[height<=720]/b",
                "--no-update",
                "--no-playlist",
                "-o",
                str(raw / "lecture.%(ext)s"),
                video_url,
            ]
        )
        vids = list(raw.glob("lecture*.mp4")) + list(raw.glob("lecture*.webm")) + list(raw.glob("lecture*.mkv"))
        if vids and not args.no_frames and meta.get("duration_seconds"):
            range_list, range_src = load_frame_range_sources(
                out, chapters if chapters else None
            )
            extract_frames(
                vids[0],
                shots,
                float(meta["duration_seconds"]),
                count=args.frame_count,
                chapters=range_list,
                range_source=range_src,
            )

    print("done:", out)
    print("next: write PREREQUISITES.md, NOTES.md, quiz questions → generate_quiz.py")


if __name__ == "__main__":
    main()
