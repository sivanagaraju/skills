# Topic planning + frames (map-first + claim-mine later)

## Goal

Topics = **boxes on the master map** for the **reader**.  
Claims = **every teaching unit in the transcript** for **completeness**.

```
1. List teacher moves in order (problem → tools → payoffs → worldview shifts)
2. Draw ONE master ASCII (whole video point)
3. State worldview arc: "from ___ to ___" (required for math/theory)
4. Cluster into map boxes with MM:SS ranges (see topic count rules below)
5. ★ Mine claims per time range (transcript-mining.md) — do not skip
6. Assign screenshots by type priority (below)
```

**Critical:** Topic count means **merge for reading**, not “skip spoken definitions.”  
**Mine every minute for claims; merge claims into topics.** Never drop a definition, slogan, board procedure, or end-of-lecture review list.

---

## Master map test (required before writing)

> “This video moves the student from ___ to ___.”

Examples:

- “from function approximation slogan to model+algorithm workflow”  
- “from deterministic FA to probabilistic / distribution estimation”  
- “from sample space to probability measure P”

If blank, do not write NOTES yet.

### Worldview / contrast test (math & theory)

If the lecture contrasts two frameworks (deterministic vs probabilistic, physics vs statistics, …), the **Exec Summary map must show both** and at least one topic must teach the **shift**, not only one side.

---

## Topic count (map + claims first; duration is soft)

**One-liner:** Topic count follows the **architecture map and claim clusters**. Duration only suggests a soft range. Prefer **deeper** topics over more topics when the teacher stays on one system; prefer **more** topics when a short video installs many distinct objects.

### Primary signal — map architecture

Topics = **boxes on the master map**, not “minutes of video.”

**Split** into a new topic when at least one holds:

- New **problem / obstacle** the prior box cannot solve  
- New **object or definition** that must stick (e.g. RE vs Ω vs *P*)  
- New **board procedure** (stacking, derivation, axiom list)  
- New **worldview shift** (physics path → stats path)  
- A distinct **trap** that needs its own wrong/right treatment  

**Do not split** when:

- Same claim with more examples or emphasis  
- Pure timestamp gap (still the same map box)  
- Teacher loops on one system for a long time  

**Claim-mine support:** a coherent cluster of Must-teach claims → one topic; a new cluster → new topic. Mine densely; merge for reading.

### Secondary signal — duration (soft guide only)

| Duration | Soft guide (not law) |
|----------|----------------------|
| ~15–25 min | often **4–8** (more if dense definitions; fewer if one arc) |
| ~25–45 min | often **6–10** |
| ~45–90 min | often **7–10** — deepen middle topics; do **not** invent boxes for repetition |

### Hard bounds (always)

| Bound | Rule |
|-------|------|
| **Floor** | At least **4** topics (full package) — below this the map collapses into an essay |
| **Ceiling** | At most **10** topics — above this is micro-topic anti-pattern (forbidden) |

Do **not** use 20–30 micro-topics.  
Do **not** pad to 10 because the video is long.  
Do **not** under-split a dense short lecture into 4 thin topics that omit claims.

### Decision table

| Situation | Action |
|-----------|--------|
| Same definition for 15 min with 3 examples | **One** topic; deep establishing |
| Three co-defined terms each need wrong/right + ASCII | Prefer **separate** topics |
| 20 min with many slogans/definitions | Prefer **more** topics (up to 10), each with real Must-teach weight |
| 70 min recap looping one system | Prefer **fewer** topics + richer establishing; no Topic-1a / Topic-1b clones |

---

## Per-topic checklist

- [ ] Map box named  
- [ ] Timestamp range  
- [ ] `raw/transcript-by-topic/topic-NN.txt` sliced  
- [ ] `raw/claims/topic-NN.md` filled (definitions, procedures, slogans, ~times)  
- [ ] Screenshot path or “no content frame — ASCII only”  
- [ ] Establishing will teach **all** Must-teach claims  
- [ ] ASCII for every board **procedure** in this range  
- [ ] Analogy short confirmation only  
- [ ] Bridge to next map box  
- [ ] Type-specific extras filled (formulas / code / clicks) per `scenarios.md`  

---

## Frame / screenshot priorities (from analyzer `priority_frames`)

When selecting or labeling frames, prefer:

| content_type | Prefer capturing |
|--------------|------------------|
| math_technical | formula, derivation, graph, whiteboard |
| code_tutorial | code_editor, terminal, output, error |
| tool_product | ui_screen, configuration, result, comparison |
| theory_concept | concept_text, diagram, comparison_table, framework |
| research_review | formula, graph, table, benchmark_result |
| soft_skills | concept_text, framework, comparison_table |
| mixed | concept_text, diagram, code_editor, comparison_table |

### Capture hygiene (port of timestamp prompt constraints)

- **No talking-head-only** frames as the topic figure  
- Prefer clean boards/slides fully visible  
- Spread coverage: start, middle, **final 20%** of video (do not stop at halfway)  
- Prefer later frame if same slide partially revealed  
- Aim ~1 content frame per topic minimum when possible  
- **Final-minute review lists** often live on the board — capture them  

### Embed

```markdown
![what to notice](./screenshots/composites/…)
**Figure — ~MM:SS:** one-line caption of board content (not only a clock)
```

---

## Ingest script note — screenshots (multi-frame + 2×2 composites)

`scripts/ingest_youtube.py` (with `--download-video` or `--frames-only`) captures **many** frames per chapter, then builds **2×2 composite panels** for NOTES.

```
screenshots/
  raw/           # individual tiles
  composites/    # 2×2 grids — USE THESE IN NOTES
  manifest.json
```

Policy by chapter length (approx):

| Chapter length | Raw frames | Composites |
|----------------|------------|------------|
| Short | 4 | 1 |
| Medium | 8 | 2 |
| Long | 12 | 3 |

In NOTES Board slots:

1. Prefer **`composites/*.png`**, not single sparse grids.  
2. Short topic → **1** composite.  
3. **Long topic** (code-heavy / ≥15 min chapter) → embed **2–3** composites.  
4. Caption what to notice on the chalk/IDE.

```bash
# full ingest + multi-frame composites
python …/ingest_youtube.py --url URL --out path --download-video

# re-run composites only (existing lecture.mp4 + chapters.json)
python …/ingest_youtube.py --url URL --out path --frames-only
```
