# Diagrams & Mermaid safety (from analyzer; ASCII-first)

**Source:** `gemini_youtube_analyzer_v6_0.py` ASCII + Mermaid rules  
**User lock:** ASCII-first; Mermaid **sparse** (not 2 per topic).

---

## ASCII (required default)

- Executive Summary: **one** whole-video architecture (15–40 lines, box-drawing: `┌─┐│└▼═╔║`)  
- Each topic: local ASCII under **Local picture**  
- Prefer ASCII for: pipelines, bags/sets, before/after, build steps, onions  

---

## Visualization budget (required for hard topics)

Structure can be perfect and still leave the reader lost if every diagram is a **title restated in boxes**. Treat visualization as teaching, not decoration.

### Per-topic minimum (math / hard theory)

| Piece | Requirement |
|-------|-------------|
| **Local picture** | Shows a **relation** (before→after, many-to-one, fail-vs-work, class→pick one). Not three empty boxes labeled with the section title. |
| **Notice line** | One sentence after the fence that adds insight the boxes alone do not say. |
| **Micro numbers** | When the idea is formal (domain, data, vectors, overfitting), put **tiny concrete values** in the diagram (times, labels 0/1, 2×2 pixels → vector). |
| **See-it ladder** (hard middle topics) | Prefer **two panels** in one fence or two short fences: (1) picture / table of instances, (2) the same objects renamed as symbols. |

### Soft budget by content_type

| content_type | Extra viz expectation |
|--------------|------------------------|
| **math_technical** | Hard topics (definitions, ill-posed, models, vectors): micro-example ASCII with numbers + symbol rename. Master map stays one whole-video architecture. |
| **code_tutorial** | Call graph / file layout ASCII **plus** real code fences (see `code-extraction.md`). |
| **tool_product** | UI path as numbered steps; screenshot beats abstract boxes. |
| **theory_concept** | Contrast diagram (A vs B) when the lecture is a distinction. |
| **mixed** | Follow the **primary** thread’s budget. |

### Fail (rewrite the diagram)

```
  BAD — title restated
  ┌─────────────┐
  │ overfitting │
  └─────────────┘

  BAD — slogan boxes with no relation
  data → model → predict
  (no fail case, no new x, no numbers)
```

```
  GOOD — relation + numbers + leftover
  observed only:
    (t=1 → pos=2)  (t=2 → pos=5)  (t=3 → pos=10)

  table "function":
    knows t=1,2,3 only  →  FAILS at t=4 (never seen)

  NEED: a rule that answers new t, not a lookup of D
```

### Optional second local view

When one idea has stages (guess class → pick member; sensor → label → statistics), use a **two-stage** ASCII or a small **mapping table** under the analogy. Do **not** invent a separate “Diagrams” section.

---

## When to add Mermaid (optional)

Add **at most 0–2 Mermaid diagrams for the whole NOTES** unless the video is pure systems design and a second view truly helps.

Use Mermaid only for:

- Multi-step process / state  
- Sequence over time (request path)  
- Decision flow hard to show in ASCII  

Never create a separate “Diagrams” section — keep inline.

---

## Safe Mermaid types (ONLY these)

```
graph TD
graph LR
flowchart TD
flowchart LR
sequenceDiagram
classDiagram
stateDiagram-v2
erDiagram
pie
mindmap
journey
timeline
gitGraph
```

`quadrantChart` only if coordinates are bare numbers `[0.3, 0.7]` (not strings).

---

## Banned Mermaid types (break GitHub / VS Code preview)

```
block-beta
sankey-beta
xychart-beta
requirementDiagram
C4Context
C4Container
C4Deployment
C4Dynamic
architecture
```

(Analyzer also banned several experimental types — do not use them.)

---

## Type-biased Mermaid choice (if you add one)

Port of `_MERMAID_TYPE_HINTS` (hints only):

| content_type | Prefer |
|--------------|--------|
| math_technical | `graph TD` / `graph LR` for derivation or pipeline |
| code_tutorial | `sequenceDiagram`, `stateDiagram-v2`, `graph TD` |
| tool_product | `journey`, `graph TD` with subgraphs |
| theory_concept | `mindmap`, `stateDiagram-v2`, `graph TD` |
| research_review | `graph TD`, `erDiagram`, `timeline`, `pie` |
| soft_skills | `mindmap`, `journey`, `graph TD` |
| mixed | whatever matches the primary thread |

---

## Do NOT port from analyzer

- “Each topic MUST have 2 different Mermaid types”  
- Gemini image-gen concept/architecture PNGs  
- Separate visual appendix sections  
