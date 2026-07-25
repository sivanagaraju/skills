# Production / apply scenarios (optional section)

**Source idea:** `QUIZ_AND_SCENARIO_PROMPT` in `gemini_youtube_analyzer_v6_0.py`  
**Adapted for:** learner + engineer, not senior-only interview tone always.

---

## When to include

| content_type | Include `## Apply it (scenarios)` ? |
|--------------|-------------------------------------|
| math_technical | **No** (default) |
| theory_concept | **No** for pure foundations (MFML default); Yes if video is applied systems theory |
| code_tutorial | **Yes** — 3–5 scenarios |
| tool_product | **Yes** — 3–5 scenarios |
| research_review | **Yes** — 3–5 scenarios |
| soft_skills | **Yes** — 3–5 scenarios |
| mixed | **Yes** if primary type would include |

Place in NOTES **after External references, before Sources**.

---

## Section shape

```markdown
## Apply it (scenarios)

*Workplace-style situations that use ideas from this video only.*

### Scenario 1: <title>
**Context:** team / load / constraints  
**Challenge:** …  
**Questions:**  
1. …  
2. …  

<details>
<summary>Show solution sketch</summary>

- Tie back to **Topic N** / master-map box: …
- Concrete steps: …

</details>
```

---

## Scenario types to mix (from analyzer)

- Scale / load (“10M requests/day…”)  
- Migration / upgrade choice  
- Incident / debugging  
- Cost / efficiency  
- Team decision A vs B  

**CRITICAL:** every scenario must use **specific** names, numbers, or techniques from **this** video — no generic filler.

---

## Relationship to quiz.html

| Mechanism | Role |
|-----------|------|
| `quiz.html` Part A/B | Primary check: warm-up + map/topics |
| Apply it (scenarios) | Optional deep application for non-math videos |

Do **not** replace dual-part quiz with scenarios only.
