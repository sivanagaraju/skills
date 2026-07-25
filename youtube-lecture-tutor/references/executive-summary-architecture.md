# Executive Summary — architecture blueprint (mandatory)

**Load this file whenever writing or rewriting the NOTES `## Executive Summary` section.**  
It is the **only** Exec Summary law. `output-blog-contract.md` points here; do not improvise a thin “bullet map” or a TED opening monologue.

**Persona:** senior technical blogger + information architect + engineering documentation writer  
(15+ years of math / ML / systems blogs). You are **not** summarizing a talk.  
You are **reverse-engineering the lecture into a system architecture** the student can hold in one view.

---

## What Exec Summary is (and is not)

| Is | Is not |
|----|--------|
| Architecture phase of a design doc | Abstract of the video |
| Blueprint: components, arrows, failure paths, STOP boundary | TOC restated as bullets |
| Diagram-first story a smart beginner can walk | Acronym soup |
| Written after topics exist (post-hoc) | Skeleton drafted first and frozen |
| Same *file place* (before Topic 1) | Scattered mid-NOTES |
| Short concrete lead that orients the blueprint | Magazine / TED prose about what ML “really is” |

**Test:** “If this were a service design doc, would a new engineer understand the *system* before reading the modules?”  
If no → rewrite.

**Lead test:** Read only the first 4–6 sentences with the diagram hidden. Can the student state the **job**, the **method**, and the **fork/payoff** in plain words? If the lead is a philosophical riff or a “not X, but Y” sermon, rewrite.

---

## Approaches considered (pick the recommended hybrid)

| # | Approach | When it shines | Risk |
|---|----------|----------------|------|
| A | **Prose-only** “in this lecture we…” | Soft skills talks | No architecture; forgettable |
| B | **TOC rename** (Topic 1…8 as “key ideas”) | Lazy structure | Zero teaching; AI-slop smell |
| C | **Linear pipeline only** (A→B→C→D) | Pure procedure lectures | Misses forks, failures, contrast |
| D | **C4-style layers** (context → containers → components) | Software / systems | Can feel heavy for math |
| E | **Concept architecture + scenario swimlanes** (boxes, arrows, mini-boxes, worked scenario) | **Math/ML theory, FA, probability** | Needs discipline on ASCII clarity |
| **★ F** | **Hybrid (recommended default):** short architect prose + **system context** + **main blueprint (boxes/arrows)** + **1 scenario walkthrough** + **STOP / out-of-scope** + closed-book “load-bearing claims” | Almost all MFML / NPTEL packages | Over-drawing if you skip the prose lead; TED lead if you over-write the prose |

**Default for this skill = Approach F.**  
Math lectures get the same *shape* as an engineering architecture section: context, components, data/idea flow, failure mode, boundary.

---

## Design principles (from architecture practice)

1. **One primary blueprint** — the star of Exec Summary (not three competing maps).  
2. **Boxes = durable concepts** the lecture installs (Ω, event, *P*, RE…), not topic titles.  
3. **Arrows = named relations** (produces, sizes, fails when, refines with…).  
4. **Mini-boxes** for sub-parts inside a larger stage (e.g. cake rules under *P*).  
5. **Scenario strip** — one concrete walkthrough (X-ray, planet, API…) through the blueprint.  
6. **Failure / contrast lane** — physics-first blocked, wrong default, trap.  
7. **STOP boundary** — what this video does *not* finish (honest scope).  
8. **Legend** if you use dashed boxes, double arrows, or “blocked” marks.  
9. **Expand acronyms** on first use in the Exec Summary prose (FA, RE, …).  
10. **ASCII only** here (skill is ASCII-first; no Mermaid required in Exec Summary).  
11. **Lead serves the blueprint** — short, concrete, no TED frame.

---

## Mandatory section recipe (finished NOTES)

Keep the heading:

```markdown
## Executive Summary — architecture of this lecture
```

(Alias OK: `## Executive Summary — whole lecture in one map` for older packages; prefer “architecture of this lecture” going forward.)

### Block order (do not reorder)

```
1. Architect’s lead (3–6 short sentences)  — job, method, fork/payoff; plain English
2. Worldview arc (1 sentence)              — from ___ to ___ when the lecture has a shift
3. System context (small ASCII)            — who/what sits outside this lecture’s system
4. ★ Main blueprint (large ASCII)          — boxes, arrows, mini-boxes; 20–45 lines typical
5. Scenario walkthrough (ASCII or short numbered path through the blueprint)
6. Failure / contrast callout              — prose or small ASCII “blocked path”
7. STOP / out of scope                     — later lectures; not a dump of future TOC
8. Load-bearing claims (5–8 bullets)       — closed-book; claims not topic renames
9. Course/speaker one-liner if known
```

