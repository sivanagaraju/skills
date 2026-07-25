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
   → master map + 4–10 topics with MM:SS (map/claims first)
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
1. **ID:** T01-C01
   **Claim:** …
   - **~MM:SS:** …
   - **Board example:** …
   - **Definition/slogan?:** yes/no — …
   - **Must teach in establishing:** yes
   - **ASCII needed?:** yes/no — (procedure / contrast / stacking / …)

2. **ID:** T01-C02
   **Claim:** …
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
- **Stable IDs (required on new/edited claim sheets):** `T{topic:02d}-C{n:02d}`  
  e.g. Topic 3 claim 2 → `T03-C02`. IDs never renumber silently after NOTES is written.

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

## Step 3b — Coverage receipt (traceability)

After claim sheets exist (and again after NOTES establishing is drafted), write:

`raw/coverage-receipt.md`

This is **not** the same as `coverage-checklist.md` (whole-video must-scan).  
The receipt maps **each Must-teach claim ID → where it was taught in NOTES**.

```markdown
# Coverage receipt — <video title>

## How to read
- Status: covered | merged (into other claim) | deferred (out of scope this video)
- NOTES location: heading text or anchor fragment (e.g. topic-5-sample-space)

| Claim ID | Topic | NOTES location | Status | Notes |
|----------|-------|----------------|--------|-------|
| T01-C01 | 1 | Topic 1 establishing | covered | |
| T01-C02 | 1 | Topic 1 establishing | covered | |
| T02-C01 | 2 | Topic 2 establishing | covered | |
```

### Receipt rules

- One row per **Must teach: yes** claim (preferred) or every numbered claim if unmarked.  
- **Status `covered`** = you assert establishing (or intentional merge) teaches it — still a human/agent judgment; the validator only checks **trace structure**.  
- **merged** requires a note pointing at the surviving Claim ID.  
- **deferred** only if the lecture truly does not teach it (rare; usually drop from Must-teach instead).  
- Migration: if older claim sheets lack `**ID:**` lines, add IDs when next editing; until then list provisional IDs `Tnn-C01…` in the receipt matching claim order and set status covered/merged.

### What the validator checks (deterministic only)

| Check | Severity (non-legacy) |
|-------|------------------------|
| `coverage-receipt.md` missing | **ERROR** |
| Receipt has no Claim ID cells | **ERROR** |
| Claim sheet has `Tnn-Cnn` IDs but receipt omits some | **ERROR** |
| Claim sheets have zero IDs | **WARN** (migrate to IDs) |
| NOTES heading/anchor in receipt not found | **WARN** (optional location check) |
| Whether prose *really* teaches the idea | **Not automated** — human/agent blindfold review |

---

## Step 4 — Write NOTES from claims (not from memory)

For each topic establishing section:

1. Open `raw/claims/topic-NN.md` + `topic-NN.txt`.  
2. Teach **every** `Must teach: yes` claim in flowing prose.  
3. Add ASCII for every claim marked `ASCII needed: yes`.  
4. Analogy stays short confirmation — **not** a second dump of claims.  
5. After draft: update `coverage-receipt.md` rows; any unticked claim = rewrite establishing or mark merged/deferred.

---

## Step 5 — Coverage gate (before quiz / done)

- Count claims with `Must teach: yes`.  
- Confirm each appears in NOTES (paraphrase OK; total omission fails).  
- Confirm coverage-checklist FOUND items appear in NOTES.  
- Confirm coverage-receipt lists every Must-teach ID (or provisional IDs).  
- Confirm worldview arc appears in Executive Summary.  
- **Default:** `validate_package.py` **errors** if claim sheets, coverage checklist, or coverage receipt are missing.  
- **Legacy only:** `package_status: "legacy"` softens missing artifacts to WARN.  
- Setting `requires_claim_mining: false` without `package_status: "legacy"` is an ERROR.  
- Human/agent must still verify Must-teach content appears in NOTES (presence of files ≠ teaching quality).

---

## Anti-patterns (fail the mining pass)

| Smell | Fix |
|-------|-----|
| Claim sheet is 2 vague bullets for a 10-min topic | Re-read transcript slice; add definitions/examples |
| NOTES written before claim sheets | Stop; mine first |
| Claims only in Analogy slot | Move into establishing |
| “Covered in map” without prose | Teach in establishing |
| Dropping end review list as homework fluff | List the items and explain their meanings in plain language in the final topic |

