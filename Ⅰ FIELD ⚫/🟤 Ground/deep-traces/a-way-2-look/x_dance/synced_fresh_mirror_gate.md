# Synced Fresh Mirror Gate

Status: PUBLIC CANDIDATE  
Scope: X execution / repo safety / context verification  
Layer: X Dance / Verification gate  
Claim level: Mechanism described here is not proof of correct use in any specific session  
Date: 2026-05-08  

## Core Idea

A new synced conversation can act as a **fresh mirror**: a checkpoint that re-reads the same project context from a slightly zoomed-out stance **before** impact operations (staging, committing, merging, pushing, or widening visibility).

This is **not** an extra authority. It does not elevate the assistant in the mirror to “decider.”

Purpose: interrupt long execution loops long enough that **human intent**, **exact paths**, and **git-visible trace** stay aligned.

## Position In The Movement Chain

The gate sits between:

- local editing and file churn  
- staging  
- commits  
- pushes  
- merges  
- public visibility  

## Why It Helps

Long build sessions can crowd the field:

- many files open at once  
- multiple branches in play  
- staged and untracked paths mixed  
- non-public or local-only material adjacent to public candidates in the working tree  
- assistant narratives that say “safe” while `git status` still shows leakage risk  
- human fatigue, urgency, excitement, or speed  

A synced fresh mirror is one way to **break momentum** and re-anchor on **observable** state.

## What The Fresh Mirror Should Check

1. Current branch (`git branch --show-current`)  
2. Short status (`git status --short`)  
3. Staged files (`git diff --cached --stat` and path-level review when needed)  
4. Unstaged changes on tracked files (`git diff --stat`)  
5. Untracked paths and directories  
6. Whether the working tree is **clean**, **dirty only on intended paths**, or **leaking** (e.g. broad untracked sets, risky adjacency)  
7. Whether local-only or consent-gated material is **near** public impact (same tree, easy mistaken `git add`)  
8. Whether the **intended commit scope** is still one basket, with an explicit path list  
9. Whether prior assistant or X statements match the **actual** trace (status + diff)  
10. Whether the proposed next step is still the **smallest safe landing**  

## Core Rule

A fresh mirror is **not truth**.

A fresh mirror is a **verification gate**.

**Diff, status, staged paths, and file content are stronger than assistant statements.**  
The mirror may summarize; it does not override the repository’s ground truth.

## Benefits (Mechanism-Level)

### 1. Reduces momentum blindness

Interrupts automatic continuation so intent can be re-checked against trace.

### 2. Detects scope drift

Surfaces when multiple baskets are open at once (e.g. mechanics, connectors, origin layers, prompts, safety docs, local-only trees) so mixed commits are less likely.

### 3. Protects boundary-sensitive material

Flags when non-public-by-intent paths sit beside public candidates **before** staging widens.

### 4. Improves accountability of X-output

Questions the mirror invites (without answering them by fiat):

- Did X observe only, or claim actions that lack git trace?  
- Did staging match the stated intent?  
- Was “GREEN” asserted while status still showed leakage-shaped patterns?  

### 5. Acknowledges human state without moralizing

The gate names that speed and fatigue affect execution. That framing is **field safety**, not a judgment of the human.

## Dangers

### 1. False authority

Confidence in a new chat is **not** verification. Avoid: “another model agreed, so it is safe.”

### 2. Context pollution

Highly detailed private or emotionally loaded context increases the chance that wording drifts into public docs. Prefer **mechanism extraction** when publishing.

### 3. Agreement bias

The mirror must ask counter-questions:

- What could be wrong here?  
- What is explicitly **not** proven by this narrative?  
- What should remain parked?  
- Which baskets are being mixed?

### 4. Public vs local-only confusion

A pattern may be publication-worthy while a particular chat log or excerpt is **not**.

Rule of thumb for public repos:

> Publish **mechanism** and governance text with clear claim level;  
> Do not treat raw session logs as the deliverable unless a separate boundary review says so.

### 5. Branch confusion

Never assume “last known branch” from memory. Re-run live branch and status in the mirror session.

### 6. Authority laundering

Repetition across models is **not** evidence. Verification needs **path, diff, status, boundary, human gate**.

## Safe Use Pattern

### Trap 0 — Observe

The fresh mirror may **only** observe.

**Allowed:** summarize visible git state, name risks, label dirty / leaking / clean-enough-for-next-step, suggest the next trap.

**Not allowed:** stage, commit, push, merge, or move local-only trees into public visibility.

### Trap 1 — Scope

Choose **one basket** only (examples: one docs subtree, one connector area, one prompts pack, or “local-only: no public movement”).

### Trap 2 — Exact Path Gate

Before impact, list **exact paths**. No path list, no movement.

### Trap 3 — Diff Gate

Review diffs. **Diff is stronger than statement.**

### Trap 4 — Human Gate

The human decides: **GREEN**, **PARK**, or **RED**.  
Assistants may advise; they do not own the gate.

## Output Format For A Fresh Mirror Check

Every synced fresh mirror response that follows this pattern should include something like:

```text
Branch:
Current status:
Staged files:
Unstaged tracked files:
Untracked files:
Dirty condition:
Public/private risk:
Scope drift risk:
GREEN / YELLOW / RED:
Smallest safe next landing:
Do not touch:
```

Ratings are **advisory** unless the human adopts them in Trap 4.

## Claim Safety

This document describes a **process pattern**. It does not guarantee safety in any repository. It does not replace code review, security review, or legal review. Local policy and consent boundaries always apply outside this text.