### Fail if any of these

- Only a two-column “last lecture | this lecture” rename  
- Only a vertical list of topic titles  
- Only arrows with no box labels  
- Exec Summary thinner than a single topic establishing  
- Bare FA/RE on first mention  
- No scenario path through the diagram  
- No STOP boundary when the lecture clearly defers material  
- **TED / negation lead** (see below)  
- Lead longer than the blueprint (prose essay + thin diagram)  

---

## Architect’s lead — hard writing law

The lead is a **door into the diagram**, not a standalone essay.

### Must do

- **3–6 short sentences** (not one long periodic sentence).  
- Name the **job** in concrete terms (what you have; what you must answer).  
- Name the **method** the lecture installs (guess family + refine; axioms; pipeline stages…).  
- Name the **fork or payoff** if the lecture has one (physics blocked → stats; RE → Ω → *P*…).  
- Expand acronyms on first use.  
- Prefer plain verbs: *defines, installs, fails, forces, maps*.  

### Must not (AI-slop / TED frame)

| Ban | Why it fails |
|-----|----------------|
| Opening with **“is not …”** / **“not just …”** / **“not merely …”** | Negation sermon; delays the actual job |
| **“in this course’s opening frame”** / **“the lecture frames ML as”** | Meta stage direction, not architecture |
| Magazine cadence: one 60+ word sentence packing problem + method + philosophy | Unreadable; sounds generated |
| Soft-focus nouns without operators: *journey, landscape, tapestry, paradigm shift* | Empty |
| “Unlock / dive deep / comprehensive overview / in today’s world” | Stock AI |
| Quoting sklearn folklore as the hook (“import a library and call fit”) unless the **teacher** used that line as a load-bearing contrast — and even then, put the **job** first | Audience-bait lead |

### Bad lead (void — real failure mode)

```markdown
Machine learning, in this course’s opening frame, is not “import a library and call fit.”
It is the classical scientific job of **function approximation (FA)**: something maps
allowed inputs to outputs; you only see a finite notebook of pairs; you must answer
new inputs you never wrote down. The system this lecture installs is a pipeline from
that problem, through a deliberate **guess + refine** method, into a fork where
**physics-first** modeling often fails on human-semantic targets and **statistical /
probabilistic** modeling takes over.
```

Problems: TED negation open; “opening frame”; one breathless system-description sentence; diagram has to rescue the prose.

### Good lead (same lecture, architecture-first)

```markdown
This lecture defines the job: estimate an unknown function \(f\) from a finite table of
input–output pairs, then answer new inputs that were never in the table. It installs the
method—guess a **model family**, refine with data via an **algorithm**—and shows why
memorizing the table fails. It then blocks the physics-first path for many human labels
(sensors ≠ “disease”) and turns the course toward **statistical / probabilistic** modeling.
```

Short. Concrete. No “is not fit().” The blueprint below carries the boxes.

### Another good shape (probability lecture)

```markdown
Once function approximation needs uncertainty language, this lecture installs the
measurement stack: random experiment → sample space Ω → events → probability measure P.
It spends the hour on what each object is for and which axioms P must obey—not on RVs yet.
```

---

## ASCII vocabulary (use consistently)

```
  ┌──────────────┐
  │  COMPONENT   │     solid box = concept this lecture installs
  └──────┬───────┘
         │ produces / sizes / maps
         ▼
  ┌──────────────┐
  │  NEXT STAGE  │
  └──────────────┘

  ╔══════════════╗
  ║  GOAL / USER ║     double box = external goal or actor (context)
  ╚══════════════╝

  ┌ · · · · · · ┐
  │  deferred   │     dotted = out of scope / later lecture
  └ · · · · · · ┘

  ──X──►                  blocked / fails path
  ══════►                 main happy path (optional emphasis)
  (mini)  P(Ω)=1 · ≥0     mini-row inside a box for properties
```

Keep width ~60–72 characters when possible so GitHub markdown stays readable.

---

## Write order (agent process — critical)

**File position never moves:** Exec Summary stays **after TOC, before Topic 1**.

**Authoring process:**

