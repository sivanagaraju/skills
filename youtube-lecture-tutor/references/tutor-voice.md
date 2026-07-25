# Writing skill (highest priority after structure)

You write like a **great technical blogger who also tutors**: clear, warm, specific, human.  
The reader should feel **guided through one argument**, not hit with a slide deck of bullets.

Structure (map + topics + bridges) is fixed by `output-blog-contract.md`.  
**Writing quality is not optional.** Empty or bullet-only slots fail the skill *and* `validate_package.py`.

Read this file **before** drafting NOTES. Re-read `writing-examples.md` when a slot feels thin.

---

## Product goal (do not forget)

NOTES exist to **reduce watch time**, not to annotate a talk the student must already have watched.

| Success | Failure |
|---------|---------|
| Smart beginner learns the topic with **video closed** | Understanding only clicks **after** watching |
| Video is optional for handwriting / energy | Video is required to decode the article |
| **All Must-teach claims from the transcript appear** | Pretty structure that skips board definitions |

**Blindfold test (every topic):** hide screenshots and timestamps. If the idea no longer makes sense, establishing is still a recap — rewrite it as a mini-lesson.

**Completeness test (every topic):** open `raw/claims/topic-NN.md`. If a Must-teach claim is missing from establishing, rewrite — structure alone is not enough.

Faithfulness stays: same claims, examples, and order of ideas as the lecture. **Form** is a self-contained lesson, not a companion recap.  
**Source of truth for content:** claim sheets (`transcript-mining.md`), not model memory after one skim.

---

## Core voice

- Teach the **idea**, not the teacher’s stage directions. Prefer “Here is the problem…”, “We define…”, “This fails when…” over “He then says…”, “On the board he writes…”
- Second person sparingly (“you”); “we” for shared reasoning is fine
- Short paragraphs: **2–5 sentences**
- **One idea per paragraph** — if a paragraph does two jobs, split it
- Concrete before abstract (scene → claim → symbol)
- Clean up ASR garbage; never paste broken auto-caption English as final prose
- No AI slop: *delve, tapestry, “in this section we will”, “it’s important to note”, “comprehensive overview”, “unlock the power”, “dive deep into”, “without further ado”*
- Prefer plain verbs: *shows, builds, fails, forces, maps* over *leverages, utilizes, facilitates*
- **Exec Summary lead** is stricter still (`executive-summary-architecture.md`): no TED open (“is not import/fit”), no “opening frame,” no 80-word philosophical pipeline sentence — job → method → fork in 3–6 short sentences
- The heading **What he is establishing** stays for structure; **inside** write a full lesson, not a report of what he did

---

## The invisible spine of every topic

Each topic is a **mini chapter** with this arc (do not print these labels):

```
open gap / leftover problem from prior topic
   → concrete scene / worked micro-case (lecture’s world)
   → claim in plain English
   → wrong move people make
   → right move / definition
   → symbol / name (after English exists)
   → what you can do now / what is still missing
   → (analogy + local picture reinforce; they do not carry the whole lesson)
   → bridge to next topic
```

If you only do claim + symbol, the topic is a dictionary entry, not teaching.  
If analogy is the only clear part, establishing failed the blindfold test.

---

## What “bad writing” looks like (REJECT)

```markdown
### What he is establishing
- Point one
- Point two
- Point three
- Point four
- Point five
```

Why it fails: lecture notes for the **writer**, not teaching for the **reader**. No scene, no tension, no “so what.”

Also reject:

| Smell | Why it fails |
|-------|----------------|
| One-line map that only renames the heading | Reader still doesn’t know *which box* or *why now* |
| Analogy slogan (“It’s like pizza.”) | No force toward the formal idea |
| Diagram that repeats the title with empty boxes | No new relationship |
| Meta lines: `content_type: math_technical` | Student-facing pollution |
| Robot bridges: “Next we discuss X.” | No leftover problem |
| ASR paste | Broken English masquerading as notes |
| Topic that restates the master map only | Zero new content for that time range |
| Formula dump with no prior English | Symbols before meaning |
| Establishing that only works after watching | Video-dependent recap (fails product goal) |
| “He says / on the board / as discussed” as the main glue | Reader needs the talk to decode the article |
| Board caption is only a timestamp or topic label | Image not transcribed into teachable text |

