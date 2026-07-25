# Content types — depth knobs only (from educative analyzer research)

**Source of ideas:** `educative.io/src/gemini_youtube_analyzer_v6_0.py`  
**Not used:** Vertex API, image-gen, forced 2 Mermaids per topic, 20–30 micro-topics.

**Layout never changes.** Always: PREREQS → TOC → Exec Summary (master ASCII) → 6–10 topics → external refs → (optional apply scenarios) → sources → dual quiz.

Classify early; put `content_type` in `metadata.json`.

---

## Registry

| Type | Signals | Prefer screenshots of | Inside topics emphasize | De-emphasize |
|------|---------|------------------------|-------------------------|--------------|
| **theory_concept** | Mental models, definitions, frameworks | concept text, diagrams, comparison tables | Why on map, analogy, contrast, bridges | Fake code, fake UI |
| **math_technical** | Board, proofs, formulas | formula, derivation, graph, whiteboard | Step chains, symbols after example, LaTeX | Product marketing |
| **code_tutorial** | IDE, terminal, live coding | code_editor, terminal, output, error | Full code, files, imports, exact commands | Pure theory digressions |
| **tool_product** | UI demos, settings | ui_screen, configuration, result, comparison | Click paths, setting names, before/after UI | Fake math |
| **research_review** | Papers, SOTA, benchmarks | formula, graph, table, benchmark_result | Claim → method → evidence → limits | Tutorial fluff |
| **soft_skills** | Leadership, career, productivity | concept_text, framework, comparison_table | Named frameworks, tradeoffs, actions | Fake rigor diagrams |
| **mixed** | Multiple modes | concept + diagram + code as present | Follow **primary** thread | Forcing one style |

**MFML / NPTEL math foundations:** default `theory_concept` or `math_technical`.

---

## Domain formatting (port of STRUCTURED_BLOG domain rules)

### When `math_technical` (or math-heavy theory)

Follow **`math-formatting.md`** (full rules). Summary:

- **Inline:** `$...$` only — **never** `\(...\)` or `\[...\]` (breaks GitHub / many previews)  
- **Display:** blank line + `$$` on its own line + formula + `$$` on its own line  
- **Never** ```` ```latex ```` for formulas  
- Under dense display formulas, add **one plain-English line** (“In words: …”)  
- Subscripts only inside math: `$x_i$`, not bare `x_i`  
- Note matrix sizes / dimensions when spoken (e.g. `[768×64]`)  
- Prefer derivation as numbered steps + ASCII, not only prose  

#### Math / chalk must-capture (scan transcript; mark FOUND/ABSENT in coverage-checklist)

| Scan for… | If FOUND, NOTES must… |
|-----------|------------------------|
| Core problem one-liner (“given D find f”, …) | Teach it early + Exec Summary |
| Co-defined terms (model **and** algorithm; Ω **and** P; …) | Define **both**, not one |
| Board procedure (stacking, derivation steps, algorithm steps) | Step list + **ASCII** |
| Main contrast (deterministic vs probabilistic; physics vs stats; …) | Dedicated explanation + map arc |
| Slogans (“all models wrong…”, “data is oil”, “ignorance modeling”, …) | Quote + plain meaning |
| Warnings / traps (table lookup, random labels, overfitting seed) | Explicit wrong-move teaching |
| End review / homework list | List + short meaning of each item |
| Forward pointer (next lecture link) | Final bridge / last topic |
| Generative / probabilistic motivation | Why course uses probability |

Use `transcript-mining.md` claim sheets. Skipping FOUND items is a package fail even if structure validates.

### When `code_tutorial`

Follow **`code-extraction.md`** (full rules). Summary:

- Complete code blocks with language tags  
- All file names, imports, terminal commands **exactly**  
- Brief what-it-does after each block  
- GitHub URL if shown  

### When `tool_product`

- Exact click path: menu → setting → value  
- Before/after UI state  
- Screenshot > abstract diagram when UI is the point  

### When `research_review`

- Explicit: claim, method, result/number, limit/caveat  
- Do not invent metrics not in video  

### When `soft_skills`

- Name the framework; give one workplace situation  
- Tradeoffs over fake UML  

### When `mixed`

- Pick one primary type for depth knobs  
- Secondary types only where video actually switches  

---

## Topic subsection variants (same 6 headings, different fill)

Fixed headings (always):

```
### Where this sits on the master map
### Board / screenshot
### What he is establishing
### Analogy for this topic only
### Local picture
### Bridge
```

| Type | Under “What he is establishing” also include |
|------|-----------------------------------------------|
| math | formulas + short step chain |
| code | code/commands + run order |
| tool | click path + settings |
| research | claim / evidence / limit |
| theory | definition after motivation + contrast |
| soft | framework steps + tradeoff |

| Type | “Board / screenshot” means |
|------|----------------------------|
| math / theory | whiteboard / slide with content |
| code | IDE or terminal (not face) |
| tool | UI panel |
| research | chart / table from paper slide |
| soft | framework slide if any; else ASCII only |

---

## Production scenarios section (optional by type)

**Single source of truth:** `production-scenarios.md` (when to include + section shape).  
Do not duplicate the gating table here.

---

## Depth scaling (soft, not 30 topics)

From analyzer depth idea, adapted:

- ~30–50 min → 6–10 topics  
- Aim roughly **60–100 words of clear prose per minute of topic** (soft; diagrams count as teaching)  
- Prefer fewer deep topics over many shallow ones  
- Cover full timeline by **merging** asides into map boxes, not by exploding topic count  
- **Mine every minute for claims**; merge into topics — length ≠ completeness  
- Establishing budget ≫ analogy (tutor-voice.md teaching budget)  
