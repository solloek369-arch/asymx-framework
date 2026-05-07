# Case 05 — Open Questions Layer

## Purpose

Case 05 verzamelt de operationele vragen die zichtbaar kunnen worden wanneer een foodservice / warehouse / DC-operatie wordt bekeken door de AsymX Level 1-lens.

Deze laag doet geen diagnose.  
Deze laag is geen audit.  
Deze laag is geen pitch.

Case 05 ankert wat al duidelijk zichtbaar is en nodigt uit tot gezamenlijke validatie waar het patroon nog niet duidelijk genoeg is.

## Scope

Case 05 kijkt alleen naar vragen die ontstaan rond het verschil tussen:

- fysieke werkelijkheid op de vloer (T0);
- systeembeeld / systeemregistratie (T1);
- de verschilruimte daartussen (Delta T).

AsymX Level 1 is hierbij een zichtbaarheidslaag.

Geen vervanging van bestaande systemen.  
Geen oordeel over systemen, locaties, teams of medewerkers.

## Non-Claims

- Dit is geen audit.
- Dit is geen diagnose.
- Dit igeen beoordeling van systemen, locaties of teams.
- Dit is geen verkoopdocument.
- Geen enkele vraag is een claim over een specifieke operatie.
- Geen enkele vraag bewijst een oorzaak.

## Core Question

Waar loopt de fysieke werkelijkheid op de vloer (T0) lokaal uit de pas met het systeembeeld (T1)?

## Question Map

1. Waar ontstaat het verschil tussen wat het systeem denkt dat er is en wat de vloer werkelijk aantreft?
2. Welke correcties worden door mensen gedaan die niet zichtbaar worden in de systeemdata?
3. Welke locaties veroorzaken herhaaldelijk kleine vertragingen die afzonderlijk klein lijken maar samen flowverlies geven?
4. Welke bestaande operationele data wordt nog niet gelezen als patroonveld van frictie?
5. Wanneer is een patroon zichtbaar genoeg om niet langer als los incident gedragen te hoeven worden?

---

## 1. System Image vs Physical Reality

### Question

Waar ontstaat het verschil tussen wat het systeem denkt dat er is en wat de vloer werkelijk aantreft?

### Why it matters

Dit is de basisvraag van AsymX Level 1.

Het gaat niet om de vraag wie gelijk heeft.  
Het gaat om het zichtbaar maken van plekken waar systeembeeld en fysieke werkelijkheid tijdelijk niet volledig samenvallen.

### What it may reveal

- manco;
- short pick;
- locatieverschil;
- voorraadverschil;
- vertraagde registratie;
- afwijking tussen scan, export en fysieke situatie.

### Possible light observation method

- bestaande picklogs bekijken;
- manco-registraties groeperen;
- locatie-afwijkingen tellen;
- kijken of dezelfde locatie, SKU of zone terugkomt.

### Possible data source

- WMS-export;
- AS400-export;
- SAP-export;
- picklogs;
- manco-registraties;
- locatiecorrecties;
- handmatige CSV-export.

### Claim-safe wording

“Dit type vraag onderzoekt waar systeembeeld en fysieke werkelijkheid mogelijk tijdelijk uit elkaar lopen.”

### Risk if phrased badly

Niet zeggen:

“Het systeem klopt niet.”

Dat maakt het een IT-verdedigingsvraag in plaats van een gezamenlijke observatievraag.

### Route

Parkeren of valideren volgens het Visibility Threshold Model.

---

## 2. Human Corrections Not Visible in System Data

### Question

Welke correcties worden door mensen gedaan die niet zichtbaar worden in de systeemdata?

### Why it matters

In complexe operaties lossen mensen vaak kleine afwijkingen op voordat ze als formele fout zichtbaar worden.

Case 05 beoordeelt dat niet.  
Case 05 vraagt alleen of zulke correcties ergens als patroon zichtbaar kunnen worden.