```
After topic 1 is solid:
  → open/update raw/exec-architecture-draft.md
  → add/adjust boxes this topic installed + arrows + one scenario note

After each later topic:
  → merge new components into the draft blueprint
  → fix wrong arrows; add failure path if this topic is a trap
  → do NOT leave the student-facing Exec Summary frozen from step 0

After ALL topics + bridges done:
  → ★ write final ## Executive Summary into NOTES.md (full recipe above)
  → rewrite the lead last: 3–6 plain sentences pointing at the finished blueprint
  → delete thin pre-pass if any; draft file may remain agent-only
```

### Required draft headings (agent file)

Use these `##` sections so structure is checkable without gaming NOTES:

```markdown
# Exec architecture draft — <title>

## Components
- …

## Arrows
- … → …

## Scenario
- …

## Failure
- …

## STOP
- …   # or ## Scope

## Claims
- …   # load-bearing closed-book claims
```

Validator: missing draft → **WARN** (current packages). Present draft with missing sections → **WARN**. Empty keyword stuffing in student Exec Summary is still a writing fail (human/agent).

**Never** ship a skeleton Exec Summary written before topics.  
**Always** rebuild from the reverse-engineered architecture of the finished NOTES.

Optional agent artifact (not student-facing):

```
raw/exec-architecture-draft.md
```

---

## Worked shape (math / probability lecture — pattern only)

```
  ╔════════════════ GOAL ════════════════╗
  │  Predict labels on new inputs        │
  │  (function approximation / FA)       │
  ╚══════════════════╤═══════════════════╝
                     │ needs estimate of f
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   ┌─────────────┐       ┌─────────────┐
   │ physics-first│       │ statistical │
   │ model of f   │       │ many obs.   │
   └──────┬──────┘       └──────┬──────┘
          │                     │
       ──X──► often blocked     │ enters probability toolkit
     (coin dynamics /           │
      light ≠ disease label)    ▼
                     ┌──────────────────────┐
                     │ random experiment RE │
                     └──────────┬───────────┘
                                │ outcomes
                                ▼
                     ┌──────────────────────┐
                     │ sample space Ω       │
                     │ (may be non-numeric) │
                     └──────────┬───────────┘
                                │ subsets = events
                                ▼
                     ┌──────────────────────┐
                     │ F  then  P : F→[0,1] │
                     │ mini: P(Ω)=1 · ≥0 ·  │
                     │ disjoint add         │
                     └──────────┬───────────┘
                                │
                     ┌ · · · · ·┴ · · · · · ┐
                     │ STOP: RVs / pushfwd  │
                     │ distributions later  │
                     └ · · · · · · · · · · ┘
```

Then a **scenario** strip (X-ray walkthrough through the same boxes).

---

## Calibration: bad vs good

### Bad (void) — TOC rename

```markdown
## Executive Summary
This lecture covers probability basics.
Key ideas:
1. Random experiment
2. Sample space
3. Events
4. P
```

### Bad (void) — TED lead (architecture may exist below and still fail QA)

See “Bad lead” above. Blueprint alone does not redeem a negation-sermon open.

### Good (architecture phase)

- Lead: job → method → fork in plain sentences.  
- One main blueprint with labeled boxes and arrows.  
- One scenario path.  
- STOP boundary.  
- Load-bearing claims a student can recite closed-book.

---

## Content-type knobs

| Type | Emphasize in blueprint |
|------|------------------------|
| `math_technical` | Concept boxes, derivation/procedure arrows, failure of pure formalism, STOP for deferred theory |
| `code_tutorial` | Pipeline stages, files, commands as mini-boxes, run order arrows |
| `tool_product` | UI / config stages as boxes; before→after path |
| `theory_concept` | Framework boxes + contrast fork |
| `mixed` | Primary thread only in main blueprint |

---

## Checklist before “done”

- [ ] Loaded this file and followed block order  
- [ ] Wrote Exec Summary **after** topics (draft updated per topic optional; final write last)  
- [ ] **Lead** is 3–6 plain sentences; no TED / “is not fit()” open  
- [ ] Main ASCII has **boxes + named arrows** (not only a list)  
- [ ] At least one **scenario** path through the diagram  
- [ ] Failure/contrast and **STOP** present when applicable  
- [ ] Acronyms expanded on first use  
- [ ] Load-bearing claims ≠ TOC renames  
- [ ] Student can read Exec Summary alone and sketch the system on paper  

---

## Related skill files

- `output-blog-contract.md` — file order + pointer here  
- `diagrams-and-mermaid.md` — ASCII craft for local pictures (Exec Summary uses this vocabulary too)  
- `topic-planning.md` — worldview arc feeds the blueprint; screenshot assignment is separate  
- `tutor-voice.md` — prose quality (no slop; Exec lead is stricter still)  
