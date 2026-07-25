# Brutal audit — `youtube-lecture-tutor` skill

| Field | Value |
|-------|--------|
| **Skill path** | `~/.grok/skills/youtube-lecture-tutor/` |
| **Audit date** | 2026-07-23 |
| **Scope** | Whole skill: `SKILL.md` + 17 references + 3 scripts (~3.6k lines) |
| **Type** | Review only (not a new skill; not an auto-fix PR) |
| **Audience** | Skill owner / human review before hardening |

---

## 1. Executive verdict

**Directionally right. Overgrown. Under-enforced. Docs sometimes lie.**

The skill will keep producing the same user pain (thin Exec Summaries, stamp rituals, all-A quizzes, structure without claims) unless:

1. The **validator actually ERRORs** what the skill calls FAIL, and  
2. The **load order is cut** so the agent can obey a short non-negotiable list.

| Question | Answer |
|----------|--------|
| Is the skill directionally right? | **Yes** |
| Is it currently trustworthy alone? | **No — too soft, too fat, inconsistent** |
| Biggest single fix? | Validator ERROR for real FAILs + stop over-promising in docs |
| Second biggest? | Remove contradictions (stamps, ELI5 residue, dead `04v3` bar) |
| Package 02 architecture Exec retrofit? | Optional series polish — **not** a skill fix |

**Ship confidence** (“skill alone produces good packages”): **Medium–Low**.  
Good packages appear when a human fights the agent; the skill optimizes for structure over truth when rushed.

---

## 2. Overall grades

| Area | Grade | One-line hit |
|------|:-----:|--------------|
| Product vision | **A−** | Right package shape; clear student path |
| Completeness (claim-mine) | **B+** | Mining idea is correct |
| Writing quality rules | **B** | Good principles; still re-teaches stamps by example |
| Exec Summary architecture | **B+** | New law is clear; barely enforced |
| Validator honesty | **D+** | Docs claim ERROR/WARN the code never does |
| Skill size / loadability | **D** | Agent cannot hold 17 refs + 930-line validator every run |
| Consistency / dead refs | **C−** | Ghost templates, twin leftovers, missing `04v3` folder |
| Single-skill cleanup | **B** | Mostly done; residue remains |

---

## 3. What the skill is trying to be

### 3.1 Intended product

```
PREREQUISITES.md  →  NOTES.md  →  quiz.html
```

Student path:

```
warm-up → architecture Exec Summary → topics → external links → quiz
```

Product goal: NOTES teach with **video closed** (not recap-only).

### 3.2 Intended pipeline (compressed)

```
goal → ingest → content_type → topic map + worldview
     → claim-mine → PREREQS → topics (from claims)
     → architecture Exec Summary (after all topics)
     → coverage → quiz (mixed keys) → validate → confidence
```

### 3.3 Inventory on disk

| Kind | Count / notes |
|------|----------------|
| `SKILL.md` | ~280 lines |
| `references/*.md` | **17** files |
| Scripts | `ingest_youtube.py`, `generate_quiz.py`, `validate_package.py` (~930 lines) |
| Total md+py | ~**3,600** lines |

**Heavy references (by size):** `tutor-voice`, `writing-examples`, `executive-summary-architecture`, `output-blog-contract`, `transcript-mining`, `diagrams-and-mermaid`, …

---

## 4. Critical issues (P0)

### 4.1 Law without police (docs ≠ validator)

| Skill / quiz-spec claims | `validate_package.py` reality |
|--------------------------|-------------------------------|
| Answer keys not all A → **ERROR** | **Not implemented** (no answer-key distribution check) |
| Ownership stamps → fail / WARN | **Not implemented** |
| Claim mining required | Soft **WARN** only — missing `raw/claims/` can still exit 0 |
| Exec Summary architecture | Partial: box-drawing / fence — **not** scenario + STOP + load-bearing claims |
| “Writing WARNINGs are tickets” | Agent treats WARN as noise; default **exit 0** |

**Brutal truth:** Policy is aspirational; the gate is lax. The gate will always lose under time pressure.

### 4.2 Cognitive overload — skill too big to obey

Load order points at **17 references**. No agent re-reads all of them every package. Typical behavior:

- Skim absolute rules in `SKILL.md`  
- Sample `tutor-voice` / contract  
- Freestyle the rest  

That is **attention budget failure**, not model “stupidity.” Symptoms you already saw:

- Bare FA / acronym soup  
- Bold stamp closers  
- Thin Exec maps  
- All-quiz-answers A  