### What it may reveal

- extra zoeken;
- extra lopen;
- navragen;
- lokale kennis;
- mentale correcties;
- kleine procesadaptaties;
- correcties die de flow herstellen maar niet als data terugkomen.

### Possible light observation method

- korte micro-interviews;
- anonieme observatienotities;
- eenvoudige frictietelling;
- vergelijking tussen verwachte en werkelijke picktijd;
- één shift of één zone licht volgen zonder prestatiebeoordeling.

### Possible data source

- picktijd;
- routeverschillen;
- operatorfeedback;
- shiftobservatie;
- correcogs;
- korte teamlead-validatie.

### Claim-safe wording

“Deze vraag onderzoekt welke correcties mogelijk plaatsvinden zonder zichtbaar te worden in systeemdata.”

### Risk if phrased badly

Niet zeggen:

“Medewerkers repareren systeemfouten.”

Dat klinkt als schuld richting IT of als controle richting medewerkers.

### Route

Meestal eerst volgen of licht valideren.  
Alleen bij duidelijke herhaling en lokale bevestiging door naar Case 06.

---

## 3. Repeated Local Deviations

### Question

Welke locaties veroorzaken herhaaldelijk kleine vertragingen die afzonderlijk klein lijken maar samen flowverlies geven?

### Why it matters

Een losse afwijking kan ruis zijn.

Een terugkerende afwijking kan een signaal worden.

Case 05 behandelt herhaling niet als bewijs, maar als uitnodiging om samen te kijken.

### What it may reveal

- terugkerende manco’s;
- short-pick-clusters;
- locatie-hotspots;
- onduidelijke labeling;
- slecht vindbare voorraad;
- herhaling per locatie, SKU, zone of shift.

### Poht observation method

- afwijkingen groeperen per locatie;
- afwijkingen groeperen per SKU;
- afwijkingen vergelijken tussen shifts;
- tellen of dezelfde afwijking terugkomt in 48 uur of 7 dagen;
- volume meenemen bij drukke locaties.

### Possible data source

- picklogs;
- manco-logs;
- short-pick-logs;
- locatiecorrecties;
- CSV-export;
- eenvoudige shadow run.

### Claim-safe wording

“Dit signaal keert terug en is geschikt voor lichte validatie.”

### Risk if phrased badly

Niet zeggen:

“Deze locatie is het probleem.”

Een locatie met herhaling is geen bewezen oorzaak, maar een plek om samen te valideren.

### Route

Bij herhaling: licht valideren.  
Bij herhaling plus context plus bevestiging: kandidaat voor Case 06.

---

## 4. Existing Data as Friction Traces

### Question

Welke bestaande operationele data wordt nog niet gelezen als patroonveld van frictie?

### Why it matters

Level 1 hoeft geen nieuw systeem te zijn.

Veel eerste zichtbaarheid kan ontstaan door bestaande exports opnieuwn als sporen van frictie.

### What it may reveal

- terugkerende afwijkingen;
- correctielussen;
- vertragingen;
- locatieclusters;
- verborgen herhaling;
- verschil tussen administratie en fysieke flow.

### Possible light observation method

- read-only CSV-analyse;
- locatie/SKU/shift-groepering;
- repeated-signal check;
- eenvoudige tellingen;
- geen backend;
- geen integratie;
- geen wijziging in bronsystemen.

### Possible data source

- bestaande exports;
- picklogs;
- manco-registraties;
- correctielogs;
- AS400/SAP/WMS-export;
- handmatig gemaakte CSV.

### Claim-safe wording

“Dit type vraag onderzoekt of bestaande operationele data veilig kan worden gelezen als patroonveld van frictie.”

### Risk if phrased badly

Niet zeggen:

“De antwoorden zitten al in jullie data.”

Dat klinkt alsof bestaande rapportage of IT tekortschiet.

### Route

