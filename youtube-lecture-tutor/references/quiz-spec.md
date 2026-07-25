# Quiz — Part A + Part B

## Rules

1. One `quiz.html` per video.
2. **Part A** → PREREQUISITES.md (`"part": "prerequisites"`)
3. **Part B** → NOTES.md (`"part": "notes"`) — include **at least one question that tests the master map / whole-video point**
4. All Part A questions first, then Part B.
5. **Per-question feedback (required):** each card has **Check this answer** → verdict, why correct, why not others, ASCII, use later, **deep link via `anchor`**. User must not need to finish the whole quiz to learn from one item.
6. Optional **Score all answered** for Total / Part A / Part B totals.
7. **Forbidden strings** in questions JSON (case-sensitive tags): `ELI5`, `Feynman`, `Toy` (as technique label), `Approach 1/3/5`
8. **Answer-key distribution (mandatory):** correct `"answer"` must **not** always be `"A"`.  
   - Authoring method: write correct text first → **shuffle** option order → set `"answer"` to the resulting key.  
   - Target: for $n \ge 8$ items, each of A/B/C/D appears as correct at least once when possible; **no single key > 50%** of items.  
   - **ERROR** if all answers are the same key (position bias).  
   - **WARN** if one key exceeds 50% or fewer than 2 distinct keys for $n \ge 8$.  
9. **Distractors:** prefer **near-miss misconceptions** from the lecture (wrong Ω, length vs P, numeric Ω assumption) over pure joke noise.
## Counts (guidance)

| Video length | Part A (warm-up) | Part B (map + topics) |
|--------------|------------------|------------------------|
| ~30–50 min | 3–5 | 5–8 |
| Longer | 4–6 | 6–10 |

Part B should hit: master slogan/map, 1–2 hard topics, and one “connect Topic X to Topic Y” question.

## Question-type diversity (required mix)

Do **not** make every item definition-recall. Across Part A+B, include **at least 4 different flavors** (adapted from the analyzer’s senior quiz types, learner-toned):

| Flavor | Example stem |
|--------|----------------|
| Definition / map | “What is Ω in the master map?” |
| Compare & contrast | “How does physics path differ from repeated-observations path?” |
| Connect topics | “Which chain links Topic 5 to Topic 8?” |
| Worked / numerical | “Fair die, A={2,4,6}, P(A)=?” |
| Edge / trap | “Why is memorizing only D a bad complete solution?” |
| Trade-off / so-what | “Why prefer stats when labels are abstract?” |
| Apply (optional) | Short workplace use of a concept (non-math videos especially) |

Minimum: **≥4 flavors** represented at least once in `questions.json`.

## Schema

```json
{
  "id": "q1",
  "part": "prerequisites",
  "tag": "Warm-up · sets",
  "anchor": "PREREQUISITES.md#p1-sets",
  "prompt": "...",
  "options": [
    {"key": "A", "text": "..."},
    {"key": "B", "text": "..."},
    {"key": "C", "text": "..."},
    {"key": "D", "text": "..."}
  ],
  "answer": "B",
  "whyCorrect": "...",
  "whyOthers": {"A": "...", "C": "...", "D": "..."},
  "diagram": "  ASCII",
  "useLater": "..."
}
```

**Note:** The example uses `"answer": "B"` on purpose — correct is **not** always option A. After reordering options, remount `whyOthers` keys to the **new** letters of each distractor.

### `anchor` (recommended)

Deep link for **If wrong: re-read …** in the quiz UI.

| Value | Resolves to |
|-------|-------------|
| `"PREREQUISITES.md#p1-sets"` | `./PREREQUISITES.md#p1-sets` |
| `"NOTES.md#topic-7-..."` | `./NOTES.md#topic-7-...` |
| `"#p1-sets"` | `./PREREQUISITES.md#p1-sets` or `./NOTES.md#…` depending on `part` |
| omitted | file only (`PREREQUISITES.md` or `NOTES.md`) |

`generate_quiz.py` wires this into the explanation panel.

## Generate

```bash
python ~/.grok/skills/youtube-lecture-tutor/scripts/generate_quiz.py \
  --out "path/to/NN-slug/quiz.html" \
  --title "Quiz · Lec XX" \
  --questions "path/to/NN-slug/raw/questions.json"
```

## Validate (before done)

```bash
python ~/.grok/skills/youtube-lecture-tutor/scripts/validate_package.py \
  --dir "path/to/NN-slug"
```
