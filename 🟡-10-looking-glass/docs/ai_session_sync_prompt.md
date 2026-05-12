# AsymX AI Session Sync Prompt v1

Datum: 2026-05-06

Gebruik dit aan het begin van een nieuwe AI- of Cursor-sessie om meteen synchroon te starten.

```text
Je werkt in het AsymX / SoLuTri Field Engine project van Loek.

Repo:
/Users/loek/SWON/asymx-framework

Huidige basis:
- Logistics Level 1 staat als publieke statische lokale lens in `🔵-30-workbench/logistics-level1/`.
- Release-tag: `logistics-level1-v1.0`.
- Engine Register v1 staat in `🟡-10-looking-glass/docs/engine_register.md` en `🟡-10-looking-glass/docs/engine_register.json`.
- Pressure Queue staat in `🟡-10-looking-glass/docs/pressure_queue.md`.
- Open Eindjes Register staat in `🟡-10-looking-glass/docs/open_eindjes_register.md`.
- Level 1 Open Field Map staat in `🟡-10-looking-glass/docs/level_1_open_field_map.md`.

Niet doen:
- geen bron overschrijven
- geen bestaande werkende files slopen
- geen refactor zonder expliciete opdracht
- geen backend/npm/externe libs/API/tracking toevoegen aan Level 1 tools
- geen echte bedrijfsdata toevoegen
- geen harde claims maken
- geen nieuwe engine bouwen voordat hij in het Engine Register staat

Heilige regels:
1. Bron blijft heilig.
2. Verwerking is metadata, pointer, label, route of tijdelijke expressie.
3. Level 1 = lokaal, statisch, inspecteerbaar, veilig.
4. Nieuwe gedachten eerst registreren of parkeren; niet meteen bouwen.
5. Kleinste veilige stap boven grote visie.

Actuele drukverlagende prioriteit:
Maak eerst Chat Capsule / Chat Web Index mogelijk, zodat oude chats veilig ingeklapt kunnen worden zonder projectgeheugen te verliezen.

Voordat je iets wijzigt:
1. Run `git status`.
2. Lees `🟡-10-looking-glass/docs/engine_register.md`.
3. Lees `🟡-10-looking-glass/docs/pressure_queue.md`.
4. Lees `🟡-10-looking-glass/docs/open_eindjes_register.md`.
5. Benoem exact welke file(s) je wilt wijzigen.
6. Geef één kleine veilige stap.

Als je code of docs aanpast:
- maak alleen de gevraagde wijziging
- rapporteer gewijzigde files
- sluit af met test/controlecommando’s
- commit niet automatisch tenzij Loek dat vraagt

Doel van deze sessie:
Druk verlagen, synchroniteit vergroten, bron intact houden.
```