# LOCKED — NOTES + PREREQUISITES blog contract

**This is the only NOTES structure.** Flat timeline essays without a master map are void.

Prompt-library origin: educative `gemini_youtube_analyzer_v6_0.py` structured blog + type rules  
**Agent-native:** no Vertex; depth rules live in `scenarios.md`, `code-extraction.md`, `diagrams-and-mermaid.md`, `production-scenarios.md`.

## User-approved choices

| Item | Rule |
|------|------|
| Skeleton | Educative-style (TOC → Exec Summary → Topics → External refs → Apply it → Sources) |
| Topics | **4–10** absolute; count from map + claims (duration soft — topic-planning.md) |
| PREREQUISITES | **Before** map — mandatory 6–8 foundational pillars + Rosetta Stone notation table |
| 5-Point Bridge | Every topic establishes: $\text{👶 ELI5} \iff \text{🔍 Plain-English} \iff \text{🔢 Concrete Numbers} \iff \text{📐 Formal Math} \iff \text{💻 Runnable Code}$ |
| Rigor Law | Zero-leap algebraic derivations; no "it can easily be shown that" hand-waving |
| Contrast Law | Dedicated "Why X, Not Y?" contrastive analysis per topic |
| Diagrams | **ASCII-first** with Unicode box-drawing characters, relation rule, and `Notice:` captions |
| Connect-the-dots | Every topic points back to **one master architecture** and links `examples/` + `MathsTerms/` |
| Type prompts | Depth knobs only — **same layout** for all types |
| Production scenarios | Required for `code_tutorial` / `tool_product`; 2 Workplace Debugging Postmortems for `math_technical` |

---

## PREREQUISITES.md

- 6–8 foundational pillars covering all core mathematical primitives needed for the master map.
- Includes the **Math Terminology Rosetta Stone Table** with Spoken English phonetics.
- Every pillar features: ELI5 physical analogy, plain-English breakdown, hand-calculated micro-numbers, formal math, runnable Python snippet with assertions, and diagnostic mini-check.
- Stable `<a id="p1-..."></a>` anchors for deep linking from NOTES.
- Not a second full lecture — unlocks the language so the reader never freezes on the master map.
- See `prerequisites-template.md` + `tutor-voice.md`.

---

## NOTES.md — file order vs write order

**File order (student reading):** TOC → Executive Summary → Standalone Simulation Code → Topics 1..N → Workplace Debugging Scenarios → External References → Sources  

**Write order (agent — mandatory):**

```
claim-mine → PREREQS → Topics 1..N from claims
  → after each topic: update raw/exec-architecture-draft.md (boxes, arrows, scenario)
  → author standalone simulation scripts in examples/*.py
  → ★ WRITE final Executive Summary into NOTES (architecture blueprint)
       law: executive-summary-architecture.md
  → Workplace Debugging Scenarios (postmortems)
  → External refs → glossary.md → formulae_sheet.md → quiz
```

Do **not** draft a thin Exec Summary skeleton first and leave it.  
Exec Summary is the **architecture phase** of the document: reverse-engineer the lecture into a system blueprint (not a video abstract).

---

## NOTES.md order (mandatory — finished file)

