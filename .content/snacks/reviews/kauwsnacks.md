# Review — Kauwsnacks

## Métadonnées

- URL cible : `/soorten/kauwsnacks/`
- URL concurrente interne : `/kauwsnacks/`
- Date : 2026-09-19
- Mode : `AUDIT`
- Workflow : `snack-analysis-workflow`
- Robots : `noindex,follow`
- Décision cible : `DEEP_REWRITE`
- Décision cluster : `MERGE /kauwsnacks/ → /soorten/kauwsnacks/`
- Confiance : `HIGH`

## Intention / SERP

La SERP actuelle de `kauwsnacks hond` est dominée par des catégories marchandes et des assortiments structurés par **type de matière/morceau**, protéine, taille et usage : huid, pezen, oren, sticks, botten, vis, etc.

Exemples observés :
- Kauwsnacks.nl structure directement l’offre par `Botten / Pezen / Huid / Oren / Pens / Strips`.
- Zooplus expose une catégorie dédiée aux natuurlijke kauwsnacks.
- Natuurlijk voor de hond mélange runderhuid, paardenhuid, kabeljouwhuid, sprotjes et runderpees.
- Braaaf distingue notamment runderhuid, vissnacks et autres familles.

La SERP ne demande donc pas seulement « quel produit acheter ? ». Elle demande d’abord :
> **quel type de kauwsnack convient au comportement de mastication et au niveau de risque acceptable ?**

## Problème de la version actuelle

La version actuelle suit encore une architecture industrialisée proche des pages sœurs :

1. tableau de types ;
2. sélection de 4 produits ;
3. stopregels ;
4. distinction avec tandsnacks ;
5. tableau final de recommandation ;
6. sources.

Cette structure est très proche de `gedroogde-hondensnacks` :
- tableau introductif ;
- 4 cartes produit symétriques ;
- section de limites/claims ;
- tableau final « wanneer kies je welke » ;
- sources.

Le workflow `anti-ai-slop` / cluster similarity considère cela comme un signal de structure clonée, même si les faits sont corrects.

## Insight spécifique à Kauwsnacks

Le site possède déjà six sous-types dédiés :

- `/kauwsnacks/bullepees/`
- `/kauwsnacks/konijnenoren/`
- `/kauwsnacks/runderkophuid/`
- `/kauwsnacks/runderhuid/`
- `/kauwsnacks/kippenpoten/`
- `/kauwsnacks/kippennekken/`

Le vrai rôle de la page mère doit donc être de **faire comprendre la différence entre ces familles**, leurs compromis et leurs limites, puis d’orienter vers la bonne sous-page.

## Cannibalisation interne

`/kauwsnacks/` est aujourd’hui un hub de navigation qui cible exactement le même terme principal que `/soorten/kauwsnacks/`.

Deux URLs :
- même H1 ;
- même sujet ;
- même niveau de catégorie ;
- l’une fait hub, l’autre fait comparaison.

Cette séparation n’apporte pas assez de différence éditoriale.

### Recommandation
- conserver `/soorten/kauwsnacks/` comme URL principale ;
- intégrer la taxonomie et les liens enfants dans cette page ;
- merger/rediriger `/kauwsnacks/` vers `/soorten/kauwsnacks/` ;
- conserver les pages enfants sous `/kauwsnacks/<type>/`.

## JTBD

Le lecteur doit pouvoir répondre à trois questions avant de choisir une référence :

1. **Quel comportement cherche-t-il ?**
   - petite mastication ;
   - occupation plus longue ;
   - morceau facile à finir ;
   - peau/pees plus résistante.

2. **Qu’est-ce qui peut rendre un type inadapté ?**
   - produit trop dur ;
   - morceau trop petit ;
   - tendance à avaler des gros morceaux ;
   - dentition fragile ;
   - os / parties très dures.

3. **Quelle famille mérite ensuite une page détaillée ?**
   - pees ;
   - huid/kophuid ;
   - oren ;
   - nekken/poten, avec avertissement sécurité renforcé.

## Preuves de sécurité structurantes

FEDIAF recommande :
- un format/une forme adaptés au chien ;
- une supervision systématique ;
- d’éviter les chews excessivement durs ;
- de tenir compte du risque d’avaler de gros morceaux.

WSAVA recommande d’éviter :
- os crus ou cuits ;
- chews excessivement durs comme geweien et hoeven ;
- produits à bords coupants.

Ces éléments doivent structurer la page avant toute recommandation produit.

## Rôle des produits

La page n’a pas besoin de quatre cartes symétriques.

Deux exemples suffisent à matérialiser deux familles :
- **Yarrah biologische kauwstaafjes** : petite chew biologique, 33 g / 3 sticks, portionnable ;
- **Bandit Bio lamspezen** : exemple biologique d’une famille plus orientée mastication.

Les autres familles doivent être traitées d’abord comme **types de kauwsnacks**, avec liens vers les pages dédiées, pas comme quatre produits choisis artificiellement pour remplir un comparatif.

## Architecture éditoriale recommandée

Pas de template comparatif.

Structure spécifique au sujet :

1. **Le vrai choix : ce que le chien fait du snack**  
   knagen, stukken afbreken, snel inslikken.

2. **Carte des familles du site**  
   pees / huid / oor / kippennek-poot avec rôle et vigilance propres.

3. **Deux familles qui méritent une recommandation produit immédiate**  
   petit chew bio vs pees bio.

4. **Les catégories que nous ne voulons pas “recommander” sans réserve**  
   os/nek/poot et très dur, avec justification WSAVA/FEDIAF.

5. **Vers quelle sous-page aller maintenant ?**  
   navigation contextuelle vers les enfants.

6. Sources.

Pas de tableau final récapitulatif répétant le contenu.

## Verdict

### `/soorten/kauwsnacks/`
`DEEP_REWRITE`

### `/kauwsnacks/`
`MERGE` vers `/soorten/kauwsnacks/`

## Valeur à préserver

- les facts produit vérifiés de Yarrah et Bandit ;
- les sources WSAVA / FEDIAF / VOHC ;
- le lien avec le guide sécurité ;
- la distinction avec `tandsnacks`.

## À supprimer/reconstruire

- la logique de quatre cartes produits symétriques ;
- le tableau final `Welke past...` ;
- les recommandations artificiellement réparties en quatre « meilleurs profils » ;
- le hub doublon `/kauwsnacks/`.

Statut : `AUDIT_COMPLETE — DEEP_REWRITE + MERGE_DUPLICATE_HUB`.
