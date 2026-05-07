# Case 06 — Plug-and-Play Validation Patterns

## Purpose

Case 06 zet een zichtbaar genoeg signaal uit Case 05 om in een kleine, veilige en herhaalbare validatieroute.

Het doel is niet om een oorzaak te bewijzen.  
Het doel is niet om een oplossing te verkopen.  
Het doel is niet om een audit te starten.

Het doel is om te bepalen welke signalen uit Case 05 met bestaande exports, lichte observatie of lokale bevestiging veilig getoetst kunnen worden.

## Relation to Case 05

Case 05 is de vraaglaag.

Case 06 is de validatielaag.

Case 05 vraagt:

- wat wordt zichtbaar?
- wat blijft ruis?
- wat moet gevolgd worden?
- wat is zichtbaar genoeg om samen te bekijken?

Case 06 vraagt:

- welk klein validatiepatroon past hierbij?
- welke minimale data is nodig?
- wat kan veilig gezegd worden?
- wat mag nog niet gezegd worden?
- welke routblijft open, en welke route moet parkeren?

## What this case is not

Case 06 is niet:

- een audit;
- een diagnose;
- een implementatieplan;
- een dashboardproject;
- een verkoopdocument;
- een performance-analyse van medewerkers;
- een claim over een specifieke operatie;
- een vervanging van AS400, SAP, WMS, ERP of planningssystemen.

Case 06 raakt live systemen niet aan.

Case 06 schrijft niets terug.

Case 06 werkt alleen met read-only signalen, bestaande exports, mockdata of lichte observatie.

## Entry Criteria

Een signaal mag Case 06 alleen binnenkomen wanneer het uit Case 05 minimaal één van deze statussen heeft:

| Case 05 status | Case 06 action |
|---|---|
| Noise / Single Event | Niet openen. Parkeren. |
| Soft Signal | Meestal niet openen. Alleen volgen. |
| Repeated Signal | Alleen openen voor lichte validatie als er genoeg context is. |
| Validation-ready Pattern | Openen als validatiepatroon. |
| Candidate for Case 06 | Openen als kleine, afgebakende validatieroute. |

Case 06 opent niet j:

- losse ruis;
- alleen vermoeden;
- geen bron;
- geen context;
- geen herhaling;
- te brede vragen;
- signalen die direct naar een oplossing springen.

## Enterprise Safety Principles

Case 06 moet veilig blijven voor IT, Operations en Directie.

### IT safety

- read-only;
- bestaande exports;
- geen backend;
- geen API-koppeling;
- geen live systeemimpact;
- geen schrijfrechten;
- geen performancebelasting op bronsystemen;
- brondata blijft intact.

Veilige zin:

“Deze validatie gebruikt alleen een statische export of lokale testdata en heeft geen interactie met live systemen.”

### Operations safety

- geen medewerkerbeoordeling;
- geen individuele prestatiemeting;
- geen stopwatchcultuur;
- geen oordeel over teams, shifts of locaties;
- focus op patronen in procesdata, niet op personen.

Veilige zin:

“Deze validatie kijkt naar terugkerende signalen in het proces, niet naar individuele prestaties.”

### Directie safety

- kleine scope;
- omkeerbare test;
- bestaande data;
- geen ROI-belofte;diagnose;
- geen zware implementatie;
- duidelijke stopknop.

Veilige zin:

“Dit is een kleine read-only validatieroute op bestaande data om te zien welke patronen voldoende zichtbaar zijn voor gezamenlijke beoordeling.”

## Validation Pattern Map

Case 06 gebruikt de volgende plug-and-play validatiepatronen:

1. Repeated Manco / Short-Pick Cluster Check
2. Location Hotspot Check
3. SKU Hotspot Check
4. Shift Comparison Check
5. Picktime Anomaly Check
6. Correction Loop Check
7. Data Completeness Check
8. Human Confirmation Check
9. Shadow Run Template
10. Local CSV Analyzer Route
11. No-Upload / No-Backend Data Review

---

## Pattern 1 — Repeated Manco / Short-Pick Cluster Check

### Case 05 question

Waar ontstaat het verschil tussen wat het systeem denkt dat er is en wat de vloer werkelijk aantreft?

### What it validates

Of dezelfde soort manco, short-pick of afwijking terugkeert in dezelfde lokale context.

### Required minimal data

- event type;
- locatie;
- timestamp;
- eventueel SKU of artie.

### Optional extra data

- zone;
- shift of tijdblok;
- ordertype;
- volume per locatie;
- correctienotitie.

### Method