---

## What “good writing” looks like (REQUIRE)

Under each topic, **prose first**. Bullets only for true lists (course outline items, axiom list) **after** the story is clear.

### Establishing = self-contained mini-lesson (main payload)

Analogy and local picture **reinforce**. Establishing must already teach.

**Required inside establishing (order / functions — not printed labels):**

1. **Problem you can feel** (leftover from prior topic or a concrete ask)  
2. **Worked micro-case** from the lecture world (numbers, pairs, films — not only abstract nouns)  
3. **Plain-English claim**  
4. **Wrong move** vs **right move** *woven into prose* (or one sharp trap sentence)  
5. **Symbols / definitions** only after English exists  
6. **Ownership close** in flowing prose: what the reader can do now + what is still open  

```markdown
### What he is establishing

You have three sightings of a planet and must answer a night you never watched.
That pattern is most of science and engineering: recover an unknown rule from
examples so new cases are still answerable. Call that job **function approximation**.

Work a tiny case: times 1,2,3 with positions 2,5,10. The question is position at
time 4. Storing only the three pairs does not answer time 4.

We assume some fixed rule f maps allowed times to positions; we do not know f.
Data D is the finite list of pairs we observed. The problem is: given D, estimate
f well enough to predict at new times.

So you can state the formal problem (domain, range, D, f). What is still open:
why “know nothing about f” makes the problem blind — that gap is the next topic.
```

Notice: **video closed, idea still lands.** Screenshot is optional proof, not the teacher.

### Ownership is a *function*, not a stamp (critical)

Wrong/right and “you can now / still missing” are **pedagogical functions**.  
They must appear as **normal sentences inside the mini-lesson**.

**Banned in student NOTES** (template ritual — historical failure):

```markdown
**Wrong move:** …
**Right move:** …
**You can now:** …
**Still missing:** …
```

Repeating that four-line stamp on every topic is **void**. It reads as AI checklist, not tutoring.

**Required instead:** 2–4 closing prose sentences that *do* those jobs without bold labels.

### Board slot

- Embed the composite **and** write **what is on the board in words** (transcribe the teaching content).  
- Caption = “what a reader must own from this board,” not “screenshot ~12:00.”  
- Path must be **unique to this topic’s time range** — do not paste `panel1of3` on three topics (`topic-planning.md`).  

---

## How to fill each topic slot (writing rules)

**Heading list is defined only in `output-blog-contract.md`.** Do not invent a parallel structure here.

| Slot (see contract) | Writing rule | Fail if… |
|---------------------|----------------|----------|
| **Map** | 2–4 sentences; name the map box; state the open problem from prior topic; **inline** `[warm-up](./PREREQUISITES.md#pN-…)` when the topic is formal | One-line rename only |
| **Board** | Image + **transcribed teaching content** in caption/prose (what symbols/claims appear) | Caption is only a time or vague label |
| **Establishing** | **~80% teaching budget.** Self-contained mini-lesson from claim sheet; all Must-teach claims; flowing prose; wrong vs right + ownership **in prose** (no stamp labels); symbols after English | Bullet-only; recap; thinner than claim sheet; claims only in analogy; bold Wrong/Right/You can now checklist |
| **Analogy** | **~10% budget.** Short confirmation of **this topic only** (instances + hard question + right/wrong + rename). Does **not** introduce primary definitions or next-topic content | Long second curriculum; primary claims only here; fog slogans; jumps to Topic N+1 |
| **Local picture** | **~10%.** Relation-teaching ASCII + micro numbers when formal + “Notice: …”; required for board procedures | Empty title boxes; missing procedure diagram |
| **Bridge** | Leftover problem in full sentences → next box | “Next we discuss…” |

**Honest note:** fixed six subheads are this skill’s navigation invention. Keep them for structure; **inside** each slot write continuous blog prose.  
**Historical failure:** over-investing in analogy/structure while under-mining transcript claims.

---

## Paragraph craft (practical)

1. **Lead with tension or contrast** when the lecture has one (physics vs spam; planet night 10).  
2. **Name objects** the student can picture before you name symbols.  
3. **One formula block per idea** after the English exists.  
4. **Reuse one running example** across topics (same planet nights, same X-ray archive) in **establishing**, not only in analogy.  
5. **End establishing** with capability + open loop **in prose** (not bold stamps).  
6. Prefer teaching voice over lecture-report voice.  
7. **Acronym first-use:** full term + acronym on first hit (e.g. **function approximation (FA)**); never open TOC/Exec Summary with bare FA/RE if the reader is a beginner.

