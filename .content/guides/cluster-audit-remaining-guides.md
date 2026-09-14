# Cluster audit — remaining `/gidsen/` batch

Date: 2026-09-14
Mode: `CLUSTER_AUDIT`

## Decision
Alle negen resterende URLs hebben een verdedigbare eigen reader job, maar vijf hebben sterke overlaprisico's met categoriepagina's. Daarom blijft de scheiding strikt:

- `/gidsen/hondensnacks-zonder-toevoegingen/` = claim begrijpen/verifiëren; `/ingredienten/hondensnacks-zonder-toevoegingen/` = producten verkennen.
- `/gidsen/wat-is-mono-eiwit/` = term, beperkingen en allergiecontext; `/voor-gevoelige-honden/mono-eiwit-hondensnacks/` = categorie.
- `/gidsen/welke-hondensnacks-zijn-gezond/` = besliskader; `/ingredienten/gezonde-hondensnacks/` = categorie.
- `/gidsen/welke-snacks-voor-een-puppy/` = veiligheids-/keuzekader voor groei; `/levensfase/hondensnacks-puppy/` en `/soorten/puppy-snacks/` = categorieën.
- `/gidsen/welke-kauwsnack-voor-mijn-hond/` = maat, hardheid, toezicht, gebruiksdoel; `/soorten/kauwsnacks/` en `/kauwsnacks/*` = producttypen.

De drie biologische guides hebben aparte taken:
- `wat-zijn-biologische-hondensnacks` = brede definitie en consequenties;
- `biologische-of-natuurlijke-hondensnacks` = begripsvergelijking;
- `biologisch-keurmerk-hondensnacks` = verificatiemethode.

`ingredienten-hondensnacks-lezen` blijft de generieke label-reading hub. `hoeveel-snacks-mag-een-hond-per-dag` bezit het calorie-/hoeveelheidsprobleem.

## Structural similarity gate
De batch gebruikt geen vast H2-, tabel- of FAQ-template. Elke pagina krijgt een structuur gebaseerd op het reader job: wettelijke verificatie, rekenschema, labeltutorial, claimuitleg, veterinaire begripsafbakening, keuze-gates of safety decision tree.

## Indexation
Alle pagina's blijven `noindex,follow` tot menselijke validatie. Geen merge/redirect/indexatie uitgevoerd.