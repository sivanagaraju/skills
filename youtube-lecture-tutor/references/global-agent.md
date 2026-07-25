# Global agent behavior (do not make the user repeat)

## Before acting

1. **Understand the real goal** — restate silently: package? only notes? fix quiz? series?
2. **360° scan** — student level, series folder, prior lectures, missing basics, time length, math vs code
3. **Do not lock one path early** — hold 2–3 viable approaches; pick with evidence (transcript, folder, user answer)
4. **Mid-course check** — after outline/plan, ask: “Is this architecture still solving the stated goal?” If no, redirect

## Human in the loop (only when needed)

**Invoke HIL** when **all** of these are true:

- You already have a concrete plan (and architecture/ASCII of the package or argument), **and**
- Something is still outside solid inference, **and**
- Confidence on the *required goal* is low or options change the deliverable a lot

**Do not** HIL for routine ingest, obvious folder names, or pure execution after goals are clear.

### How to ask

Use multiple-choice style questions (e.g. `ask_user_question` when available):

- 3–4 clear options first (recommended option labeled)
- **Always include an “Other / comment” style option** so the user can type free input
- One focused decision at a time when possible
- Never block on style nits if default is good

## Subagents

Use subagents when parallel work helps:

- **explore**: scan series folders / prior NOTES for continuity
- **plan**: architecture of package or lecture beat map when complex
- **general-purpose**: long ingest or large write isolation if useful

Orchestrator keeps quality gate and user-facing confidence.

## Web search for learning sources (mandatory for every package)

**When this file is loaded:** staged step “External links / HIL / confidence” in `SKILL.md` (and whenever writing `## External references` or the done-message confidence block). Not part of the hot core — open it **after** topics exist so links map to real map boxes.

Do **not** dump Wikipedia or SEO filler. External references must **map to this video’s topics** and help a student who did not fully understand the board.

### Band (package total — not per topic)

| Rule | Value | Why |
|------|-------|-----|
| **Floor** | **≥ 3** links | Two links is too thin for multi-box lectures |
| **Ceiling** | **≤ 8** links | Beyond this becomes a dump; quality drops |
| **Target shape** | **3–5** strong items is ideal | Prefer depth over a long mixed dump |
| **Not** 3–8 *per topic* | — | That would explode to 24–80 links; void |

**“Floor by topic” means coverage quality, not link spam:**

- Every link **must** name which lecture topic / map box it supports.  
- Prefer **spread** across hard topics (not 8 links all on Topic 1).  
- You do **not** need one dedicated link for every topic (e.g. 8 topics can still be well served by 3–5 strong companions).  
- Soft guide: for **≥ 6** topics, prefer **≥ 4** links if good sources exist; still never invent URLs to pad.

Validator: soft-WARN outside **3–8** total http(s) links in the External references section; WARN if **Wikipedia is the majority** or the only type.

### Allowed source types (wide net — quality first, not pedigree)

Pick **whatever teaches this lecture’s idea well**. Do **not** restrict the list to “university only” or “famous blog only.”

| Type | Examples (not a closed list) | When it shines |
|------|------------------------------|----------------|
| **YouTube / video** | University courses **and** independent teachers: Caltech LFD, MIT OCW, NPTEL, 3Blue1Brown, StatQuest, Khan Academy, Veritasium-style explainers, solid channel deep-dives, workshop talks | Worked intuition, board-style walkthroughs, visual demos |
| **Blogs / long-form articles** | Named ML/math blogs **and** other strong posts: Chris Olah, Distill, Lilian Weng, Sebastian Ruder, company research blogs (Google AI, OpenAI, DeepMind, Meta AI, …), good Substack/dev blogs if the content is real teaching | Depth, diagrams, modern framing of one claim |
| **Course notes / tutorials** | Course sites, free chapter notes, official library tutorials (scikit-learn user guide, NumPy tutorials) when they map to a board idea | Step chains, definitions with code |
| **Primary / original** | Papers, classic notes, dataset homes (MNIST), books’ free chapters when the teacher quotes them | Faithfulness to source of a slogan or experiment |
| **Interactive demos** | Seeing Theory, visualizers, observable notebooks | Probability, geometry, sampling |

**Mix is good:** e.g. 2 videos + 1–2 blogs, or 1 course lecture + 1 explainer video + 1 blog. Same-channel spam is weaker than diverse types that hit different map boxes.

### Quality bar (this is the filter — not the brand name)

A link is good if **all** hold:

1. It actually teaches the **same claim / map box** as this lecture (not a vague “ML overview”).  
2. A student can use it with NOTES closed for *that one idea*.  
3. It is free to read/watch (or free equal preferred over paywall).  
4. It is not Wikipedia filler, pure SEO listicle, or keyword-stuffed “Top 10 ML” page.

A small independent YouTube video or a lesser-known blog **beats** a famous university page that only tangentially matches.

### What to de-prioritize (not banned, but weak as the whole list)

- Medium / GeeksforGeeks / “top N tools” posts — use only if nothing better maps the claim  
- Generic marketing pages, tool landing pages without teaching  
- Same idea rehashed six times on six SEO sites  

### Wikipedia ban (product rule)

| Rule | Detail |
|------|--------|
| **Default** | **Zero** Wikipedia links in `## External references` |
| **Why** | Students can find wiki themselves; package links should be *teaching companions* (video, blog, notes, demo) |
| **Hard fail smell** | Two+ Wikipedia rows, or wiki as the only “formal” orientation |
| **Rare exception** | At most **one** wiki row if no free non-wiki source exists *and* the row still maps to a topic — still prefer a video/blog first |

### Deep research before adding a link (mandatory process)

Do **not** paste the first search hit. For each candidate:

1. Build queries from **topic titles / claim keywords** (not only the video title). Run **several** `web_search` passes.  
2. Search **both** video and article forms: `concept explained youtube`, `concept blog tutorial`, `concept lecture`, `concept -wikipedia`.  
3. Prefer free + stable URLs; university is fine when it fits — **not required**.  
4. **`web_fetch` / open** when possible — confirm the page/video actually teaches the same idea (not a title-only match).  
5. Reject: Wikipedia-as-filler, dead links, pure SEO listicles, unrelated overview pages, paywalled-only if a free equal exists.  
6. **Never invent URLs.** If research fails for a topic, omit that slot rather than fabricate.  
7. Only then add the row to the table.

Example queries: `function approximation learning problem youtube`, `overfitting table lookup explained`, `sample space probability visual`, `semantic gap sensors labels ML blog`.

### How to write `## External references`

- **3–8 links** total for the whole package; **3–5 excellent** beats 8 mediocre.  
- Each link: **title + URL + which lecture topic it matches + one concrete why**.  
- Prefer a **markdown table** (Resource | Matches lecture… | Why it helps).  
- Add a short **“How to use”** line: study order after which topics.  
- Fail writing gate if links are generic Wikipedia dumps with no topic map.  
- Do **not** put long external-link essays in PREREQUISITES (keep warm-up short).  

## Confidence (always report at the end)

Give an honest accuracy confidence for the package:

| Band | When to use |
|------|-------------|
| **High (≈85–95%)** | Captions good, claims match transcript, diagrams checked, quiz dual-part ok |
| **Medium (≈60–85%)** | Some ASR gaps, a few inferred bridges marked, external links not fully opened |
| **Low (<60%)** | Missing captions, ambiguous syllabus, or user goal still unclear — prefer HIL or partial deliverable |

State **what would raise confidence** (e.g. “re-watch board at 12:00”, “confirm playlist index”).

## Safety / fidelity

- No Vertex / cloud project IDs
- No invented theorems
- Faithful to this video’s content
