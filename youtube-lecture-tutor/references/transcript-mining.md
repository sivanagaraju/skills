# Transcript mining (mandatory before NOTES)

**Why this exists:** Package structure alone produces pretty but incomplete notes.  
Gemini-style completeness comes from **segment Q&A on the transcript**. This file forces that pass.

**When:** After topic list + master map exist; **before** writing `NOTES.md` establishing prose.

**Product goal unchanged:** NOTES must still be video-optional teaching — but teaching must cover **mined claims**, not vibes.

---

## Pipeline placement

```
ingest (timed captions + frames)
   → classify content_type
   → master map + 6–10 topics with MM:SS
   → ★ CLAIM MINE (this file)
   → PREREQUISITES
   → NOTES (establishing written FROM claim sheets)
   → coverage check
   → quiz (prefer claims as sources)
   → validate_package.py
```

---

## Artifacts to write (under package `raw/`)

| Path | Purpose |
|------|---------|
| `raw/transcript-by-topic/topic-NN.txt` | Timed caption slice for that topic’s time range |
| `raw/claims/topic-NN.md` | Claim inventory for that topic |
| `raw/coverage-checklist.md` | Whole-video must-capture + found/absent |
| `raw/worldview-arc.md` | One-line arc (optional but recommended) |

Do **not** put these in student-facing NOTES. They are agent work products for completeness.

---

## Step 1 — Clean and slice the transcript

1. Prefer `raw/captions.en.timed.txt` (or rebuild from VTT).  
2. **Dedupe ASR garbage:** collapse exact 2×/3× repeated word runs (common on auto-captions).  
3. For each topic with range `(MM:SS–MM:SS)`, extract lines whose timestamps fall in range →  
   `raw/transcript-by-topic/topic-NN.txt`.  
4. If a topic has almost no lines, fix timestamps or re-slice; do not invent speech.

---

## Step 2 — Claim sheet format (per topic)

Write `raw/claims/topic-NN.md`:

```markdown
# Claims — Topic N: <title> (MM:SS–MM:SS)

## Worldview / map box
- Box: PROBLEM | OBSTACLE | METHOD | …

## Claims (numbered)
1. **Claim:** …
   - **~MM:SS:** …
   - **Board example:** …
   - **Definition/slogan?:** yes/no — …
   - **Must teach in establishing:** yes
   - **ASCII needed?:** yes/no — (procedure / contrast / stacking / …)

2. **Claim:** …
   …

## Explicit definitions to install
- term → one-line meaning (from lecture)

## Procedures (step lists spoken on board)
- e.g. stack columns → vector

## Slogans / warnings
- e.g. all models wrong… / table lookup fails / random labels

## Merge notes
- Claim #k also needed in Topic M: …
```

### Claim quality rules

- One idea per claim (not a paragraph).  
- Prefer teacher’s **examples** (planet, X-ray, speech) over generic rewrites.  
- Every **definition**, **slogan**, **procedure**, and **review list item** is a claim.  
- Mark `Must teach in establishing: yes` for all definitions/procedures/slogans.  
- Do **not** invent theorems; if ASR is garbled, note `ASR uncertain` and keep meaning conservative.

---

## Step 3 — Whole-video coverage checklist

Write `raw/coverage-checklist.md`:

```markdown
# Coverage checklist — <video title>

## Worldview arc
- From: …
- To: …
- (e.g. deterministic function approximation → probabilistic / distribution estimation)

## Must-scan items (mark FOUND / ABSENT / N/A)
| Item | Status | Topic # | ~MM:SS |
|------|--------|---------|--------|
| Core problem one-liner | FOUND | 2 | 11:06 |
| Model defined | | | |
| Algorithm defined (vs model) | | | |
| Board procedure (stacking/derivation/…) | | | |
| Main contrast (A vs B) | | | |
| Slogan(s) | | | |
| Warning / trap | | | |
| End-of-lecture review / homework list | | | |
| Forward pointer (next lecture) | | | |
| Type-specific extras (see scenarios.md) | | | |

## Gaps before NOTES
- …
```

**Math chalk lectures** must also run the **math_technical must-capture** list in `scenarios.md`.

---

## Step 4 — Write NOTES from claims (not from memory)

For each topic establishing section:

1. Open `raw/claims/topic-NN.md` + `topic-NN.txt`.  
2. Teach **every** `Must teach: yes` claim in flowing prose.  
3. Add ASCII for every claim marked `ASCII needed: yes`.  
4. Analogy stays short confirmation — **not** a second dump of claims.  
5. After draft: tick claims off; any unticked claim = rewrite establishing or document intentional merge.

---

## Step 5 — Coverage gate (before quiz / done)

- Count claims with `Must teach: yes`.  
- Confirm each appears in NOTES (paraphrase OK; total omission fails).  
- Confirm coverage-checklist FOUND items appear in NOTES.  
- Confirm worldview arc appears in Executive Summary.  
- When `metadata.json` sets `requires_claim_mining: true`, `validate_package.py` errors if claim sheets or the coverage checklist are missing. **Human/agent must still verify content**.

---

## Anti-patterns (fail the mining pass)

| Smell | Fix |
|-------|-----|
| Claim sheet is 2 vague bullets for a 10-min topic | Re-read transcript slice; add definitions/examples |
| NOTES written before claim sheets | Stop; mine first |
| Claims only in Analogy slot | Move into establishing |
| “Covered in map” without prose | Teach in establishing |
| Dropping end review list as homework fluff | List the items and explain their meanings in plain language in the final topic |