Groepeer events per locatie, SKU of zone en tel herhaling binnen een beperkte observatieperiode.

Voorbeelden van observatievensters:

- 48 uur bij snelle flow;
- 7 dagen bij lagere frequentie;
- langer venster alleen als het volume laag is.

### Safe output

“Deze locatie/SKU toont herhaalde signalen binnen de gekozen observatieperiode.”

### What it may not claim

Niet zeggen:

- “Deze locatie is het probleem.”
- “Dit bewijst voorraadfalen.”
- “Dit bewijst systeemfalen.”
- “Dit verklaart de oorzaak.”

### Risk if used wrong

Zonder volumecontext kan een drukke locatie zwaarder lijken dan zij werkelijk is.

### Data still needed

- locatie;
- timestamp;
- event type;
- volumecontext indien locaties worden vergeleken.

### Route after validation

- volgen;
- samen valideren;
- of bij voldoende bevestiging parkeren als kandidaat voor Case 07-overzicht.

---

## Pattspot Check

### Case 05 question

Welke locaties veroorzaken herhaaldelijk kleine vertragingen die afzonderlijk klein lijken maar samen zichtbaar kunnen worden als patroon?

### What it validates

Of afwijkingen zich concentreren rond bepaalde locaties, gangen, zones of opslagplekken.

### Required minimal data

- locatiecode;
- event type;
- timestamp.

### Optional extra data

- totaal aantal picks per locatie;
- zone;
- shift;
- SKU;
- correctietype.

### Method

Vergelijk afwijkingsdichtheid per locatie.

Bij voorkeur:

- afwijkingen delen door totaal aantal picks;
- locaties alleen vergelijken als volume vergelijkbaar is;
- drukke locaties niet automatisch zwaarder interpreteren.

### Safe output

“Locatie X toont een hogere concentratie van terugkerende signalen dan vergelijkbare locaties in deze export.”

### What it may not claim

Niet zeggen:

- “Locatie X is slecht beheerd.”
- “Locatie X veroorzaakt het probleem.”
- “Deze locatie moet worden geblokkeerd.”

### Risk if used wrong

tie kan volume worden verward met afwijking.

### Data still needed

- locatie;
- event type;
- volume per locatie of vergelijkbare context.

### Route after validation

- volgen;
- lokale bevestiging vragen;
- eventueel route naar Case 07 als veilig overzichtspunt.

---

## Pattern 3 — SKU Hotspot Check

### Case 05 question

Welke bestaande operationele data wordt nog niet gelezen als patroonveld?

### What it validates

Of bepaalde SKU’s of artikelgroepen opvallend vaak terugkeren in manco’s, short-picks, correcties of locatieverschillen.

### Required minimal data

- SKU of artikelcode;
- event type;
- timestamp.

### Optional extra data

- locatie;
- productcategorie;
- omloopsnelheid;
- opslagtype;
- leverancier;
- volume.

### Method

Groepeer signalen per SKU en controleer herhaling.

Let op:

- high-volume SKU’s kunnen vanzelf vaker voorkomen;
- zonder volumecontext geen harde ernstconclusie.

### Safe output

“SKU Y toont herhaalde signalen die geschikt zijn voor verdere lokale beoordeliWhat it may not claim

Niet zeggen:

- “Dit artikel veroorzaakt de fout.”
- “De leverancier is de oorzaak.”
- “Dit product is problematisch.”

### Risk if used wrong

SKU’s met hoog volume kunnen vals zwaarder lijken.

### Data still needed

- SKU;
- event type;
- timestamp;
- volume of omloopsnelheid indien beschikbaar.

### Route after validation

- volgen;
- vergelijken met volume;
- lokale validatie.

---

## Pattern 4 — Shift Comparison Check

### Case 05 question

Welke correcties of signalen worden zichtbaar in specifieke tijdblokken zonder direct een oorzaak te claimen?

### What it validates

Of afwijkingen zich concentreren in bepaalde shifts, dagdelen of tijdvensters.

### Required minimal data

- timestamp;
- event type;
- locatie of SKU.

### Optional extra data

- shiftindeling;
- volume per shift;
- zone;
- type werkzaamheden.

### Method

Vergelijk signalen per shift of tijdblok.

Belangrijk:

- niet gebruiken als teamranking;
- alleen vergelijken met volumecontext;
- verschi interpreteren als menselijk falen.

### Safe output

“Dit tijdblok toont meer signalen dan vergelijkbare tijdblokken en is geschikt voor lichte validatie.”

### What it may not claim

Niet zeggen:

