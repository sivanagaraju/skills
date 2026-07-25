# Writing examples (bad → good)

Use these as calibration. Same structure slot, different writing skill.  
When rewriting a thin package, match the **GOOD** rhythm, not only the slot names.

---

## Example A — “What he is establishing” (self-contained mini-lesson)

### BAD (bullet deck)

```markdown
### What he is establishing

- Model uncertainty
- Physics works for rigid bodies
- Spam is abstract
- Use probability
```

### BAD (video-dependent recap)

```markdown
### What he is establishing

He then explains on the board why abstract labels need probability, as
discussed earlier in the mission, and introduces the X-ray setup he will use.
```

(Reader must have watched to know what any of that means.)

### STILL BAD (bullets with commas)

```markdown
### What he is establishing

The lecture covers modeling uncertainty, physics for rigid bodies, spam
as abstract, tumors as abstract, and using probability.
```

### GOOD (video closed — idea still lands)

```markdown
### What he is establishing

If a rigid body moves from A to B, you measure position and momentum, write
Newton’s laws, and the path is determined. Sensors and physics close the loop.

Now ask: is this email spam? Is there a tumor on this X-ray? Those answers are
not dial readings. A camera measures light; “tumor present” is a human judgment
stuck on after looking.

So the first tool is not a fake F=ma for spam. When the target is abstract, we
model uncertainty with probability and statistics and learn from many labeled
examples.

You can now say why ML in this course is probabilistic. Still missing: the
precise objects (sample space, random variable) — later lectures.
```

**Pattern:** problem → contrast → claim → ownership. Passes the blindfold test.

---

## Example B — Bridge

### BAD

```markdown
### Bridge

Next we discuss sample space.
```

### GOOD

```markdown
### Bridge

We now have a strategy—repeat the messy situation and learn from many
runs—but we still lack a precise language for “all possible runs” and
“how big is this set of outcomes?” That language starts with a random
experiment and its sample space Ω.
```

**Pattern:** what we have → what is still missing → named next box.

---

## Example C — Analogy (scene → question → right/wrong → rename)

### BAD (slogan)

```markdown
### Analogy for this topic only

It's like pizza.
```

### BAD (table worksheet)

```markdown
### Analogy for this topic only

| Everyday piece | Formal object |
|----------------|---------------|
| secret recipe book | unknown $f$ |
| plated dishes | data $D$ |
```

### BAD (pretty abstract fog — symbols early, no instances)

```markdown
### Analogy for this topic only

Stay with the planet story. Nature already “knows” a rule that turns time
into position — that hidden rule is $f$. You never get the full rulebook;
you only get a short logbook of sightings $D$. Function approximation means
writing a useful stand-in for the rule…
```

(Sounds smart; reader still cannot *see* the idea. This pattern failed real users.)

### GOOD (instances + hard question + right vs wrong + symbols last)

```markdown
### Analogy for this topic only

Suppose you only watched the sky three times:

- night 1 → planet at position A
- night 2 → position B
- night 3 → position C

Someone asks: **where is it on night 10?** You never watched night 10.

There is a real path the planet follows. You are not given that path — only
the three sightings. Function approximation means: invent a path that fits
A, B, C *and* can answer night 10.

If you only recite nights 1–3 and shrug for night 10, you stored the
sightings; you did not approximate the path.

In lecture words: hidden path = f, three sightings = data D, night 10 = new x.
```

**Pattern:** scene → concrete cases → one question memory fails → success vs failure in plain words → one rename line.

---

## Example D — Map slot

### BAD

```markdown
### Where this sits on the master map

METHOD box.
```

### GOOD

```markdown
### Where this sits on the master map

On the master map we already accepted that physics fails for abstract
labels. This topic fills the **METHOD** box: what do we *do* instead?
The answer is operational, not philosophical—collect many labeled
examples and treat them as repeated runs of the same experiment.
If “set / subset” is shaky, open [sets](./PREREQUISITES.md#p1-sets) before
the next formal topic.
```

**Pattern:** prior box → this box → why now → optional PREREQ deep link.

---

## Example E — Local picture + Notice line

### BAD

```markdown
### Local picture

```
  probability
```
```

### STILL BAD (boxes rename the heading)

```markdown
### Local picture

```
  ┌──────────────┐
  │ ill-posed f  │
  └──────────────┘
```
```

### GOOD (relation)

```markdown
### Local picture

```
  cannot write full physics f
            │
            ▼
     many labeled / repeated runs
            │
            ▼
     fit a probabilistic model
```

Notice: the “model” is still unnamed formally—Ω and P arrive next on purpose.
```

### GOOD (see-it ladder: numbers → symbols)

```markdown
### Local picture

```
  SEE (micro table)
    t=1 → pos≈2
    t=2 → pos≈5
    t=3 → pos≈10
    t=4 → ???   ← purpose of approximation

  SAME objects, formal names
    D = {(1,2),(2,5),(3,10)}
    want estimate of f so f̂(4) is defined
```

Notice: three training hits never automatically invent a value at a new $t$;
that is why “given $D$, find $f$” is not table lookup.
```

---

## Example F — Board caption

### BAD

```markdown
![slide](./screenshots/03.png)

Screenshot.
```

### GOOD

```markdown
![Toward the triplet ~43 min](./screenshots/08-t2613s.png)

**Figure — ~43:30:** board is assembling events and a size function P;
watch for the moment he boxes (Ω, F, P) as one object, not three slogans.
```

---

## Example G — Thin vs rich formal topic (measure / triplet)

### BAD (thin for a 15+ min formal segment)

```markdown
### What he is establishing

He defines events as subsets, P as a map to [0,1], and the triplet (Ω,F,P).
```

### GOOD (still one establishing slot, but with work)

```markdown
### What he is establishing

Once Ω exists, questions about outcomes (“even face?”, “spam?”) become
subsets—events. He equips those subsets with a size function P that lands
in [0,1], with P(Ω)=1 and additivity on disjoint pieces.

A fair die makes the arithmetic honest: A={2,4,6} gets size 1/2 under
uniform faces. Multiplying sizes is *not* that axiom; adding is.

The three pieces together are the probability triplet (Ω, F, P)—the
starter kit every later generative model will quietly reuse.
```

---

## Meta lines (never in student NOTES)

```markdown
content_type: math_technical   ← BAD in student-facing body
Apply-it scenarios: no         ← BAD; just omit the section
```

Put type only in `metadata.json`.

---

## Quick rewrite checklist (use after a draft)

For each topic:

- [ ] Establishing is **story**, not comma-joined bullets  
- [ ] At least one **named concrete** (spam, die, X-ray, GPT, line of code…)  
- [ ] Analogy has **instances + hard question + right/wrong + rename last** (not abstract fog or tables)  
- [ ] Local picture shows a **relation**; hard math has **micro numbers**  
- [ ] **Notice:** line after ASCII adds insight  
- [ ] Bridge states a **missing piece**, not “Next we…”  
- [ ] Formal topics link `./PREREQUISITES.md#…`  
- [ ] No ELI5 / Feynman / Toy / Approach-N labels  
