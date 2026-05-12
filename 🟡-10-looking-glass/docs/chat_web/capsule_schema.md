# Capsule schema

Capsules zijn **compressies en routes**, geen vervanging van de bron. De ruwe bron blijft waar hij hoort (lokaal, kluis, of ander kanaal); de capsule **wijst** en **ordert**.

## Velden

Elke capsule ondersteunt minimaal de volgende velden (JSON-achtige sleutels; waarden zijn mens-leesbaar):

| Veld | Bedoeling |
| --- | --- |
| `source_type` | Soort bron (bijv. chat_export, repo_doc, issue, mail_thread, notitie) |
| `source_pointer` | Stabiele verwijzing naar waar de bron leeft (pad, URL, repo-locatie); geen volledige raw dump in de capsule |
| `chat_name` | Menselijke naam of label van het gesprek / de thread (indien van toepassing) |
| `date` | Datum of datumbereik van de beweging |
| `raw_source_status` | Bijv. intact, alleen_pointer, excerpt_allowed, niet_kopiëren |
| `summary` | Korte samenvatting; geen claim van volledigheid |
| `anchors` | Vaste ankers (titels, besluitregels, file-ankers) |
| `labels` | Tags voor routing (thema, domein, urgentie-vrij) |
| `status` | Bijv. intake, gelabeld, gecapsuleerd, in_index, geparkeerd |
| `pressure` | Druklabel (bijv. laag / middel / hoog) — geen harde meting, wel zichtbaarheid |
| `visibility` | Bijv. vault, garden, park, public_trace — past bij zichtbaarheids poort |
| `linked_files` | Lijst van gerelateerde bestanden in repo of kennisbank |
| `linked_engines` | Verwijzingen naar engine-register / lens-namen waar relevant |
| `linked_threads` | Andere chats of capsules die hierop aansluiten |
| `linked_people_or_roles` | Rollen of namen op hoog niveau (geen gevoelige details verplicht) |
| `claim_status` | Bijv. observatie, hypothese, bron_gesterkt, alleen_vraag |
| `safety_gate` | Wat eerst door mens/trainer moet (bijv. groen voor publicatie) |
| `next_safe_step` | Eén kleine volgende stap |

## Gebruik

1. Eén capsule per duidelijke eenheid van beweging.
2. Geen private raw chat in het `summary` of in losse velden tenzij expres toegestaan en gelabeld.
3. `source_pointer` is leidend; bij twijfel uitbreiden, niet de bron “verbeteren” in de capsule.
