# Package contract (folder only)

## Required files

```
NN-short-slug/
  PREREQUISITES.md   # short warm-up — read FIRST
  NOTES.md           # educative blog — see output-blog-contract.md
  quiz.html          # Part A = PREREQUISITES · Part B = NOTES
  TRANSCRIPT.md
  metadata.json
  screenshots/
    raw/             # individual frames
    composites/      # 2×2 panels for Board slots
  raw/
    claims/                 # ★ claim sheets (agent work product)
      topic-NN.md
    transcript-by-topic/    # timed caption slices
      topic-NN.txt
    coverage-checklist.md   # whole-video FOUND/ABSENT must-scan
    coverage-receipt.md     # ★ claim ID → NOTES location (trace)
    exec-architecture-draft.md  # agent draft while building topics
    captions… questions.json …
```

Agent-only completeness artifacts (`raw/claims/`, coverage checklist, **coverage receipt**) are **required by default** (see `metadata-schema.md` + `transcript-mining.md`). Soft WARN only when `package_status` is `"legacy"`. Not student-facing.  
`exec-architecture-draft.md` is strongly recommended (validator WARN if missing on current packages).

## Roles (do not blur)

| File | Job | Anti-job |
|------|-----|----------|
| PREREQUISITES | Unlock 3–6 words/ideas needed to read the master map | Full lecture retelling |
| NOTES | Master architecture + 4–10 topics (map/claims) + screenshots + bridges | Flat essay without map |
| quiz | Prove warm-up + map/topics stuck | Quiz on only one file |

## Golden package (regression)

**Current golden candidate (series):**  
`Mathematical-Foundations-of-ML/03-Lec02-Recap-Probability-Theory-Part1/`

When changing the skill:

1. Run `validate_package.py --dir <golden>` — fix ERROR regressions.  
2. Spot-check: claim sheets, coverage-receipt, architecture Exec Summary, dual quiz.  
3. Human blindfold on one hard topic (video closed).  
4. Do **not** treat a path that fails validate as golden.

Update this pointer only when a better package exists and passes the gate.

## Style bar

Use the golden package (or another that passes the **current** gate) as structure reference. Do not copy an older layout that conflicts with this contract.

## NOTES body law

All NOTES **structure** lives in **`output-blog-contract.md` only**.  
All NOTES **prose quality** lives in **`tutor-voice.md`** + **`writing-examples.md`**.  
This file does not redefine either.

If another reference restates headings, it is a pointer — edit the contract first.
