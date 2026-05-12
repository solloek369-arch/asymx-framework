# MakaChain Payment Friction Lens

Public mechanism note — observation only

## 1. Why this note exists

Betalingsketens kunnen zichtbare gebruikerswrijving verlagen (bijvoorbeeld door duidelijkere fee-logica of minder noodzaak voor een aparte gas-token-ervaring) terwijl daaronder **enterprise-interpretatiewrijving** kan blijven bestaan: hoe finance, boekhouding en compliance de keten zien, niet alleen of de transfer technisch rondgaat.

Deze notitie scheidt bewust:

- on-chain payment mechanics
- merchant- en accounting-interpretatie
- compliance-vragen (als vraag, niet als oordeel)
- developer-integrationsoppervlak
- een **public correction path** voor fouten in de openbare “lens”

## 2. The visible strength

Volgens publieke MakaChain/Cregis-materialen wordt een model geschetst met onder andere: een vaste **transaction fee** rond USD $0,10, betaald in het **asset van de transfer** (zelfde vermogen als de betaling), met **minder behoefte aan een aparte gas-token** voor de gebruiker, en een op **payment** gerichte infrastructuurrichting.

Dit is **geen** claim op volledigheid, live beschikbaarheid bij elke merchant, of uniforme rechterlijke/belastingconclusie — alleen: wat in het publieke materiaal naar voren komt als ontwerpintentie.

## 3. The remaining beetle on the shoulder

Metafoor: er blijft een **kever op de schouder** als de technische betalingsroute redelijk helder oogt, maar de **bedrijfsmatige interpretatie** nog niet volledig zichtbaar is (rapportage, reconciliatie, vertrouwen bij inkopers).

Vijf **publieke enterprise-vragen** (open, geen antwoord geclaimd):

1. Hoe reconcileert een merchant **bruto**bedrag, **fee**, **netto**-settlement en **tijdstip** in eigen processen?
2. Welke receipt/event-velden zijn nodig voor accounting-systemen — zonder ERP‑mapping hier als waarheid vast te leggen?
3. Welke **compliance-relevante** gebeurtenissen moeten zichtbaar zijn zonder onnodige persoonsdata te exposen?
4. Hoe testen ontwikkelaars flows **zonder** dat elke integratie eerst eigen interpretatiewerk dupliceert?
5. Wat moet **herhaald en aantoonbaar** verschijnen voordat enterprise-kopers het patroon vertrouwen?

## 4. Proposed public schema direction

### Payment Receipt Event Schema v0.1

Niet-bindend voorbeeld — **possible schema**, **needs confirmation** per use-case.

| Veld | Rol (indicatief) |
|------|------------------|
| transaction_id | keten-identificatie van de betaling |
| chain_id | netwerkcontext |
| asset_sent | vermogen dat de betaling draagt |
| gross_amount | bedrag vóór fee in vergelijkbare eenheid |
| fee_asset | asset waarin fee wordt uitgedrukt |
| fee_amount | fee-bedrag |
| net_amount | indicatie van netto na fee (definitie: ter discussie) |
| timestamp | tijdsanker voor reconciliatie |
| sender_reference_optional | optionele referentie zonder PII te forceren |
| receiver_reference_optional | idem ontvanger-kant |
| settlement_status | statuslabel; semantiek moet nog **public correction** krijgen |
| source_hash | herleidbare bron voor integriteit van het event-record |
| interpretation_notes | expliciet veld voor voorbehoud en context |

**Waarschuwing:** dit is **geen** boekhoud-, belasting-, juridisch of compliance-standaard. Het is een **discussion schema** voor alignment en correcties.

## 5. AsymX value

AsymX vervangt MakaChain niet en claimt geen protocol-autoriteit. Het voegt een **publieke vertaallens** toe:

on-chain event → zakelijke vraag → schema-kandidaat → **correction loop** (open, herzienbaar).

## 6. Silent Threshold

Als **dezelfde** wrijving onafhankelijk uit **drie** verschillende bronnen terugkomt (merchant, dev, reviewer-achtige observatie), wordt het een **kandidaat** voor een publieke checklist of schema-update — nog steeds geen automatische waarheid.

## 7. Public correction path

MakaChain, ontwikkelaars, merchants, payment providers, accountants en compliance-reviewers zijn uitgenodigd om deze lens te **verbeteren of te weerspreken** met concrete, publiek veilige toevoegingen: welke velden ontbreken, welke termen verkeerd begrepen worden, welke voorbeelden nodig zijn. Geen claims van goedkeuring of adoptie door een project vereist om feedback geldig te maken.

## 8. Status

Observation only.

No partnership claim.

No investment advice.

No legal, tax, accounting, compliance or security guarantee.

No claim that MakaChain has adopted this structure.