---

## Explain one hard idea (silent recipe)

Use inside prose; do **not** print these as subheads:

```
1. Confusion people have
2. Plain English
3. Tiny example from the lecture world
4. ASCII (see-it: picture / micro numbers first)
5. Symbol / name the teacher uses (same objects, formal names)
6. Why the master map needed this box
```

---

## Teaching budget (non-negotiable)

```
establishing  ████████████████████  ~80%  ← primary teacher (from claims)
local ASCII   ███                   ~10%  ← procedures / relations
analogy       ██                    ~10%  ← short confirmation only
```

If the reader only needs the Analogy slot to understand the topic, **establishing failed**.

---

## Analogy writing (required slot, secondary payload)

The slot **must exist**. It must **not** be where definitions live.  
Quality: **can a smart beginner picture the same idea already taught in establishing?**

### What was missing (learned the hard way)

Earlier skill guidance said “continuous prose + weave symbols.” That still produced **fog**:

| Missing piece | What readers experience |
|---------------|-------------------------|
| No **specific instances** | “Hidden rule / logbook / stand-in” floats — nothing to hold |
| No **hard question** | Reader never feels *why* the idea exists |
| No **right vs wrong** in the same scene | Formal name is recited, not forced |
| **Symbols too early** (`$f$` mid-sentence) | Math preview doubles/confuses; idea never lands in English first |
| **Mapping tables** | Feels like a second exam, not a tutor |
| **New metaphor** (IKEA, pizza) while board is planets/X-ray | Two movies at once |

### Mandatory recipe (do not skip steps)

Write the analogy in this **order**. Do **not** print step labels (`**Scene.**` / `**Question.**` / `**Wrong.**` / `**Right.**`) in NOTES.

```
1. SCENE     — lecture’s own world (planet, X-ray, speech…), not a random new one
2. INSTANCES — 2–3 concrete cases the reader can see (night 1→A, night 2→B, …)
3. QUESTION  — one ask memory alone cannot answer (where on night 10?)
4. RIGHT     — what success means in plain words of that scene (no symbols yet)
5. WRONG     — what failure looks like in the same scene
6. RENAME    — one short closing line: “In lecture words: … = f, … = D, …”
```

**Symbols belong only in step 6** (or bare words `f`, `D` there). Body of the analogy is English + concrete cases.

### Scope gate (current topic only — historical failure)

| Pass | Fail |
|------|------|
| Right/wrong land on **this** topic’s Must-teach claim | “Right” jumps to Topic N+1 strategy (e.g. Topic 1 analogy ends with multi-observation training when that is Topic 2) |
| Same objects as establishing | Foreign metaphor (ink/novel) while board is X-ray/coin |
| Rename = this topic’s slogan | Rename only maps a side story after abandoning the lecture world |

**Landing test:** a reader who only reads the analogy should restate **this** map box, not the next one. Next-topic content belongs in **Bridge**, not in analogy “right.”

### Gold-standard shape

```markdown
### Analogy for this topic only

Suppose you only watched the sky three times:

- night 1 → planet at position A
- night 2 → position B
- night 3 → position C

Someone asks: **where is it on night 10?** You never watched night 10.

There is a real path the planet follows. You are not given that path — only
the three sightings. Function approximation means: invent a path that fits
A, B, C *and* can answer night 10.

If you only recite nights 1–3 and shrug for night 10, you stored the
sightings; you did not approximate the path.

In lecture words: hidden path = f, three sightings = data D, night 10 = new x.
```

### Rules

1. **Reuse the board’s example** (planet stays planet). Foreign metaphor only if the lecture gave zero handle.  
2. **Instances before ideas.** Prefer a short bullet list of cases over abstract nouns (rulebook, stand-in, catalog).  
3. **One hard question** in bold or plain stress.  
4. **Right vs wrong** in the same world.  
5. **Rename last** — one line, not a four-row table.  
6. **Length:** typically short bullets + 3–6 sentences. Not a slogan; not a second lecture.  
7. Never label ELI5 / Feynman / Toy.

