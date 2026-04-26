# AsymX Framework


A minimal structural framework for asymmetry, intersection, and path formation.

---

## Practical Architecture Layer

This framework is currently used in a working system with three core mechanisms:

### 1. The Golden Triangle (Antenna – Scissors – Glue)

- Antenna: captures raw input (voice or text)
- Scissors (LLM): performs zero-shot extraction (stateless)
- Glue (code): deterministic state handling

Key property:
The main intake never crashes due to AI uncertainty.

---

### 2. Silent Threshold Learning (threshold = 3)

The system does not ask users for validation.

Instead:
- patterns are observed silently
- after repeated confirmations, they become stable nodes

Learning is:
- asynchronous
- non-intrusive
- separate from the intake

---

### 3. Presence-first Computing (BEING vs DOING)

The system distinguishes between:

- BEING: presence, observation, expression
- DOING: actionable tasks

This prevents:
- over-triggering
- unnecessary actions

The system remains passive unless action is clearly required.

---

## Example (simplified)

Input:
"Sheila asked something, I need wood from Praxis, grandma is fine"

Output:
[
  {"type": "task", "action": "get wood", "location": "Praxis"},
  {"type": "task", "person": "Sheila", "unknown": true},
  {"type": "status", "person": "grandma", "state": "ok"}
]

Uncertainty is stored, not resolved immediately.

---

## What is AsymX?

Created by Loek Verdonk.

Four primitives:

- ⚫ field — completely passive, no boundary, no source
- * appearance — distinction without origin
- − disappearance — loss of distinction
- X intersection — active crossing of + and − when intersectable

From this, paths form.
Multiple paths can exist at the same time.
Rivalry can stay without needing to be solved.

---

## Core idea

Not everything that differs can intersect.

An X only exists when + and − are **intersectable**:

- real asymmetry
- non-trivial overlap
- distinction remains under contact

This allows tension without collapse.

---

## Simulation

You will see:

⚫ field (black)
appearance (red)
− disappearance (blue)
X intersection (yellow)
path (green)

The system evolves continuously.


Status
This is an early structural simulation.
Not everything is solved yet.
Not everything is stable yet.
That is intentional.
Why I share this
This is not about being right.
This is about not forcing structure too early.
Collaboration
If something in here resonates with you,
feel free to build on it.
This does not belong to me.


Run:

```bash
python3 -m pip install -r requirements.txt
python3 asymx_sim.py
