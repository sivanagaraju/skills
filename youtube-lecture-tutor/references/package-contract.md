# Package contract (folder only)

## Required files (The 7-Pillar Learning Package)

Every finished lecture study package must be structured as a self-contained, 7-pillar learning suite:

```
NN-short-slug/
  PREREQUISITES.md           # Pillar 1: 6–8 foundational pillars + Rosetta Stone notation table + phonetics + curriculum bridge
  NOTES.md                   # Pillar 2: Master architecture blueprint + topics + 5-point bridge + contrastive + debugging postmortems (delegates references to references.md)
  references.md              # Pillar 3: Dedicated annotated reference hub (Curriculum bridges, seminal papers, textbooks, industry guides, visualizers)
  examples/                  # Pillar 4: Standalone runnable Python simulations & mathematical verifications
    01_numerical_verification.py
    02_torch_autograd_simulation.py
  glossary.md                # Pillar 5: 6-column dictionary + Spoken English phonetics + MathsTerms links
  formulae_sheet.md          # Pillar 6: High-density rapid revision sheet (equations + tensor shapes + guarantees + contrastive matrix)
  quiz.html                  # Pillar 7: Standalone interactive dual-part quiz (Part A = PREREQUISITES · Part B = NOTES)
  TRANSCRIPT.md              # Cleaned, speaker-aligned ASR transcript
  metadata.json              # Package metadata schema (content_type, topic counts, package_status)
  screenshots/
    raw/                     # Individual video frames
    composites/              # 2×2 panels for Board slots
    manifest.json            # Frame-to-timestamp mappings
  raw/
    claims/                  # ★ claim sheets (agent work product, IDs Tnn-Cnn)
      topic-NN.md
    transcript-by-topic/     # Timed caption slices
      topic-NN.txt
    coverage-checklist.md    # Whole-video FOUND/ABSENT must-scan
    coverage-receipt.md      # ★ claim ID → NOTES location trace
    exec-architecture-draft.md # Agent draft while building topics
    questions.json           # Dual-part question bank with mixed answer keys
```

Agent-only completeness artifacts (`raw/claims/`, coverage checklist, **coverage receipt**) are **required by default** (see `metadata-schema.md` + `transcript-mining.md`). Soft WARN only when `package_status` is `"legacy"`. Not student-facing.  
`exec-architecture-draft.md` is strongly recommended (validator WARN if missing on current packages).

---

## Roles of the 7 Student-Facing Pillars (do not blur)

| File | Primary Pedagogical Job | Anti-job (Forbidden) |
| :--- | :--- | :--- |
| **`PREREQUISITES.md`** | Unlock 6–8 foundational mathematical primitives and notation needed to read the master map with zero prior memory; includes Spoken English phonetics, concrete numbers, and Curriculum Prerequisite Bridge table to sibling courses. | Full lecture retelling; repeating topic proofs; or vague abstract summaries. |
| **`NOTES.md`** | Master architecture blueprint (Unicode ASCII) + 4–10 topic deep dives with 5-point pedagogical bridge, zero-leap derivations, contrastive "Why X, Not Y" analyses, and 2 workplace debugging postmortems. References section replaced with clean callout to `references.md`. | Flat timeline essay without architecture map; slide-deck bullet notes; hand-waving proofs; video recap; or dumping 50+ raw citations inline. |
| **`references.md`** | Authoritative, curated, and annotated reference hub: Curriculum/sibling course bridges (`../../Mathematical-foundation-ml/`), seminal papers with arXiv links and "Why Read This", textbook chapter alignments, and interactive visualizers. | Unannotated raw URL lists; broken relative paths; or skipping prerequisite links. |
| **`examples/*.py`** | Standalone, runnable Python simulations with numerical assertions (`torch.allclose`, `np.allclose`) proving lecture math and exiting cleanly with code 0. Deep-linked from PREREQUISITES and NOTES. | Pseudo-code; non-executable snippets; GPU-dependent scripts; unverified approximations; scripts exiting with non-zero codes. |
| **`glossary.md`** | Master terminology glossary with formal definitions, plain-English meanings, spoken English phonetic pronunciations, and dynamic `MathsTerms/` links. | Unstructured list; missing phonetics; repeating full lecture text; informal definitions without formal notation. |
| **`formulae_sheet.md`** | High-density rapid revision sheet with LaTeX equations, input/output tensor shapes, mathematical guarantees, contrastive decision matrices, and hardware stability notes. | Narrative essay; wordy derivations without tabular summary; omitting tensor shapes or failure modes. |
| **`quiz.html`** | Standalone interactive dual-part quiz (Part A: Prereqs, Part B: Notes) generated from `raw/questions.json` with mixed answer keys. | Single-file quiz; quiz where all answers are A; superficial questions that don't test the master map. |

---

## Dynamic `MathsTerms/` Integration Rule

Do **not** restrict mathematical vocabulary to a static dictionary. During the processing of each lecture:
1. **Aggressive On-Demand Discovery**: Scan the lecture transcript, claim sheets, notes, and prerequisites for every mathematical term, operator, distribution, matrix operation, or optimization algorithm.
2. **Creation Standard**: If a discovered term does not exist in `../../MathsTerms/`, author a dedicated reference file following the 7-section visual gold standard of `Softmax.md`:
   - §1: Title & High-Impact 3-Stage Visual ASCII Pipeline
   - §2: 👶 **ELI5 Intuition** (Physical analogy & narrative)
   - §3: 🔍 **Plain-English Breakdown & Notation Rosetta Stone Table**
   - §4: 📐 **Formal Mathematical Formulation, Properties & Guarantees**
   - §5: 🔗 **Connecting the Dots: How this Concept Powers Modern ML & Generative AI**
   - §6: 💻 **Complete Standalone Executable Python/PyTorch Verification Script**
   - §7: 🩺 **Diagnostic Mini-Checks & Common Traps**
3. **Bidirectional Hyperlinking**: Explicitly cross-link the term in `PREREQUISITES.md`, `NOTES.md`, and `glossary.md` using relative markdown links (e.g., `[Softmax](../../MathsTerms/03-Multivariate-Calculus-and-Optimization/06-Softmax.md)`).
4. **Link Integrity**: `validate_package.py` programmatically asserts that every relative link to `../../MathsTerms/*.md` resolves to an existing file on disk.

---

## Golden package (regression)

**Current golden candidate (series):**  
`Mathematical-Foundations-of-ML/03-Lec02-Recap-Probability-Theory-Part1/`

When changing the skill or validator:
1. Run `validate_package.py --dir <golden>` — fix ERROR regressions.  
2. Spot-check: claim sheets, coverage-receipt, architecture Exec Summary, dual quiz, glossary, formulae sheet, and example script execution.  
3. Human blindfold on one hard topic (video closed).  
4. Do **not** treat a path that fails validation as golden.  
5. On legacy packages, set `package_status: "legacy"` in `metadata.json` to soften new structural requirements (`examples/`, `glossary.md`, `formulae_sheet.md`) to WARN.

---

## NOTES body law

All NOTES **structure** lives in **`output-blog-contract.md` only**.  
All NOTES **prose quality** lives in **`tutor-voice.md`** + **`writing-examples.md`**.  
This file does not redefine either.

If another reference restates headings, it is a pointer — edit the contract first.
