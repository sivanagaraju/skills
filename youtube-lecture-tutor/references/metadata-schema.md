# metadata.json (required fields)

```json
{
  "title": "Lec …",
  "video_id": "…",
  "url": "https://www.youtube.com/watch?v=…",
  "duration_seconds": 0,
  "channel": "…",
  "instructor": "…",
  "playlist_index": 0,
  "skill": "youtube-lecture-tutor",
  "content_type": "theory_concept",
  "topic_count": 8,
  "package_variant": "educative-spine-v3",
  "package_status": "current",
  "requires_claim_mining": true,
  "beginner_prereqs": false,
  "ingest_evidence": "E3",
  "topics": ["short", "list", "of", "topic", "titles"]
}
```

`content_type` must be one of:  
`math_technical` | `code_tutorial` | `tool_product` | `theory_concept` | `research_review` | `soft_skills` | `mixed`

---

## Claim mining (enforcement)

Claim sheets and the coverage checklist are **required by default** for every package.

| `package_status` | Missing `raw/claims/` or `coverage-checklist.md` |
|------------------|--------------------------------------------------|
| `"current"` or **omitted** | **ERROR** |
| `"legacy"` | **WARN** only (older packages not yet retrofitted) |

| Field | Meaning |
|-------|---------|
| `requires_claim_mining: true` | Explicit confirmation for **current** packages (recommended on every new package) |
| `requires_claim_mining: false` | **Only** allowed with `"package_status": "legacy"` |
| Flag omitted | **Not** an opt-out — non-legacy packages still require mining artifacts |

**Canonical soft path for old packages:** `"package_status": "legacy"`.  
How to mine claims: see `transcript-mining.md`. Validator enforces file presence; teaching quality still needs agent/human coverage review.

---

## Beginner PREREQUISITES

| `beginner_prereqs` | PREREQUISITES idea-section guidance |
|--------------------|-------------------------------------|
| omitted / `false` | **3–6** short ideas |
| `true` | **3–8** allowed (deeper warm-up for beginners) |

Still not a second full lecture. See `prerequisites-template.md`.

---

## Topic count

**Primary:** architecture map boxes + claim clusters (`topic-planning.md`).  
**Absolute (validator ERROR):** **4–10** topics.  
**Soft (validator WARN):** duration only suggests a usual range — dense short lectures may sit high; long deep dives may sit lower.

| Duration | Soft guide (not a hard fail) |
|----------|------------------------------|
| ~15–25 min | often 4–8 |
| ~25–45 min | often 6–10 |
| ~45–90 min | often 7–10 (deepen; do not invent boxes) |

`duration_seconds` should still be set accurately for soft checks and quiz guidance.

---

## Ingest evidence (optional)

| `ingest_evidence` | Meaning |
|-------------------|---------|
| `E3` | Captions + usable frames/composites |
| `E2` | Captions only |
| `E1` | Partial / poor ASR |
| `E0` | No transcript source — do not invent NOTES |

See `ingest-recovery.md` when downloads/frames fail.
