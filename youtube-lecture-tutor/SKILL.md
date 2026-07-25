---
name: youtube-lecture-tutor
description: >
  Canonical skill for YouTube lecture study packages (math/ML/code/software/soft-skills):
  PREREQUISITES.md, then NOTES.md (TOC, architecture Executive Summary, 4-10 topics
  from map/claim clusters with map/screenshot/prose/analogy/ASCII/bridge), dual quiz Part A/B.
  Claim-mine before NOTES (default required). Writing quality mandatory (tutor-voice).
  Triggers: lecture URL, extract lecture, study package, prereqs notes quiz, MFML next,
  /youtube-lecture-tutor. Only skill for full lecture packages.
---

# YouTube Lecture Tutor

**One skill. One package shape. Do not invent alternate layouts.**

```
PREREQUISITES.md  →  NOTES.md  →  quiz.html
```

Study path for the student:

```
warm-up → architecture Executive Summary → topics (each box on the map)
       → external links → (optional apply scenarios) → quiz
```

---

## Load references (staged)

**Rule:** always load the **hot core** first. Open other references only at the pipeline step that needs them.  
All files under `references/` remain part of the skill — staging is about *when* to load, not deleting detail.

### Hot core (always)

1. `references/output-blog-contract.md` — NOTES + PREREQS structure law  
2. `references/tutor-voice.md` — writing quality (establishing 80%, analogy scope, no stamps)  
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
| PREREQS drafting | `prerequisites-template.md` |
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

1. **PREREQUISITES first** — default 3–6 ideas; set `beginner_prereqs: true` for 3–8 deeper warm-ups; unlocks the map; not a second lecture.  
2. **NOTES educative spine only** — TOC → Exec Summary (architecture blueprint) → topics → External references → (optional Apply it) → Sources.  
   **Topic count:** driven by **map boxes + claim clusters** (not clock alone). Absolute **4–10**. Soft duration guide only (topic-planning.md): dense short lectures may need more topics; long deep dives may need fewer, richer ones.  
3. **Claim-mine before NOTES (default required)** — timed slices + `raw/claims/topic-NN.md` (IDs `Tnn-Cnn`) + `coverage-checklist.md` + **`coverage-receipt.md`** (`transcript-mining.md`). Set `requires_claim_mining: true` and `package_status: "current"` (or omit status). **Only** `package_status: "legacy"` softens missing artifacts to WARN. Never write establishing from a single skim.  
4. **Each topic fixed subsections** filled with continuous prose — see `tutor-voice.md`.  
   Map · board · establishing (~80%) · analogy (~10%) · local ASCII (~10%) · bridge.  
   **Fail if establishing is only bullets or thinner than the claim sheet.**  
   **Fail if ownership is a bold stamp checklist** (`**Wrong move:**` / `**You can now:**`) — use prose.  
5. **Analogy = this topic only** — does not teach Topic N+1; no foreign metaphor when lecture has a world; no printed Scene/Question labels.  
6. **Exec Summary = architecture blueprint** (`executive-summary-architecture.md`).  
   Reverse-engineer the lecture into boxes, arrows, mini-boxes, scenario walkthrough, failure path, STOP.  
   **File place:** after TOC, before Topic 1. **Write process:** update draft after each topic; **final write after all topics**.  
   Fail if TOC renames, thin list, or no scenario path.  
7. **Acronym first-use** — expand FA/RE/etc. on first hit; PREREQS unlocks map words.  
8. **quiz.html** Part A = PREREQUISITES, Part B = NOTES (master-map question required).  
   **Answer keys mixed** — not all A (`quiz-spec.md`); near-miss distractors preferred.  
9. **ASCII-first**; Mermaid sparse; only safe Mermaid types (`diagrams-and-mermaid.md`).  
10. **No** ELI5 / Feynman / Toy / Approach-N headings; no student-facing `content_type:` meta lines.  
11. **Faithful** to video; clean ASR; no invented theorems; Must-teach claims covered.  
12. **No Vertex / project IDs** (prompt *rules* only from analyzer research).  
13. Classify **content_type** for depth: math formulas / code extraction / UI paths (`scenarios.md`).  
14. **External references** — package total **3–8** topic-mapped links after deep research (`global-agent.md`; staged load when writing this section). Not 3–8 per topic. Never invent URLs.  
15. **Apply it (scenarios)** when type is non-math (`production-scenarios.md`).  
16. **Confidence** on every finished package **with claim coverage numbers**.  
17. **HIL** only when plan+architecture exist and goal confidence is still low.  
18. **Subagents** when useful (topic map, parallel claim mine for long videos).  

