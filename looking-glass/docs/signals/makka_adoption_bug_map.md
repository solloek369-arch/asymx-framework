# Makka Adoption Bug Map — ACX External Mirror

## 1. Status

Externe mirror / adoptie-zichtbaarheidsrapport.

Geen integratieclaims, geen partnerclaims, geen goedkeuring door Makka.

Documentstatus: observatie- en structuurnoot voor ACX-tak; inhoud is claim-safe bedoeld.

## 2. Executive Summary

Makka kan op protocolniveau wrijving rond gas-tokens verlagen.

Zolang adoptie menselijk en organisatorisch blijft, blijft er wrijving: begrip bij merchants, vertrouwen in enterprise-context, compliance-vragen, boekhoudkundige helderheid, support-toestanden, integratie door ontwikkelaars, wallet-onboarding, claim-safe publieke taal, en differentiatie ten opzichte van grotere stablecoin-betalingsinfra.

**Makka makes the payment move.**  
**ACX detects where the movement can still get stuck.**

Dit rapport is een **Adoption Bug Map**: waar “betalen” technisch kan bewegen, maar adoptie alsnog vastloopt.

## 3. Core Makka Signal

Signaalrichting (niet als bewijs van live product-einde voor deze lezer):

Een protocolgerichte benadering die de betalingsbeweging wil verlichten ten opzichte van klassieke gas-token-stappen voor eindgebruikers en trajecten waar payment UX centraal staat.

Exacte productgrenzen en beschikbaarheid: volgens eigen due diligence en primaire bronnen valideren—hier niet gespecificeerd.

## 4. Why This Matters

Als de betalingsbeweging soepeler wordt, verschuift de bottleneck vaak naar:

- uitleg en onboarding
- vertrouwen en reputatie
- compliance en verantwoording
- operationele ondersteuning en foutafhandeling
- integratie-arbeid en testomgevingen
- duidelijke, niet-overclaimende communicatie

ACX richt zich op deze restfrictie als in kaart te brengen veld—niet op prijsvoorspelling of “wie wint de markt” in enkelvoud.

## 5. Market Context

Stablecoin- en payment-infrastructuur is concurrerend en snel evoluerend.

Grotere rails, wallets en compliance-kaders beïnvloeden verwachtingen van merchants en gebruikers.

Een kleinere of andere aanbieder moet vaak **extra verklaarbaarheid** leveren, niet alleen techniek.

Dit rapport stelt geen unieke marktpositie vast en voorspelt geen succes.

## 6. The Core ACX Gift

ACX biedt hier een **Payment Infrastructure Observability**-bril: een gestructureerde manier om adoptie-beletnissen te zien als een kaart van bugs en vertrouwenskloven, niet alleen als “meer marketing”.

Het geschenk is observatie-architectuur en taal om veilig te spreken over wat nog klemzit.

## 7. Beetle / Bug Layer

“Bug” in deze context: elk punt waar de gebruiker of organisatie stilstaat ondanks dat de keten op papier beweegt.

Voorbeeldcategorieën (indicatief):

- UX-interpretatie van “wie draait voor wat”
- refund, chargeback-achtige verwachting versus on-chain realiteit
- KYC/AML-verwachting per corridor en per merchant-type
- accounting mapping (revenue vs settlement, tijdstip, rapportage)
- support: wie is first-line, wat is escalatie
- developer sandbox, documentatie, SDK-volwassenheid

## 8. Adoption Bug Map

**Adoption Bug Map** (samenvatting van clusters):

| Cluster | Typische vastlopers |
|--------|----------------------|
| Merchantbegrip | fee-mental model, reconciliation, klantcommunicatie |
| Enterprise trust | audit trail, vendor due diligence, contractuele helderheid |
| Compliance vragen | jurisdictie, stablecoin-policy, vendor risk |
| Accounting clarity | grootboek, btw/omzet, periodeafbakening |
| Support states | incident, disputed payment, user education |
| Developer integration | API-stabiliteit, testdata, monitoring |
| Wallet onboarding | installatie, recovery, device security perception |
| Taal / positionering | differentiatie vs grote rails zonder overclaim |
| Differentiatie | waarom deze route naast bestaande PSP/stack |

Leegtes in de kaart = open observatiepunten; geen implicatie dat Makka ze niet aanpakt—dit is een externe mirror.

## 9. Trust Gap Map