- “Deze shift presteert slechter.”
- “Dit team maakt meer fouten.”
- “Deze ploeg veroorzaakt afwijkingen.”

### Risk if used wrong

Kan onveilig voelen als medewerker- of teamcontrole.

### Data still needed

- tijdblok;
- event type;
- volumecontext;
- eventueel lokale uitleg.

### Route after validation

- volgen;
- parkeren;
- of samen valideren met Operations.

---

## Pattern 5 — Picktime Anomaly Check

### Case 05 question

Waar wijkt de werkelijke uitvoering af van het systeembeeld zonder dat dit als formele fout zichtbaar wordt?

### What it validates

Of bepaalde taken, locaties of routes herhaaldelijk langer duren dan vergelijkbare taken.

### Required minimal data

- starttijd;
- eindtijd;
- locatie of processtap.

### Optional extra data

- SKU;
- ordergrootte;
- route;
- zone;
- vo
### Method

Zoek naar duurverschillen tussen vergelijkbare taken.

Alleen vergelijken wanneer taken voldoende vergelijkbaar zijn.

### Safe output

“Deze route/locatie toont een terugkerende tijdsafwijking die geschikt is voor lokale beoordeling.”

### What it may not claim

Niet zeggen:

- “Medewerkers zijn te langzaam.”
- “De route is inefficiënt.”
- “Hier gaat tijd verloren door fout gedrag.”

### Risk if used wrong

Dit patroon kan snel voelen als performance tracking.

### Data still needed

- timestamps;
- vergelijkbare taakcontext;
- geen persoonsanalyse.

### Route after validation

- alleen gebruiken met extra voorzichtigheid;
- lokale bevestiging vereist;
- anders parkeren.

---

## Pattern 6 — Correction Loop Check

### Case 05 question

Welke correcties worden door mensen gedaan die niet zichtbaar worden in de systeemdata?

### What it validates

Of hetzelfde type correctie, override, tweede scan, handmatige wijziging of uitzonderingshandeling terugkeert.

### Required minima-event;
- timestamp;
- locatie of processtap.

### Optional extra data

- reason code;
- tweede scan;
- exception code;
- korte observatienotitie;
- operatorfeedback zonder persoonsbeoordeling.

### Method

Groepeer correctie-events per locatie, processtap of type.

Zoek naar herhaling zonder direct oorzaak te claimen.

### Safe output

“Dit correctietype keert terug in dezelfde lokale context en is geschikt voor gezamenlijke validatie.”

### What it may not claim

Niet zeggen:

- “Medewerkers omzeilen regels.”
- “Het systeem wordt structureel overruled.”
- “De vloer corrigeert systeemfalen.”

### Risk if used wrong

Kan voelen als controle op medewerkers of als aanval op IT.

### Data still needed

- correctietype;
- tijdstip;
- locatie/processtap;
- lokale bevestiging.

### Route after validation

- menselijke bevestiging vragen;
- pas daarna route naar breder overzicht.

---

## Pattern 7 — Data Completeness Check

### Case 05 question

Welke bestaande operationele data is wel aanwezig,lig leesbaar als patroonveld?

### What it validates

Of een export compleet genoeg is voor claimveilige analyse.

### Required minimal data

Een export met minimaal:

- timestamp;
- event type;
- locatie of SKU.

### Optional extra data

- shift;
- zone;
- volume;
- reason code;
- correctienotitie.

### Method

Controleer:

- ontbrekende velden;
- lege waarden;
- dubbele regels;
- onmogelijke timestamps;
- ontbrekende locatiecodes;
- ontbrekende eventtypes;
- niet-vergelijkbare volumes.

### Safe output

“Deze export is wel/niet voldoende compleet voor een eerste lokale patroonreview.”

### What it may not claim

Niet zeggen:

- “De data is slecht.”
- “De systemen registreren verkeerd.”
- “Hierdoor klopt de operatie niet.”

### Risk if used wrong

Datakwaliteit kan onterecht worden gelezen als operationeel patroon.

### Data still needed

- veldnamen;
- structuur;
- voorbeeldregels;
- missing-value check.

### Route after validation

- gebruiken;
- opschonen als kopie;
- of parkeren tot betikbaar is.

---

## Pattern 8 — Human Confirmation Check

### Case 05 question

Wanneer is een patroon zichtbaar genoeg om samen te bekijken?

### What it validates

Of een zichtbaar datasignaal wordt herkend door lokale praktijkkennis.

### Required minimal data

- één zichtbaar patroon;
- één korte bevestigingsronde.

### Optional extra data

