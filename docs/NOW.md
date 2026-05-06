# AsymX NOW State v1

Datum: 2026-05-06

Doel: één actuele sync-laag voor mens + AI + repo. Dit bestand verlaagt druk: eerst lezen, dan pas bouwen.

## Huidige repo-status

- Repo: `/Users/loek/SWON/asymx-framework`
- Remote: `https://github.com/solloek369-arch/asymx-framework.git`
- Branch: `main`
- Laatst bevestigde status: clean, up to date with `origin/main`
- Laatst bevestigd tijdens basis-sync: `fc6a7d5` — Add Level 1 lens registry

## Laatste ankers in Git

- `fc6a7d5` — Add Level 1 lens registry
- `44d380e` — Add pressure queue and open ends register
- `8b4db78` — Add engine register v1
- `be86ebd` — Add Level 1 open field map
- `541106c` — Add static logistics level 1 shadow run lens
- Tag: `logistics-level1-v1.0`

## Actieve drukverlagende documenten

- `docs/engine_register.md` — wat bestaat er?
- `docs/engine_register.json` — machineleesbare engine-status
- `docs/pressure_queue.md` — wat vraagt nu aandacht?
- `docs/open_eindjes_register.md` — wat mag blijven liggen zonder hoofd-druk?
- `docs/level_1_open_field_map.md` — publieke Level 1 veldkaart

## Actieve publieke Level 1-lens

- `logistics-level1/`
- Status: public/static/local-only Level 1
- Tag: `logistics-level1-v1.0`
- Geen backend
- Geen npm
- Geen externe libraries
- Geen upload
- Geen tracking
- Geen echte bedrijfsdata
- Geen harde claims

## Heilige regels

1. Bron blijft heilig.
2. Geen bestaande werkende files overschrijven zonder expliciete opdracht.
3. Geen refactor om het refactoren.
4. Geen nieuwe engine bouwen voordat hij in `docs/engine_register.md` staat.
5. Geen grote app maken als één markdown/protocol de druk al verlaagt.
6. Geen claims harder maken dan bewijs toestaat.
7. Level 1 blijft lokaal, statisch, inspecteerbaar en veilig.

## Nu niet trekken

- Always-On productlaag: parkeren; core werkt als fundament.
- Familie/persoonlijke interface: parkeren; architectuur is helder maar niet nu bouwen.
- Symbool Engine: inhoudelijk rijp, maar nog niet als publieke lens trekken.
- Sligro eindvorm: gebruiker bepaalt zelf wanneer en hoe groot; niet forceren.

## Nu wel aandacht waard

1. Chat Capsule / Chat Web Index — nodig voordat oude chats veilig gewist kunnen worden.
2. Prompt Router / AI Output Status — nodig voor output van ChatGPT/Gemini/Grok/Perplexity/Cursor.
3. Cursor Prompt Safety — nodig vóór grotere bouwopdrachten.
4. Export Alles / Bundle Engine — nodig om bron + capsules + open eindjes samen te bewaren.

## Kleinste volgende stap

Niet bouwen aan de grote engines.

Maak eerst één Chat Capsule schema waarmee oude chats veilig kunnen worden ingeklapt:

- titel
- datum/periode
- bron/chat-id of link
- hoofdanker
- subankers
- gekoppelde engines
- beslissingen
- gemaakte bestanden/commits
- open eindjes
- volgende kleinste stap
- status: ACTIVE / PARKED / DONE

## Stopregel

Als iets nieuw opkomt:

- staat het al in Engine Register? Zo niet: registreren.
- is het een open eindje? Zo ja: parkeren in Open Eindjes Register.
- verlaagt het nú druk? Alleen dan uitvoeren.

## Eénzinssamenvatting

AsymX staat nu in een veilige Level 1-publicatiefase: de eerste publieke logistieke lens is getagd, de enginekaart bestaat, de drukwachtrij bestaat, en losse open eindjes hoeven niet meer in het hoofd te blijven hangen.
## Update — Level 1 lenses geoogst

Na de eerste NOW-sync zijn twee extra bestaande engines veilig geoogst als Level 1-lenzen:

- `chat-intake-level1/` — tag: `chat-intake-level1-v1.0`
- `story-filter-level1/` — tag: `story-filter-level1-v1.0`

Actuele released Level 1-lenzen:

1. `logistics-level1/`
2. `chat-intake-level1/`
3. `story-filter-level1/`

Zie ook: `docs/lens_registry.md`.

## Update — drie Level 1-lenzen zichtbaar

 huidige stand is bijgewerkt in:

- `docs/RELEASE_STATE.md`
- `docs/lens_registry.md`

Actuele released Level 1-lenzen:

1. `logistics-level1/` — `logistics-level1-v1.0`
2. `chat-intake-level1/` — `chat-intake-level1-v1.0`
3. `story-filter-level1/` — `story-filter-level1-v1.0`

Deze releases zijn ankerpunten, geen eindwaarheden.

Volgende oogstbare kandidaten, zonder nu te forceren:

- `claim-safety-level1/`
- `sligro-anchor-level1/`

Basisregel blijft:

Wat zichtbaar genoeg is, hoeft nu niet opnieuw gedragen te worden.
Wat levend moet blijven, wordt niet dichtgezet.
