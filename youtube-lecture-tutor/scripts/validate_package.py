#!/usr/bin/env python3
"""
validate_package.py — automated quality gate for a youtube-lecture-tutor
package (PREREQUISITES.md, NOTES.md, quiz raw/questions.json, metadata.json).

Modeled on gemini_youtube_analyzer_v6_0.py's evaluate_blog_completeness():
regex/structural checks, not semantic grading.

Also soft-checks claim-mining artifacts (raw/claims/, coverage-checklist.md)
per transcript-mining.md — completeness gate for new packages.

  ERROR = hard spec violation → exit 1
  WARN  = advisory (human look) → exit 0, or exit 1 with --strict

Usage:
  python validate_package.py --dir path/to/NN-slug
  python validate_package.py --dir path/to/NN-slug --strict
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ALLOWED_CONTENT_TYPES = {
    "math_technical",
    "code_tutorial",
    "tool_product",
    "theory_concept",
    "research_review",
    "soft_skills",
    "mixed",
}
SCENARIOS_REQUIRED_FOR = {
    "code_tutorial",
    "tool_product",
    "research_review",
    "soft_skills",
}

# Technique labels only — NOT casual English like "toys" / "toy problem" in prose.
# Prefer multi-word / heading-style patterns so we don't false-fail lecture English.
FORBIDDEN_LABEL_PATTERNS = [
    r"\bELI5\b",
    r"\bFeynman\b",
    r"\bApproach\s*[1-5]\b",
    r"^###\s*Toy\b",
    r"\bToy\s*·",
    r"·\s*Toy\b",
    r"Prereq\s+P\d+\s*·\s*Toy",
    r'"tag"\s*:\s*"[^"]*\bToy\b',
    r"\bthe toy for this\b",
    r"\bthe toy before\b",
    r"\bELI5\s*/\s*Feynman\b",
]

# Soft AI-slop (WARN). Prefer multi-word stock phrases; single words are high false-positive.
AI_SLOP_PHRASES = [
    "delve",
    "tapestry",
    "in this section we will",
    "it's important to note",
    "it is important to note",
    "comprehensive overview",
    "unlock the power",
    "dive deep into",
    "without further ado",
    "in today's world",
]
# Single words: warn only when used as filler near meta prose (still soft).
AI_SLOP_WORDS_SOFT = ["pivotal", "robust landscape", "ever-evolving"]

BANNED_MERMAID = [
    "block-beta",
    "sankey-beta",
    "xychart-beta",
    "requirementDiagram",
    "C4Context",
    "C4Container",
    "C4Deployment",
    "C4Dynamic",
    "architecture",
]
SAFE_MERMAID_HEAD = re.compile(
    r"^\s*(graph\s+(TD|LR)|flowchart\s+(TD|LR)|sequenceDiagram|classDiagram|"
    r"stateDiagram-v2|erDiagram|pie|mindmap|journey|timeline|gitGraph|quadrantChart)",
    re.MULTILINE | re.IGNORECASE,
)
TOPIC_SLOTS = [
    "Where this sits on the master map",
    "Board / screenshot",
    "What he is establishing",
    "Analogy for this topic only",
    "Local picture",
    "Bridge",
]
OWNERSHIP_STAMP_RE = re.compile(
    r"\*\*(?:wrong move|right move|you can now|still missing):\*\*", re.IGNORECASE
)
TIMESTAMP_RE = re.compile(
    r"\((\d{1,2}):(\d{2})\s*[–-]\s*(\d{1,2}):(\d{2})\)"
)
WORD_RE = re.compile(r"\b[\w']+\b", re.UNICODE)
BOX_CHARS = "┌┐└┘│─▼═╔╗╚╝║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬"


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warns: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warns.append(msg)

    def dump(self, strict: bool) -> int:
        print(f"\n{'=' * 60}\nvalidate_package.py report\n{'=' * 60}")
        if self.errors:
            print(f"\nERRORS ({len(self.errors)}) — fix before shipping:")
            for e in self.errors:
                print(f"  ✗ {e}")
        if self.warns:
            print(f"\nWARNINGS ({len(self.warns)}) — advisory, human judgment call:")
            for w in self.warns:
                print(f"  ! {w}")
        if not self.errors and not self.warns:
            print("\nAll automated checks passed. ✓")
        print()
        if self.errors:
            print("RESULT  FAIL")
            return 1
        if strict and self.warns:
            print("RESULT  FAIL (strict + warnings)")
            return 1
        if self.warns:
            print("RESULT  PASS WITH WARNINGS")
        else:
            print("RESULT  PASS")
        return 0


def word_count(text: str) -> int:
    return len(WORD_RE.findall(text))


def slugify(text: str) -> str:
    """Collapsed slug (spaces → single hyphens)."""
    text = text.strip()
    text = re.sub(r"^#+\s*", "", text)
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_]+", "-", text).strip("-")
    return text


def slugify_toc_style(text: str) -> str:
    """
    Match common VS Code / some GFM TOC generators:
    drop punctuation (and often non-ASCII symbols like Ω), then each space → '-'
    so 'ML = modeling' becomes 'ml--modeling'.
    """
    text = re.sub(r"^#+\s*", "", text.strip()).lower()
    # drop non-ascii letters that TOC often omits (Ω, arrows, …)
    text = re.sub(r"[^\x00-\x7f]", " ", text)
    text = re.sub(r"[^\w\s-]", "", text)  # ASCII word/space/hyphen only
    text = re.sub(r"\s", "-", text)  # do NOT collapse runs
    text = re.sub(r"-{3,}", "--", text)
    return text.strip("-")


def find_sections(text: str, heading_pattern: str) -> list[tuple[str, int, int]]:
    matches = list(re.finditer(heading_pattern, text, re.MULTILINE))
    out: list[tuple[str, int, int]] = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out.append((m.group().strip(), m.start(), end))
    return out


def collect_md_anchors(text: str) -> set[str]:
    """Explicit <a id>, same-file TOC fragments, and heading slug variants."""
    anchors = set(re.findall(r'<a id="([^"]+)"', text))
    # fragments already used in markdown links (TOC is source of truth for navigation)
    anchors.update(re.findall(r"\]\(#([^)]+)\)", text))
    for m in re.finditer(r"^(#{2,3})\s+(.+)$", text, re.MULTILINE):
        title = m.group(2)
        anchors.add(slugify(title))
        anchors.add(slugify_toc_style(title))
    return anchors


def scan_forbidden_labels(text: str, where: str, rep: Report) -> None:
    for pat in FORBIDDEN_LABEL_PATTERNS:
        for m in re.finditer(pat, text, re.MULTILINE | re.IGNORECASE):
            rep.err(
                f"{where}: forbidden technique-label '{m.group()}' "
                f"(no ELI5/Feynman/Toy-tag/Approach-N in student-facing text)"
            )


def scan_ai_slop(text: str, where: str, rep: Report) -> None:
    lower = text.lower()
    for phrase in AI_SLOP_PHRASES:
        if phrase in lower:
            rep.warn(
                f"{where}: possible AI-slop phrase '{phrase}' — rewrite if it is filler"
            )
    for phrase in AI_SLOP_WORDS_SOFT:
        if phrase in lower:
            rep.warn(f"{where}: soft AI-slop cue '{phrase}' — check tone")


def scan_meta_lines(text: str, where: str, rep: Report) -> None:
    if re.search(r"^\s*(\*\*)?content_type\s*:", text, re.MULTILINE | re.IGNORECASE):
        rep.err(
            f"{where}: 'content_type:' meta line found in student-facing text "
            f"(belongs only in metadata.json)"
        )


def scan_mermaid(text: str, where: str, rep: Report) -> int:
    blocks = re.findall(r"```mermaid\s*\n(.*?)```", text, re.DOTALL | re.IGNORECASE)
    for b in blocks:
        for banned in BANNED_MERMAID:
            if banned.lower() in b.lower():
                rep.err(
                    f"{where}: banned Mermaid type '{banned}' "
                    f"(breaks GitHub/VS Code preview)"
                )
        if "quadrantchart" in b.lower() and re.search(r'\[\s*"[^"]*"\s*,', b):
            rep.err(
                f"{where}: quadrantChart has quoted-string coordinates — use bare numbers"
            )
        if not SAFE_MERMAID_HEAD.search(b):
            rep.warn(
                f"{where}: Mermaid block doesn't start with a recognized safe type — verify"
            )
    return len(blocks)


def check_prerequisites(
    path: Path, rep: Report, metadata: dict | None = None
) -> set[str]:
    if not path.exists():
        rep.err("PREREQUISITES.md is missing")
        return set()
    text = path.read_text(encoding="utf-8", errors="replace")
    anchors = collect_md_anchors(text)

    idea_headings = re.findall(r"^## .+$", text, re.MULTILINE)
    n_ideas = len(idea_headings)
    meta = metadata or {}
    if meta.get("beginner_prereqs") is True:
        lo, hi = 3, 8
        band = "3–8 (beginner_prereqs: true)"
    else:
        lo, hi = 3, 6
        band = "3–6 (default; set beginner_prereqs: true for deeper warm-ups)"
    if n_ideas and not (lo <= n_ideas <= hi):
        rep.warn(
            f"PREREQUISITES.md: {n_ideas} idea sections found; guidance is {band}"
        )

    # Prefer explicit anchors for connect-the-dots
    explicit = set(re.findall(r'<a id="([^"]+)"', text))
    if n_ideas and len(explicit) < min(3, n_ideas):
        rep.warn(
            "PREREQUISITES.md: fewer than 3 explicit <a id=\"…\"> anchors — "
            "NOTES deep links need stable targets"
        )

    scan_forbidden_labels(text, "PREREQUISITES.md", rep)
    scan_ai_slop(text, "PREREQUISITES.md", rep)
    scan_meta_lines(text, "PREREQUISITES.md", rep)

    wc = word_count(text)
    if "full lecture" in text.lower() or wc > 2500:
        rep.warn(
            f"PREREQUISITES.md: long ({wc} words) — check it isn't a second lecture"
        )

    return anchors


def check_notes(
    path: Path,
    prereq_anchors: set[str],
    rep: Report,
    metadata: dict | None = None,
) -> tuple[int, set[str]]:
    if not path.exists():
        rep.err("NOTES.md is missing")
        return 0, set()
    text = path.read_text(encoding="utf-8", errors="replace")
    notes_anchors = collect_md_anchors(text)

    stamp_count = len(OWNERSHIP_STAMP_RE.findall(text))
    if stamp_count >= 2:
        rep.warn(
            f"NOTES.md: {stamp_count} bold ownership stamps found "
            "('Wrong move:' / 'You can now:' etc.) -- weave these ideas into prose"
        )

    # Warm-up banner
    head = text.split("## Table of Contents")[0] if "## Table of Contents" in text else text[:900]
    if "PREREQUISITES.md" not in head:
        rep.err(
            "NOTES.md: no link to PREREQUISITES.md near the top "
            "('warm-up first' banner missing)"
        )

    if "## Table of Contents" not in text:
        rep.err("NOTES.md: missing '## Table of Contents' heading")
    if "## Executive Summary" not in text and "## Executive summary" not in text:
        rep.err("NOTES.md: missing '## Executive Summary' heading")
    else:
        key = "## Executive Summary" if "## Executive Summary" in text else "## Executive summary"
        exec_start = text.index(key)
        first_topic = re.search(r"^## Topic \d+:", text, re.MULTILINE)
        exec_end = first_topic.start() if first_topic else len(text)
        exec_body = text[exec_start:exec_end]
        if not any(c in exec_body for c in BOX_CHARS):
            # also accept pure ASCII maps that use | and +
            if not re.search(r"```[\s\S]{40,}?```", exec_body):
                rep.err(
                    "NOTES.md: Executive Summary has no architecture diagram "
                    "(no box-drawing chars and no substantial fenced ASCII)"
                )
            else:
                rep.warn(
                    "NOTES.md: Executive Summary has a fenced block but no box-drawing "
                    "chars — OK if the map is clear ASCII"
                )

    topics = find_sections(text, r"^## Topic \d+:.*$")
    # stop topic body before global sections if last topic absorbs them
    cleaned: list[tuple[str, str]] = []
    for heading, start, end in topics:
        body = text[start:end]
        for stopper in (
            "\n## External references",
            "\n## Apply it",
            "\n## Sources",
        ):
            idx = body.find(stopper)
            if idx > 0:
                body = body[:idx]
        cleaned.append((heading, body))

    n_topics = len(cleaned)
    # Hard bounds only (topic-planning.md): map/claims drive count; duration is soft.
    hard_lo, hard_hi = 4, 10
    if not (hard_lo <= n_topics <= hard_hi):
        rep.err(
            f"NOTES.md: {n_topics} '## Topic N:' sections found; "
            f"absolute range is {hard_lo}–{hard_hi} "
            "(map boxes + claim clusters; topic-planning.md)"
        )
    else:
        print(f"OK  topics: {n_topics} (absolute {hard_lo}–{hard_hi})")

    # Soft duration guide — WARN only (dense short vs deep long lectures).
    duration_min = ((metadata or {}).get("duration_seconds") or 0) / 60
    if duration_min and hard_lo <= n_topics <= hard_hi:
        if duration_min < 25:
            soft_lo, soft_hi = 4, 8
            soft_band = "often 4–8 for ~15–25 min (more if dense; fewer if one arc)"
        elif duration_min <= 45:
            soft_lo, soft_hi = 6, 10
            soft_band = "often 6–10 for ~25–45 min"
        else:
            soft_lo, soft_hi = 7, 10
            soft_band = "often 7–10 for ~45–90 min (deepen, do not invent boxes)"
        if not (soft_lo <= n_topics <= soft_hi):
            rep.warn(
                f"NOTES.md: {n_topics} topics is outside soft duration guide "
                f"({soft_band}). Check density: split packed claims or merge "
                f"repetition (topic-planning.md) — not an automatic fail."
            )

    for heading, body in cleaned:
        missing_slots = [s for s in TOPIC_SLOTS if f"### {s}" not in body]
        if missing_slots:
            rep.err(
                f"NOTES.md '{heading[:55]}': missing subsection(s): "
                f"{', '.join(missing_slots)}"
            )

        slot_bodies: dict[str, str] = {}
        slot_matches = list(re.finditer(r"^### (.+)$", body, re.MULTILINE))
        for i, m in enumerate(slot_matches):
            s_end = slot_matches[i + 1].start() if i + 1 < len(slot_matches) else len(body)
            slot_bodies[m.group(1).strip()] = body[m.end() : s_end].strip()

        establishing = slot_bodies.get("What he is establishing", "")
        if establishing:
            lines = [ln for ln in establishing.splitlines() if ln.strip()]
            bullet_lines = [
                ln for ln in lines if re.match(r"^\s*([-*•]|\d+[.)])\s", ln)
            ]
            prose_lines = [
                ln
                for ln in lines
                if len(ln.split()) >= 12
                and not re.match(r"^\s*([-*•]|\d+[.)])\s", ln)
                and not ln.strip().startswith("```")
                and not ln.strip().startswith("|")
            ]
            if lines and len(bullet_lines) / max(len(lines), 1) >= 0.6 and not prose_lines:
                rep.err(
                    f"NOTES.md '{heading[:55]}': 'What he is establishing' looks "
                    f"bullet-only ({len(bullet_lines)}/{len(lines)} bullet lines, "
                    f"no prose) — continuous tutor prose required"
                )
            if word_count(establishing) < 80:
                rep.warn(
                    f"NOTES.md '{heading[:55]}': 'What he is establishing' is short "
                    f"({word_count(establishing)} words) — mini-lesson needs more than a recap stub"
                )
            # writing smell: long establishing with zero concrete cue (skip short intro frames)
            if word_count(establishing) >= 100 and not re.search(
                r"\b(for example|e\.g\.|spam|coin|die|image|email|tumor|dataset|"
                r"suppose|imagine|consider|say |like |GPT|Python|PyTorch|VAE|GAN|"
                r"diffusion|transformer|X-ray|pixel|token|planet|Kepler|ellipse|"
                r"parabola|radiologist|speech|digit|MNIST|Gaussian|Newton|"
                r"observe|observation|training|pair|vector|night|film|time t)\b",
                establishing,
                re.I,
            ):
                rep.warn(
                    f"NOTES.md '{heading[:55]}': establishing has little concrete "
                    f"example language — check writing-examples.md (scene → contrast)"
                )
            # video-dependent recap smell
            he_hits = len(
                re.findall(
                    r"\b(he (then |also |next |now )?(says|said|explains|writes|shows|notes|mentions|argues|stresses|flags)|"
                    r"the teacher (says|explains|writes)|on the board he|as (he |the lecture )discussed)\b",
                    establishing,
                    re.I,
                )
            )
            if he_hits >= 3 and word_count(establishing) < 200:
                rep.warn(
                    f"NOTES.md '{heading[:55]}': establishing sounds lecture-report "
                    f"('he says/explains…') — teach the idea for video-closed reading"
                )
            # ownership / still-missing cue for substantial topics
            if word_count(establishing) >= 120 and not re.search(
                r"\b(you can now|still missing|what is left|left open|not yet|"
                r"we now have|we still (need|lack)|ownership)\b",
                establishing,
                re.I,
            ):
                rep.warn(
                    f"NOTES.md '{heading[:55]}': establishing may lack ownership line "
                    f"('you can now…' / 'still missing…') — tutor-voice mini-lesson"
                )
            # wrong vs right / fail cue
            if word_count(establishing) >= 120 and not re.search(
                r"\b(wrong|fail|mistake|trap|instead|cannot|does not|don't|"
                r"not enough|not the goal|bad idea)\b",
                establishing,
                re.I,
            ):
                rep.warn(
                    f"NOTES.md '{heading[:55]}': establishing may lack wrong-vs-right "
                    f"contrast — common cause of 'I need the video to understand'"
                )

        bridge = slot_bodies.get("Bridge", "")
        if bridge:
            if word_count(bridge) < 8:
                rep.warn(
                    f"NOTES.md '{heading[:55]}': Bridge is very short "
                    f"('{bridge.strip()[:60]}') — see writing-examples.md Example B"
                )
            if re.match(
                r"^\s*(Bridge:\s*)?Next\s+(we\s+)?(discuss|cover|explore|topic|look)",
                bridge,
                re.IGNORECASE,
            ):
                rep.warn(
                    f"NOTES.md '{heading[:55]}': robot-bridge anti-pattern "
                    f"('Next we discuss…') — leave a real leftover problem"
                )

        map_slot = slot_bodies.get("Where this sits on the master map", "")
        if map_slot and word_count(map_slot) < 10:
            rep.warn(
                f"NOTES.md '{heading[:55]}': map slot is very short — likely a "
                f"one-line tag rename (writing-examples.md Example D)"
            )

        analogy = slot_bodies.get("Analogy for this topic only", "")
        if analogy:
            if word_count(analogy) < 40:
                rep.warn(
                    f"NOTES.md '{heading[:55]}': analogy is thin — need scene, "
                    f"instances, hard question, right vs wrong (tutor-voice Analogy writing)"
                )
            # table-as-default smell
            pipe_lines = [
                ln for ln in analogy.splitlines() if ln.strip().startswith("|")
            ]
            prose_lines = [
                ln
                for ln in analogy.splitlines()
                if ln.strip()
                and not ln.strip().startswith("|")
                and not re.match(r"^\s*\|?\s*-{2,}", ln)
                and len(ln.split()) >= 8
            ]
            if len(pipe_lines) >= 4 and len(prose_lines) == 0:
                rep.warn(
                    f"NOTES.md '{heading[:55]}': analogy is a mapping table only — "
                    f"use scene → instances → question → right/wrong → rename"
                )
            # abstract-fog smell (the pattern that confused real readers)
            if re.search(
                r"\b(rulebook|stand-in|logbook|useful estimate of the rule|"
                r"hidden rule is \$)\b",
                analogy,
                re.I,
            ):
                rep.warn(
                    f"NOTES.md '{heading[:55]}': analogy has abstract-fog wording "
                    f"(rulebook/stand-in/…) — use concrete instances instead"
                )
            # hard question / tension cue
            if not re.search(
                r"(\?|where is|what about|what if|can you|how do you|"
                r"someone asks|now ask)",
                analogy,
                re.I,
            ):
                rep.warn(
                    f"NOTES.md '{heading[:55]}': analogy may lack a hard question "
                    f"the reader cannot answer by memory alone"
                )
            # rename / formal cue somewhere (prefer end; soft check any)
            has_rename = re.search(
                r"(in lecture words|in the lecture|that is (the |our )?|"
                r"\b(f|D|model|class|sample space)\b|\$[A-Za-z\\])",
                analogy,
                re.I,
            )
            if word_count(analogy) >= 40 and not has_rename:
                rep.warn(
                    f"NOTES.md '{heading[:55]}': analogy never renames to a formal "
                    f"object — end with one short 'In lecture words: …' line"
                )
            # early math: first ~80 chars already full of $...$
            head = analogy.lstrip()[:100]
            if len(re.findall(r"\$[^$]+\$", head)) >= 2:
                rep.warn(
                    f"NOTES.md '{heading[:55]}': analogy opens with heavy math — "
                    f"keep symbols for the final rename line"
                )

        local = slot_bodies.get("Local picture", "")
        if local:
            if not re.search(r"(?i)notice\s*:", local):
                rep.warn(
                    f"NOTES.md '{heading[:55]}': Local picture missing "
                    f"'Notice: …' insight line (diagrams-and-mermaid.md)"
                )
            # thin diagram: fence exists but almost no structure chars / arrows
            fence = re.search(r"```[^\n]*\n(.*?)```", local, re.S)
            if fence:
                body_ascii = fence.group(1)
                if len(body_ascii.strip()) < 20:
                    rep.warn(
                        f"NOTES.md '{heading[:55]}': Local picture ASCII is tiny — "
                        f"show a relation, not a title (viz budget)"
                    )
                elif not re.search(r"[│┌└▼→←↔─═|/\\+vV<>]", body_ascii):
                    # allow plain multi-line tables of pairs without box art
                    if body_ascii.count("\n") < 2:
                        rep.warn(
                            f"NOTES.md '{heading[:55]}': Local picture looks like "
                            f"a one-line label — add before/after or micro numbers"
                        )

        # soft depth vs duration
        tm = TIMESTAMP_RE.search(heading)
        if tm:
            t0 = int(tm.group(1)) * 60 + int(tm.group(2))
            t1 = int(tm.group(3)) * 60 + int(tm.group(4))
            dur_min = max((t1 - t0) / 60.0, 0.5)
            w = word_count(body)
            min_words = int(40 * dur_min)
            if w < min_words:
                rep.warn(
                    f"NOTES.md '{heading[:55]}': ~{w} words for ~{dur_min:.1f} min "
                    f"(under soft floor ~{min_words} words)"
                )

        # formal topics should deep-link PREREQS
        if re.search(
            r"\b(sample space|measure|triplet|random variable|Ω|omega)\b",
            body,
            re.I,
        ):
            if "PREREQUISITES.md#" not in body and "./PREREQUISITES.md#" not in body:
                rep.warn(
                    f"NOTES.md '{heading[:55]}': formal topic with no "
                    f"./PREREQUISITES.md# deep link in map/body"
                )

    # broken connect-the-dots
    for m in re.finditer(r"\(\./?PREREQUISITES\.md#([\w-]+)\)", text):
        frag = m.group(1)
        if frag not in prereq_anchors:
            rep.err(
                f"NOTES.md links to PREREQUISITES.md#{frag}, but no matching "
                f"anchor exists in PREREQUISITES.md"
            )

    scan_forbidden_labels(text, "NOTES.md", rep)
    scan_ai_slop(text, "NOTES.md", rep)
    scan_meta_lines(text, "NOTES.md", rep)
    mermaid_count = scan_mermaid(text, "NOTES.md", rep)
    print(f"OK  mermaid blocks: {mermaid_count}")
    if mermaid_count > 2:
        rep.warn(
            f"NOTES.md: {mermaid_count} Mermaid diagrams; skill is ASCII-first "
            f"(0–2 unless pure systems design)"
        )

    if "## External references" in text:
        ext_start = text.index("## External references")
        next_h2 = re.search(r"^## ", text[ext_start + 3 :], re.MULTILINE)
        ext_end = ext_start + 3 + next_h2.start() if next_h2 else len(text)
        ext_body = text[ext_start:ext_end]
        n_links = len(re.findall(r"\[.+?\]\(https?://", ext_body))
        # Package-level band (global-agent.md): 3–8 total, not per topic.
        if not (3 <= n_links <= 8):
            rep.warn(
                f"NOTES.md: {n_links} external references found; "
                "spec is 3–8 package total (not per topic) — global-agent.md"
            )
        # Soft: multi-topic lectures usually need more than the bare floor.
        if n_topics and n_topics >= 6 and 0 < n_links < 4:
            rep.warn(
                f"NOTES.md: {n_topics} topics but only {n_links} external refs — "
                "prefer ≥4 strong topic-mapped companions when sources exist "
                "(still ≤8; do not pad with SEO)"
            )
        # Quality smells: topic mapping / diversity
        if n_links >= 3 and not re.search(
            r"topic|matches lecture|why it helps|how to use", ext_body, re.I
        ):
            rep.warn(
                "NOTES.md External references: no topic-mapping language "
                "(prefer table or 'Matches lecture…' / 'Why it helps' — global-agent.md)"
            )
        wiki_only = n_links > 0 and all(
            "wikipedia.org" in m.group(0).lower()
            for m in re.finditer(r"\]\((https?://[^)]+)\)", ext_body)
        )
        if wiki_only and n_links >= 2:
            rep.warn(
                "NOTES.md External references: only Wikipedia links — "
                "add original blogs / university lectures / primary sources"
            )
    else:
        rep.warn("NOTES.md: no '## External references' section found")

    img_count = len(re.findall(r"!\[.*?\]\(.*?\)", text))
    if img_count == 0:
        rep.warn(
            "NOTES.md: no image references (![...]) found — weave screenshots in"
        )
    elif n_topics and img_count < n_topics * 0.5:
        rep.warn(
            f"NOTES.md: only {img_count} images for {n_topics} topics — "
            f"many topics may lack a screenshot"
        )
    composite_refs = len(re.findall(r"screenshots/composites/", text))
    if (pkg := path.parent) and (pkg / "screenshots" / "composites").is_dir():
        n_comp = len(list((pkg / "screenshots" / "composites").glob("*.png")))
        if n_comp >= 3 and composite_refs == 0:
            rep.warn(
                "NOTES.md: composites/ exists but no embeds of screenshots/composites/ "
                "— prefer 2×2 panels over single sparse frames"
            )

    # code_tutorial: expect fenced code somewhere in NOTES
    code_fences = len(re.findall(r"```(?:python|bash|ts|js|yaml|json)", text, re.I))
    if code_fences == 0 and re.search(
        r"create_|import |pip install|uv |def |class ", text
    ):
        rep.warn(
            "NOTES.md: code-like prose but no fenced python/bash blocks — "
            "for code_tutorial see code-extraction.md"
        )

    # Math delimiter hygiene (GitHub / VS Code preview)
    if re.search(r"\\\(|\\\)|\\\[|\\\]", text):
        rep.err(
            "NOTES.md: contains \\( \\) or \\[ \\] math delimiters — "
            "use $...$ and $$...$$ only (see math-formatting.md)"
        )
    # bare LaTeX on a line with no $ and not inside a $$ display block
    in_display = False
    for i, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if stripped == "$$":
            in_display = not in_display
            continue
        if in_display or "$" in line:
            continue
        if re.search(r"\\(?:mathcal|mathbb|mathrm|frac|sum|int|ldots)\b", line):
            rep.warn(
                f"NOTES.md line {i}: LaTeX command outside $...$ / $$ blocks — "
                f"use $\\mathcal{{X}}$ style (math-formatting.md)"
            )
            break

    return n_topics, notes_anchors


def check_metadata(path: Path, rep: Report) -> dict:
    if not path.exists():
        rep.err("metadata.json is missing")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        rep.err(f"metadata.json is not valid JSON: {e}")
        return {}
    required = [
        "title",
        "video_id",
        "url",
        "duration_seconds",
        "channel",
        "instructor",
        "playlist_index",
        "skill",
        "content_type",
        "topic_count",
        "package_variant",
        "topics",
    ]
    for field in required:
        if field not in data:
            rep.err(f"metadata.json missing required field: {field}")
    ct = data.get("content_type")
    if ct and ct not in ALLOWED_CONTENT_TYPES:
        rep.err(
            f"metadata.json content_type '{ct}' not in allowed set "
            f"{sorted(ALLOWED_CONTENT_TYPES)}"
        )
    if (
        "requires_claim_mining" in data
        and not isinstance(data["requires_claim_mining"], bool)
    ):
        rep.err("metadata.json requires_claim_mining must be true or false")
    status = data.get("package_status")
    if status is not None and status not in ("legacy", "current", ""):
        rep.warn(
            f"metadata.json package_status '{status}' is unknown "
            "(use \"current\" or \"legacy\")"
        )
    if "beginner_prereqs" in data and not isinstance(data["beginner_prereqs"], bool):
        rep.err("metadata.json beginner_prereqs must be true or false")
    return data


def detect_quiz_flavors(questions: list) -> set[str]:
    flavors: set[str] = set()
    for q in questions:
        p = str(q.get("prompt", "")).lower()
        if re.search(r"\bwhat is\b|\bmeans\b|best (thought|described)|closest to", p):
            flavors.add("definition")
        if re.search(r"differ|contrast|vs\.|versus|rather than|how does", p):
            flavors.add("compare")
        if re.search(r"connect|chain|links topic|which chain", p):
            flavors.add("connect")
        if re.search(r"p\(|=\s*\?|how many|compute|fair die|3/6|1/2", p):
            flavors.add("numerical")
        if re.search(r"why is|bad complete|trap|fail|wrong complete|without \(Ω", p):
            flavors.add("trap")
        if re.search(r"prefer|should|when would|workplace|team|so what", p):
            flavors.add("tradeoff")
        if re.search(r"master|whole lecture|point of this lecture", p):
            flavors.add("map")
    return flavors


def check_questions(
    path: Path,
    prereq_anchors: set[str],
    notes_anchors: set[str],
    metadata: dict,
    rep: Report,
) -> None:
    if not path.exists():
        rep.warn(
            "raw/questions.json not found — skipping quiz checks "
            "(ok if quiz not built yet)"
        )
        return
    try:
        questions = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        rep.err(f"raw/questions.json is not valid JSON: {e}")
        return
    if not isinstance(questions, list) or not questions:
        rep.err("raw/questions.json must be a non-empty JSON array")
        return

    answer_keys = [
        str(q.get("answer", "")).strip().upper()
        for q in questions
        if isinstance(q, dict) and str(q.get("answer", "")).strip()
    ]
    if len(answer_keys) >= 2 and len(set(answer_keys)) == 1:
        rep.err(
            "questions.json: all answers use the same key "
            f"({answer_keys[0]}) -- shuffle correct-option positions"
        )

    parts = {q.get("part") for q in questions}
    if "prerequisites" not in parts:
        rep.err('questions.json: no question with part="prerequisites" (Part A missing)')
    if "notes" not in parts:
        rep.err('questions.json: no question with part="notes" (Part B missing)')

    required_fields = [
        "id",
        "prompt",
        "options",
        "answer",
        "whyCorrect",
        "whyOthers",
        "diagram",
    ]
    for q in questions:
        qid = q.get("id", "?")
        for field in required_fields:
            if field not in q:
                rep.err(f"questions.json q={qid}: missing required field '{field}'")
        if "part" not in q:
            rep.err(f"questions.json q={qid}: missing 'part'")

        if "anchor" not in q or not q.get("anchor"):
            rep.warn(
                f"questions.json q={qid}: no 'anchor' field — quiz links whole file"
            )
        else:
            anchor = str(q["anchor"])
            frag = anchor.split("#")[-1] if "#" in anchor else anchor.lstrip("#")
            if q.get("part") == "prerequisites" or anchor.startswith("PREREQUISITES"):
                pool = prereq_anchors
            else:
                pool = notes_anchors
            if frag and frag not in pool:
                # fuzzy: allow if any anchor endswith frag or vice versa
                if not any(frag in a or a in frag for a in pool):
                    rep.warn(
                        f"questions.json q={qid}: anchor '{anchor}' not found in "
                        f"known headings/ids (slug match is approximate)"
                    )

        blob = json.dumps(q, ensure_ascii=False)
        for pat in FORBIDDEN_LABEL_PATTERNS:
            if re.search(pat, blob, re.IGNORECASE | re.MULTILINE):
                rep.err(
                    f"questions.json q={qid}: forbidden technique label matching /{pat}/"
                )

    n_pre = sum(1 for q in questions if q.get("part") == "prerequisites")
    n_notes = sum(1 for q in questions if q.get("part") == "notes")
    duration_min = (metadata.get("duration_seconds") or 0) / 60
    if duration_min:
        lo_pre, hi_pre = (3, 5) if duration_min <= 50 else (4, 6)
        lo_notes, hi_notes = (5, 8) if duration_min <= 50 else (6, 10)
        if not (lo_pre <= n_pre <= hi_pre):
            rep.warn(
                f"questions.json: {n_pre} Part A questions; guidance for "
                f"{duration_min:.0f}min video is {lo_pre}–{hi_pre}"
            )
        if not (lo_notes <= n_notes <= hi_notes):
            rep.warn(
                f"questions.json: {n_notes} Part B questions; guidance for "
                f"{duration_min:.0f}min video is {lo_notes}–{hi_notes}"
            )

    prompts_notes = " ".join(
        str(q.get("prompt", "")) for q in questions if q.get("part") == "notes"
    )
    if not re.search(
        r"master|whole|triplet|point of this lecture|connect|chain",
        prompts_notes,
        re.I,
    ):
        rep.warn(
            "questions.json Part B: no obvious master-map / connect-the-dots question"
        )

    flavors = detect_quiz_flavors(questions)
    if len(flavors) < 4:
        rep.warn(
            f"questions.json: only {len(flavors)} detected flavors "
            f"{sorted(flavors) or '[]'} — aim for ≥4 (quiz-spec.md)"
        )
    else:
        print(f"OK  quiz flavors: {sorted(flavors)}")


def check_scenarios_gate(notes_path: Path, metadata: dict, rep: Report) -> None:
    if not notes_path.exists():
        return
    text = notes_path.read_text(encoding="utf-8", errors="replace")
    has_section = "## Apply it" in text
    ct = metadata.get("content_type")
    if ct in SCENARIOS_REQUIRED_FOR and not has_section:
        rep.warn(
            f"NOTES.md: content_type='{ct}' should include '## Apply it (scenarios)' "
            f"per production-scenarios.md"
        )
    if ct == "math_technical" and has_section:
        rep.warn(
            "NOTES.md: content_type='math_technical' has 'Apply it' — confirm exception"
        )


def check_claim_mining(
    pkg: Path, n_topics: int, notes_path: Path, metadata: dict, rep: Report
) -> None:
    """
    Completeness gate: claim sheets, coverage checklist, coverage receipt
    (transcript-mining.md). Default required (ERROR if missing). Soften only for
    package_status: "legacy" (WARN). requires_claim_mining=false without legacy
    is an ERROR. Exec architecture draft: WARN if missing/thin structure.
    """
    claims_dir = pkg / "raw" / "claims"
    slices_dir = pkg / "raw" / "transcript-by-topic"
    coverage = pkg / "raw" / "coverage-checklist.md"
    notes_text = ""
    if notes_path.exists():
        notes_text = notes_path.read_text(encoding="utf-8", errors="replace")

    # Claim mining required by default. Only package_status: "legacy" softens to WARN.
    status = str(metadata.get("package_status") or "").strip().lower()
    is_legacy = status == "legacy"
    if not is_legacy and metadata.get("requires_claim_mining") is False:
        rep.err(
            "metadata.json: requires_claim_mining=false is only allowed when "
            "package_status is \"legacy\""
        )
    claim_mining_required = not is_legacy

    def required_artifact_issue(message: str) -> None:
        if claim_mining_required:
            rep.err(message)
        else:
            rep.warn(f"{message} (legacy package: advisory only)")

    if not claims_dir.is_dir():
        required_artifact_issue(
            "raw/claims/ missing -- claim sheets are required before NOTES "
            "(transcript-mining.md)"
        )
    else:
        claim_files = sorted(claims_dir.glob("topic-*.md"))
        if n_topics and len(claim_files) < n_topics:
            required_artifact_issue(
                f"raw/claims/: {len(claim_files)} topic-*.md files for {n_topics} "
                "NOTES topics -- one claim sheet per topic required"
            )
        thin = 0
        for cf in claim_files:
            body = cf.read_text(encoding="utf-8", errors="replace")
            # count claim-like lines
            n_claims = len(
                re.findall(r"(?m)^\d+\.\s+\*\*Claim:\*\*|^[-*]\s+\*\*Claim:\*\*", body)
            )
            if n_claims == 0:
                n_claims = len(re.findall(r"(?m)^\d+\.\s+", body))
            if word_count(body) < 40 or n_claims < 2:
                thin += 1
            # soft: definition keywords in claims should appear in NOTES
            for term in re.findall(
                r"(?i)\b(model|algorithm|sample space|random variable|"
                r"probability measure|vector|overfitting)\b",
                body,
            ):
                if notes_text and not re.search(
                    rf"\b{re.escape(term)}\b", notes_text, re.I
                ):
                    rep.warn(
                        f"claim sheet {cf.name} mentions '{term}' but NOTES.md "
                        f"may omit it — check establishing coverage"
                    )
                    break
        if thin:
            rep.warn(
                f"raw/claims/: {thin} sheet(s) look thin (<2 claims or <40 words) — "
                f"re-read transcript slice"
            )
        else:
            print(f"OK  claim sheets: {len(claim_files)}")

    if not slices_dir.is_dir():
        rep.warn(
            "raw/transcript-by-topic/ missing — slice timed captions per topic "
            "(transcript-mining.md)"
        )
    elif n_topics:
        n_slices = len(list(slices_dir.glob("topic-*.txt")))
        if n_slices < max(n_topics - 1, 1):
            rep.warn(
                f"raw/transcript-by-topic/: {n_slices} slices for {n_topics} topics"
            )

    if not coverage.exists():
        required_artifact_issue(
            "raw/coverage-checklist.md missing -- whole-video must-capture "
            "FOUND/ABSENT list required (transcript-mining.md)"
        )
    else:
        cov = coverage.read_text(encoding="utf-8", errors="replace")
        if not re.search(r"(?i)worldview|from:|to:", cov):
            rep.warn(
                "coverage-checklist.md: no worldview arc (from ___ to ___) — "
                "topic-planning.md"
            )
        if not re.search(r"(?i)FOUND|ABSENT|N/A", cov):
            rep.warn(
                "coverage-checklist.md: no FOUND/ABSENT marks — fill must-capture table"
            )
        # if checklist says FOUND for review list, NOTES should have list-like content
        if re.search(r"(?i)review.*FOUND|FOUND.*review", cov) and notes_text:
            if not re.search(
                r"(?i)sample space|random variable|review|homework", notes_text
            ):
                rep.warn(
                    "coverage-checklist marks review list FOUND but NOTES lacks "
                    "review vocabulary — teach end-of-lecture list"
                )
        print("OK  coverage-checklist.md present")

    # Coverage receipt: claim ID → NOTES location (trace structure only)
    receipt_path = pkg / "raw" / "coverage-receipt.md"
    claim_id_re = re.compile(r"\bT(\d{2})-C(\d{2})\b", re.I)
    if not receipt_path.exists():
        required_artifact_issue(
            "raw/coverage-receipt.md missing -- claim ID → NOTES trace required "
            "(transcript-mining.md Step 3b)"
        )
    else:
        receipt_text = receipt_path.read_text(encoding="utf-8", errors="replace")
        receipt_ids = {m.group(0).upper() for m in claim_id_re.finditer(receipt_text)}
        if not receipt_ids:
            required_artifact_issue(
                "raw/coverage-receipt.md has no Claim IDs (expected Tnn-Cnn) — "
                "transcript-mining.md"
            )
        else:
            print(f"OK  coverage-receipt.md ({len(receipt_ids)} claim IDs)")

        sheet_ids: set[str] = set()
        if claims_dir.is_dir():
            for cf in sorted(claims_dir.glob("topic-*.md")):
                body = cf.read_text(encoding="utf-8", errors="replace")
                sheet_ids |= {
                    m.group(0).upper() for m in claim_id_re.finditer(body)
                }
        if not sheet_ids:
            rep.warn(
                "raw/claims/: no Tnn-Cnn IDs found — add **ID:** lines when editing "
                "(coverage-receipt can use provisional IDs until then)"
            )
        else:
            missing = sorted(sheet_ids - receipt_ids)
            if missing:
                required_artifact_issue(
                    "coverage-receipt.md missing claim IDs present in claim sheets: "
                    + ", ".join(missing[:12])
                    + ("…" if len(missing) > 12 else "")
                )
            extra = sorted(receipt_ids - sheet_ids)
            if extra and len(extra) > len(sheet_ids):
                rep.warn(
                    "coverage-receipt.md has many IDs not found in claim sheets — "
                    "check renumbering"
                )

        # Soft: if receipt cites a NOTES heading fragment, warn when absent
        if notes_text and receipt_ids:
            for loc in re.findall(
                r"(?i)(?:NOTES location|location)\s*[|:]+\s*([^|\n]+)",
                receipt_text,
            ):
                frag = loc.strip().strip("`").strip()
                if len(frag) < 8 or frag.lower() in (
                    "covered",
                    "merged",
                    "deferred",
                    "status",
                ):
                    continue
                # use a few distinctive words from location cell
                words = [w for w in re.findall(r"[A-Za-z]{4,}", frag)[:4]]
                if words and not all(
                    re.search(re.escape(w), notes_text, re.I) for w in words[:2]
                ):
                    rep.warn(
                        f"coverage-receipt location may not match NOTES: '{frag[:60]}'"
                    )
                    break

    # Exec architecture draft: preferred for current packages; structured soft checks
    exec_draft = pkg / "raw" / "exec-architecture-draft.md"
    if not exec_draft.exists():
        if claim_mining_required:
            rep.warn(
                "raw/exec-architecture-draft.md missing — recommended while building "
                "topics; final Exec Summary still required in NOTES "
                "(executive-summary-architecture.md)"
            )
    else:
        draft = exec_draft.read_text(encoding="utf-8", errors="replace")
        # Field presence by heading/label — not by empty keyword spam in NOTES
        field_pats = {
            "components": r"(?im)^##\s*components\b",
            "arrows": r"(?im)^##\s*arrows\b",
            "scenario": r"(?im)^##\s*scenario",
            "failure": r"(?im)^##\s*(failure|failures|contrast)\b",
            "stop": r"(?im)^##\s*(stop|out of scope|scope)\b",
            "claims": r"(?im)^##\s*(claims|load-bearing)\b",
        }
        missing_fields = [
            name
            for name, pat in field_pats.items()
            if not re.search(pat, draft)
        ]
        if missing_fields:
            rep.warn(
                "exec-architecture-draft.md missing structured sections: "
                + ", ".join(missing_fields)
                + " (use ## Components / ## Arrows / ## Scenario / ## Failure / "
                "## STOP or ## Scope / ## Claims — executive-summary-architecture.md)"
            )
        elif word_count(draft) < 40:
            rep.warn(
                "exec-architecture-draft.md is very thin — fill boxes/arrows before "
                "final Exec Summary"
            )
        else:
            print("OK  exec-architecture-draft.md structured sections present")

    # Exec summary worldview soft check when notes mention both frameworks
    if notes_text and re.search(r"(?i)deterministic", notes_text) and re.search(
        r"(?i)probabilistic", notes_text
    ):
        # first 4000 chars ≈ exec summary region
        head = notes_text[:4500]
        if not (
            re.search(r"(?i)deterministic", head)
            and re.search(r"(?i)probabilistic", head)
        ):
            rep.warn(
                "NOTES mentions deterministic and probabilistic but Exec Summary "
                "region may omit the worldview arc — put both in the map prose"
            )


def check_quiz_html(path: Path, rep: Report) -> None:
    if not path.exists():
        rep.warn("quiz.html not found — run generate_quiz.py")
        return
    html = path.read_text(encoding="utf-8", errors="replace")
    if "prerequisites" not in html:
        rep.err("quiz.html: missing prerequisites part")
    if "notes" not in html:
        rep.err("quiz.html: missing notes part")
    if "Part A" not in html or "Part B" not in html:
        rep.warn("quiz.html: Part A/B banners not found")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Validate a youtube-lecture-tutor package"
    )
    ap.add_argument(
        "--dir",
        required=True,
        help="Package folder (PREREQUISITES.md, NOTES.md, …)",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as failures",
    )
    args = ap.parse_args()
    d = Path(args.dir)
    if not d.is_dir():
        print(f"ERROR not a directory: {d}")
        sys.exit(1)

    rep = Report()
    metadata = check_metadata(d / "metadata.json", rep)
    prereq_anchors = check_prerequisites(d / "PREREQUISITES.md", rep, metadata)
    n_topics, notes_anchors = check_notes(
        d / "NOTES.md", prereq_anchors, rep, metadata
    )
    check_claim_mining(d, n_topics or 0, d / "NOTES.md", metadata, rep)
    check_questions(
        d / "raw" / "questions.json",
        prereq_anchors,
        notes_anchors,
        metadata,
        rep,
    )
    check_scenarios_gate(d / "NOTES.md", metadata, rep)
    check_quiz_html(d / "quiz.html", rep)

    if metadata.get("topic_count") and n_topics and metadata["topic_count"] != n_topics:
        rep.warn(
            f"metadata.json topic_count={metadata['topic_count']} doesn't match "
            f"{n_topics} '## Topic N:' sections in NOTES.md"
        )
    if not (d / "TRANSCRIPT.md").exists():
        rep.warn("TRANSCRIPT.md not found")

    sys.exit(rep.dump(args.strict))


if __name__ == "__main__":
    main()
