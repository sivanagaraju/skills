---
name: youtube-lecture-tutor
description: >
  Canonical skill for YouTube lecture study packages (math/ML/code/software/soft-skills):
  6-pillar learning package (PREREQUISITES.md with 6-8 foundational pillars and phonetics,
  NOTES.md with master blueprint, 4-10 topics with 5-point pedagogical bridge, zero-leap
  derivations, contrastive Why X Not Y sections, workplace debugging postmortems,
  examples/*.py runnable simulations, glossary.md dictionary with spoken phonetics,
  formulae_sheet.md rapid revision, quiz.html dual quiz Part A/B, and dynamic MathsTerms/ links).
  Claim-mine before NOTES (default required). Writing quality mandatory (tutor-voice).
  Triggers: lecture URL, extract lecture, study package, prereqs notes quiz, MFML next,
  /youtube-lecture-tutor. Only skill for full lecture packages.
---

# YouTube Lecture Tutor

**One skill. One package shape. Do not invent alternate layouts.**

```
PREREQUISITES.md  →  NOTES.md  →  examples/*.py  →  glossary.md  →  formulae_sheet.md  →  quiz.html
```

The 6-Pillar Production Study Package:
1. `PREREQUISITES.md`: 6–8 foundational pillars, Rosetta Stone notation decoder with spoken English phonetics, concrete numbers, and `#pN` anchors.
2. `NOTES.md`: Executive Summary with Unicode ASCII blueprint, Chalkboard Rosetta Stone, Topic Deep Dives (5-point pedagogical bridge), zero-leap derivations, contrastive "Why X, Not Y" analyses, 2 Workplace Debugging Scenarios, Centralized External References, and `quiz.html` anchors.
3. `examples/*.py`: Fully self-contained, heavily commented, runnable Python simulations with numerical assertions (`torch.allclose`, `np.allclose`) proving lecture math and exiting cleanly with code 0.
4. `glossary.md`: Master terminology glossary with formal definitions, plain-English software meanings, spoken English phonetic pronunciations, and dynamic `MathsTerms/` links.
5. `formulae_sheet.md`: High-density rapid revision sheet with KaTeX display equations, input/output tensor shapes, mathematical guarantees, contrastive decision matrices, and hardware stability notes.
6. `quiz.html`: Standalone interactive dual-part quiz (Part A: Prereqs, Part B: Notes) generated from `raw/questions.json`.

Study path for the student:

```
warm-up (PREREQUISITES.md + Rosetta Stone phonetics)
→ architecture Executive Summary (NOTES.md blueprint)
→ topics (each box on the map + zero-leap proofs + why X not Y)
→ runnable code verifications (examples/*.py)
→ rapid revision & definitions (glossary.md + formulae_sheet.md)
→ external links → workplace debugging scenarios → quiz (Part A / Part B)
```

---

## Load references (staged)

**Rule:** always load the **hot core** first. Open other references only at the pipeline step that needs them.  
All files under `references/` remain part of the skill — staging is about *when* to load, not deleting detail.

### Hot core (always)

1. `references/output-blog-contract.md` — NOTES + PREREQS structure law  
2. `references/tutor-voice.md` — writing quality (establishing 80%, analogy scope, no stamps, zero-leap derivations)  
3. `references/transcript-mining.md` — claim sheets + coverage before NOTES  
4. `references/executive-summary-architecture.md` — Exec Summary = architecture blueprint  

### Staged (load when needed)

| When | Open |
|------|------|
| Goal / folder layout | `package-contract.md`, `metadata-schema.md` |
| Topic map + frames | `topic-planning.md`, `diagrams-and-mermaid.md` |
| Ingest failures / partial media | `ingest-recovery.md` |
| After `content_type` known | `scenarios.md` (+ `math-formatting.md` if math; `code-extraction.md` if code) |
| Writing feels thin | `writing-examples.md` |
| PREREQS drafting | `prerequisites-template.md` (6–8 pillars + Rosetta Stone phonetics) |
| Standalone simulations | `examples-contract.md` (`examples/*.py` runnable simulations) |
| Glossary authoring | `glossary-template.md` (6-column schema + phonetics) |
| Formulae sheet authoring | `formulae-sheet-template.md` (equations + tensor shapes + guarantees) |
| Non-math Apply-it section | `production-scenarios.md` |
| Quiz build | `quiz-spec.md` |
| External links / HIL / confidence | `global-agent.md` (band 3–8; deep research before each URL) |
| Optional header connect snippet | `notes-connect-block.md` |

**Prompt library origin:** rules adapted from `educative.io/src/gemini_youtube_analyzer_v6_0.py`  
**Do not run** that file or use Vertex/project IDs for this skill.

**Void / do not use as full-package design:**

- Flat continuous NOTES without master map  
- Flat “blog-only” notes without PREREQS + dual quiz (this skill is the full package)  
- Copying an older package layout when it conflicts with this contract  
- Analyzer rule “2 Mermaids per topic”  

**Single skill:** Only **`youtube-lecture-tutor`** is the lecture study-package skill.  
Do not maintain or call removed aliases (`lecture-study-package`, `youtube-blog-notes`).  

---

## Absolute rules

1. **PREREQUISITES first** — 6–8 foundational pillars tailored to the lecture topics (incorporating physical analogies, concrete numbers, standalone runnable Python snippets, Diagnostic Mini-Checks, Math Terminology Rosetta Stone with spoken English phonetics, and `#pN` anchors); unlocks the map; not a second lecture.
2. **NOTES educative spine only** — TOC → Exec Summary (architecture blueprint) → topics (5-point pedagogical bridge, zero-leap derivations, contrastive "Why X, Not Y" analyses) → Workplace Debugging Scenarios (2 real-world postmortems) → External references → (optional Apply it) → Sources.  
   **Topic count:** driven by **map boxes + claim clusters** (not clock alone). Absolute **4–10**. Soft duration guide only (topic-planning.md): dense short lectures may need more topics; long deep dives may need fewer, richer ones.
3. **Claim-mine before NOTES (default required)** — timed slices + `raw/claims/topic-NN.md` (IDs `Tnn-Cnn`) + `coverage-checklist.md` + **`coverage-receipt.md`** (`transcript-mining.md`). Set `requires_claim_mining: true` and `package_status: "current"` (or omit status). **Only** `package_status: "legacy"` softens missing artifacts to WARN. Never write establishing from a single skim.
4. **Each topic fixed subsections** filled with continuous prose — see `tutor-voice.md`.  
   Map · board · establishing (~80%) · analogy (~10%) · local ASCII (~10%) · bridge.  
   Implement the 5-point pedagogical bridge: $\text{👶 ELI5 Intuition} \iff \text{🔍 Plain-English} \iff \text{🔢 Concrete Numbers} \iff \text{📐 Formal Math} \iff \text{💻 Runnable Code}$.  
   Include dedicated contrastive "Why X, Not Y" rationale explaining why naive alternatives fail.  
   **Fail if establishing is only bullets or thinner than the claim sheet.**  
   **Fail if ownership is a bold stamp checklist** (`**Wrong move:**` / `**You can now:**`) — use prose.
5. **Analogy = this topic only** — does not teach Topic N+1; no foreign metaphor when lecture has a world; no printed Scene/Question labels.
6. **Exec Summary = architecture blueprint** (`executive-summary-architecture.md`).  
   Reverse-engineer the lecture into boxes, arrows, mini-boxes, scenario walkthrough, failure path, STOP.  
   **File place:** after TOC, before Topic 1. **Write process:** update draft after each topic; **final write after all topics**.  
   **Lead:** 3–6 plain sentences (job → method → fork). **Fail** TED/negation open (“is not import/fit”, “opening frame”), TOC renames, thin list, or no scenario path.
7. **Screenshots are time-aligned and unique per topic** (`topic-planning.md`).  
   Prefer `composites/*` from `manifest.json` times that overlap the topic MM:SS. **Never** reuse the same composite path on multiple topics.  
   If panels are few (old whole-video sample): write `raw/topic-ranges.json` → `--frames-only` → re-assign. Do not pad Boards by recycling 3 panels across 8 topics.
8. **Acronym first-use** — expand FA/RE/etc. on first hit; PREREQS unlocks map words.
9. **quiz.html** Part A = PREREQUISITES, Part B = NOTES (master-map question required).  
   **Answer keys mixed** — not all A (`quiz-spec.md`); near-miss distractors preferred.
10. **ASCII-first**; rich multi-stage diagrams with Unicode box-drawing characters (`┌─┐│└─┘`); Mermaid sparse; only safe Mermaid types (`diagrams-and-mermaid.md`).
11. **Progressive Pedagogy & Anti-Slop Headings** — Mandate the 3-layer progressive structure (`👶 ELI5 Intuition` → `🔍 Plain-English Breakdown` → `📐 Formal Math`). The heading `👶 ELI5 Intuition` is explicitly permitted and required for physical intuition. Forbid marketing/promotional gimmick headings (e.g. bare "Feynman Technique", "Approach 1/2", "Toy Implementation", "Mind-Blowing Hack"), robotic stamp checklists (`**Wrong move:**` / `**You can now:**`), and student-facing `content_type:` meta lines.
12. **Faithful** to video; clean ASR; no invented theorems; Must-teach claims covered.
13. **No Vertex / project IDs** (prompt *rules* only from analyzer research).
14. Classify **content_type** for depth: math formulas / code extraction / UI paths (`scenarios.md`).
15. **External references** — package total **15–25** curated, authoritative, non-hallucinated citations categorized by seminal papers, authoritative textbooks/lectures, and industry implementation guides (`global-agent.md`). Not 15–25 per topic. Never invent URLs.
16. **Workplace Debugging Scenarios** — Include 2 complete, self-contained real-world engineering incidents with Problem → Root Cause → Debugging Steps → Python Code Fix.
17. **Confidence** on every finished package **with claim coverage numbers**.
18. **HIL** only when plan+architecture exist and goal confidence is still low.
19. **Subagents** when useful (topic map, parallel claim mine for long videos).
20. **6-Pillar Study Package Contract** — Every lecture package must produce all 6 deliverables: `PREREQUISITES.md`, `NOTES.md`, `examples/*.py`, `glossary.md`, `formulae_sheet.md`, and `quiz.html`. Omission of any pillar without `package_status: "legacy"` fails validation.
21. **Zero-Leap Mathematical Derivations** — Every mathematical equation, rule, or theorem must show all intermediate algebraic transitions step-by-step. Never skip intermediate steps or use hand-waving phrases ("it can easily be shown that", "trivially", "obviously").
22. **Spoken English Phonetics** — Every mathematical symbol, Greek operator, and formal expression in `glossary.md` and `PREREQUISITES.md` must include explicit spoken English phonetics (e.g., $\nabla f$: "DEL EFF", $\partial$: "PAR-shul", $\mathbb{E}[X]$: "EX-pek-TAY-shun of EKS").
23. **Contrastive "Why X, Not Y" Justification** — For every core algorithm, loss function, or mathematical formulation, provide explicit contrastive analysis demonstrating why intuitive/naive alternatives fail in modern ML/GenAI systems.
24. **Executable Code Verification** — All Python scripts in `examples/*.py` must be completely self-contained, CPU-runnable, execute cleanly with exit code 0 under 30 seconds, and assert numerical correctness using `torch.allclose` or `np.allclose`.
25. **Dynamic MathsTerms/ Integration** — Scan transcripts and claims for all mathematical concepts. Missing foundational terms must be authored under `MathsTerms/` adhering to the 7-section visual gold standard (`Softmax.md` model). Bidirectional relative cross-links (`../../MathsTerms/*.md`) in `PREREQUISITES.md`, `NOTES.md`, and `glossary.md` are mandatory.

---

## Pipeline

```
1. Goal check (series path, URL, playlist index)
2. Ingest (metadata, captions, frames) → TRANSCRIPT.md, screenshots/, metadata.json  
   Screenshots: multi-frame → **2×2 composites** per **time range** (priority: `raw/topic-ranges.json` → YouTube chapters → **synthetic ~6 min slices**). Never starve a long lecture to one “full” range with 3 panels. Use `composites/` + `manifest.json` times in Board slots (`topic-planning.md`). `--frames-only` re-extracts (wipes prior pngs); URL optional when video already on disk.
   Clean ASR duplicates when building timed captions (transcript-mining.md).
   On failure/partial success → ingest-recovery.md (evidence E3–E0; do not invent transcript).
3. Classify content_type (scenarios.md)
4. Draft architecture map + topic list with times (topic-planning.md: map/claims first; duration soft)
   → worldview arc: from ___ to ___ (required for theory/math)
   → write raw/topic-ranges.json from topic MM:SS → re-run --frames-only so each topic owns a unique panel
5. ★ CLAIM MINE (transcript-mining.md) — required before NOTES (default ERROR if missing)
   - raw/transcript-by-topic/topic-NN.txt
   - raw/claims/topic-NN.md (IDs Tnn-Cnn + definitions, procedures, slogans, ~MM:SS)
   - raw/coverage-checklist.md (FOUND/ABSENT must-capture items)
   - raw/coverage-receipt.md (claim ID → NOTES location; update after establishing)
6. ★ Dynamic MathsTerms/ Discovery & Integration
   - Scan transcript and claims for all mathematical terms, distributions, operators, and losses
   - Check existing terms in MathsTerms/; author missing terms using the 7-section visual gold standard (Softmax.md model)
   - Prepare relative links (../../MathsTerms/*.md) for bidirectional referencing
7. Write PREREQUISITES.md (prerequisites-template.md)
   - 6–8 foundational pillars tailored to lecture topics
   - Math Terminology Rosetta Stone with spoken English phonetics
   - Concrete numbers, runnable Python snippets, #pN anchors, and MathsTerms/ links
8. Author examples/*.py (examples-contract.md)
   - Standalone, CPU-compatible, runnable Python simulations with rich docstrings
   - Validate lecture mathematics with torch.allclose / np.allclose assertions
   - Verify clean exit code 0 in under 30s
9. Write NOTES topics from claim sheets (output-blog-contract.md + tutor-voice.md)
   - 5-point pedagogical bridge on every topic (👶 ELI5 Intuition → 🔍 Plain-English → 🔢 Concrete Numbers → 📐 Formal Math → 💻 Runnable Code)
   - Zero-leap derivations showing all algebraic steps
   - Dedicated contrastive "Why X, Not Y" sections
   - Time-aligned unique composite screenshots (screenshots/composites/)
   - Bidirectional hyperlinks to examples/*.py and ../../MathsTerms/*.md
   - Update raw/exec-architecture-draft.md after each topic
10. ★ Write final Executive Summary & Workplace Debugging into NOTES
    - Executive Summary: architecture blueprint ASCII diagram, plain lead (job→method→fork), comparative matrices
    - 2 Workplace Debugging Scenarios (real-world postmortems: Problem → Root Cause → Debugging Steps → Python Code Fix)
    - Centralized External References (15–25 curated, non-hallucinated citations)
11. Author glossary.md (glossary-template.md)
    - 6-column dictionary schema: Term / Notation | Formal Definition | Plain-English Software Meaning | Spoken English (Phonetics) | Real-World Analogy | Dedicated MathsTerm Link
    - Comprehensive categorization (Greek Symbols, Linear Algebra, Probability, ML/GenAI)
12. Author formulae_sheet.md (formulae-sheet-template.md)
    - Master Equations Index (KaTeX display equations)
    - Input/Output Tensor Dimensionality Table (shapes, dimensions, semantic meaning)
    - Mathematical Guarantees & Invariants Table (convexity, bounds, failure modes)
    - Contrastive "Why X, Not Y" Quick Decision Table
    - Hardware Realities & Numerical Stability (float32, LogSumExp, memory)
13. Author raw/questions.json & Generate quiz.html (quiz-spec.md)
    - Part A (Prereqs) + Part B (Notes), mixed answer keys, near-miss distractors
    - python scripts/generate_quiz.py --out <NN-slug>/quiz.html --title "Quiz · Lec XX" --questions <NN-slug>/raw/questions.json
14. ★ Run Automated Quality Gate: validate_package.py
    - python scripts/validate_package.py --dir <NN-slug> [--strict]
    - Must exit 0 (verifies 6 pillars, code execution, phonetics, contrastive sections, MathsTerms links)
15. Update series README & deliver Done message with confidence report
```

---

## Folder layout

```
<series>/
  <NN-short-slug>/
    PREREQUISITES.md           # 6-8 pillars + Rosetta Stone + Spoken Phonetics + #pN anchors
    NOTES.md                   # Blueprint + Topics + Zero-Leap + Why X Not Y + Debugging
    glossary.md                # 6-column dictionary + Spoken Phonetics + MathsTerms links
    formulae_sheet.md          # Equations + Tensor Shapes + Guarantees + Why X Not Y table
    examples/                  # Standalone runnable Python simulations with numerical assertions
      01_numerical_verification.py
      02_torch_autograd_simulation.py
    quiz.html                  # Standalone interactive dual-part quiz
    TRANSCRIPT.md              # Cleaned ASR transcript
    metadata.json              # Lecture metadata schema
    screenshots/
      raw/                     # Individual chapter tiles
      composites/              # 2×2 panels — unique per topic
      manifest.json
    raw/                       # Captions, claims, coverage receipt, questions.json
  README.md
```

**Structural quality bar / golden package:**  
See `package-contract.md` → **Golden package**. Re-validate that path after skill changes; do not treat a failing or missing path as canonical.

---

## Commands

### Ingest

```bash
python "%USERPROFILE%\.gemini\config\skills\youtube-lecture-tutor\scripts\ingest_youtube.py" ^
  --url "URL" --out "path\to\NN-slug" --playlist-index N --download-video
```

```bash
python ~/.gemini/config/skills/youtube-lecture-tutor/scripts/ingest_youtube.py \
  --url "URL" --out "path/to/NN-slug" --playlist-index N --download-video
```

Re-extract multi-frame composites only (existing `raw/lecture.*`). Prefer after writing `raw/topic-ranges.json`:

```bash
python "%USERPROFILE%\.gemini\config\skills\youtube-lecture-tutor\scripts\ingest_youtube.py" ^
  --out "path\to\NN-slug" --frames-only
```

### Quiz

```bash
python "%USERPROFILE%\.gemini\config\skills\youtube-lecture-tutor\scripts\generate_quiz.py" ^
  --out "path\to\NN-slug\quiz.html" ^
  --title "Quiz · Lec XX" ^
  --questions "path\to\NN-slug\raw\questions.json"
```

```bash
python ~/.gemini/config/skills/youtube-lecture-tutor/scripts/generate_quiz.py \
  --out "path/to/NN-slug/quiz.html" \
  --title "Quiz · Lec XX" \
  --questions "path/to/NN-slug/raw/questions.json"
```

### Validate (required before “done”)

Standard validation (executes `examples/*.py`, asserts all 6 pillars):
```bash
python "%USERPROFILE%\.gemini\config\skills\youtube-lecture-tutor\scripts\validate_package.py" ^
  --dir "path\to\NN-slug"
```

Strict mode (treats all warnings as fatal errors; returns exit code 1 if warnings exist):
```bash
python "%USERPROFILE%\.gemini\config\skills\youtube-lecture-tutor\scripts\validate_package.py" ^
  --dir "path\to\NN-slug" --strict
```

Fast validation without code execution (skips subprocess script execution in `examples/`):
```bash
python "%USERPROFILE%\.gemini\config\skills\youtube-lecture-tutor\scripts\validate_package.py" ^
  --dir "path\to\NN-slug" --skip-exec
```

Custom script execution timeout (default: 30 seconds):
```bash
python "%USERPROFILE%\.gemini\config\skills\youtube-lecture-tutor\scripts\validate_package.py" ^
  --dir "path\to\NN-slug" --exec-timeout 45
```

Automated test suite execution (runs comprehensive pytest validation suite):
```bash
python -m pytest scripts/test_validate_package.py -v
```

Automated checks enforced by `validate_package.py`:
- **6-Pillar Package Completeness:** Asserts presence and non-emptiness of `PREREQUISITES.md`, `NOTES.md`, `examples/*.py`, `glossary.md`, `formulae_sheet.md`, and `quiz.html` (softened to WARN only when `"package_status": "legacy"`).
- **Subprocess Code Execution:** Executes all scripts in `examples/*.py` using `sys.executable`, asserts clean termination with exit code 0 within timeout, and verifies `torch.allclose` / `np.allclose` assertions.
- **Dynamic MathsTerms Relative Links:** Extracts all relative links to `../../MathsTerms/*.md` and verifies target files exist on disk.
- **Glossary Schema:** Checks `glossary.md` for required 6 columns (`Term / Notation`, `Formal Definition`, `Plain-English Software Meaning`, `Spoken English (Phonetics)`).
- **Formulae Sheet Schema:** Checks `formulae_sheet.md` for Master Equations Index, Input/Output Tensor Dimensionality, Mathematical Guarantees, and Contrastive Quick Table.
- **Phonetic Pronunciations:** Verifies spoken English pronunciation entries for Greek letters and mathematical operators in `glossary.md` and `PREREQUISITES.md`.
- **Pedagogy & Anti-Slop Linters:** Checks contrastive "Why X, Not Y" rationale sections, active comprehension blocks (`Recall`, `Apply`, `Diagnose`, `Vocabulary`), expanded AI-slop phrase blacklist, and zero-leap derivation gap heuristics.
- **Console Robustness:** UTF-8 encoded console output with ASCII-safe indicators (`[PASS]`, `[FAIL]`, `[WARN]`), preventing Windows CP1252 crash.

---

## Quality gate (fail if any miss)

### Automated
- [ ] `validate_package.py --dir <package>` exits 0 with zero ERRORs.
- [ ] Code execution verifier runs all `examples/*.py` with exit code 0.
- [ ] All `../../MathsTerms/*.md` relative links resolve to existing files on disk.

### 6-Pillar Structure
- [ ] `PREREQUISITES.md`: 6–8 foundational pillars, Rosetta Stone with spoken English phonetics, concrete numbers, runnable Python snippets, `#pN` anchors.
- [ ] `NOTES.md`: Executive Summary architecture blueprint (Unicode ASCII), Chalkboard Rosetta Stone, 4–10 topic deep dives with 5-point pedagogical bridge, zero-leap derivations, contrastive "Why X, Not Y" analyses, 2 workplace debugging postmortems, 15–25 centralized external references.
- [ ] `examples/*.py`: Fully self-contained, CPU-runnable Python simulations with `torch.allclose` / `np.allclose` assertions, referenced in markdown.
- [ ] `glossary.md`: 6-column terminology dictionary (`Term / Notation`, `Formal Definition`, `Plain-English Software Meaning`, `Spoken English (Phonetics)`, `Real-World Analogy`, `Dedicated MathsTerm Link`).
- [ ] `formulae_sheet.md`: High-density rapid revision sheet (Master Equations, Tensor Dimensionality, Mathematical Guarantees, Contrastive Quick Table, Hardware Stability).
- [ ] `quiz.html`: Standalone interactive dual-part quiz (Part A: Prereqs, Part B: Notes) with mixed answer keys.
- [ ] `metadata.json`: Matches schema with `content_type`, `topic_count`, `package_status: "current"`, and `requires_claim_mining: true`.
- [ ] Screenshots: Prefer `screenshots/composites/*` (2×2); **unique path per topic** by MM:SS; no cross-topic screenshot reuse.

### Completeness & Pedagogy (was the historical failure mode)
- [ ] Claim mining: `raw/claims/topic-*.md` with `Tnn-Cnn` IDs + `coverage-checklist.md` + `coverage-receipt.md` mapping all IDs to `NOTES.md`.
- [ ] 5-point pedagogical bridge implemented on every topic:
      $$\text{👶 ELI5 Intuition} \iff \text{🔍 Plain-English} \iff \text{🔢 Concrete Numbers} \iff \text{📐 Formal Math} \iff \text{💻 Runnable Code}$$
- [ ] Zero-leap algebraic derivations: every transition from ground primitives to final formulas shows intermediate algebraic steps without hand-waving.
- [ ] Contrastive "Why X, Not Y" sections exist for all core algorithms, equations, and loss functions.
- [ ] Spoken English phonetic pronunciations provided for all Greek symbols and mathematical shorthand.
- [ ] Dynamic `MathsTerms/` discovery: missing concepts authored under `MathsTerms/` adhering to the 7-section visual gold standard.

### Writing & Anti-Slop (as important as structure)
- [ ] **Product goal:** topic understandable with **video closed** (blindfold test) — NOTES reduce watch time, not only recap.
- [ ] Establishing = **~80%** teaching budget from claim sheets; flowing lesson not lecture-report.
- [ ] Ownership close in **prose** — no bold Wrong/Right/You can now stamp blocks.
- [ ] Analogy = **short confirmation of this topic only** (~10%); does not carry primary claims or Topic N+1.
- [ ] Board captions **transcribe** teaching content + **time-aligned unique** composites (no multi-topic reuse).
- [ ] Bridges state a **leftover problem**, not “Next topic: …”.
- [ ] Local pictures teach a **relation**; hard math topics include **micro numbers** + `Notice:` line.
- [ ] Rich visual ASCII diagrams with Unicode box-drawing characters (`┌─┐│└─┘`).
- [ ] No AI slop (zero matches against expanded blacklist: "delve", "tapestry", "crucial", "testament", "paramount", "beacon", "landscape").
- [ ] No derivation gaps ("it can easily be shown that", "trivially", "obviously", "as is well known").
- [ ] Confidence reported with **claims mined / covered / gaps**.

---

## Done message

1. Folder path  
2. Study path: PREREQUISITES → NOTES architecture Exec Summary → topics → quiz  
3. content_type + topic count + one-line whole-video point + **worldview arc**  
4. **Coverage:** claims mined ≈ N · covered in NOTES ≈ M · gaps (if any)  
5. External links (+ apply-scenarios yes/no)  
6. **Confidence** High/Medium/Low (+ what would raise it; High only if coverage high)  
7. HIL used? (yes/no + what)  

---

## Other skills

| Skill | Status |
|-------|--------|
| **youtube-lecture-tutor** | **Only / final skill** for full YouTube lecture study packages |
| ~~lecture-study-package~~ | **Removed** — do not use or re-create as a second skill |
| ~~youtube-blog-notes~~ | **Removed** — do not use for full packages |

All lecture package work goes through **`/youtube-lecture-tutor`** only.
