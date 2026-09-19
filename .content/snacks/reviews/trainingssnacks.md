# Review — Trainingssnacks

## Métadonnées

- URL : `/soorten/trainingssnacks/`
- Date : 2026-09-19
- Modes exécutés : `AUDIT`, production test, `PUBLISH_REVIEW`
- Décision initiale : `DEEP_REWRITE`
- Verdict précédent : `PASS — READY_FOR_HUMAN_VALIDATION`
- Verdict après réaudit produit : `REVISION_APPLIED — PUBLISH_REVIEW_TO_RERUN`
- Robots : `noindex,follow`
- Source éditoriale : `soorten/trainingssnacks/index.html`, préservée par le build

## Audit initial

La page était un placeholder générique : title court, meta description commune au site, trois blocs sans contenu, aucun claim, aucune preuve et aucune valeur propre. L’URL possède néanmoins un job distinct : choisir une récompense adaptée à des répétitions d’entraînement. La décision `DEEP_REWRITE` porte sur le contenu, pas sur l’existence de l’URL.

## Intention, JTBD et frontières

La page répond à “qu’est-ce qui rend une snack pratique et raisonnable pendant un entraînement ?” **et “quels produits actuels illustrent réellement ces critères ?”**. Le premier audit avait sous-estimé la composante transactionnelle de l’intention. La sélection produit est désormais traitée via les workflows Comparatif copiés depuis `cafetiere-italienne`.

Les motivations émotionnelles du propriétaire ou les préférences universelles du chien ne sont pas présentées comme des faits. Les conseils portent sur les contraintes observables : répétitions, interruption de l’exercice, taille, quantité et compatibilité alimentaire.

## Preuves et factualité

Les quatre claims externes qui structurent la page sont liés à AVSAB, ASPCA, NVWA et Commission européenne. La règle des 10 % est présentée comme une règle générale et non comme une prescription. La page n’affirme pas qu’un produit biologique est plus sain ou plus adapté. Aucun prix fixe, test, mesure propriétaire ni avis utilisateur n’est inventé.

Produits vérifiés le 2026-09-19 :
- Yarrah Biologische Mini Snack 100 g : source fabricant, 97% viande bio, sans céréales, 403,35 kcal/100 g ;
- STRAYZ BIO Trainingssnack Kip 80 g : retailer NL, 100% poulet bio, mono-protéine ;
- STRAYZ Veggie Trainingssnack 80 g : retailer NL, bio, vegan, sans sucre et céréales selon la fiche contrôlée.

La disponibilité et les prix restant volatils, ils ne sont pas figés dans la page.

## Rédaction et naturalité

La rédaction est en néerlandais natif, avec une réponse directe et des phrases de longueur variée. Les sections suivent le raisonnement propre à la page ; elles ne reproduisent pas les placeholders ni un plan produit symétrique. Les formulations promotionnelles, le faux “wij hebben getest” et les superlatifs ont été exclus.

## Valeur affiliée

La page contient désormais un module de sélection produit, mais le raisonnement, les critères, les limites et l’alternative des croquettes restent utilisables sans lien affilié. Aucun produit n’est favorisé en fonction d’une commission.

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

Le précédent PASS est invalidé par le nouveau gate produit. La correction éditoriale est appliquée ; le `PUBLISH_REVIEW` complet doit être rejoué sur le rendu final avant de rétablir `PASS — READY_FOR_HUMAN_VALIDATION`.

La page reste `noindex,follow`.
