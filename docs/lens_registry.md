# AsymX Level 1 Lens Registry

Doel: één publiek overzicht van Level 1-lenzen die al geoogst, gepubliceerd of gepland zijn.

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

## Released Level 1 lenses

| Nr | Lens | Pad | Status | Tag | Doel |
|---:|---|---|---|---|---|
| 01 | Logistics Level 1 / Static Shadow Run Lens | `logistics-level1/` | RELEASED | `logistics-level1-v1.0` | Herhaalde manco / ghost pick / short-pick clusters lokaal zichtbaar maken. |
| 02 | Chat Intake Vault | `chat-intake-level1/` | RELEASED | `chat-intake-level1-v1.0` | AI/chats veilig innemen; bron intact houden; eerste routing mogelijk maken. |
| 03 | Story Filter | `story-filter-level1/` | RELEASED | `story-filter-level1-v1.0` |kst splitsen in verhaalopbouw, herhaling en ruis/nu niet. |

## Planned / parked lenses

| Lens | Status | Reden |
|---|---|---|
| Claim Safety Level 1 | PLANNED | Bewijsveiligheid als aparte kleine lens. |
| Prompt Router Level 1 | ACTIVE_PRESSURE | AI-output routeren naar FILE / ANCHOR / PROMPT / CLAIMCHECK / NOISE / OPEN_END. |
| Cursor Prompt Safety Level 1 | ACTIVE_PRESSURE | Grotere bouwsessies beschermen tegen overschrijven/refactoren. |
| Export Bundle Level 1 | ACTIVE_PRESSURE | Bron + labels + open eindjes + outputs samen exporteren. |
| Symbol Engine Level 1 | PARKED | Inhoudelijk rijp, maar nog niet trekken. |
| Family Interface Level 1 | PARKED | Architectuur helder, maar nog niet bouwen. |
| Always-On Field Level 1 | PARKED | Werkende capture-basis bestaat; productlaag later. |

## Werkregel

Nieuwe lens pas toevoegen als:
1. hij in `docs/engine_register.md` staat;
2. hij in `docs/pressure_queue.md` of `docs/open_eindjes_register.md` past;
3. hij klein genoeg is voor Level 1;
4. hij geen bron overschrijft.
