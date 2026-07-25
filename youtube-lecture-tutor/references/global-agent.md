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

Do **not** dump random Wikipedia/SEO links. External references must **map to this video’s topics** and help a student who did not fully understand the board.

### Band (package total — not per topic)

| Rule | Value | Why |
|------|-------|-----|
| **Floor** | **≥ 3** links | Two links is too thin for multi-box lectures |
| **Ceiling** | **≤ 8** links | Beyond this becomes a dump; quality drops |
| **Not** 3–8 *per topic* | — | That would explode to 24–80 links; void |

**“Floor by topic” means coverage quality, not link spam:**

- Every link **must** name which lecture topic / map box it supports.  
- Prefer **spread** across hard topics (not 8 links all on Topic 1).  
- You do **not** need one dedicated link for every topic (e.g. 8 topics can still be well served by 5–6 strong companions).  
- Soft guide: for **≥ 6** topics, prefer **≥ 4** links if good sources exist; still never invent URLs to pad.

Validator: soft-WARN outside **3–8** total http(s) links in the External references section.

### What to find (prefer quality order)

1. **Original / primary sources** when the teacher quotes or implies them (papers, classic course notes, PDFs)  
2. **University lectures** on YouTube (Caltech, MIT OCW, NPTEL siblings, 3Blue1Brown, StatQuest, etc.) that parallel the same idea  
3. **Original pedagogical blogs** (named authors, Distill-like, serious ML/math blogs — not pure SEO listicles)  
4. **Interactive demos** (Seeing Theory, visualizers) when probability/geometry is involved  
5. Medium / GeeksforGeeks only if better sources fail — never as the whole list  

Prefer a **mix** of types when possible (not all Wikipedia, not all one channel).

### Deep research before adding a link (mandatory process)

Do **not** paste the first search hit. For each candidate:

1. Build queries from **topic titles / claim keywords** (not only the video title). Run **several** `web_search` passes.  
2. Prefer free + stable URLs (`.edu`, OCW, known authors, arXiv/PDF when primary).  
3. **`web_fetch` / open** when possible — confirm the page actually teaches the same idea (not a title-only match).  
4. Reject: dead links, pure SEO listicles, unrelated “ML overview” pages, paywalled-only if a free equal exists.  
5. **Never invent URLs.** If research fails for a topic, omit that slot rather than fabricate.  
6. Only then add the row to the table.

Example queries: `"sample space" probability lecture site:edu`, `Kolmogorov axioms intuitive`, concept + `MIT OCW`, concept + `interactive`.

### How to write `## External references`

- **3–8 links** total for the whole package (see band above).  
- Each link: **title + URL + which lecture topic it matches + one concrete why**.  
- Prefer a **markdown table** (Resource | Matches lecture… | Why it helps).  
- Add a short **“How to use”** line: study order after which topics (e.g. after Topics 5–8).  
- Fail writing gate if links are generic (“Wikipedia ML”) with no topic map.  
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
