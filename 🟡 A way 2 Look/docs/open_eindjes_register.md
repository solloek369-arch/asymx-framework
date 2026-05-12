# AsymX Open Eindjes Register v1

Datum: 2026-05-06

Doel: losse drukpunten bewaren zonder ze meteen te hoeven oplossen.

## Regels

- Een open eindje is geen taak.
- Een open eindje mag blijven liggen.
- Alleen als het drie keer terugkomt of iets blokkeert, krijgt het aandacht.
- Bron blijft intact; dit register is alleen metadata.

## Signaalwoorden

later, nog niet, mist, ontbreekt, parkeren, terugkomen, na Sligro, niet af, moet nog, open, twijfel, checken, bewaren

## Open eindjes

### OE-001 — Symbool Engine staat nog niet als publieke GitHub-lens.

- **Gekoppelde engine:** Symbool Engine
- **Status:** `PARKED`
- **Kleinste veilige stap:** Pas oppakken na Prompt Router / Open Eindjes basis.

### OE-002 — Chat Capsule / Chat Web Index nodig voordat oude chats veilig gewist kunnen worden.

- **Gekoppelde engine:** Chat Capsule Engine
- **Status:** `ACTIVE_PRESSURE`
- **Kleinste veilige stap:** Schema maken: titel, datum, hoofdanker, subankers, engines, open eindjes.

### OE-003 — Prompt Router nodig voor output van ChatGPT/Gemini/Grok/Perplexity/Cursor.

- **Gekoppelde engine:** Prompt Router
- **Status:** `ACTIVE_PRESSURE`
- **Kleinste veilige stap:** Minimal paste-and-label tool: FILE / ANCHOR / PROMPT / CLAIMCHECK / NOISE / OPEN_END.

### OE-004 — Cursor Prompt Safety nodig vóór grotere build-opdrachten.

- **Gekoppelde engine:** Cursor Prompt Safety
- **Status:** `ACTIVE_PRESSURE`
- **Kleinste veilige stap:** Vaste beschermprompt maken: preserve source, inspect first, no deletion, no refactor.

### OE-005 — Export Alles / Bundle Engine nodig om bron + labels + outputs + open eindjes samen te bewaren.

- **Gekoppelde engine:** Export Bundle
- **Status:** `ACTIVE_PRESSURE`
- **Kleinste veilige stap:** Bundle JSON + Markdown schema maken.

### OE-006 — Always-On productlaag is geparkeerd tot na Sligro/registry-stabilisatie.

- **Gekoppelde engine:** Always-On Field
- **Status:** `PARKED`
- **Kleinste veilige stap:** Core files heilig houden; niet nu doorbouwen.

### OE-007 — Familie/persoonlijke interface is architectuur-helder maar nog niet bouwen.

- **Gekoppelde engine:** Family Interface
- **Status:** `PARKED`
- **Kleinste veilige stap:** Alleen registry/status bijhouden.

## Nieuwe open eindjes template

```text
OE-XXX — [korte zin]
Gekoppelde engine:
Status: PARKED / ACTIVE_PRESSURE / WAITING / DONE
Kleinste veilige stap:
Bron/chat:
```