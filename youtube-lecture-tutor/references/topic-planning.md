# Topic planning + frames (map-first + claim-mine later)

## Goal

Topics = **boxes on the master map** for the **reader**.  
Claims = **every teaching unit in the transcript** for **completeness**.

```
1. List teacher moves in order (problem → tools → payoffs → worldview shifts)
2. Draw ONE master ASCII (whole video point)
3. State worldview arc: "from ___ to ___" (required for math/theory)
3b. ★ Prerequisite & Curriculum Audit (curriculum-bridge-contract.md):
    - Identify assumed concepts from Mathematical-foundation-ml
    - Cross-reference MathsTerms/ and flag any missing terms for creation
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
- [ ] **Unique** screenshot path whose times fall in this topic (or “no content frame — ASCII only”)  
- [ ] Establishing will teach **all** Must-teach claims  
- [ ] ASCII for every board **procedure** in this range  
- [ ] Analogy short confirmation only  
- [ ] Bridge to next map box  
- [ ] Type-specific extras filled (formulas / code / clicks) per `scenarios.md`  

---

## Screenshots — generation + Board assignment (hard law)

**Product failure this section kills:** three panels from a whole-video sample, then the same `panel1of3` pasted on Topics 1–3, `panel2` on Topics 4–6, `panel3` on Topics 7–8. That is not coverage. Boards must track **time**.

### Why panels run out

| Cause | What happens |
|-------|----------------|
| No YouTube chapters | Old pipeline treated the whole video as one range → max ~12 frames → **3 composites** for a 45+ min lecture |
| Agent ignores `manifest.json` times | Picks the first composite repeatedly |
| Topic map has 8 boxes, disk has 3 panels | Agent “fills” Board slots by **reuse** instead of **re-extract** |

### Ingest policy (script)

`scripts/ingest_youtube.py` builds ranges in this **priority**:

1. **`raw/topic-ranges.json`** (best) — write after the topic map exists; one slice per topic  
2. YouTube / description chapters  
3. **Synthetic ~6 min slices** if neither exists (never a single `full` range on a long video)

Each range → multi-frame tiles → **2×2 composites** in `screenshots/composites/`.  
`screenshots/manifest.json` lists each composite with `time_start` / `time_end` (and range bounds).

```bash
# first pass (no topic map yet): synthetic or chapter ranges
python …/ingest_youtube.py --url URL --out path --download-video

# after topic MM:SS exist — write topic-ranges, then re-extract
# raw/topic-ranges.json example:
# [
#   {"start_time": 0, "end_time": 390, "title": "topic-01-mission"},
#   {"start_time": 390, "end_time": 724, "title": "topic-02-fa"}
# ]
python …/ingest_youtube.py --out path --frames-only
```

`--frames-only` **wipes** prior `screenshots/raw` and `composites` pngs so stale panels do not mix with new ones. URL optional on frames-only.

### Board assignment rules (agent — non-negotiable)

1. Open `screenshots/manifest.json`.  
2. For each topic with range `[T0, T1]`, pick composite(s) whose **`time_start`–`time_end` overlaps `[T0, T1]`** (or whose `range_start`–`range_end` is that topic slice).  
3. **One composite path → one topic.** Do **not** reuse the same path on another topic.  
4. Exception (rare): teacher re-shows the exact same board in two topics — still prefer a later/earlier tile if one exists; if truly identical, caption must say “same board revisited” and only one topic owns the embed.  
5. Short topic → **1** panel. Long / board-dense topic → **2–3** panels from **that** range only.  
6. Prefer **`composites/*.png`**, not sparse single tiles.  
7. Caption = **what is on the board** + ~MM:SS of the tiles — not only a topic label.  
8. **If `composite_count` < topic count** (or many topics would share panels):  
   - Write / refresh `raw/topic-ranges.json` from the topic map  
   - Re-run `--frames-only`  
   - **Do not** pad Boards by recycling the same three files  
9. If still no usable video (E2): every Board is **ASCII-only** + honest “no content frame” — never invent paths.

### Fail (void)

| Smell | Fix |
|-------|-----|
| Same `composites/…png` path in ≥2 topics | Re-assign by time or re-extract |
| Only `ch01-full-panel*` for an 8-topic package | Synthetic/topic-range re-extract; rewrite Boards |
| Board caption is only a clock or “early lecture frames” | Transcribe board content |
| Talking-head-only as the topic figure | Prefer board/slide tiles |

### Capture hygiene

- No talking-head-only as the sole figure  
- Prefer clean boards/slides fully visible  
- Cover start, middle, **final 20%** of the lecture timeline  
- Prefer later frame if the same slide is only partially revealed  
- Final-minute review lists on the board — capture them  

### Embed shape

```markdown
![what to notice on the board](./screenshots/composites/ch03-topic-03-….png)
**Figure — ~12:04–14:40:** domain/range sketch + table of (x,y) pairs; notice …
```

### Frame priorities by content_type

| content_type | Prefer capturing |
|--------------|------------------|
| math_technical | formula, derivation, graph, whiteboard |
| code_tutorial | code_editor, terminal, output, error |
| tool_product | ui_screen, configuration, result, comparison |
| theory_concept | concept_text, diagram, comparison_table, framework |
| research_review | formula, graph, table, benchmark_result |
| soft_skills | concept_text, framework, comparison_table |
| mixed | concept_text, diagram, code_editor, comparison_table |

### After topic map (pipeline hook)

```
topic list with MM:SS
  → write raw/topic-ranges.json
  → --frames-only (if video on disk)
  → assign unique composites per topic from manifest
  → then claim-mine / write NOTES Boards
```
