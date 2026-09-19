# Content brief — Gedroogde hondensnacks

## Cadrage

- URL : `/soorten/gedroogde-hondensnacks/`
- Langue / marché : néerlandais, Pays-Bas
- Décision d’audit : `DEEP_REWRITE`
- Robots : conserver `noindex,follow`
- Intention dominante : choisir et comparer des snacks séchés concrets.
- Job : comprendre quel type de morceau séché correspond à l’usage recherché, puis choisir un produit réel sans confondre séché, naturel, biologique et mono-ingrédient.

## Scope de comparaison

### Candidats principaux

1. Bandit Bio kipfilet gedroogd 100 g
2. Bandit Bio lamslong trainers 100 g
3. Bandit Bio lamspens staafjes 100 g
4. Bandit Bio lamspezen 100 g

### Candidats de contrôle / marché

- Organimal Lamslong Trainers — utile pour comparer un produit 100% gedroogde lamslong non présenté comme biologique.
- Wolf of Wilderness gevriesdroogde snacks — utile pour distinguer gedroogd et gevriesdroogd.
- Yarrah assortiment bio — utile comme contrôle de catégorie, mais ne pas inclure automatiquement un produit si son mode de transformation ne correspond pas clairement au scope.

## Critères

1. usage : training, beloning, tussendoor, kauwen ;
2. type de morceau ;
3. texture / dureté ;
4. taille / portionnabilité ;
5. composition et nombre d’ingrédients ;
6. protéine ;
7. statut biologique vérifiable ;
8. information nutritionnelle utile si disponible ;
9. disponibilité NL/BE.

## Preuves principales

- Bandit présente ses snacks comme `puur, gedroogd vlees`, sans additifs, colorants ni arômes ajoutés.
- Floris Vlees liste actuellement :
  - Bio kipfilet gedroogd 100 g ;
  - Bio lamslong trainers 100 g ;
  - Bio lamspens staafjes 100 g ;
  - Bio lamspezen 100 g.
- Organimal Lamslong Trainers : 100% gedroogde lamslong ; analyse publiée : eiwit 81%, vet 2,7%, as 3,8%, vocht 9,8%, vezel 1,6%.
- Wolf of Wilderness : références gevriesdroogd à base de 100% ingewanden ou vis.
- Yarrah utilise le terme `gedroogde hondensnacks` au niveau catégorie, mais tous ses snacks ne sont pas équivalents à de simples morceaux de viande séchée.

## Logique de recommandation

- Bandit Bio lamslong trainers : meilleur profil pour training parmi les candidats bio grâce au format trainer.
- Bandit Bio lamspezen : meilleur profil pour une mastication plus longue parmi les candidats du scope.
- Bandit Bio kipfilet : meilleur profil si l’on veut un morceau de viande simple et identifiable.
- Bandit Bio lamspens staafjes : option intermédiaire entre petite récompense et mastication légère.
- Pas de classement global.

## Architecture

La page doit être structurée autour des différences entre **morceaux et usages**, pas comme un clone de Trainingssnacks.

Architecture cible :
1. réponse directe ;
2. différence entre type de morceau et usage ;
3. repères de décision ;
4. sélection produit ;
5. différence gedroogd / gevriesdroogd / natuurlijk / biologisch ;
6. limites et sécurité ;
7. sources.

## Anti-patterns

- ne pas écrire `gedroogd = biologisch` ;
- ne pas écrire `100% vlees = hypoallergeen` ;
- ne pas reprendre `gezond`, `licht verteerbaar`, `goed voor het gebit` comme faits ;
- ne pas affirmer que le séchage conserve les nutriments sans source adaptée ;
- ne pas inventer une sensation de texture ou d’odeur non documentée ;
- ne pas faire de top global entre poumon, tendon, filet et panse.
