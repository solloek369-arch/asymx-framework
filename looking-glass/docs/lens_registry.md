# AsymX Level 1 Lens Registry

Doel: één overzicht van Level 1-lenzen die released, oogstbaar, actief of geparkeerd zijn.

Dit register is geen eindlijst.
Het is een huidige kaart van wat zichtbaar genoeg is om niet meer los in het hoofd te hoeven hangen.

Level 1 betekent:
- lokaal
- statisch
- inspecteerbaar
- geen backend
- geen upload
- geen tracking
- geen echte privé- of bedrijfsdata
- geen harde claims
- bron blijft intact

## Released

| Nr | Lens | Pad | Tag |
|---:|---|---|---|
| 01 | Logistics Level 1 / Static Shadow Run Lens | `workbench/logistics-level1/` | `logistics-level1-v1.0` |
| 02 | Chat Intake Vault | `workbench/chat-intake-level1/` | `chat-intake-level1-v1.0` |
| 03 | Story Filter | `workbench/story-filter-level1/` | `story-filter-level1-v1.0` |

## Next candidates

| Nr | Lens | Mogelijke map | Status |
|---:|---|---|---|
| 04 | Claim Safety / Dancing Trust | `claim-safety-el1/` | NEXT_CANDIDATE |
| 05 | Sligro Zichtbaarheidsanker | `sligro-anchor-level1/` | NEXT_CANDIDATE |

## Active pressure

| Lens | Status | Reden |
|---|---|---|
| Prompt Router Level 1 | ACTIVE_PRESSURE | AI-output routeren naar FILE / ANCHOR / PROMPT / CLAIMCHECK / NOISE / OPEN_END |
| Cursor Prompt Safety Level 1 | ACTIVE_PRESSURE | Bouwsessies beschermen tegen overschrijven/refactoren |
| Export Bundle Level 1 | ACTIVE_PRESSURE | Bron + labels + open eindjes + outputs samen exporteren |

## Parked

| Lens | Status |
|---|---|
| Symbol Engine Level 1 | PARKED |
| Family Interface Level 1 | PARKED |
| Always-On Field Level 1 | PARKED |

## Werkregel

Nieuwe lens pas toevoegen als:
1. hij in `looking-glass/docs/engine_register.md` staat;
2. hij past in `looking-glass/docs/pressure_queue.md` of `looking-glass/docs/open_eindjes_register.md`;
3. hij klein genoeg is voor Level 1;
4. hij geen bron overschrijft;
5. hij nu druk verlaagt.