**create-skill guideline:** *SKILL.md is a prompt for the agent, not documentation.*  
This skill is **documentation pretending to be a prompt**.

### 4.3 Internal contradictions that still bite

| Conflict | Where |
|----------|--------|
| Ban bold `**Wrong move:**` / `**You can now:**` | `tutor-voice.md` still **shows those labels** as the banned form; models copy surface form. `writing-examples.md` ends with “You can now…” |
| PREREQS “3–6 ideas, short” | Also “deeper OK if beginner”; real package 03 has **8** ideas → permanent WARN |
| Structural bar `04v3-Lec01-…` | **Folder does not exist** in MFML (only `02`, `03`, `09`) — dead quality bar |
| Absolute rule “Fail if stamps” | Validator **rewards** ownership via regex (`you can now` / `still missing`) — pulls agents toward checklist language |
| Mining anti-pattern still says “List + **ELI5** meanings” | `transcript-mining.md` — fights your own ban |
| `## Twin skill` section still present | Body says single skill; zombie header remains |
| Quiz “≥4 flavors required” | Soft WARN; flavor detector is keyword toy, not real pedagogy |

### 4.4 Completeness is not closed-loop

Claim-mine is the best idea in the skill. Enforcement is soft:

- No ERROR if claims missing  
- No reliable “Must-teach claim appears in NOTES” matching (keyword freestyle only)  
- Human coverage gate is easy to skip  

You can still ship **pretty structure + thin truth**. That was the historical failure mode.

### 4.5 Ingest is fragile; skill pretends it is reliable

Observed failure modes in real sessions:

- HTTP 403 on some video formats  
- Missing ffmpeg  
- PowerShell does not support `&&`  
- Exit code 1 after partial success (captions OK, video fail)  

Pipeline step 2 reads as “always get TRANSCRIPT + screenshots.” **No recovery path** is documented (format 18, captions-only, frames-only first). Agents fail or over-claim completeness.

---

## 5. High-priority issues (P1)

### 5.1 PREREQS policy is incoherent

- Template: 3–6 ideas, one screen each  
- User demand: deep basics for beginners  
- Validator: warn if >6 **or** long  

**Result:** every serious beginner package is “PASS WITH WARNINGS” by design → agents learn to ignore WARNs.

### 5.2 Exec Summary architecture is good law, half-wired

`executive-summary-architecture.md` is the right persona (blueprint, not abstract). Automation still missing:

- Require scenario strip  
- Require STOP / out-of-scope  
- Require load-bearing claims ≠ TOC renames  
- Optional `raw/exec-architecture-draft.md` is never checked  

### 5.3 Vocabulary drift: “master map” vs “architecture blueprint”

Some gates still say “master ASCII”; new law says architecture blueprint. Agents default to the old thin map.

### 5.4 Topic count 6–10 is rigid for short lectures

Topic-planning has duration guidance; notes check still **ERROR** outside 6–10. Short videos get padded topics.

### 5.5 External refs / web search always mandatory

`global-agent.md` requires multiple quality searches. Good when online; no “skip if user / offline.”

### 5.6 Confidence theater

Always report High/Medium/Low — often uncalibrated after WARN spam unless agent is disciplined about claim counts.

---

## 6. Medium issues (P2)

| Issue | Note |
|-------|------|
| `notes-connect-block.md` | Easy to skip; unclear when required |
| `production-scenarios.md` | Fine for non-math; rare in MFML |
| `generate_quiz.py` | No key-shuffle helper; habit is “correct first → A” |
| `example_questions.json` | May still teach all-A if not audited |
| Frontmatter `description` | Still “ONE whole-video ASCII map,” not architecture blueprint |
| Shell docs | Mix bash `&&` and `^`; real shell often PowerShell |
| Ghost **04v3** | Still in `SKILL.md`, `package-contract`, `output-blog-contract`, `notes-connect-block` |
| Twin residue | `transcript-mining.md` still has `## Twin skill` header |

---

## 7. What is actually good (credit)

1. **One package shape** — PREREQS → NOTES → quiz  
2. **Claim-mine before NOTES** — correct root-cause for incomplete notes  
3. **80/10/10 teaching budget** — establishing owns teaching  
4. **Analogy = this topic only** — correct after user feedback  
5. **Single skill cleanup** — only `youtube-lecture-tutor` remains on disk  
6. **ASCII-first + math `$` / `$$`** — practical for GitHub  
7. **Dual-part quiz + anchors** — solid assessment shape when keys are mixed  
8. **Validator structure base** — topics, six slots, mermaid ban, meta lines, partial Exec box check  

