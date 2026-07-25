# Math formatting (must render in GitHub / VS Code / most Markdown previews)

**When:** `math_technical`, theory with formulas, or any `$` symbols.

**Goal:** every equation the student needs is readable **without** a special KaTeX-only export.

---

## Use only these delimiters

| Kind | Correct | Do **not** use |
|------|---------|----------------|
| **Inline** | `$f : \mathcal{X} \to \mathcal{Y}$` | `\(...\)`, `\\( ... \\)`, bare `x_i` for math |
| **Display / important formula** | Blank line, then `$$` alone, formula, `$$` alone, blank line | `\[...\]`, ```` ```latex ```` for the formula itself |

### Display example (copy this shape)

```markdown
The observation set is

$$
D = \{(x_1,y_1),\ldots,(x_n,y_n)\}
$$

and we seek an estimate of $f$.
```

### Inline example

```markdown
Domain set $\mathcal{X}$ (inputs). Range set $\mathcal{Y}$ (outputs).
Pairs $(x_i, y_i)$ for $i=1,\ldots,n$.
```

---

## Hard rules (fail writing gate if broken)

1. **Never** `\(` `\)` or `\[` `\]` in package Markdown — many previews show the raw backslashes.  
2. **Never** put multi-line display math inside a table cell or bullet without `$...$` only (prefer short inline or move to a `$$` block above/below the list).  
3. Subscripts/superscripts **must** be inside math: write `$x_i$`, not `x_i` (underscores italicize or break Markdown).  
4. Sets/calligraphy: `$\mathcal{X}$`, `$\mathcal{Y}$`, `$\mathbb{R}^d$`.  
5. One idea per display formula; long derivations = several `$$` blocks + numbered prose steps.  
6. If a viewer still fails, add a **plain-English line under the formula** (required for dense formulas):

```markdown
$$
f : \mathcal{X} \to \mathcal{Y}
$$

In words: $f$ is a rule that takes any allowed input from the domain and returns one output in the range.
```

7. Headings: avoid heavy math in `##` titles when possible (anchors break). Prefer words: `Guess a class of f` not `Guess $\mathcal{H}$`.

---

## Common failures → fixes

| Broken (what student sees) | Fix |
|----------------------------|-----|
| `(\mathcal{X})` raw or weird parens | `$\mathcal{X}$` |
| `pairs ((x_i, y_i))` | pairs `$(x_i, y_i)$` |
| `i=1,\ldots,n` outside math | `$i=1,\ldots,n$` |
| Formula stuck to bullet text | Blank line + `$$` block |
| `x_i` italic garbage in prose | `$x_i$` |
| ```` ```latex ```` block | Use `$$` instead |

---

## ASCII still allowed for structure

Keep master map and local pictures as **ASCII**, not Mermaid, for pipelines. Use `$...$` only for real math symbols inside prose/formulas.

---

## Checklist before “done” on a math package

- [ ] No `\(` `\)` `\[` `\]` left in NOTES.md / PREREQUISITES.md  
- [ ] Every multi-symbol formula either `$...$` or `$$...$$`  
- [ ] Dense `$$` blocks have a plain-English line under them  
- [ ] Preview in GitHub or VS Code markdown preview once  