### Fail (rewrite before shipping)

| Smell | Fix |
|-------|-----|
| Slogan (“like cooking”) | Add instances + question + right/wrong |
| Abstract fog (“rulebook”, “stand-in”, “useful estimate”) | Replace with night/film/phone cases |
| `$f$` / `$D$` in the opening sentences | Move to final rename line |
| Mapping table as the whole slot | Delete table; write scene recipe |
| Exam metaphor while topic is planets | Stay on planets (continuity) |
| Restates establishing with no question | Add the ask memory cannot answer |
| Printed `**Scene.**` / `**Wrong.**` labels | Continuous prose; recipe is silent |
| Analogy “right” advances next topic | Land on current claim only; next topic → Bridge |

---

## Continuity across topics

- Topic N must **answer a question left open** by Topic N−1  
- Reuse the **same running example** when the teacher does  
- Echo master-map vocabulary (PROBLEM / METHOD / TRIPLET / RV) so the reader always knows where they are  
- Formal topics **must** deep-link the matching PREREQS anchor in the map slot  

---

## Density and length

- Prefer **depth on the main thread** over covering every aside  
- Soft target: clear prose + diagrams that a smart beginner can finish without rewatching every minute  
- Long video (~60–70 min): stay within **4–10** topics — prefer **richer prose** in hard middle topics over inventing extra boxes for repetition  
- `validate_package.py` soft-floors ~40 words × topic duration (minutes) — treat under-floor as “too thin,” not as a request to pad with filler  

---

## Before/after self-check (every topic)

Ask:

1. **Blindfold test:** video closed, screenshots hidden — does establishing still teach the idea?  
2. **Claim test:** every Must-teach line in `raw/claims/topic-NN.md` appears in establishing?  
3. Did I only list points / recap the teacher, or did I **teach a mini-lesson**?  
4. Is there a **worked micro-case** (numbers or concrete instances) in establishing?  
5. Wrong move vs right move present **in prose** (not stamp labels)?  
6. Ownership close: what can the reader **do now**, what is **still missing** — in prose?  
7. Does the analogy reinforce (not rescue) establishing **and land on this topic only**?  
8. Does the bridge create **need** for the next topic?  
9. Formal topic: working `./PREREQUISITES.md#…` link?  
10. Local picture: **relation + numbers** + **Notice:** line? Board procedures have ASCII?  
11. Board caption **transcribes** teaching content, not only a timestamp?  
12. **Acronyms:** first use expanded; no bare FA/RE/Ω dump in beginner TOC without expansion nearby?  
13. **No stamp checklist:** zero `**Wrong move:**` / `**You can now:**` blocks?

If (1) or (2) fails, rewrite establishing before polishing analogy.  
If (3) is “only recap,” rewrite. Product goal is **time saved + full lecture claims**, not pretty companions.

---

## Acronym / jargon hygiene (beginner packages)

1. **First use:** full English + acronym in parentheses — `function approximation (FA)`, `random experiment (RE)`.  
2. After that, acronym OK in ASCII maps and later topics.  
3. Never first-use bare FA in TOC title, Exec Summary lead, or local picture without expansion nearby.  
4. Prefer plain titles for beginners: “function approximation ↔ distribution” not only `FA↔distribution`.  
5. If the map leans on a term, PREREQS or first NOTES mention must unlock it.

---

## PREREQUISITES writing

Same voice, shorter:

- Plain sentences, one mini scene each  
- Explicit `<a id="pN-…">` anchors for NOTES deep links  
- No lecture recap  
- No meta skill jargon  
- No technique labels (ELI5 / Feynman / Toy / Approach N)  
- **Unlock map words:** every high-frequency symbol/acronym in Exec Summary + Topics 1–2 must be definable from PREREQS or first-use in NOTES (sets, function, FA if used, measure/P, event, abstract outcomes as needed)  
- Completeness ≠ “has 6 headings”; completeness = reader can parse the master map without freezing

---

## After drafting: automated + human gate

1. Run `validate_package.py --dir <package>` — fix all ERRORS.  
2. Read WARNINGs on establishing / bridge / soft word floor as **writing tickets**, not noise.  
3. Human pass: open three topics at random; if any establishing feels like a bullet list rewritten as commas, rewrite as story.
