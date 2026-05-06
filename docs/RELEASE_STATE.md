# AsymX Release State

Doel: zichtbaar maken wat op dit moment voldoende gedragen wordt, zodat het niet meer in het hoofd hoeft te blijven.

Dit document sluit niets definitief af.
Het markeert alleen de huidige stand van het veld.

Een release is hier geen eindwaarheid.
Een release is een ankerpunt: een zichtbare, terugvindbare staat waarop later verder kan worden afgestemd.

## Huidige staat

AsymX Framework staat in een veilige Level 1-publicatiefase.

Er zijn nu drie Level 1-lenzen geoogst, gepusht en getagd.

## Released Level 1 lenses

| Nr | Lens | Pad | Tag | Betekenis |
|---:|---|---|---|---|
| 01 | Logistics Level 1 / Static Shadow Run Lens | `logistics-level1/` | `logistics-level1-v1.0` | Logistieke frictie lokaal zichtbaar maken zonder upload of harde claims. |
| 02 | Chat Intake Vault | `chat-intake-level1/` `chat-intake-level1-v1.0` | AI/chats veilig innemen; bron intact houden; eerste routing mogelijk maken. |
| 03 | Story Filter | `story-filter-level1/` | `story-filter-level1-v1.0` | Tekst splitsen in verhaalopbouw, herhaling en ruis/nu niet. |

## Actieve drukverlagende documenten

| Document | Functie |
|---|---|
| `docs/NOW.md` | Waar staan we nu? |
| `docs/engine_register.md` | Welke engines bestaan er? |
| `docs/engine_register.json` | Machineleesbare enginekaart |
| `docs/pressure_queue.md` | Wat vraagt nu aandacht? |
| `docs/open_eindjes_register.md` | Wat mag blijven liggen zonder hoofd-druk? |
| `docs/ai_session_sync_prompt.md` | Startprompt voor AI/Cursor-sessies |
| `docs/level_1_open_field_map.md` | Publieke Level 1 veldkaart |

## Basisregels

1. Bron blijft heilig.
2. Oogsten gebeurt via kopiëren, niet verplaatsen.
3. Een lens is geen waarheid, maar een kijkrichting.
4. Een tag is geen eindpunt, maar een markeringspunt.
5. Geen bestaande werkende files overschrijven zonder expliciete opdracht.
6. Geen backend, upload, tracking of externe libraries toevoegen aan Level 1.
7. Geen echte privédata of bedrijfsdata committen.
8. Geen harde claims zonder bewijs.
9. Wat zichtbaagenoeg is, hoeft nu niet opnieuw gedragen te worden.
10. Wat levend moet blijven, wordt niet dichtgezet.

## Volgende oogstbare kandidaten

Deze kandidaten lijken rijp, maar hoeven nu nog niet te trekken.

| Kandidaat | Mogelijke bron | Mogelijke map | Status |
|---|---|---|---|
| Claim Safety / Dancing Trust | `structuur_engine_v12_dancing_trust_filter.html` | `claim-safety-level1/` | NEXT_CANDIDATE |
| Sligro Zichtbaarheidsanker | `structuur_engine_sligro_anchor_builder.html` | `sligro-anchor-level1/` | NEXT_CANDIDATE |

## Niet nu forceren

| Tak | Status |
|---|---|
| Symbool Engine | PARKED |
| Always-On productlaag | PARKED |
| Familie / persoonlijke interfaces | PARKED |
| Export Bundle Engine | ACTIVE_PRESSURE, maar eerst schema |
| Prompt Router | ACTIVE_PRESSURE, maar klein houden |
| Cursor Prompt Safety | ACTIVE_PRESSURE, als beschermprompt/protocol |

## Eénzinssamenvatting

De druk is verlaagd doordat AsymX nu drie zichtbare Level 1-ankers heeft plus een registerlaag die bewaart wat bestaat, at trekt, en wat rustig mag blijven liggen.
