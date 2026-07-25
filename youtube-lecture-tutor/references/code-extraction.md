# Code & repository extraction (from analyzer CODE_AND_REPO rules)

**When:** `content_type` is `code_tutorial`, or code appears in `mixed` / `tool_product`.  
**Where:** inside the relevant Topic under **What he is establishing** (and next to Board composites) — **never** only a prose summary with zero fenced code for a coding chapter.

**Pair with screenshots:** Board composites show the IDE/terminal; **fenced code blocks** reconstruct the runnable steps. Both are required for code-heavy topics.

---

## Fail the package if (code_tutorial)

For any topic that covers **live coding / API wiring / install** in the video:

- [ ] At least one fenced code or bash block with language tag  
- [ ] Main entry API named (e.g. `create_deep_agent`, class, CLI)  
- [ ] Install / env steps if the teacher ran them  
- [ ] Repo URL in Sources or topic if shown  

Prose-only establishing for a “Building with LangChain” chapter = **fail writing gate**.

---

## Mandatory captures (if shown in video)

1. **GitHub / repo URL** — exact string; note timestamp if known  
2. **QR code nearby text/URL** if mentioned under the code  
3. **File names** on screen (`run_research.py`, `config.yaml`, `streamlit_app.py`, …)  
4. **Import lists** exactly (or cleaned ASR with note if garbled)  
5. **Complete code blocks** for the main demo path (not half snippets presented as full files)  
6. **Terminal commands** exact flags and arguments (`uv init`, `streamlit run …`)  
7. **Config / requirements** visible content (`requirements.txt`, `.env` key *names*)  
8. **Parameter lists** for factories (`model=`, `tools=`, `backend=`, `skills=`, `subagents=`)  

If ASR is broken: clean identifiers, mark uncertain names, prefer **repo/notebook** over inventing APIs.

## Formatting

```markdown
```python
from deepagents import create_deep_agent
# full block as taught
```

**What this does:** one or two sentences.

```bash
uv init
streamlit run streamlit_app.py
```
```

Language tags: `python`, `bash`, `yaml`, `json`, `typescript`, etc.

### Suggested blocks per coding topic

| Topic kind | Minimum blocks |
|------------|----------------|
| Project setup | `bash` install + env |
| First agent / API | `python` imports + factory + `invoke` |
| Backends / memory / skills / subs | `python` showing the **new parameter** |
| E2E app | `bash` run command + optional app wiring sketch |

## Resources line (if repo shown)

In **Sources** or topic:

```markdown
- **GitHub:** https://github.com/org/repo (shown ~MM:SS)
- **Files shown:** `src/a.py`, `config/b.yaml`
- **Install:** `pip install -r requirements.txt` or `uv …`
```

## Forbidden

- Inventing code not shown or not in the linked repo  
- Incomplete “…” snippets labeled as the full file when the full file was visible  
- Skipping run order when the teacher has one  
- **Code video with zero fenced blocks** in coding topics  

## PREREQUISITES for code videos

Warm-up may include: repo layout terms, “what is an import”, environment — **short**.  
Do not paste the whole project into PREREQUISITES.
