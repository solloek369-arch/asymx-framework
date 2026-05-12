# Dual Language Output Protocol

Status: PUBLIC MECHANIC  
Purpose: Reduce human cognitive load while preserving traceability, decision authority and external-impact gates.

## Core Rule

Loek sees symbols.  
X sees commands.  
Git preserves traces.  
AI translates between layers.

Computer language is not removed.  
Computer language is moved to the execution layer.

## Two-Layer Output

Every AI/X response in this repository should prefer this order:

### 1. LOEK-LAAG / SYMBOL FIELD

Use symbol language first:

- 🌬️ ADEM = observe only
- 👁️ SPOREN = visible changes
- 🧺 MAND = related cluster
- ⚖️ WEGING = risk / claim / impact check
- 🟢 GROEN = safe to continue
- 🟡 PARK = keep local / later / not public yet
- 🔴 ROOD = stop
- ⚫ KLUIS = private / local vault
- 🚪 POORT = Loek must decide
- 🔥 IMPACT = public, person, company, family, legal, mail, commit or push effect
- 🕷️ SPRING = one small safe movement
- 🪨 LANDING = post-action status check

Loek should be able to decide without reading computer language.

### 2. AI/X-LAAG / TECHNICAL TRACE

Use exact computer language only after the symbol layer:

- files
- paths
- commands
- git status
- diff summaries
- proposed execution commands
- verification output
- recovery notes

The technical trace exists for execution, verification and auditability.

## Autonomy Boundary

Autonomous or near-autonomous:

- observe
- summarize status
- group files into baskets
- identify risk
- propose next step
- repair small typos when explicitly allowed
- prepare landing cards

Human gate required:

- commit
- push
- mail
- publication
- external claim
- company/person/family impact
- deletion
- overwrite
- legal or formal language

## AI Comparison Trace

This protocol emerged through comparison between multiple AI outputs provided by Loek:

- ChatGPT
- Gemini
- Grok
- Perplexity

The shared pattern was:

> Symbol language first for Loek.  
> Computer language second for AI/X execution.  
> Loek decides from the symbol layer.  
> X executes from the technical layer.  
> External impact requires an explicit human gate.

These AI outputs are treated as comparison traces, not as proof, authority, endorsement or final truth.

## Claim-Safety Note

This protocol does not claim that AI autonomy is safe by default.

It defines a local operating pattern:

- more autonomy before impact
- stricter human gate at impact
- one basket at a time
- one small jump at a time
- landing visible after every movement

## Required Response Shape

### LOEK-LAAG / SYMBOL FIELD

🌬️ ADEM: what is visible?  
👁️ SPOREN: what changed?  
🧺 MANDEN: what belongs together?  
⚖️ WEGING: what is the risk?  
🟢🟡🔴 ADVIES: green, park or red?  
🚪 POORT: what does Loek need to decide?  
🕷️ KLEINSTE SPRING: what is the smallest safe next movement?  
🪨 LANDINGSEIS: what must be visible after movement?

### AI/X-LAAG / TECHNICAL TRACE

Exact files, commands, git state, diff summary and proposed command.

## Closing Rule

No computer-language-only answer.

No execution without symbol-layer landing.

No external impact without explicit human green.
