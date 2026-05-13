# AsymX Pressure Queue v1

Datum: 2026-05-06

Doel: druk verlagen door zichtbaar te maken welke engines nu aandacht vragen, welke alleen bewaakt worden, en welke bewust geparkeerd blijven.

## Werkregel

Niet kiezen uit alle engines. Alleen kiezen uit de eerstvolgende drukverlager.

## Eerstvolgende drukverlagers

Deze engines vragen aandacht omdat ze overzicht, veiligheid of geheugen ontlasten.

### 1. ENG-011 — Prompt Router / AI Output Status Engine

- **Waarom nu:** Route AI output into usable statuses: FILE, ANCHOR, PROMPT, CLAIMCHECK, NOISE, OPEN_END.
- **Kleinste stap:** Build a minimal local Level 1 paste-and-label tool.
- **Niet doen:** geen grote app, geen refactor, geen samenvoeging met andere engines.

### 2. ENG-012 — Cursor Prompt Safety Engine

- **Waarom nu:** Protect working files from destructive edits, unwanted refactors, deletion, overbuilding, or source mutation.
- **Kleinste stap:** Create fixed Cursor safety prompt and checklist.
- **Niet doen:** geen grote app, geen refactor, geen samenvoeging met andere engines.

### 3. ENG-013 — Open Eindjes Engine

- **Waarom nu:** Capture phrases like later, missing, not ready, after Sligro, park this, open end, and turn them into visible follow-up anchors.
- **Kleinste stap:** Add open_eindjes section to every chat capsule and bundle export.
- **Niet doen:** geen grote app, geen refactor, geen samenvoeging met andere engines.

### 4. ENG-014 — Chat Capsule / Chat Web Index Engine

- **Waarom nu:** Compress full chats into durable capsules with title, date, anchors, engines, open ends, and source links before chats are deleted.
- **Kleinste stap:** Define capsule schema and create first manual capsule export.
- **Niet doen:** geen grote app, geen refactor, geen samenvoeging met andere engines.

### 5. ENG-015 — Export Alles / Bundle Engine

- **Waarom nu:** Export source, chunks, labels, claims, report/book/kid versions, deepsearch, conclusions, open ends, and engine status in one bundle.
- **Kleinste stap:** Define bundle JSON + Markdown format.
- **Niet doen:** geen grote app, geen refactor, geen samenvoeging met andere engines.

## Daarna pas

- **ENG-004 — Claim Safety / Bewijsveiligheid Engine** — Create or link a small Level 1 claim-safety lens.
- **ENG-008 — Structuur Engine Chat Intake Vault** — Connect output format to Engine Register / Chat Capsule format.
- **ENG-010 — Fractal Web Navigator V3** — Treat as prototype; do not merge into main app until register/dependencies are clear.
- **ENG-016 — Engine Dependency Map** — Generate simple A → feeds → B list from this register.
- **ENG-017 — Public GitHub Lens Registry** — Create docs/lens_registry.md from Engine Register.
- **ENG-018 — Symbool Engine** — Do not build yet; first register as planned lens.
- **ENG-019 — Always-On Field Engine** — Park until after Sligro/registry stabilization; keep core files sacred.
- **ENG-021 — Family / Personal Interface Engine** — Keep parked; only add to registry now.
- **ENG-022 — Report / Book / Kid Story Output Engine** — Wait for Export Bundle format; then make one-button outputs.

## Bewust niet trekken

- **ENG-001 — Source Vault / Bron-Kluis Engine** — status: `STABLE_CORE`
- **ENG-002 — Non-Destructive Fractal Architecture** — status: `STABLE_CORE`
- **ENG-003 — AsymX SoLuTri Field Engine** — status: `STABLE_META_ENGINE`
- **ENG-005 — Release Level 1 Protocol** — status: `READY_AS_PROTOCOL`
- **ENG-006 — Logistics Level 1 / Ghost Pick Analyzer** — status: `PUBLIC_LEVEL_1_READY`
- **ENG-007 — Intentional Alignment / SEO Engine** — status: `READY_AS_PROTOCOL`
- **ENG-009 — Story Filter / Verhaalfilter** — status: `V1_READY`
- **ENG-020 — Audio-Haptic Feedback Engine** — status: `PROTOCOL_READY_NOT_BUILT`
- **ENG-023 — Sligro / AsymX Anchor Engine** — status: `RELEASE_LEVEL_1_ANCHOR`
- **ENG-024 — Hypothesis / Samenkomst Engine** — status: `READY_AS_PROTOCOL`
- **ENG-025 — BEING / Presence Engine** — status: `FOUNDATIONAL_PASSIVE`

## Actieve keuze

De volgende echte stap is niet bouwen maar vangen:

> Maak de Open Eindjes Engine v1 als simpele lijst/capsule-laag, zodat losse 'later / mist / nog niet / parkeren'-signalen niet meer in het hoofd blijven hangen.

## Stopregel

Als een nieuwe gedachte opkomt, voeg hem toe aan `open_eindjes` of aan het `engine_register`. Niet meteen bouwen.