- micro-interview;
- teamleadreactie;
- operatorfeedback;
- observatienotitie.

### Method

Toon het patroon neutraal en vraag:

“Herkennen jullie dit als iets dat in de praktijk voorkomt?”

Antwoordopties:

- ja;
- nee;
- deels;
- onbekend;
- te weinig context.

### Safe output

“Het patroon is wel/niet/deels herkend door lokale praktijkkennis.”

### What it may not claim

Niet zeggen:

- “Eén bevestiging bewijst de waarheid.”
- “De vloer heeft bevestigd dat dit de oorzaak is.”
- “Deze persoon bevestigt het probleem.”

### Risk if used wrong

Kan voelen als interview-audit of schuldvraag.

### Data still needed

- zichtbaar patroon;
- veilersoonsbeoordeling.

### Route after validation

- verhogen naar validation-ready;
- parkeren;
- of splitsen in meerdere vragen.

---

## Pattern 9 — Shadow Run Template

### Case 05 question

Welke signalen kunnen lokaal worden bekeken zonder live systemen te raken?

### What it validates

Of een patroon uit een export ook zichtbaar blijft in een afgebakende observatieperiode.

### Required minimal data

- bestaande export;
- afgebakend tijdvak;
- duidelijke observatievraag.

### Optional extra data

- plan vs observed;
- route;
- zone;
- shift;
- observatienotitie.

### Method

Kies één vraag, één zone of één tijdvak.

Vergelijk:

- wat de data suggereert;
- wat lokaal wordt waargenomen;
- wat door praktijkkennis wordt herkend.

### Safe output

“Deze shadow run toont of het signaal in dit afgebakende tijdvak zichtbaar blijft.”

### What it may not claim

Niet zeggen:

- “De operatie werkt zo.”
- “Dit is representatief voor het hele DC.”
- “De oorzaak is vastgesteld.”

### Risk if hadow run kan te groot worden geïnterpreteerd.

### Data still needed

- afgebakende scope;
- observatieperiode;
- lokale bevestiging.

### Route after validation

- valideren;
- herhalen;
- parkeren;
- of meenemen als veilig overzichtspunt.

---

## Pattern 10 — Local CSV Analyzer Route

### Case 05 question

Welke bestaande operationele data kan lokaal worden gelezen als patroonveld?

### What it validates

Of een simpele CSV-export genoeg is om eerste herhalingssignalen zichtbaar te maken.

### Required minimal data

- CSV-export;
- minimaal timestamp + event type + locatie of SKU.

### Optional extra data

- zone;
- shift;
- volume;
- reason code.

### Method

Voer lokaal een read-only analyse uit:

- geen upload;
- geen backend;
- geen database;
- geen wijziging aan bronbestand;
- alleen afgeleide tellingen en patronen.

### Safe output

“De lokale CSV-review toont herhalingssignalen die geschikt zijn om te volgen of te valideren.”

### What it may not claim

Niet zeggen:

- “Deze tool ziet alDit vervangt bestaande analyse.”
- “Dit bewijst de oorzaak.”

### Risk if used wrong

Kan worden oversold als analytics-product.

### Data still needed

- CSV-structuur;
- kolomnamen;
- voorbeeldregels;
- datakwaliteit.

### Route after validation

- volgen;
- valideren;
- of parkeren.

---

## Pattern 11 — No-Upload / No-Backend Data Review

### Case 05 question

Hoe kan een eerste patroonreview veilig plaatsvinden zonder systeemrisico?

### What it validates

Of bestaande exports lokaal genoeg informatie bevatten voor een eerste patroonreview.

### Required minimal data

- een export;
- mockdata;
- of handmatige observatielijst.

### Optional extra data

- contextnotitie;
- datadictionary;
- kolombeschrijving.

### Method

Review lokaal:

- bron blijft intact;
- geen upload;
- geen netwerk;
- geen backend;
- geen opslag buiten lokale omgeving;
- output blijft tijdelijk en claimveilig.

### Safe output

“Deze review toont welke signalen lokaal zichtbaar zijn zonder systeemkoppeling.”

### What laim

Niet zeggen:

- “Er is volledig inzicht.”
- “Alle oorzaken zijn zichtbaar.”
- “Dit is een officiële audit.”

### Risk if used wrong

Kan lijken alsof governance wordt omzeild.

### Data still needed

- bronbestand;
- context;
- toestemming voor lokale read-only review.

### Route after validation

- veilig als eerste route;
- daarna eventueel naar gericht patroon.

---

## Waiting for Data

Sommige patronen mogen al online staan als validatieroute, maar blijven inhoudelijk wachten op echte data.