The skill is not “bad.” It is **over-specified and under-enforced**.

---

## 8. Root-cause diagram

```
  ┌─────────────────────┐
  │  Too many laws      │
  │  (17 refs)          │
  └──────────┬──────────┘
             │ agent samples randomly
             ▼
  ┌─────────────────────┐
  │  Soft validator     │──────► green "PASS WITH WARNINGS"
  │  (structure OK)     │        feels like done
  └──────────┬──────────┘
             │
             ▼
  ┌─────────────────────┐
  │  User pain          │
  │  FA stamps, thin    │
  │  exec, all-A quiz   │
  └─────────────────────┘
```

Adding more law without enforcement **recreates the same failures**.

---

## 9. Skill “personality” problem

The skill tries to be simultaneously:

- course designer  
- writing coach  
- measure-theory tutor  
- quiz psychometrician  
- ingest ops  
- architecture information designer  

That is a **platform**, not a skill.

A healthy skill should force **~10 non-negotiables + a validator that fails them**. Depth docs load **on demand**.

---

## 10. Recommended fix roadmap

### Phase A — Honesty (1 session)

1. **`validate_package.py`**
   - **ERROR** if all quiz answers share the same key  
   - **WARN or ERROR** on stamp density (`**Wrong move:**` / `**You can now:**`)  
   - **ERROR** if `raw/claims/` missing (or gate via `package_variant` / “new package”)  
2. Align docs with code — **never claim ERROR until implemented**  
3. Kill **04v3** bar; point to real packages `02` / `03`  
4. Delete **Twin skill** header; fix mining “ELI5 meanings” line  

### Phase B — Slim the prompt (hard cut)

| Keep hot path (always load) | Load only when needed |
|-----------------------------|------------------------|
| Short `SKILL.md` (≤12 absolute rules) | `production-scenarios.md` |
| `output-blog-contract.md` | `code-extraction.md` |
| `tutor-voice.md` | `writing-examples.md` (when writing thin) |
| `transcript-mining.md` | `notes-connect-block.md` |
| `executive-summary-architecture.md` | … |
| `quiz-spec.md` | … |

### Phase C — PREREQS policy rewrite

Two modes via `metadata.json`:

| Flag | Policy |
|------|--------|
| `beginner_prereqs: true` | Allow 5–8 ideas, longer warm-up |
| default / false | 3–6 short ideas |

Validator respects the flag (no permanent false WARN).

### Phase D — One golden package

Pick **`03-Lec02-Recap-Probability-Theory-Part1`** as the structural bar (architecture Exec + claims).  
Delete fiction of non-existent `04v3`.

---

## 11. Optional product work (not skill core)

| Item | Note |
|------|------|
| Retrofit package **02** Exec Summary to architecture style | Series consistency only; do when you ask |
| Package **09** upgrade to claim-mine + architecture Exec | Same |
| Ingest recovery runbook in SKILL | format 18, captions-only, frames-only |

---

## 12. Review checklist (for you)

Use this when reading the skill files:

- [ ] Can I state the **10 non-negotiables** without opening 17 refs?  
- [ ] Does every “ERROR” in docs have a **matching line** in `validate_package.py`?  
- [ ] Would a new agent ignore WARNs because packages always WARN?  
- [ ] Is any quality bar path **missing on disk**?  
- [ ] Does any example re-teach a **banned surface form** (stamps, ELI5)?  
- [ ] Is load order **short enough** for one package build?  

---

## 13. Bottom line (one paragraph)

`youtube-lecture-tutor` has the **right product** (PREREQS → architecture NOTES → dual quiz) and the **right completeness idea** (claim-mine). It fails operationally because it is **too large to load**, **internally inconsistent**, and **validated softly** so “PASS WITH WARNINGS” becomes fake success. Fix **enforcement + size + contradictions** before adding more pedagogical law.

---

## 14. Suggested next action (pick one)

| Option | Scope |
|--------|--------|
| **A only** | Wire validator + kill doc lies + dead refs |
| **A + B** | A, plus slim SKILL load order |
| **Full hardening** | A + B + C + D across skill files |

---

## 15. Document control

| | |
|--|--|
| **Related skill files** | `SKILL.md`, `references/*`, `scripts/validate_package.py` |
| **Related packages** | `02-…`, `03-…`, `09-…` under `Mathematical-Foundations-of-ML/` |
| **Architecture Exec law** | `references/executive-summary-architecture.md` |
| **This audit path** | `Mathematical-Foundations-of-ML/00-package-contract/youtube-lecture-tutor-skill-audit.md` |

*End of audit.*
