# Ingest recovery (when download / frames fail)

**Load when:** pipeline step 2 (ingest) hits errors, incomplete files, or partial success.  
**Goal:** never ship confident NOTES as if evidence were complete when it was not.

---

## Evidence levels (record in metadata or done message)

| Level | Meaning | Package OK to finish? |
|-------|---------|------------------------|
| **E3** | Timed captions + usable video frames/composites | Yes — full pipeline |
| **E2** | Timed captions only (no video / no frames) | Yes with honesty — ASCII-only boards; note gaps |
| **E1** | Partial captions or heavy ASR garbage | Partial — mine carefully; lower confidence |
| **E0** | No captions and no transcript source | **Stop** — do not invent a lecture |

Set optional metadata:

```json
"ingest_evidence": "E3"
```

Values: `E3` | `E2` | `E1` | `E0`.

---

## Failure modes and recovery

### Captions / subtitles fail

1. Retry: `yt-dlp` auto-subs (`--write-auto-sub --sub-lang en`).  
2. If only VTT exists, rebuild timed text (ingest script or manual parse).  
3. If still none → **E0**: report to user; do not fabricate TRANSCRIPT from memory.

### Video download fails (HTTP 403, format missing, etc.)

1. Retry with progressive formats (e.g. format `18` / `mp4` 360p) — no merge needed.  
2. Prefer `python -m yt_dlp` over bare `yt-dlp` when path issues appear.  
3. On Windows PowerShell: do **not** use bash `&&`; use `;` or separate commands.  
4. If video still fails but captions exist → continue as **E2** (frames-only later if video appears).

### ffmpeg missing / merge fails

1. Prefer single-file progressive download (no separate audio+video merge).  
2. Frames: may still work with pure video mp4 via OpenCV without ffmpeg merge.  
3. Document in done message: “no ffmpeg; used progressive format.”

### Frames / composites fail

1. Re-run: `ingest_youtube.py … --frames-only` when `raw/lecture.*` exists.  
2. If no video file → **E2**: Board slots use ASCII-only + “no content frame”.  
3. Do not fake screenshot paths.

### yt-dlp exit code 1 after partial success

1. Check what files actually landed (`raw/captions*`, `TRANSCRIPT.md`, `raw/lecture.*`).  
2. Partial success is OK if evidence level is set honestly.  
3. Re-run only the missing step (captions vs video vs frames).

---

## Done-message honesty

Always state:

- Captions: yes/no  
- Video file: yes/no  
- Frames/composites: yes/no  
- `ingest_evidence`: E3/E2/E1/E0  

Lower confidence when not E3. Never claim “full multi-frame boards” without composites on disk.

---

## Anti-patterns

| Smell | Fix |
|-------|-----|
| Inventing transcript from model memory | Stop; get captions or abort |
| NOTES with screenshot paths that do not exist | ASCII-only or re-extract frames |
| Silent continue after 403 as if video worked | Mark E2 and say so |
| Treating WARN-free validate as proof of ingest quality | Validate does not fully audit media files |
