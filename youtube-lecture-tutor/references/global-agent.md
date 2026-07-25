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

Do **not** dump 5 random Wikipedia links. External references must **map to this video’s topics** and help a student who did not fully understand the board.

### What to find (prefer quality order)

1. **Original / primary sources** when the teacher quotes or implies them (papers, classic course notes, PDFs)  
2. **University lectures** on YouTube (Caltech, MIT OCW, NPTEL siblings, 3Blue1Brown, StatQuest, etc.) that parallel the same idea  
3. **Original pedagogical blogs** (named authors, Distill-like, serious ML/math blogs — not pure SEO listicles)  
4. **Interactive demos** (Seeing Theory, visualizers) when probability/geometry is involved  
5. Medium / GeeksforGeeks only if better sources fail — never as the whole list  

### How to search

- Run **several** `web_search` queries from the lecture’s actual topics (not only the video title)  
- Example queries: `"function approximation" supervised learning blog`, `hypothesis class overfitting explained university`, concept + `lecture site:edu`  
- Prefer free + stable URLs; `web_fetch` / open when possible to verify the page matches the claim  

### How to write `## External references`

- **2–6 links** total (validator soft-warns outside this band)  
- Each link: **title + URL + what lecture topic it matches + one concrete why**  
- Prefer a **markdown table** (Resource | Matches lecture… | Why it helps)  
- Add a short **“How to use”** line: study order after which topics  
- Fail writing gate if links are generic (“Wikipedia ML”) with no topic map  

4. Do **not** scatter long external-link essays inside PREREQUISITES (keep warm-up short)  
5. Never invent URLs

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
