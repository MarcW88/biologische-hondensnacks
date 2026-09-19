# Review — Kauwsnacks

## 1. Métadonnées

- URL : `/soorten/kauwsnacks/`
- Date : 2026-09-19
- Mode : `AUDIT`
- Workflow : `snack-analysis-workflow`
- Robots : `noindex,follow`
- Source de vérité : `soorten/kauwsnacks/index.html`
- Décision : `DEEP_REWRITE`
- Confiance : `HIGH`

## 2. Intention et JTBD

La SERP est principalement transactionnelle/comparative. Le lecteur cherche une kauwsnack concrète, mais le choix dépend davantage de la sécurité et du comportement de mastication que du simple ingrédient.

Job dominant :

> choisir une kauwsnack suffisamment intéressante pour occuper le chien sans sélectionner un produit trop dur, trop petit ou mal adapté à son comportement de mastication.

Sous-jobs :
- choisir un format adapté ;
- distinguer snack de mastication et récompense ;
- éviter les produits extrêmement durs ;
- tenir compte du gebit ;
- tenir compte du risque d’avaler de gros morceaux ;
- choisir une protéine/composition compatible ;
- vérifier séparément toute claim dentaire.

## 3. État actuel

Placeholder complet :
- 0 produit ;
- 0 critère ;
- 0 source ;
- meta générique ;
- canonical absent ;
- aucune application du guide existant.

## 4. Frontière avec les pages voisines

### Guide `/gidsen/welke-kauwsnack-voor-mijn-hond/`
Le guide explique la méthode : taille, hardheid, kauwgedrag, gebit, toezicht, calorieën.

La page `/soorten/kauwsnacks/` doit appliquer cette méthode à des produits réels et éviter de la réécrire.

### `/soorten/gedroogde-hondensnacks/`
Gedroogde = angle procédé/type de morceau.
Kauwsnacks = angle usage de mastication/sécurité.

### `/soorten/tandsnacks/`
Tandsnacks = produits explicitement positionnés pour l’hygiène dentaire.
Kauwsnacks = mastication au sens large ; aucune efficacité dentaire ne doit être présumée.

## 5. Scope marché

Candidats / familles utiles :
- Yarrah Bio chewsticks pour chiens : produit bio explicitement positionné comme chewstick ;
- Bandit Bio lamspezen : produit bio séché orienté mastication ;
- Beeztees runderkophuid : exemple de rawhide/runderhuid avec formats longs ;
- Yakka/Yak cheese chew : exemple de produit très dur à traiter avec prudence ;
- Yarrah vegan dental sticks : utile comme frontière avec Tandsnacks, pas comme candidat central de cette page.

Le scope final doit privilégier des produits dont les dimensions, ingrédients et recommandations sont vérifiables.

## 6. Critères

1. formaat / lengte ;
2. hardheid / materiaal ;
3. kauwgedrag attendu ;
4. risque d’ingestion de gros morceaux ;
5. état du gebit ;
6. composition / protéine ;
7. calories si disponibles ;
8. statut biologique ;
9. éventuelle claim dentaire séparée de la simple mastication.

## 7. Preuves et risques

Le guide existant s’appuie déjà sur WSAVA, FEDIAF et VOHC.

Règles de preuve à conserver :
- ne pas écrire `harder = beter` ;
- ne pas recommander geweien/hoeven ou autres objets extrêmement durs ;
- ne pas transformer une claim retailer `goed voor het gebit` en fait établi ;
- ne pas écrire qu’une kauwsnack nettoie les dents sans preuve appropriée ;
- distinguer sécurité mécanique et qualité nutritionnelle.

La liste VOHC 2026 confirme que certains edible chew treats disposent d’une acceptation spécifique pour plaque/tartre, ce qui montre justement que ces claims demandent un niveau de preuve distinct.

## 8. Architecture recommandée

1. réponse directe : commencer par sécurité et usage ;
2. tableau rapide par type de kauwsnack ;
3. sélection produit conditionnelle ;
4. section “ce qu’on évite / ce qu’on surveille” ;
5. différence kauwsnack vs tandsnack ;
6. lien vers le guide complet ;
7. sources.

## 9. SEO / GEO

Blockers actuels :
- title générique ;
- meta générique ;
- canonical absent ;
- aucun passage répondant à `welke kauwsnack` ;
- aucune entité produit ;
- aucune source ;
- aucun signal clair de frontière avec Tandsnacks.

Questions GEO à couvrir :
- Welke kauwsnack voor een kleine/grote hond?
- Welke kauwsnack is niet te hard?
- Wat is het verschil tussen een kauwsnack en tandsnack?
- Welke biologische kauwsnacks bestaan er?
- Waar moet ik op letten bij runderhuid, pezen of harde kaassticks?

## 10. Verdict

`DEEP_REWRITE`

L’URL doit rester autonome et devenir une vraie page de sélection produit. Elle ne doit pas être mergée avec Gedroogde ni avec le guide.

Statut : `AUDIT_COMPLETE — DEEP_REWRITE`.
