# Topic planning + frames (map-first + claim-mine later)

## Goal

Topics = **boxes on the master map** for the **reader**.  
Claims = **every teaching unit in the transcript** for **completeness**.

```
1. List teacher moves in order (problem → tools → payoffs → worldview shifts)
2. Draw ONE master ASCII (whole video point)
3. State worldview arc: "from ___ to ___" (required for math/theory)
4. Cluster into 6–10 topics with MM:SS ranges
5. ★ Mine claims per time range (transcript-mining.md) — do not skip
6. Assign screenshots by type priority (below)
```

**Critical:** “6–10 topics” means **merge for reading**, not “skip spoken definitions.”  
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

## Topic count

| Duration | Topics |
|----------|--------|
| ~20–30 min | 5–8 |
| ~30–50 min | **6–10** |
| ~60–90 min | still **8–10** major topics (merge harder; deepen each) |

Do **not** use 20–30 micro-topics (even if some educative samples did).  
Do **not** use few topics as an excuse for thin establishing.

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