---

## Pipeline

```
1. Goal check (series path, URL, playlist index)
2. Ingest (metadata, captions, frames) → TRANSCRIPT.md, screenshots/, metadata.json  
   Screenshots: **per-chapter multi-frame** → **2×2 composites** (short 1 panel / long 2–3 panels of 4 tiles). Use `composites/` in NOTES Board slots; see topic-planning.md. `--frames-only` re-extracts without re-download.
   Clean ASR duplicates when building timed captions (transcript-mining.md).
   On failure/partial success → `ingest-recovery.md` (evidence E3–E0; do not invent transcript).
3. Classify content_type (scenarios.md)
4. Draft architecture map + topic list with times (topic-planning.md: map/claims first; duration soft)
   → worldview arc: from ___ to ___ (required for theory/math)
   → if goal still unclear → HIL
5. ★ CLAIM MINE (transcript-mining.md) — required before NOTES (default ERROR if missing)
   - raw/transcript-by-topic/topic-NN.txt
   - raw/claims/topic-NN.md  (IDs Tnn-Cnn + definitions, procedures, slogans, ~MM:SS)
   - raw/coverage-checklist.md (FOUND/ABSENT must-capture items)
   - raw/coverage-receipt.md (claim ID → NOTES location; update after establishing)
   Mine every minute for claims; merge into topics for reading — do not drop definitions.
6. Write PREREQUISITES.md (3–6 ideas default; beginner_prereqs: true → up to 8; unlock map words)
7. Write NOTES **topics** from claim sheets (output-blog-contract.md + tutor-voice.md)
   Establishing ~80% in prose (no ownership stamps); analogy = this topic only;
   ASCII for procedures (+ code/math/apply by type)
   After **each** topic: update `raw/exec-architecture-draft.md` (components, arrows, scenario notes)
8. ★ Write final **Executive Summary** into NOTES (still before Topic 1) using
   `executive-summary-architecture.md` — architecture blueprint, not a video abstract
9. Coverage gate: every Must-teach claim in NOTES; checklist FOUND items; receipt IDs complete
10. raw/questions.json (Part A + Part B; claims as sources; map question; **shuffle answer keys**)
11. generate_quiz.py → quiz.html
12. validate_package.py --dir <NN-slug>   ← **required before done**
13. Update series README
14. Human quality gate (writing + coverage) + confidence report
    Report: claims mined / claims in NOTES / gaps
```

**Anti-pattern (void):** writing full NOTES from memory/summary after a single transcript skim.  
**Anti-pattern (void):** thin Exec Summary first + never rewrite; TOC-as-summary; bold ownership stamps; all-quiz-answers A.  
**Required multi-pass:** map → claim sheets → topics (+ incremental architecture draft) → **architecture Exec Summary** → coverage → quiz (mixed keys).

---

## Folder layout

```
<series>/
  <NN-short-slug>/
    PREREQUISITES.md
    NOTES.md
    quiz.html
    TRANSCRIPT.md
    metadata.json
    screenshots/
      raw/           # individual chapter tiles
      composites/    # 2×2 panels — prefer these in NOTES Board slots
      manifest.json
    raw/   # captions, chapters.json, questions.json, optional video
  README.md
```

**Structural quality bar / golden package:**  
See `package-contract.md` → **Golden package**. Re-validate that path after skill changes; do not treat a failing or missing path as canonical.

---

## Commands

### Ingest

```bash
python "%USERPROFILE%\.grok\skills\youtube-lecture-tutor\scripts\ingest_youtube.py" ^
  --url "URL" --out "path\to\NN-slug" --playlist-index N --download-video
```

```bash
python ~/.grok/skills/youtube-lecture-tutor/scripts/ingest_youtube.py \
  --url "URL" --out "path/to/NN-slug" --playlist-index N --download-video
```

Re-extract multi-frame composites only (existing `raw/lecture.*`):

```bash
python "%USERPROFILE%\.grok\skills\youtube-lecture-tutor\scripts\ingest_youtube.py" ^
  --url "URL" --out "path\to\NN-slug" --frames-only
```

### Quiz

```bash
python "%USERPROFILE%\.grok\skills\youtube-lecture-tutor\scripts\generate_quiz.py" ^
  --out "path\to\NN-slug\quiz.html" ^
  --title "Quiz · Lec XX" ^
  --questions "path\to\NN-slug\raw\questions.json"
```

```bash
python ~/.grok/skills/youtube-lecture-tutor/scripts/generate_quiz.py \
  --out "path/to/NN-slug/quiz.html" \
  --title "Quiz · Lec XX" \
  --questions "path/to/NN-slug/raw/questions.json"
```

