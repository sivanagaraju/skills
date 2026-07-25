# NOTES header + topic→PREREQS linking

**Law for full structure:** `output-blog-contract.md` only.  
This file is a **snippet helper**, not a second contract.

## Required NOTES open

```markdown
# <Human title>

> **Video:** [title](url) · **~Xm**  
> **Warm-up first:** [PREREQUISITES.md](./PREREQUISITES.md) · **Quiz:** [quiz.html](./quiz.html)

**Do PREREQUISITES before this article.**

## Table of Contents
…

## Executive Summary -- architecture of this lecture
(ONE big ASCII blueprint = the lecture's system, not a topic list)

## Topic 1: … (MM:SS–MM:SS)
### Where this sits on the master map
…
### Board / screenshot
…
### What he is establishing
…
### Analogy for this topic only
…
### Local picture
…
### Bridge
…
```

## Per-topic PREREQUISITES deep links (required when topic leans on warm-up)

Do **not** rely only on the top banner. Inside **Where this sits on the master map**, link the specific warm-up:

```markdown
### Where this sits on the master map

This fills the **TRIPLET** box on the master map. If bag/subset language
is still fuzzy, open [sets warm-up](./PREREQUISITES.md#p1-sets) first, then
return here.
```

### Optional top-of-NOTES index (in addition to per-topic links)

You **may** add a short table after the PREREQUISITES banner (does not replace per-topic links):

```markdown
| When the lecture hits… | Warm-up |
|------------------------|---------|
| Sets / Ω / events | [p1-sets](./PREREQUISITES.md#p1-sets) |
| Functions / maps | [p2-functions](./PREREQUISITES.md#p2-functions) |
| Size / measure | [p3-measure](./PREREQUISITES.md#p3-measure) |
```

Use real anchors that exist in **this** video’s `PREREQUISITES.md`.

## Anti-pattern (do not use as structure template)

The educative Dynamo sample (`amazon_dynamodb_paper_explained*`) is **depth/prose inspiration only**.  
It uses **31 rigid 3-minute topics** — that is **forbidden** micro-chunking for this skill (need **6–10** map boxes).  
Quality bar for **structure:** an existing package built under this skill that has been verified against the current contract, **not** the Dynamo 31-topic HTML.
