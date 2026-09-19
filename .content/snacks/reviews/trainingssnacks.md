# Review — Trainingssnacks

## Métadonnées

- URL : `/soorten/trainingssnacks/`
- Date : 2026-09-19
- Modes exécutés : `AUDIT`, production test, `PUBLISH_REVIEW`
- Décision initiale : `DEEP_REWRITE`
- Verdict final : `PASS — READY_FOR_HUMAN_VALIDATION`
- Robots : `noindex,follow`
- Source éditoriale : `soorten/trainingssnacks/index.html`, préservée par le build

## Audit initial

La page était un placeholder générique : title court, meta description commune au site, trois blocs sans contenu, aucun claim, aucune preuve et aucune valeur propre. L’URL possède néanmoins un job distinct : choisir une récompense adaptée à des répétitions d’entraînement. La décision `DEEP_REWRITE` porte sur le contenu, pas sur l’existence de l’URL.

## Intention, JTBD et frontières

La page répond à “qu’est-ce qui rend une snack pratique et raisonnable pendant un entraînement ?”. Elle ne sélectionne pas de produits. Elle distingue son rôle des pages Beloningssnacks, ration quotidienne, ingrédients, protéines, besoins sensibles et comparatifs futurs.

Les motivations émotionnelles du propriétaire ou les préférences universelles du chien ne sont pas présentées comme des faits. Les conseils portent sur les contraintes observables : répétitions, interruption de l’exercice, taille, quantité et compatibilité alimentaire.

## Preuves et factualité

Les quatre claims externes qui structurent la page sont liés à AVSAB, ASPCA, NVWA et Commission européenne. La règle des 10 % est présentée comme une règle générale et non comme une prescription. La page n’affirme pas qu’un produit biologique est plus sain ou plus adapté. Aucun produit, prix, test, mesure propriétaire ni avis utilisateur n’est inventé.

Inconnue assumée : aucune donnée de calories par produit n’est disponible. La page demande donc de vérifier la quantité et le conseil alimentaire au lieu de publier un seuil produit.

## Rédaction et naturalité

La rédaction est en néerlandais natif, avec une réponse directe et des phrases de longueur variée. Les sections suivent le raisonnement propre à la page ; elles ne reproduisent pas les placeholders ni un plan produit symétrique. Les formulations promotionnelles, le faux “wij hebben getest” et les superlatifs ont été exclus.

## Valeur affiliée

La page ne contient encore aucun produit ni lien affilié. Sa valeur repose sur la décision, les limites et le contrôle d’étiquette. Elle reste donc intégralement utile sans monétisation.

## SEO, GEO et maillage

- title, H1 et meta description spécifiques ;
- canonical explicite ;
- réponse synthétique dans le hero et le premier bloc ;
- entités et autorités nommées dans le texte ;
- fil d’Ariane vers le hub Snacks ;
- sources accessibles et datées ;
- pas de FAQ artificielle ni de schema non justifié.

Les données GSC, volumes et SERP néerlandaise détaillée n’étaient pas disponibles dans le dépôt ; aucun chiffre n’a été inventé.

## Technique et rendu

- contenu placé dans le HTML éditorial réel ;
- `scripts/build-preserving-guides.mjs` étendu à `/soorten/` afin que le générateur ne remplace plus ces pages ;
- feuille de style dédiée, fondée sur les tokens du design existant ;
- page maintenue en `noindex,follow` ;
- `npm run build`, `npm run check` et `npm run check:snacks` : PASS ;
- revue statique du responsive : la grille de décision passe de trois colonnes à une colonne sous 700 px et le layout `.template` existant passe déjà à une colonne sous 920 px ;
- limite : la validation visuelle Playwright n’a pas pu être menée à terme, car le téléchargement du Chromium verrouillé a expiré puis retourné une archive tronquée. Aucun PASS visuel complet n’est revendiqué.

## Verdict

`PASS — READY_FOR_HUMAN_VALIDATION`

Ce PASS ne vaut ni validation humaine ni instruction d’indexation.
