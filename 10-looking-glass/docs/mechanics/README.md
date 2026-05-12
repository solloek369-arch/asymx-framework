# AsymX Mechanics

## Purpose

This folder holds **public mechanism notes**: reusable patterns, gates, guards, translation layers, and pointers to execution-trace style documents elsewhere under `docs/`. Mechanisms describe *how work is framed and routed* in the AsymX layer—not product guarantees, not closed proofs, and not a substitute for your own judgment.

Together with [discovery](../discovery/mechanism_keywords.md), [safety](../safety/README.md), [afterwords](../afterwords/README.md), [x_dance](../x_dance/synced_fresh_mirror_gate.md), and [prompts](../prompts/README.md), these notes form a **navigable map** of the mechanism field.

---

## Reading Rule

**Mechanisms are not proof, exclusive assertions about truth, or final truth.** They are inspectable working patterns: hypotheses about structure, language, and workflow that can be revised. Treat them as tooling for clarity and safer iteration, not as authority.

---

## Entry Points

Readers rarely land on one “correct” first page. These paths stay inside **public docs only**—they do not ask you to import private logs or vault material.

| If you arrive… | Start here |
|----------------|------------|
| …with a **mechanism** question | The numbered notes under [Existing Public Links](#existing-public-links) and the [cluster map](#core-mechanism-clusters) below |
| …with a **safety / external-impact** question | [Safety overview](../safety/README.md), then [external impact guards](../safety/external_impact_guards/README.md) |
| …with a **prompt / opening signal** question | [Prompts overview](../prompts/README.md), then [prompt opening translation](../prompts/prompt_opening_translation_protocol.md) |
| …looking for an **afterword / landing trace** | [Afterwords](../afterwords/README.md) |
| …following an **execution / correction trace** | [x_dance](../x_dance/synced_fresh_mirror_gate.md) and related entries in [Existing Public Links](#existing-public-links); prompt-side execution notes: [nine-branch prompt tracks](../prompts/x_execution/2026-05-08_nine_branch_prompt_tracks.md) |
| …browsing by **keywords / search-shaped traces** | [Mechanism keywords](../discovery/mechanism_keywords.md) |

---

## Public Routing Rule

Use this as a compact wiring diagram—how folders relate, not a ladder of importance.

- **Mechanics** (`docs/mechanics/`): reusable patterns for framing work, roles, and outputs. [Public Garden / Park / Vault Routing](08_public_garden_park_vault_routing.md) defines how material is held, processed, or published.
- **Safety guards** (`docs/safety/`): boundaries around harm, amplification, and external effects—not instructions to bypass judgment.
- **Prompts** (`docs/prompts/`): how openings are translated before an answer hardens around surface wording.
- **Afterwords** (`docs/afterwords/`): short landing traces after a move; they compress context, they do not replace audit.
- **x_dance** (`docs/x_dance/`): trace-style notes on execution scope, gates, and correction pressure during a run.
- **Discovery** (`docs/discovery/`): keyword-oriented maps so readers can scan language without assuming one canonical narrative order.
- **GitHub:** [GitHub as Public Connection Layer](09_github_as_public_connection_layer.md) explains how repository features can support visible discussion, proposal, review, and correction.

Nothing here closes the loop between these layers except **your reading path**. Jump across folders as needed; cross-links in this README point at concrete files.

---

## Reader Orientation

You do **not** need private source context to read this mechanism layer. These documents are written so patterns, boundaries, and traces can be inspected from the text alone. Where something depends on unstated history, treat that as a gap to flag—not a signal to fetch non-public material.

---

## Correction Invitation

Corrections, clearer wording, and safer boundaries are welcome. Prefer concrete edits (broken links, tighter boundaries, clearer routing) over narrative expansion.

---

## Core Mechanism Clusters

These clusters overlap; one document may touch several. Use them as orientation, not rigid taxonomy.

| Cluster | What it covers | Primary hooks in this repo |
|--------|-----------------|----------------------------|
| **Transparency / splitter mechanics** | Making distinctions visible; separating layers so pressure does not collapse into a single blind spot | [00_splitter_transparency_protocol.md](00_splitter_transparency_protocol.md), [02_foundation_tree.md](02_foundation_tree.md) |
| **AI deviation and correction mechanics** | Treating model drift as trace; correcting course without pretending outputs are ground truth | [03_ai_deviation_as_trace.md](03_ai_deviation_as_trace.md), [afterwords reflections](../afterwords/reflections/2026-05-08_ai_deviation_not_mistake.md) |
| **Confirmation and role mechanics** | How confirmation paths and roles are framed relative to patterns and tools—not as verdict machines | [04_confirmation_path_and_ai_role.md](04_confirmation_path_and_ai_role.md), [04_facts_patterns_and_ai_role.md](04_facts_patterns_and_ai_role.md) |
| **Dual-language / symbol-first output mechanics** | Structured or bilingual outputs when plain prose obscures mechanism | [05_dual_language_output_protocol.md](05_dual_language_output_protocol.md) |
| **External mirror and bundling mechanics** | External-facing summaries and bundles without turning outsiders into proof | [06_public_invitation_priority_protocol.md](06_public_invitation_priority_protocol.md), [07_external_mirror_bundling.md](07_external_mirror_bundling.md) |
| **Prompt opening mechanics** | Translating the opening of a prompt before answering surface wording | [prompt_opening_translation_protocol.md](../prompts/prompt_opening_translation_protocol.md), [prompts README](../prompts/README.md) |
| **Afterword / landing trace mechanics** | Short landing reflections after a move—not replacements for full audit | [afterwords README](../afterwords/README.md) |
| **Safety and external-impact guards** | Boundaries around harm, folly amplification, and external effects | [safety README](../safety/README.md), [external impact guards](../safety/external_impact_guards/README.md) |
| **X dance / execution mechanics** | Scope separation, gates, and trace-style execution notes | [synced_fresh_mirror_gate.md](../x_dance/synced_fresh_mirror_gate.md), [2026-05-08_x_king_moment_scope_separation.md](../x_dance/2026-05-08_x_king_moment_scope_separation.md), [nine-branch prompt tracks](../prompts/x_execution/2026-05-08_nine_branch_prompt_tracks.md) |
| **Discovery and keyword trace mechanics** | Keyword-oriented scanning of mechanism language | [mechanism_keywords.md](../discovery/mechanism_keywords.md) |

Supporting rhythm / pressure language (same layer, still mechanism—not prescription):

- [01_pressure_release_methodology.md](01_pressure_release_methodology.md)

---

## Existing Public Links

Paths below are **relative to this file** (`docs/mechanics/README.md`). Only entries that exist in the tree at authoring time are linked.

### Mechanism notes (`docs/mechanics/`)

- [00_splitter_transparency_protocol.md](00_splitter_transparency_protocol.md)
- [01_pressure_release_methodology.md](01_pressure_release_methodology.md)
- [02_foundation_tree.md](02_foundation_tree.md)
- [03_ai_deviation_as_trace.md](03_ai_deviation_as_trace.md)
- [04_confirmation_path_and_ai_role.md](04_confirmation_path_and_ai_role.md)
- [04_facts_patterns_and_ai_role.md](04_facts_patterns_and_ai_role.md)
- [05_dual_language_output_protocol.md](05_dual_language_output_protocol.md)
- [06_public_invitation_priority_protocol.md](06_public_invitation_priority_protocol.md)
- [07_external_mirror_bundling.md](07_external_mirror_bundling.md)
- [Public Garden / Park / Vault Routing](08_public_garden_park_vault_routing.md)
- [GitHub as Public Connection Layer](09_github_as_public_connection_layer.md)

### Discovery (`docs/discovery/`)

- [mechanism_keywords.md](../discovery/mechanism_keywords.md)

### Safety (`docs/safety/`)

- [README](../safety/README.md)
- [external_impact_guards/README](../safety/external_impact_guards/README.md)
- [external_impact_guards/idiootbescherming](../safety/external_impact_guards/idiootbescherming.md)

### Afterwords (`docs/afterwords/`)

- [README](../afterwords/README.md)
- [reflections/2026-05-08_ai_deviation_not_mistake](../afterwords/reflections/2026-05-08_ai_deviation_not_mistake.md)

### X dance / execution traces (`docs/x_dance/`)

- [synced_fresh_mirror_gate](../x_dance/synced_fresh_mirror_gate.md)
- [2026-05-08_x_king_moment_scope_separation](../x_dance/2026-05-08_x_king_moment_scope_separation.md)

### Prompts (`docs/prompts/`)

- [README](../prompts/README.md)
- [prompt_opening_translation_protocol](../prompts/prompt_opening_translation_protocol.md)
- [deepsearch/gemini_beast_mode_doc](../prompts/deepsearch/gemini_beast_mode_doc.md)
- [x_execution/2026-05-08_nine_branch_prompt_tracks](../prompts/x_execution/2026-05-08_nine_branch_prompt_tracks.md)

### Discussions (`docs/discussions/`)

- [General Discussion — What Are We Missing?](../discussions/00_general_meekijkwaaier_start.md)

### Signals (`docs/signals/`)

- [GitHub SEO / Traffic Statistics Log](../signals/github_seo_traffic_stats.md)

### Framework root

- [README](../../README.md) — high-level framing of the wider project (not identical to this mechanics map).

---

## Safety Boundary

- **Public mechanism notes abstract from lived friction.** They omit raw incidents and identifiable contexts by design.
- **Raw or private source material is not reproduced here.** Nothing in this index invites importing private logs or vault-only material into public reasoning.
- **Local or private vault paths are not public input** for readers of this map; keep separation explicit.
- **External people, signals, or mirrors are not treated as proof** in these docs—they may illustrate bundling or caution, not validation.
- **AI output is trace and instrument**, not authority: deviation is expected; correction is part of the workflow ([03_ai_deviation_as_trace.md](03_ai_deviation_as_trace.md), [prompts README](../prompts/README.md)).

---

## Working Principle

Language here aligns with:

- **Diff over statement** — prefer observable change over declarative closure.
- **Correction over certainty** — revise when structure shifts; mechanisms are versionable.
- **Smallest safe movement** — scale interventions to what the boundary allows.
- **No hidden trust** — assumptions should be visible or explicitly deferred.
- **Public garden after processing** — share after stripping identifiers and raw source; tend the public layer deliberately.
- **Source stays protected** — origin material stays non-public unless independently chosen for release.
- **Mechanism becomes visible** — patterns are documented so they can be inspected and improved.

---

## Status

This file is a **public navigation layer** for the mechanism field. It may be **corrected, extended, or re-linked** as folders grow. If a linked path moves or is removed, update this index rather than treating it as canonical architecture.
