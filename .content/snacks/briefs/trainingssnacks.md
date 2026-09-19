# Content brief — Trainingssnacks

## Cadrage

- URL : `/soorten/trainingssnacks/`
- Langue / marché : néerlandais, Pays-Bas
- Statut : test du workflow Snacks
- Décision d’audit : `DEEP_REWRITE`
- Robots : conserver `noindex,follow`
- Intention dominante : choisir des petites récompenses utilisables pendant l’entraînement **et disposer de produits concrets à comparer**. La page ne vise pas un podium universel, mais elle a une composante transactionnelle réelle.
- Job : pouvoir récompenser plusieurs fois sans casser le rythme de la séance ni perdre de vue la ration et les contraintes alimentaires du chien.

## Frontières

- La page explique les critères propres à l’usage “training”.
- `/soorten/beloningssnacks/` devra couvrir la récompense occasionnelle plus large, pas répéter cette logique de répétitions rapides.
- `/gidsen/hoeveel-snacks-mag-een-hond-per-dag/` possède l’explication détaillée de la ration.
- `/gidsen/ingredienten-hondensnacks-lezen/` possède l’apprentissage complet de lecture d’étiquette.
- Les pages `/eiwit/`, `/ingredienten/` et `/voor-gevoelige-honden/` portent les filtres correspondants.
- La sélection produit est déléguée aux workflows `comparison-analysis-workflow` / `comparison-content-workflow` copiés à l’identique depuis `MarcW88/cafetiere-italienne`. Aucun prix fixe ni claim hands-on.

## Valeur propre

Séparer quatre décisions souvent confondues : efficacité comme récompense, praticité pendant les répétitions, place dans la ration et statut biologique. Montrer explicitement que “biologique” ne prouve ni la faible densité calorique ni l’adéquation clinique.

## Registre de preuves

| Claim                                                                                                                                         | Source                                           | Niveau / portée                                                                           | Statut             |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------- | ------------------ |
| Les méthodes fondées sur la récompense sont recommandées pour l’entraînement canin                                                            | AVSAB, Humane Dog Training Position Statement    | Association vétérinaire de comportement ; principe général d’entraînement                 | vérifié 2026-09-19 |
| Les extras ne devraient pas dépasser 10 % de l’alimentation quotidienne                                                                       | ASPCA, General Dog Care                          | Règle générale, pas calcul individualisé ni prescription vétérinaire                      | vérifié 2026-09-19 |
| Étiquetage et claims couvrent aussi l’information en ligne ; claims nutritionnels/santé doivent être objectivement et scientifiquement étayés | NVWA, inspectieresultaten etikettering en claims | Autorité néerlandaise ; portée diervoeder/petfood                                         | vérifié 2026-09-19 |
| Le logo bio européen permet d’identifier des produits biologiques certifiés                                                                   | Commission européenne, The organic logo          | Portée générale de l’identification biologique ; ne prouve pas la performance comme snack | vérifié 2026-09-19 |

## Claims à ne pas faire

- “biologisch is gezonder” ;
- une composition ou une valeur calorique produit non vérifiée ;
- une promesse sur les allergies, la digestion, le poids ou une pathologie ;
- “beste trainingssnack” sans comparaison documentée ;
- un témoignage, un test ou une préférence canine inventés.

## Module produit — handoff Comparatif

Critères transmis au workflow Comparatif :

- petit format / ingestion rapide ;
- composition vérifiable ;
- statut biologique explicite ;
- utilité réelle pour des répétitions ;
- différence substantielle entre candidats ;
- aucune préférence liée à une commission.

Candidats vérifiés au 2026-09-19 :

1. **Yarrah Biologische Mini Snack 100 g** — 97% de viande bio, sans céréales, explicitement présenté par le fabricant comme snack d’entraînement ; valeur énergétique publiée.
2. **STRAYZ BIO Trainingssnack Kip 80 g** — 100% poulet bio, mono-protéine, petits morceaux ; disponibilité et composition vérifiées auprès d’un retailer NL.
3. **STRAYZ Veggie Trainingssnack 80 g** — option bio vegan, patate douce comme ingrédient principal ; disponibilité et composition vérifiées auprès d’un retailer NL.

Pas de classement global : la recommandation est conditionnelle au besoin.

## Architecture justifiée

1. Réponse directe et trois critères immédiatement actionnables.
2. Expliquer pourquoi la répétition change la décision.
3. Donner une vérification d’achat en quatre contrôles.
4. Distinguer certification biologique et aptitude à l’entraînement.
5. **Appliquer les critères à une sélection de produits actuels et achetables.**
6. Présenter la ration de croquettes comme alternative simple lorsque le contexte le permet.
7. Rendre les sources visibles près du contenu, sans transformer la page en guide réglementaire.

## Maillage

- Hub `/soorten/` dans le fil d’Ariane.
- Les liens vers les guides de ration et d’étiquette pourront être ajoutés lorsque ces pages auront reçu leur validation finale ; ne pas créer de dépendance éditoriale trompeuse dans ce test.

## Critères de succès

- Le lecteur peut juger une snack **et comparer immédiatement des produits concrets**.
- Les limites du biologique sont explicites.
- Les claims sensibles sont attribués et correctement qualifiés.
- La page reste utile sans affiliation.
- Aucun contenu n’est remplacé au build et la page reste `noindex,follow`.
