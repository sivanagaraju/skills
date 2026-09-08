# Skill enforcement & load-model changelog

Historical notes for skill maintainers. **Active product law** lives in `SKILL.md` and `references/` (not phase names).

---

## 2026-09-08 — v4.0: First-Principles Pedagogy & Multi-File Study Package Upgrade

Major architectural release upgrading the skill contract, pedagogical rigor, reference templates, automated quality gate (`validate_package.py`), and test infrastructure across Requirements R1, R2, R3, and R4.

| Requirement | Area | Key Changes |
|-------------|------|-------------|
| **R1** | **6-Pillar Contract** | Expanded package from 3 legacy files to 6 core pillars: `PREREQUISITES.md`, `NOTES.md`, `examples/*.py`, `glossary.md`, `formulae_sheet.md`, and `quiz.html`. |
| **R1** | **Dynamic MathsTerms** | Added dynamic discovery and authoring of foundational math terms under `MathsTerms/` following the 7-section visual gold standard (`Softmax.md` model) with bidirectional relative linking. |
| **R2** | **Pedagogical Bridge** | Codified 5-point pedagogical bridge: $\text{👶 ELI5 Intuition} \iff \text{🔍 Plain-English} \iff \text{🔢 Concrete Numbers} \iff \text{📐 Formal Math} \iff \text{💻 Runnable Code}$. |
| **R2** | **Zero-Leap Derivations** | Mandated complete intermediate algebraic steps for all proofs/equations; banned hand-waving phrases ("it can easily be shown that", "trivially", "obviously"). |
| **R2** | **Spoken Phonetics** | Mandated plain-English phonetic pronunciation guides (e.g., $\nabla f$: "DEL EFF", $\partial$: "PAR-shul") for all Greek letters and math operators. |
| **R2** | **Contrastive Justification** | Mandated dedicated "Why X, Not Y" deep-dives explaining why naive alternatives fail in AI/ML (e.g., float32 catastrophic cancellation, Jacobian matrix explosion). |
| **R2** | **Heading Governance** | Resolved ELI5 contradiction: `👶 ELI5 Intuition` progressive layer is explicitly mandated, while marketing gimmick headings ("Feynman", "Toy", "Approach 1-5") remain strictly banned. |
| **R2** | **Anti-Slop Expansion** | Expanded blacklist against AI filler ("delve", "tapestry", "paramount", "testament", "crucial", "indispensable", "beacon", "landscape"). |
| **R2** | **Workplace Debugging** | Mandated 2 real-world postmortem debugging scenarios in `NOTES.md` with Problem → Root Cause → Debugging Steps → Code Fix. |
| **R3** | **Validation Engine** | Upgraded `validate_package.py` with structural checks for `examples/`, `glossary.md`, `formulae_sheet.md`, and `MathsTerms/` relative links. |
| **R3** | **Code Execution** | Integrated subprocess execution engine running all scripts in `examples/*.py` with timeout (default 30s) asserting clean exit code 0 and `allclose` assertions. |
| **R3** | **CLI Flags** | Added `--strict` (treats warnings as errors), `--skip-exec` (fast dry-run validation), and `--exec-timeout <sec>`. |
| **R3** | **Cross-Platform Fix** | Reconfigured Windows console encoding to UTF-8 and implemented ASCII-safe status indicators (`[PASS]`, `[FAIL]`, `[WARN]`) to eliminate CP1252 crash on `\u2717`. |
| **R3** | **Robust Heading Parser** | Replaced brittle string matching with flexible regexes accommodating emojis (`📑`, `🔬`) and HTML anchors (`<a id="..."></a>`). |
| **R3** | **Automated Test Suite** | Created comprehensive `scripts/test_validate_package.py` with 15+ automated pytest cases verifying CLI flags, compliant packages, mutations, and execution timeouts. |
| **R4** | **Reference Templates** | Authored new reference templates: `references/glossary-template.md`, `references/formulae-sheet-template.md`, `references/examples-contract.md`. |
| **R4** | **Template Updates** | Updated existing references: `references/package-contract.md`, `references/output-blog-contract.md`, `references/tutor-voice.md`, and `references/prerequisites-template.md`. |
| **R4** | **Global Synchronization** | Synchronized all skill definitions, references, and scripts between workspace and global directory `C:\Users\sivan\.gemini\config\skills\youtube-lecture-tutor` with SHA256 checksum verification. |

### Architectural Deep-Dive: 6-Pillar Study Package Contract (R1)
Prior to v4.0, packages consisted solely of `PREREQUISITES.md`, `NOTES.md`, and `quiz.html`. In v4.0:
1. `examples/*.py`: Standalone, heavily commented, runnable Python verification scripts validating mathematical models with `torch.allclose` or `np.allclose`. Hyperlinked directly from notes and prerequisites.
2. `glossary.md`: 6-column dictionary (`Term / Notation | Formal Definition | Plain-English Software Meaning | Spoken English (Phonetics) | Real-World Analogy | Dedicated MathsTerm Link`).
3. `formulae_sheet.md`: High-density rapid revision sheet with Master Equations, Tensor Shapes, Mathematical Guarantees, Contrastive Quick Table, and Hardware Stability notes.
4. Dynamic `MathsTerms/`: Discovery and authoring of standalone terms following the 7-section visual gold standard of `Softmax.md`, cross-linked via `../../MathsTerms/*.md`.