### Validate (required before “done”)

```bash
python "%USERPROFILE%\.grok\skills\youtube-lecture-tutor\scripts\validate_package.py" ^
  --dir "path\to\NN-slug"
```

```bash
python ~/.grok/skills/youtube-lecture-tutor/scripts/validate_package.py \
  --dir "path/to/NN-slug"
```

Fixes automated gaps inspired by educative `evaluate_blog_completeness()`: topic count absolute **4–10** (ERROR) with soft duration WARN, six topic slots, bullet-only establishing (ERROR), robot bridges, PREREQS deep-link integrity, Mermaid ban-list, dual-part quiz + anchors + flavor heuristic, **answer-key distribution (ERROR if all same key)**, metadata schema, soft word-count-per-minute, AI-slop phrases, ownership-stamp density WARN, claim sheets / coverage checklist (**ERROR by default**; WARN only if `package_status: "legacy"`), beginner_prereqs PREREQ idea band. **Writing + coverage WARNINGs are tickets, not noise.** Semantic teaching quality is still human/agent review — files present ≠ claims taught.

---

## Quality gate (fail if any miss)

### Automated
- [ ] `validate_package.py --dir <package>` exits 0 (fix ERRORs)

### Structure
- [ ] PREREQUISITES warm-up only (+ `#pN-…` anchors); idea count per beginner_prereqs flag  
- [ ] NOTES: TOC + Executive Summary architecture blueprint (ASCII boxes/arrows)  
- [ ] Topic count **4–10** (map + claims primary; duration guide soft); full timeline coverage  
- [ ] Each topic has all six slots  
- [ ] Formal topics link `./PREREQUISITES.md#…` from the map slot when needed  
- [ ] External references (**3–8** package total; each mapped to a topic; deep research; not SEO/wiki dump)  
- [ ] Apply-it scenarios present **iff** content_type requires them  
- [ ] metadata.json matches schema  
- [ ] quiz Part A + Part B + anchors where useful + master-map question  
- [ ] Screenshots: prefer `screenshots/composites/*` (2×2); long topics 2–3 panels  

### Completeness (as important as structure — was the historical failure mode)
- [ ] Claim mining default: `raw/claims/topic-*.md` + `coverage-checklist.md` + **`coverage-receipt.md`** unless legacy  
- [ ] Current packages set `requires_claim_mining: true`; claim IDs `Tnn-Cnn`; receipt maps each ID → NOTES  
- [ ] Every **Must teach** claim appears in NOTES establishing (paraphrase OK; omission fails) — receipt is trace, not proof of quality  
- [ ] End-of-lecture review/homework list taught if present in transcript  
- [ ] Board **procedures** (stacking, derivation steps, …) have ASCII in NOTES  
- [ ] Definitions that co-occur in transcript (e.g. model **and** algorithm) both defined  

### Writing (as important as structure)
- [ ] **Product goal:** topic understandable with **video closed** (blindfold test) — NOTES reduce watch time, not only recap  
- [ ] Establishing = **~80%** teaching budget from claim sheets; flowing lesson not lecture-report  
- [ ] Ownership close in **prose** — no bold Wrong/Right/You can now stamp blocks  
- [ ] Analogy = **short confirmation of this topic only** (~10%); does not carry primary claims or Topic N+1  
- [ ] Board captions **transcribe** teaching content, not only timestamps  
- [ ] Bridges state a **leftover problem**, not “Next topic: …”  
- [ ] Local pictures teach a **relation**; hard math topics include **micro numbers** + Notice line  
- [ ] Map slots explain **which box** and **why now**; Exec Summary states worldview arc when lecture has one  
- [ ] Exec Summary = **architecture blueprint** (`executive-summary-architecture.md`):  
      boxes + arrows + scenario walkthrough + failure/STOP + load-bearing claims;  
      final write after topics; same file place before Topic 1  
- [ ] Acronyms expanded on first use (FA, RE, …)  
- [ ] Quiz answer keys **mixed** (not all A); near-miss distractors preferred  
- [ ] No AI slop; ASR cleaned  
- [ ] No student-facing content_type meta lines  
- [ ] **code_tutorial:** fenced code/bash in coding topics (`code-extraction.md`); not prose-only  
- [ ] **math_technical:** only `$...$` / `$$...$$` (`math-formatting.md`); math must-capture list in scenarios.md  
- [ ] Mermaid only safe types if used  
- [ ] Confidence reported with **claims mined / covered / gaps**

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
