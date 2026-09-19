# Review — Gedroogde hondensnacks

## Métadonnées
- URL : `/soorten/gedroogde-hondensnacks/`
- Date : 2026-09-19
- Mode : `AUDIT`
- Workflow : `snack-analysis-workflow`
- Robots : `noindex,follow`
- Décision : `DEEP_REWRITE`
- Confiance : `HIGH`

## 1. Intention observée
La SERP actuelle montre une vraie intention autonome autour de `gedroogde hondensnacks` : catégories e-commerce larges, dizaines de références, filtres par protéine, taille, âge et usage.

Le point important est que `gedroogd` n'est pas une intention d'usage unique. Les résultats mélangent :
- trainingshapjes ;
- beloningssnacks ;
- kauwstaafjes ;
- huid ;
- oren ;
- long ;
- pens ;
- vlees/vis ;
- parfois gevriesdroogd dans des catégories voisines.

Le job n'est donc pas simplement « choisir le meilleur produit séché », mais :
> comprendre ce que le terme gedroogd dit réellement du produit — et surtout ce qu'il ne dit pas — avant de choisir selon l'usage, la matière, la composition ou la protéine.

## 2. Pourquoi l'URL mérite de rester autonome
`gedroogde hondensnacks` existe comme vraie catégorie marchande dans la SERP, avec des pages dédiées et des assortiments importants.

La page ne doit donc pas être mergée avec :
- `/ingredienten/natuurlijke-hondensnacks/` : naturel est une qualification/composition, pas un procédé ;
- `/soorten/kauwsnacks/` : kauwen est un usage ;
- `/soorten/trainingssnacks/` : training est un usage ;
- `/voor-gevoelige-honden/mono-eiwit-hondensnacks/` : mono-eiwit est une contrainte de composition.

Verdict de rôle : URL autonome justifiée.

## 3. Problème de la version actuelle
La version actuelle est factuellement correcte sur plusieurs points, mais son architecture reste trop proche d'un comparatif générique :
- tableau introductif ;
- 4 cartes produit symétriques ;
- section de claims ;
- tableau final `Wanneer kies je welke?` ;
- sources.

Cette architecture a la même fonction éditoriale que l'ancienne version de Kauwsnacks et reste proche de Trainingssnacks : critères → sélection → limites → synthèse.

Le workflow `anti-ai-slop` / cluster similarity considère cette répétition comme un signal de structure industrialisée.

## 4. Le vrai angle spécifique au sujet
La page doit être structurée autour d'une question centrale :
> **Wat betekent ‘gedroogd’ eigenlijk als je een hondensnack kiest?**

`Gedroogd` décrit d'abord un procédé/état du produit. Il ne dit pas automatiquement :
- si la snack est biologique ;
- si elle est naturelle ;
- si elle est mono-eiwit ;
- si elle est adaptée au training ;
- si elle est adaptée au kauwen ;
- si elle est hypoallergénique ;
- si elle apporte un bénéfice dentaire.

C'est cette désambiguïsation qui doit organiser la page.

## 5. Ce que montre la SERP
Les catégories observées mélangent fortement produits et claims.

Exemples :
- NatuurlijkHondenvoer propose environ 42 références et mélange trainers, strips, kauwstaafjes, oren, huid et snacks par protéine ;
- Bellobox affiche environ 85 produits sous `gedroogde hondensnacks` ;
- d'autres acteurs qualifient automatiquement les snacks séchés de `natuurlijk`, `gezond`, `hypoallergeen` ou `goed voor het gebit`.

Conclusion : la valeur du site n'est pas d'imiter cette catégorisation, mais de séparer clairement les dimensions.

## 6. Architecture éditoriale recommandée
Pas de ranking à quatre produits.

### H2 — Gedroogd zegt alleen hoe het product is verwerkt
Rôle : poser le concept et montrer que le procédé ne suffit pas à décider.

### H2 — Eén categorie, drie totaal verschillende gebruiksmomenten
Rôle : montrer qu'un même univers de snacks séchés peut servir au training, à la récompense ou au kauwen.

Exemples :
- lamslong trainer ;
- kipfilet / vleesstrip ;
- pees / huid.

### H2 — Gedroogd is niet hetzelfde als natuurlijk, biologisch of mono-eiwit
Rôle : clarifier les quatre axes sans les fusionner.

### H2 — Waar de verpakking je gemakkelijk op het verkeerde been zet
Rôle : traiter les claims fréquents : gezond, hypoallergeen, goed voor het gebit, langzaam gedroogd.

### H2 — Wanneer gedroogd juist wél een nuttig selectiecriterium is
Rôle : expliquer les cas où le procédé/type est utile : simplicité de composition, portabilité, texture, mono-ingrédient vérifié, etc., sans inventer de bénéfice général.

### H2 — Twee of drie voorbeelden, geen kunstmatige top 4
Rôle : illustrer les différences, pas fabriquer un classement.

### H2 — Welke pagina helpt je verder?
Rôle : router vers Trainingssnacks, Kauwsnacks, Natuurlijke hondensnacks, Mono-eiwit selon la vraie question suivante.

### H2 — Bronnen

## 7. Scope produit recommandé
La page n'a pas besoin de quatre cartes symétriques.

Trois exemples suffisent pour matérialiser trois usages distincts :
- Bandit Bio lamslong trainers → training ;
- Bandit Bio kipfilet gedroogd → simple morceau de viande / beloning ;
- Bandit Bio lamspezen → kauwen.

`Lamspens staafjes` apporte moins de valeur éditoriale distincte et peut être supprimé si la page devient plus conceptuelle.

## 8. Cannibalisation à contrôler
### Avec Kauwsnacks
Ne pas expliquer la sécurité de mastication en profondeur ici. Router vers `/soorten/kauwsnacks/` et le guide dédié.

### Avec Trainingssnacks
Ne pas comparer plusieurs trainers ici. Utiliser un trainer uniquement comme exemple de format.

### Avec Natuurlijke hondensnacks
Cette page doit justement expliquer pourquoi `gedroogd ≠ natuurlijk` et router ensuite vers la page composition.

### Avec Mono-eiwit
Ne pas présenter une seule protéine comme garantie d'hypoallergénicité.

## 9. Valeur actuelle à préserver
- distinction gedroogd / gevriesdroogd / natuurlijk / biologisch ;
- vigilance sur les claims ;
- sources Bandit / Floris / Organimal / Zooplus ;
- produits Bandit déjà vérifiés ;
- canonical et SEO technique actuel.

## 10. Ce qu'il faut reconstruire
- supprimer la logique de quatre cartes produit symétriques ;
- supprimer le tableau final répétitif `Wanneer kies je welke?` ;
- faire du sens de `gedroogd` le fil conducteur ;
- utiliser les produits comme exemples, pas comme squelette ;
- renforcer le maillage vers les pages correspondant aux vraies sous-intentions.

## Verdict
`DEEP_REWRITE`

Confiance : `HIGH`

Raison principale : l'URL est légitime, mais l'architecture éditoriale actuelle reste industrialisée et ne tire pas encore parti de ce qui rend cette thématique vraiment spécifique.

Statut : `AUDIT_COMPLETE — DEEP_REWRITE`.
