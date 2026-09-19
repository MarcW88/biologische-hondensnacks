# Provenance du workflow Snacks

Date de contrôle : 2026-09-19

## Workflow source

Les workflows Snacks sont repris directement depuis les workflows Comparison existants de `MarcW88/cafetiere-italienne`, branche `main` :

- `.agents/skills/comparison-analysis-workflow/SKILL.md`
- `.agents/skills/comparison-content-workflow/SKILL.md`
- `comparison-workflow.config.yaml`

## Adaptations effectuées

Les adaptations sont limitées au site cible :

- domaine : `biologische-hondensnacks.nl` ;
- langue : néerlandais ;
- routes : `/soorten/` ;
- noms des workflows : `snack-analysis-workflow` et `snack-content-workflow` ;
- répertoires de persistance : `.content/snacks/` ;
- catégories voisines du site : merken, ingrediënten, eiwit, levensfase, gevoelige honden et gidsen ;
- faits produit à vérifier : composition, ingrédients, statut biologique, source de protéine, format, calories, prix et disponibilité ;
- source de vérité : HTML éditorial sous `soorten/*/index.html` ;
- commandes et validateur du dépôt Snacks.

La méthode d'analyse, de sélection des candidats, de définition des critères, de preuve, de recommandation, de rédaction et de review n'est pas redéfinie localement.