| Pattern | Needed data | Why needed | What can be said now | What cannot be said yet |
|---|---|---|---|---|
| Repeated manco / short-pick cluster | locatie, timestamp, event type | herhaling tellen | dit patroon kan herhaling toetsen | dat locatie X herhaling heeft |
| Location hotspot | locatie + volume | verdeling normaliseren | hotspot-check is mogelijk | dat een locatie een hotspot is |
| SKU hotspot | SKU + event type + volume | SKU-herhaling beoordelen | SKU-check is mogelijk | dat een SKs |
| Shift comparison | timestamp + tijdblok + volume | tijdvensters vergelijken | shiftvergelijking is mogelijk | dat een shift afwijkt |
| Picktime anomaly | start/eindtijd + taakcontext | vergelijkbare taken meten | picktijd-check is mogelijk | dat uitvoering afwijkt |
| Correction loop | correctie-events + context | herhaalde correcties zien | correctieloop-check is mogelijk | dat een loop bestaat |
| Data completeness | exportstructuur | analysegeschiktheid toetsen | completeness-check is mogelijk | dat data voldoende is |
| Human confirmation | zichtbaar patroon + reactie | praktijkkennis toevoegen | bevestigingscheck is mogelijk | dat patroon lokaal klopt |
| Shadow run | export + observatieperiode | signaal lokaal toetsen | shadow run is mogelijk | dat signaal standhoudt |
| CSV analyzer | CSV met kernvelden | lokaal tellen | lokale review is mogelijk | dat patroon aanwezig is |
| No-upload review | bronbestand + context | veilige eerste blik | veilige review is mogelijk | dat analyse volledig is |

## Learning Loop

Case 06 wordt sterker door elke nieuwe export, elk nieuw document, elke correctie en elke interpretatiefout.

De leerregel:

De bron blijft intact.  
De interpretatie blijft tijdelijk.  
De route blijft herzienbaar.

### Learning path

1. Source received  
   De bron komt binnen als export, document, notitie, mockdata of observatie.

2. Source preserved  
   De bron blijft onaangeraakt. Waar mogelijk krijgt de bron een versie, datum of hash.

3. Signal extracted  
   Alleen signalen, tellingen, pointers of metadata worden afgeleid.

4. Pattern compared  
   Het signaal wordt vergeleken met de Case 05-thresholds en Case 06-patterns.

5. Claim status updated  
   Het signaal blijft hypothese, wordt observatie, wordt validation-ready, of wordt geparkeerd.

6. Route updated  
   Het signaal gaat naar volgen, valideren, Case 07 of parkeren.

7. Error logged  
   Ontbrekende data, verkeerde interpretatie, foutieve kolommen of contextfouten worden expliciet gelabeld.

8. Next version created  
   Een nieuwe ronde krijgt een nieuwe versie of timestamp.

Nieuwe data kan een patroon:

- bevestigen;
- verzwakken;
- splitsen;
- samenvoegen;
- parkeren;
- of opnieuw openen.

Nieuwe data maakt nooit automatisch harde waarheid.

## Claim Safety

Use:

- “Dit patroon toetst of…”
- “Deze review kijkt of…”
- “Dit signaal keert terug binnen deze export…”
- “Dit is geschikt voor lichte validatie…”
- “Dit blijft een hypothese tot lokale bevestiging…”
- “De bron blijft intact; interpretatie is tijdelijk.”

Do not use:

- “Dit bewijst…”
- “Dit lost op…”
- “Sligro heeft…”
- “Het systeem faalt…”
- “De oorzaak is…”
- “Medewerkers corrigeren systeemfouten…”
- “Dit levert gegarandeerd besparing op…”

## Routing to Case 07

Een patroon mag alleen richting Case 07 wanneer het:

- lokaal zichtbaar is;
- claimveilig beschreven kan worden;
- herhaald of bevestigd is;
- niet afhankelijk is van verborgen aannames;
- niet als oorzaak wordt gepresente een overzicht maken.

Case 06 schrijft Case 07 nog niet.

## Parked Routes

De volgende routes blijven geparkeerd:

- forecasting vs actuele zichtbaarheid als diepe supply-chainlaag;
- bol.com / replenishment / refurbishing meta-case;
- ESG als apart hoofdstuk;
- dashboardlaag;
- living field visuals;
- scanner-UI;
- quarantaine-logica;
- automatische beslisregels;
- directiebrief;
- PowerPoint;
- ROI-berekening.

## Closing Rule

Validate only what is visible enough.

Keep everything else open.
