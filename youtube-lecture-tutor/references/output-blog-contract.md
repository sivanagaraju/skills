# LOCKED — NOTES + PREREQUISITES blog contract

**This is the only NOTES structure.** Flat timeline essays without a master map are void.

Prompt-library origin: educative `gemini_youtube_analyzer_v6_0.py` structured blog + type rules  
**Agent-native:** no Vertex; depth rules live in `scenarios.md`, `code-extraction.md`, `diagrams-and-mermaid.md`, `production-scenarios.md`.

## User-approved choices

| Item | Rule |
|------|------|
| Skeleton | Educative-style (TOC → Exec Summary → Topics → External refs) |
| Topics | **6–10** for ~30–50 min |
| PREREQUISITES | **Before** map — mandatory short warm-up |
| Diagrams | **ASCII-first**; Mermaid sparse (see `diagrams-and-mermaid.md`) |
| Connect-the-dots | Every topic points back to **one master architecture** |
| Type prompts | Depth knobs only — **same layout** for all types |
| Production scenarios | Optional section for **non-math** types (see below) |

## PREREQUISITES.md

- Short only (3–6 ideas; deeper OK if user is beginner)  
- Unlocks words needed to read the master map (including FA / event / measure if the map uses them)  
- Not a second full lecture  
- See `prerequisites-template.md` + `tutor-voice.md` PREREQUISITES writing  

## NOTES.md — file order vs write order

**File order (student reading):** TOC → Executive Summary → Topics → refs → sources  

**Write order (agent — mandatory):**

```
claim-mine → PREREQS → Topics 1..N from claims
  → after each topic: update raw/exec-architecture-draft.md (boxes, arrows, scenario)
  → ★ WRITE final Executive Summary into NOTES (architecture blueprint)
       law: executive-summary-architecture.md
  → External refs → quiz
```

Do **not** draft a thin Exec Summary skeleton first and leave it.  
Exec Summary is the **architecture phase** of the document: reverse-engineer the lecture into a system blueprint (not a video abstract).

## NOTES.md order (mandatory — finished file)

```
1. Header + link: do PREREQUISITES first
2. Table of Contents (topics with MM:SS; expand acronyms in titles if beginner)
3. ## Executive Summary — architecture of this lecture   ← final content written LAST
     **FULL LAW:** references/executive-summary-architecture.md
     Required blocks (summary):
     - Architect’s lead prose (problem → system goal → payoff)
     - Worldview arc when present (from ___ to ___; expand acronyms)
     - System context (small ASCII)
     - ★ Main blueprint: boxes, arrows, mini-boxes (not TOC list)
     - Scenario walkthrough through the blueprint
     - Failure / contrast path
     - STOP / out of scope
     - Load-bearing claims (5–8; not topic renames)
     - Speaker/course if known
     Fail if thin list, two-column rename only, no scenario, no boxes/arrows
4. ## Topic N: Name (MM:SS–MM:SS)   × 6–10

     **Prerequisite to drafting:** claim sheet `raw/claims/topic-NN.md` from transcript-mining.md
     For EACH topic, in this order (headings fixed; **writing rules in tutor-voice.md**):
     a) ### Where this sits on the master map   ← prose, not a one-line tag;
           if this topic leans on a warm-up idea, **inline** link e.g.
           [sets warm-up](./PREREQUISITES.md#p1-sets) (not only the top banner)
     b) ### Board / screenshot  (+ image; caption what to notice)
     c) ### What he is establishing  ← **~80% teaching budget**; mini-lesson from claim sheet:
           all Must-teach claims; concrete case → plain claim → wrong vs right →
           symbols after English → ownership close **in flowing prose**
           (NO bold **Wrong move:** / **You can now:** stamp blocks — tutor-voice.md)
           Blindfold test + claim test. formulas/code/clicks per scenarios.md
     d) ### Analogy for this topic only  ← **~10%**; confirms **this** topic only
           (does not introduce primary definitions; does not teach Topic N+1 —
           tutor-voice.md scope gate)
     e) ### Local picture  (ASCII relation + micro numbers; **required for board procedures**;
           “Notice: …”; diagrams-and-mermaid.md)
     f) ### Bridge  ← real leftover problem → next box (full sentences)
5. ## External references  (2–6 real links from web_search — **quality rules in global-agent.md**)
     - Each link maps to a **topic / map box** from THIS video  
     - Mix when possible: original/primary + university lecture/video + solid blog/interactive  
     - Prefer table: Resource | Matches lecture… | Why it helps  
     - Fail if only generic Wikipedia dumps with no topic mapping  
6. ## Apply it (scenarios)   ← ONLY if content_type requires it (production-scenarios.md)
7. ## Sources
```

## Writing quality (mandatory)

- Follow **`tutor-voice.md`**, **`writing-examples.md`**, **`transcript-mining.md`**  
- Student-facing NOTES must **not** show `content_type:` meta lines (metadata.json only)  
- “What he is establishing” fails QA if it is only a bullet list with no narrative  
- Establishing fails QA if thinner than the topic claim sheet (missing Must-teach claims)  
- **Fail:** bold stamp checklists (`**Wrong move:**` / `**You can now:**` on every topic)  
- **Fail:** analogy that advances the next topic’s claim  
- **Fail:** bare acronym first-use (FA, RE, …) without expansion for beginners  
- **Fail:** Exec Summary that is only a TOC, abstract, or linear bullet list without architecture ASCII  
- Soft depth: hard middle topics get richer paragraphs; do not pad with empty map tags  
- External refs must be **useful study companions**, not filler SEO  

## Completeness (mandatory)

- Mine claims **before** NOTES (`raw/claims/`, `raw/coverage-checklist.md`)  
- End-of-lecture review lists, slogans, and board procedures are not optional asides  
- See `scenarios.md` for type-specific must-capture lists (`math_technical`, …)

## Forbidden

- Flat timeline essay without master architecture  
- 15–30 micro-topics  
- Topics that do not refer to the master map  
- Technique-label spam (ELI5 / Feynman / Toy as section brands)  
- **Slide-deck notes:** only bullets under every topic  
- **Robot bridges** and empty map tags  
- **Ownership stamp blocks** (bold Wrong/Right/You can now checklist every topic)  
- **Thin Exec Summary written first** and never rewritten after topics  
- Duplicating the full lecture inside PREREQUISITES  
- Copying an older package layout when it conflicts with this contract  
- Forcing 2 Mermaid diagrams per topic  
- Calling Vertex / storing cloud project IDs  
- **Quiz with all correct answers in key A** (see quiz-spec.md)  

## Quality bar on disk (structure)

Use an existing package built under this skill as a structural reference only after verifying that it follows the current contract and its path exists.

### NOT a structure template

`educative.io/.../amazon_dynamodb_paper_explained*` is useful for **depth/prose energy**, but it uses **~31 rigid 3-minute topics**. That is the **micro-topic anti-pattern** this skill forbids. Never copy its topic count or uniform time-slicing.

## Pedagogy (woven, not labeled)

why-before-definition · concrete example · contrast when useful · one analogy · bridge sentence  

## vs full educative Vertex pipeline

| Keep from your Python research | Do not port |
|--------------------------------|-------------|
| Blog spine + overview ASCII | Vertex / Gemini API |
| Type registry as depth knobs | Image-gen concept art |
| Code/repo extraction rules | 2 Mermaids per topic mandate |
| Safe Mermaid allow/ban list | 20–30 micro-topics |
| Production scenario *ideas* | Cloud project config |
| Frame priority by type | Running the .py analyzer as required |