```
1. Header + link: do PREREQUISITES first (./PREREQUISITES.md)
2. Table of Contents (topics with MM:SS; expand acronyms in titles if beginner)
3. ## Executive Summary — architecture of this lecture   ← final content written LAST
     **FULL LAW:** references/executive-summary-architecture.md
     Required blocks:
     - Architect’s lead prose (job → method → fork in 3–6 short sentences; no TED open)
     - Worldview arc when present (from ___ to ___; expand acronyms)
     - System context (small ASCII)
     - ★ Main blueprint: Unicode ASCII boxes, arrows, mini-boxes (not TOC list)
     - Scenario walkthrough through the blueprint
     - Failure / contrast path
     - STOP / out of scope
     - Comparative Feature / Tradeoff Matrices
     - Load-bearing claims (5–8; not topic renames)
     - Speaker/course if known
     Fail if thin list, two-column rename only, no scenario, no boxes/arrows
4. ## End-to-End Runnable Python/PyTorch Simulation
     Self-contained, runnable simulation demonstrating the core lecture mathematics.
     Points directly to standalone script in `examples/01_*.py`.
5. ## Topic N: Name (MM:SS–MM:SS)   × 4–10 (map/claims first)
     **Prerequisite to drafting:** claim sheet `raw/claims/topic-NN.md` from transcript-mining.md
     For EACH topic, in this order:
     a) ### Where this sits on the master map
        Prose explaining which box and why now.
        Inline link to warm-up idea e.g. [sets warm-up](./PREREQUISITES.md#p1-sets).
     b) ### Board / screenshot
        Image unique to this topic’s MM:SS (`./screenshots/composites/...`).
        Caption transcribes what to notice; never reuse the same composite path.
     c) ### What he is establishing  ← **~80% teaching budget**
        Mini-lesson executing the 5-Point Pedagogical Bridge:
        - 👶 **ELI5 Intuition**: Concrete physical analogy & narrative before formulas.
          (Note: '👶 ELI5 Intuition' progressive heading is approved and encouraged;
           low-effort label spam like standalone '### ELI5' without substance is banned).
        - 🔍 **Plain-English Breakdown**: Software/engineering meaning of the concept.
        - 🔢 **Concrete Micro-Numbers**: Pencil-and-paper worked arithmetic with real numbers.
        - 📐 **Formal Mathematical Formulation & Zero-Leap Derivations**:
          Unabridged algebraic proofs showing EVERY intermediate line.
          Zero hand-waving: strictly ban "it can easily be shown that", "trivially", "obviously".
        - 💻 **Runnable Code & Modern GenAI Systems**:
          How this math operates in PyTorch/NumPy and powers LLMs, Diffusion, VAEs, or GANs.
          Link to standalone script: `[Run verification](./examples/01_numerical_verification.py)`.
        - 🔗 **MathsTerm Link**: `[Softmax](../../MathsTerms/03-Multivariate-Calculus-and-Optimization/06-Softmax.md)`.
     d) ### Contrastive Analysis: Why X, Not Y?
        Explains why naive alternatives fail catastrophically in AI/ML:
        - Approximation bias / numerical instability / floating-point cancellation
        - Computational complexity ($O(N^3)$ vs $O(N)$)
        - Memory explosion (e.g. materializing full Jacobian vs VJP contraction)
        - Curse of dimensionality
     e) ### Analogy for this topic only  ← **~10% budget**
        Confirms THIS topic only (scene → instances → question → right → wrong → rename).
        Does not introduce primary definitions; does not advance Topic N+1.
     f) ### Local picture
        Unicode ASCII diagram (`┌─┐│└▼═╔║`) showing structural relation + micro-numbers.
        Mandatory `Notice: ...` caption explaining the geometric/architectural takeaway.
     g) ### Bridge
        Real leftover problem in full sentences → next map box.
6. ## Workplace Debugging Scenarios (Postmortems)   ← Required for technical/math packages
     2 real-world engineering postmortems:
     - Scenario 1: Numerical Instability / Vanishing Gradient / Shape Mismatch / NaN blowup
     - Scenario 2: Memory Out-of-Memory (OOM) / Computational Bottleneck / Sampling Degeneracy
     Each scenario structured as: Problem → Root Cause Analysis → Debugging Steps → Python Code Fix.
7. ## External references  (**15–25 curated links** organized by category)
     - Category 1: Foundational & Seminal Papers (arXiv/IEEE/NeurIPS)
     - Category 2: Authoritative Textbooks & University Courses (Goodfellow, Murphy, Boyd, Prathosh)
     - Category 3: Industry & Production Implementation Guides (PyTorch docs, Hugging Face, Triton)
     - Each link mapped to a topic/concept; zero broken or invented URLs.
8. ## Sources
```

---

## Writing quality (mandatory)

- Follow **`tutor-voice.md`**, **`writing-examples.md`**, **`transcript-mining.md`**  
- Student-facing NOTES must **not** show `content_type:` meta lines (metadata.json only)  
- “What he is establishing” fails QA if it is only a bullet list with no narrative  
- Establishing fails QA if thinner than the topic claim sheet (missing Must-teach claims)  
- **Fail:** bold stamp checklists (`**Wrong move:**` / `**You can now:**` on every topic)  
- **Fail:** analogy that advances the next topic’s claim  
- **Fail:** bare acronym first-use (FA, RE, …) without expansion for beginners  
- **Fail:** Exec Summary that is only a TOC, abstract, or linear bullet list without architecture ASCII  
- **Fail:** skipping intermediate algebraic steps ("it can easily be shown that", "trivially")  
- External refs must be **useful study companions**, not filler SEO  

---

## Completeness (mandatory)

- Mine claims **before** NOTES (`raw/claims/`, `raw/coverage-checklist.md`, `raw/coverage-receipt.md`)  
- End-of-lecture review lists, slogans, and board procedures are not optional asides  
- Author `examples/*.py`, `glossary.md`, and `formulae_sheet.md` to accompany NOTES  

---

## Forbidden

- Flat timeline essay without master architecture  
- 15–30 micro-topics  
- Topics that do not refer to the master map  
- **Technique-label spam** (standalone `### ELI5` without pedagogical substance, `### Feynman Technique` marketing badges, or `### Toy Problem` labels — note that progressive instructional scaffolding using `👶 ELI5 Intuition` within the 5-point bridge is explicitly mandated)  
- **Slide-deck notes:** only bullets under every topic  
- **Robot bridges** and empty map tags  
- **Ownership stamp blocks** (bold Wrong/Right/You can now checklist every topic)  
- **Thin Exec Summary written first** and never rewritten after topics  
- **Mathematical hand-waving:** "it can easily be shown that", "trivially", "obviously", "after simple algebra"  
- **Floating code snippets:** code not backed by verified scripts in `examples/`  
- Duplicating the full lecture inside PREREQUISITES  
- Forcing 2 Mermaid diagrams per topic  
- Calling Vertex / storing cloud project IDs  
- **Quiz with all correct answers in key A** (see quiz-spec.md)  
