# Open Case Study 05 — Sligro: Deepsearch Questions and Source-Backed Answers

## Status

STRUCTUURLAAG / DEEPSEARCH-LAAG / IN ONDERZOEK / PUBLIEK-BRONVEILIG

This case is not a single operational claim.

It is the question engine behind the Sligro open case studies.

Purpose:
turn signals from Cases 01–04 into clean research questions, source-backed answers, claim-safe wording and possible AsymX Level 1 lenses.

## Working Rule

Filter signal → formulate question → find source → answer safely → map to Level 1 → decide next use.

One question should receive one grounded answer.

Prefer one strong source over many weak references.

## Claim-Safety Labels

Use one label for every answer.

### PUBLIC FACT

Directly visible in public Sligro sources, partner sources, annual figures, presentations, vacancies, interviews or official pages.

### SECTOR PATTERN

A general pattern from logistics, ERP, supply chain, operations, human factors, data quality or information systems literature.

This does not claim the pattern is happening inside Sligro.

### ASYMX INTERPRETATION

Our translation layer from public signal + sector pattern into a visibility lens.

### HYPOTHESIS / TEST NEEDED

Useful, but not operationally true until locally tested.

### DO NOT CLAIM

Too speculative, accusatory, unsupported or dependent on internal data.

## Master Deepsearch Prompt

Use this prompt when researching one question.

```text
You are helping build a public-source-safe AsymX case study.

Context:
We analyse Sligro only through public information and general sector patterns.
We do not have internal Sligro data.
We must not claim internal problems, failures, defects, delays or hidden issues.
We are looking for visibility questions that could support small, local, no-upload AsymX Level 1 lenses.

Question:
[INSERT QUESTION]

Return:

1. Short answer
Give the simplest answer in 3–6 sentences.

2. Source
Provide one strong public source, study, report, paper, case study or official page.
Prefer official sources, peer-reviewed studies, recognised industry sources or public company material.

3. What the source actually supports
State exactly what the source supports.
Do not exaggerate.

4. Claim-safe wording
Rewrite the answer so it can safely be used in an open case study.

5. What not to claim
List claims that would go too far.

6. AsymX Level 1 translation
Translate the answer into a small local visibility lens:
- local only
- no backend
- no upload
- no tracking
- source intact
- analysis as metadata
- no replacement for ERP, WMS, planning or BI systems

7. Mail value
Choose one:
MAILWAARDE / PARKEREN / LENS RIJP / NIET GEBRUIKEN

8. Suggested next question
Give one follow-up question that deepens the chain without overclaiming.
```

## Question Filter Prompt

Use this prompt to turn rough notes or AI output into researchable questions.

```text
You are the AsymX Question Filter.

Input:
[PASTE NOTES]

Task:
Extract only the questions worth researching.

Rules:
- Do not answer yet.
- Do not make claims.
- Do not assume internal Sligro truth.
- Convert vague statements into simple questions.
- Prefer questions answerable with one public source or one strong study.

Output for each question:
Question:
Domain:
Why this matters:
Possible source type:
Risk of overclaim:
Suggested claim-safety label:
```

## Source Gate Prompt

Use this prompt to judge whether a source is safe enough.

```text
You are the AsymX Source Gate.

Evaluate this source for a public-source-safe Sligro case study:

[SOURCE OR LINK]

Question it should support:
[QUESTION]

Return:
1. Source type
Official company source / partner case / academic study / industry report / vacancy / news article / weak source / unusable.

2. What it directly supports

3. What it does not support

4. Risk of overclaim

5. Safe sentence we may use

6. Unsafe sentence we must avoid

7. Verdict
USE / USE WITH CARE / PARK / DO NOT USE
```

## Answer Compression Prompt

Use this after a long deepsearch answer.

```text
Compress the following answer into a clean AsymX case-note.

Rules:
- Keep only what is useful.
- Separate fact, sector pattern, interpretation and hypothesis.
- Remove hype.
- Remove sales language.
- Remove unsupported claims.
- Preserve one source reference.

Output:
Question:
Short answer:
Source:
Claim-safe wording:
AsymX Level 1 translation:
Mail value:
Do not claim:
Next question:
```

## Sligro Mail Translation Prompt

Use this only after the answer passed the Source Gate.

```text
Translate this source-backed answer into Sligro-mail language.

Rules:
- Respect Sligro’s own systems and transition.
- Do not accuse.
- Do not say something is broken.
- Do not claim internal truth.
- Keep AsymX small, local and supportive.
- Tone: invitation, visibility, practical support, no blame.

Input answer:
[PASTE ANSWER]

Return:
1. One-sentence mail line
2. Slightly expanded paragraph
3. What not to say
4. Audience:
Operations / Supply Chain / IT-Data / Masterdata / Change / HR-Human layer / Management
```

## Reusable Answer Template

```markdown
## Question XX — [short title]

### Question

[The simple question.]

### Domain

[ERP transition / masterdata / planning / floor reality / service level / etc.]

### Short answer

[3–6 sentence answer.]

### Source

[One source or study.]

### What the source supports

[Exact support.]

### Claim-safe wording

[Sentence or paragraph we can safely reuse.]

### AsymX Level 1 translation

[Small local visibility lens.]

### Mail value

[MAILWAARDE / PARKEREN / LENS RIJP / NIET GEBRUIKEN]

### What not to claim

- [Unsafe claim 1]
- [Unsafe claim 2]

### Next question

[Follow-up question.]
```

## Starter Question Bank

### Q01 — Logistics simplicity

How can a large logistics organisation keep execution simple while planning, assortment, delivery and system complexity increase?

Domain:
supply chain execution / operational visibility

### Q02 — Planning versus floor reality

Why can a planning system be structurally useful while still needing local feedback from the floor?

Domain:
supply chain planning / human-in-the-loop / exception handling

### Q03 — Service level and invisible recovery work

How can service reliability depend on small recovery actions that are not always visible in dashboards?

Domain:
service level / human factors / operational resilience

### Q04 — Legacy to SAP transition

What typically becomes difficult when a company moves from legacy ERP logic to standardised ERP processes?

Domain:
ERP transition / masterdata / process harmonisation

### Q05 — Masterdata and physical reality

Why can masterdata quality become critical when warehouse or supply chain processes are standardised?

Domain:
masterdata / warehouse execution / ERP

### Q06 — Local lens without integration risk

When is a local no-upload visibility lens safer than a direct system integration?

Domain:
data safety / local tooling / shadow run / governance

### Q07 — Floor correction as metadata

How can floor corrections be captured as metadata without rewriting the source system?

Domain:
metadata / process mining / operational feedback

### Q08 — Claim-safe external analysis

How can an external analysis discuss public company signals without claiming internal truth?

Domain:
research method / evidence safety / OSINT ethics

## Move-to-Case-06 Rule

A question may move to Case 06 when:
- the answer is source-backed;
- claim-safe wording is clear;
- a small local tool, template or lens can be defined;
- no internal Sligro truth is needed;
- the output helps without accusing.

## Move-to-Case-07 Rule

A question may move to Case 07 when:
- it is safe enough for the Sligro-visible total overview;
- it supports the mail narrative;
- it is calm, clear and respectful;
- it does not expose private reasoning or speculative branches.

## Park Rule

Park the question when:
- the source is weak;
- the answer is too speculative;
- it creates accusation;
- it needs internal data;
- the Level 1 lens is not clear.

## Core Formula

Wat zichtbaar genoeg is, hoeft nu niet opnieuw gedragen te worden.

Wat leeft, krijgt ruimte om te groeien.