### Pedagogical Law & Voice Upgrades (R2)
- **Zero Prior Knowledge Assumed:** Explicitly designed for adult engineers returning to mathematics after 10–15 years. Every concept begins with physical primitives before introducing mathematical abstraction.
- **Zero-Leap Proofs:** Every step in mathematical derivations must be shown explicitly. Banned phrases: "it is obvious that", "trivially", "it can easily be shown".
- **Contrastive Learning:** Explicitly answers "Why this specific formulation?" by demonstrating catastrophic failure modes of naive alternatives.
- **ELI5 Progressive Structure:** Codified the 3-layer pattern: `👶 ELI5 Intuition` (physical metaphor) $\to$ `🔍 Plain-English Breakdown` (notation breakdown) $\to$ `📐 Formal Math` (rigorous formulas and proofs).

### Validation Engine & Test Suite (R3)
- `validate_package.py` now runs programmatic checks on all 6 deliverables.
- Subprocess code execution engine invokes `python examples/*.py` within a timeout and checks returncode == 0.
- Content linters check for phonetic table completeness, contrastive sections, active comprehension blocks, expanded AI-slop vocabulary, and derivation gap heuristics.
- Backward compatibility: Packages marked with `"package_status": "legacy"` soften missing new pillars to advisory WARNINGs rather than fatal ERRORs.
- Test harness `scripts/test_validate_package.py` validates compliance and catches regressions across all validation paths.

---

## 2026-07-25 — External refs: no Wikipedia default

| Change | Effect |
|--------|--------|
| `global-agent.md` | Default **zero** Wikipedia; **wide net**: any strong YouTube, blogs, course notes, primaries, demos — not university-only or “named blog” only |
| Quality bar | Same map-box teaching > brand pedigree |
| Validator | WARN on any wiki link; stronger WARN if wiki-heavy |
| Package 02 | Replaced wiki FA / Box slogan with Caltech LFD Lec 1 + Olah MNIST blog; kept StatQuest + 3B1B |

---

## 2026-07-25 — Screenshots uniqueness + Exec lead anti-slop

| Change | Effect |
|--------|--------|
| Ingest ranges | Prefer `raw/topic-ranges.json` → chapters → **synthetic ~6 min slices** (no long-video single `full` range) |
| `--frames-only` | URL optional; wipes prior pngs; denser panels for chapter-less lectures |
| `manifest.json` | `time_start` / `time_end` / `range_source` for Board assignment |
| `topic-planning.md` | Hard law: unique composite per topic by MM:SS; re-extract if under-paneled |
| `executive-summary-architecture.md` | Lead = 3–6 plain sentences (job→method→fork); bans TED/negation open with real bad example |
| Validator | WARN on multi-topic image reuse; sparse whole-video sample; Exec TED lead; missing Scenario/STOP/load-bearing cues |
| `SKILL.md` | Absolute rules 6–7; pipeline steps for topic-ranges + Boards; anti-patterns |

**Package follow-up (not this skill edit):** re-extract package 02 screenshots; rewrite package 02 Exec lead to match good example.

---

## Hardening history (summary)

| Change | Effect |
|--------|--------|
| All-same quiz keys | **ERROR** |
| Bold ownership-stamp density | **WARN** |
| Claim mining artifacts | **ERROR by default**; **WARN** only if `package_status: "legacy"` |
| `requires_claim_mining: false` without legacy | **ERROR** (no silent opt-out) |
| Docs vs validator honesty | ERROR/WARN text matches code |
| Dead paths / residue | Fixed historical `04v3` bar, twin-skill sync notes, ELI5-in-mining residual |
| Reference load | **Staged**: 4 hot-core always; other refs by pipeline step |
| `beginner_prereqs` | PREREQ idea band 3–8 when true, else 3–6 |
| Topic count | Absolute **4–10** (ERROR); duration only soft WARN; map + claim clusters primary (`topic-planning.md`) |

---

## Package metadata examples (series)

| Package | Typical flags |
|---------|----------------|
| New / current | `"package_status": "current"`, `"requires_claim_mining": true` |
| Not yet retrofitted | `"package_status": "legacy"`, `"requires_claim_mining": false` |

---

## Design rule

**Deterministic facts → hard ERROR** (missing claims, all-A quiz keys).  
**Semantic teaching quality → WARN + human/agent review** (regex cannot prove a concept was taught).

---

## External references band

| Rule | Value |
|------|--------|
| Package total | **3–8** links (was 2–6) |
| Not | 3–8 **per topic** (that would explode count) |
| Soft | ≥6 topics → prefer ≥4 links when good sources exist |
| Process | Deep research (multi-query + verify) before each URL — `global-agent.md` |

---

## Coverage receipt + ingest recovery (skill)

| Change | Effect |
|--------|--------|
| Claim IDs `Tnn-Cnn` | Required on new/edited claim sheets |
| `raw/coverage-receipt.md` | Required (ERROR if missing non-legacy); maps ID → NOTES location |
| ID mismatch sheet vs receipt | ERROR when sheets contain IDs |
| Sheets without IDs | WARN (migrate) |
| `exec-architecture-draft.md` | WARN if missing; WARN if structured sections missing |
| `ingest-recovery.md` | Captions/video/frames/ffmpeg recovery + evidence E3–E0 |
| Golden package pointer | `package-contract.md` → series package 03 |

### Still open / package work (not skill)

- Retrofit package **02** all-A quiz keys and stamp density  
- Full **ID lines inside every existing claim sheet** (receipts may use provisional IDs)  
- Automated golden fixture tests in CI (pointer exists; no CI harness yet)  