Vertrouwenskloven ontstaan waar verwachting (snel, simpel, bankachtig) botst met realiteit (on-chain settlement, finaliteit, supportgrenzen).

Observatievragen:

- Wie is contractpartij voor de eindgebruiker?
- Wat is de support-realiteit bij fout of vertraging?
- Hoe zichtbaar is de audit trail voor finance en compliance reviewers?

## 10. Merchant Flow One-Pager

Één pagina denkmodel (hoog niveau):

1. Intent: klant betaalt (online/ter plekke).  
2. Route: welke wallet, welke asset-chain combinatie, welke fee-structuur.  
3. Settlement: wanneer als “betaald” beschouwd voor order fulfillment.  
4. Boekhouding: welke export, welke sleutels voor audit.  
5. Support: pad bij mislukte betaling, gebruikersfout, netwerk-issue.  
6. Communicatie: wat mag publiek gezegd worden (zie sectie 12).

## 11. Competitor Pressure Matrix

Niet: “wij zijn beter.” Wel: drukvelden die differentiatie moeilijk maken.

| Drukbron | Effect op adoptie-story |
|----------|-------------------------|
| Brede stablecoin-adoptie bij grote platforms | Verhoogt “default verwachting” |
| Bank- en PSP-integraties | Verhoogt zorg over reconciliatie en compliance |
| Volwassen wallet UX | Verhoogt drempel bij niche flows |
| Regulatoire ruis | Verhoogt behoefte aan heldere, niet-spectaculaire taal |

Geen marktaandeelcijfers of winnaars-uitspraak in dit document.

## 12. Claim-Safe Language Layer

Richtlijnen voor publieke communicatie:

- beschrijf mechanisme en observatie, niet “goedgekeurd door”
- gebruik voorwaarden: “kan”, “richting”, “te verifiëren”, “hypothese”
- scheid technische mogelijkheid van live deployment bij specifieke merchant
- vermijd absolute veiligheids- en compliantieclaims zonder bron

## 13. Fan Passport / Guardians ID Lens

Lens (conceptueel): identiteit en toegang in fan- of community-context zijn **aparte** discussie van betalingsrails.

Voor dit rapport: betaalinfrastructuur en “passport”-achtige identity-producten mogen niet door elkaar gehaald worden in adoptie-uitleg—tenzij expliciet uitgewerkt en claim-safe vastgelegd.

Geen uitwerking van kindgerichte of familie-waarde mechanismen in dit document (bewuste scope grens).

## 14. Payment Infrastructure Observability

**Payment Infrastructure Observability** hier: het meten en zichtbaar maken van waar betalingen **menselijk en organisatorisch** haperen—los van of de on-chain transfer technisch rond kan.

Instrumenten (conceptueel): checklists, merchant interviews, fouttaxonomie, support ticket clustering, integratie-testrappen.

## 15. What This Does Not Claim

Dit document claimt **niet**:

- een partnership met Makka of derden
- dat Makka dit document heeft beoordeeld of goedgekeurd
- dat er live integratie is met een genoemd product
- juridische compliance of “veilig” in absolute zin
- uniekheid of gegarandeerd marktsucces
- prijs, yield, of beleggingsresultaat (geen financieel advies)
- dat een roadmap ergens beschikbaar is in deze repository

## 16. Suggested Outreach to Makka

Doel: verificatie en correcte framing, niet overclaimen.

- vraag naar canonieke documentatie en support-grenzen
- vraag naar merchant-fit segmenten en voorbeelden die publiek mogen
- bied aan: compacte **Adoption Bug Map** feedback op basis van openbare info en eigen tests—geen impliciete endorsement

Toon: kort, technisch-vriendelijk, geen hype.

## 17. Link to Nick

Mechanismlink: fysieke en relationele inzet opent eerst een **kanaal** (vertrouwen, timing, aanwezigheid).

In dit rapport: geen privé-inhoud, geen chatcitaten—alleen de systematische erkenning dat menselijke ingang een aparte laag is naast protocolobservatie.

## 18. Final Judgment

**Groene** duiding voor dit documenttype: het blijft observatie, mapping en taal—geen contractuele of productclaim.

**Gele** duiding voor adoptie: technische betalingsbeweging kan verbeteren zonder dat organisaties automatisch meebewegen.

Samenvatting in twee zinnen:

**Makka makes the payment move.**  
**ACX detects where the movement can still get stuck.**

Einde mirror-rapport.