Sterke basis voor Case 06, maar pas nadat de vraaglaag mechanisch staat.

---

## 5. Visible Enough

### Question

Wanneer is een patroon zichtbaar geniet langer als los incident gedragen te hoeven worden?

### Why it matters

Case 05 moet niet te vroeg concluderen.

Maar wat zichtbaar genoeg terugkeert, hoeft ook niet eindeloos als los incident behandeld te worden.

### What it may reveal

- wanneer iets ruis blijft;
- wanneer iets gevolgd mag worden;
- wanneer iets licht gevalideerd mag worden;
- wanneer iets samen bekeken mag worden;
- wanneer iets pas naar Case 06 mag.

### Claim-safe wording

“Dit is zichtbaar genoeg om samen te bekijken.”

### Risk if phrased badly

Niet zeggen:

“Dit bewijst de oorzaak.”

Case 05 bewijst geen oorzaak.  
Case 05 bepaalt alleen of een signaal geparkeerd, gevolgd, gevalideerd of doorgestuurd mag worden.

### Route

Gebruik het Visibility Threshold Model.

---

## Visibility Threshold Model

Case 05 does not prove causes.

It only helps decide whether a signal should be parked, followed, validated, or routed to Case 06.

Core rule:

If a deviation returns clearly enough, it no longer has to be carried as a loosnt. It can be looked at together.

| Level | Name | Meaning | Safe action |
|---|---|---|---|
| 0 | Noise / Single Event | One loose deviation without repetition or context | Park |
| 1 | Soft Signal | One deviation with context, or a first small cluster | Follow |
| 2 | Repeated Signal | Similar deviation returns in the same location, SKU, shift or context | Validate lightly |
| 3 | Validation-ready Pattern | Repeated signal plus context and at least one extra confirmation | Validate together |
| 4 | Candidate for Case 06 | Local, repeated and confirmed pattern that is practical enough for a small next route | Route to Case 06 |

Example filters such as “three similar deviations in 48 hours” may help start the observation, but they are not proof.

48 hours may fit fast-moving flow.

7 days may fit slower-moving patterns.

When volumes differ, compare signals in context.

When data is incomplete, local human confirmation matters.

Case 05 may say:

“This is visible enough to look at together.”

Casenot say:

“This proves the cause.”

## Claim Status

All questions in Case 05 are:

- hypothesis;
- researchable signal;
- verification invitation;
- shared observation route.

No question is a proven diagnosis.

No question is a claim about a specific organization.

## Routing

Case 05 only decides whether a signal should be:

- parked;
- followed;
- lightly validated;
- validated together;
- routed to Case 06.

## What Moves to Case 06

Only after Case 05 is mechanically clear:

- validation gate;
- quarantine logic;
- scanner-flow;
- shadow-run details;
- concrete solution patterns;
- plug-and-play tool details;
- repeated manco / ghost-pick analyzer routes.

## What Stays Parked

The following routes stay parked for now:

- forecasting vs actual visibility;
- bol.com / replenishment / refurbishing meta-case;
- ESG as a separate chapter;
- directiebrief;
- dashboard;
- living field visuals;
- full SAP / AS400 transition story;
- symbolic engine.

## Safe Language

Use:

- “Dit type vraag onderzoekt”
- “In logistieke operaties kan dit patroon zichtbaar worden…”
- “Dit is onderzoekbaar via bestaande exports…”
- “Dit kan aanleiding geven tot gezamenlijke validatie…”
- “Dit is zichtbaar genoeg om samen te bekijken.”

Do not use:

- “Sligro heeft…”
- “Het systeem faalt…”
- “De vloer moet systeemfouten repareren…”
- “Dit bewijst…”
- “Dit levert gegarandeerd…”
- “Menselijke correctie wordt zichtbaar gemaakt als draaglast.”

## Closing Rule

Vraag eerst wat zichtbaar wordt voordat je zegt wat opgelost moet worden.
