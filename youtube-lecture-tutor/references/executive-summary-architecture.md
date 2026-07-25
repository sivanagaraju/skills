# Executive Summary — architecture blueprint (mandatory)

**Load this file whenever writing or rewriting the NOTES `## Executive Summary` section.**  
It is the **only** Exec Summary law. `output-blog-contract.md` points here; do not improvise a thin “bullet map.”

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

**Test:** “If this were a service design doc, would a new engineer understand the *system* before reading the modules?”  
If no → rewrite.

---

## Approaches considered (pick the recommended hybrid)

| # | Approach | When it shines | Risk |
|---|----------|----------------|------|
| A | **Prose-only** “in this lecture we…” | Soft skills talks | No architecture; forgettable |
| B | **TOC rename** (Topic 1…8 as “key ideas”) | Lazy structure | Zero teaching; AI-slop smell |
| C | **Linear pipeline only** (A→B→C→D) | Pure procedure lectures | Misses forks, failures, contrast |
| D | **C4-style layers** (context → containers → components) | Software / systems | Can feel heavy for math |
| E | **Concept architecture + scenario swimlanes** (boxes, arrows, mini-boxes, worked scenario) | **Math/ML theory, FA, probability** | Needs discipline on ASCII clarity |
| **★ F** | **Hybrid (recommended default):** short architect prose + **system context** + **main blueprint (boxes/arrows)** + **1 scenario walkthrough** + **STOP / out-of-scope** + closed-book “load-bearing claims” | Almost all MFML / NPTEL packages | Over-drawing if you skip the prose lead |

**Default for this skill = Approach F.**  
Math lectures get the same *shape* as an engineering architecture section: context, components, data/idea flow, failure mode, boundary.

---

## Design principles (from architecture practice)

Inspired by architecture-diagram best practices (blueprint of components + relations; clarity over clutter; legend when needed; arrows that mean something) and C4 thinking (context first, then structure, then detail elsewhere).

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

---

## Mandatory section recipe (finished NOTES)

Keep the heading:

```markdown
## Executive Summary — architecture of this lecture
```

(Alias OK: `## Executive Summary — whole lecture in one map` for older packages; prefer “architecture of this lecture” going forward.)

### Block order (do not reorder)

```
1. Architect’s lead (4–8 sentences)     — problem, system goal, payoff; no diagram yet
2. Worldview arc (1 sentence)           — from ___ to ___ when the lecture has a shift
3. System context (small ASCII)         — who/what sits outside this lecture’s system
4. ★ Main blueprint (large ASCII)       — boxes, arrows, mini-boxes; 20–45 lines typical
5. Scenario walkthrough (ASCII or short numbered path through the blueprint)
6. Failure / contrast callout           — prose or small ASCII “blocked path”
7. STOP / out of scope                  — later lectures; not a dump of future TOC
8. Load-bearing claims (5–8 bullets)    — closed-book; claims not topic renames
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
  → delete thin pre-pass if any; draft file may remain agent-only
```

**Never** ship a skeleton Exec Summary written before topics.  
**Always** rebuild from the reverse-engineered architecture of the finished NOTES.

Optional agent artifact (not student-facing):

```
raw/exec-architecture-draft.md
```

Suggested draft fields: components[], arrows[], scenario, failures[], stop[], claims[].

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

### Bad (void)

```markdown
## Executive Summary
This lecture covers probability basics.
Key ideas:
1. Random experiment
2. Sample space
3. Events
4. P
```

### Good (architecture phase)

- Lead prose states the system goal and why the old path fails.  
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
- `topic-planning.md` — worldview arc feeds the blueprint  
- `tutor-voice.md` — prose quality of the architect’s lead  
