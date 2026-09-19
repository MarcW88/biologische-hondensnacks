---
name: snack-analysis-workflow
description: Analyse une page ou le cluster néerlandais /soorten/ de biologische-hondensnacks.nl avant rédaction, puis réalise le publish review. À utiliser pour auditer les familles de snacks, pas les guides, ingrédients, protéines, étapes de vie ou produits à mâcher précis.
metadata:
  adapted_for: biologische-hondensnacks.nl
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "routing /soorten/ + snack-family boundaries + evidence risk + cluster review"
---

# Snack Analysis Workflow

## Rôle et modes

Seul workflow d’analyse pour `/soorten/`. Il orchestre les skills existants et ne rédige pas la page.

- `AUDIT` : retourne `KEEP`, `LIGHT_UPDATE`, `DEEP_REWRITE`, `MERGE` ou `NOINDEX`.
- `CLUSTER_AUDIT` : contrôle l’ensemble du hub et de ses pages filles.
- `PUBLISH_REVIEW` : retourne exactement `PASS — READY_FOR_HUMAN_VALIDATION` ou `FAIL — KEEP_NOINDEX`.

Un verdict ne déclenche jamais seul une fusion, suppression, redirection ou indexation.

## Entrées

Lire la page cible, `/soorten/`, les pages sœurs, les pages voisines susceptibles de couvrir la même question, l’audit et le brief persistés, les données de recherche réellement disponibles et les sources actuelles nécessaires aux claims.

## Chaîne réutilisée

Exécuter distinctement les skills locaux pertinents :

1. `seo-content-audit` pour diagnostiquer conservation, mise à jour ou consolidation ;
2. `seo-keyword` et `search-intent` pour la famille de requêtes et le résultat attendu ;
3. `jobs-to-be-done` pour relier la famille de snacks à une situation et un progrès concret ;
4. `content-refresh` pour une page existante à corriger ;
5. `fact-check`, et `evidence-based-reviews` uniquement si un jugement expérientiel le nécessite ;
6. `affiliate-value` lorsque la page influence l’achat ;
7. `internal-linking-audit`, `anti-ai-slop`, `seo-onpage`, `seo-technical` et `editorial-qa` pour les contrôles correspondants.

Ne pas condenser ces méthodes dans ce fichier et ne pas déclarer un skill PASS sur la seule base d’un script.

## Couche custom : fonction de la page

Une page `/soorten/` aide à comprendre quand une famille de snacks convient, quels critères changent la décision, quelles limites comptent et vers quelle sous-question poursuivre.

Frontières :

- `/gidsen/` explique une notion, une règle ou une procédure ;
- `/kauwsnacks/` traite un objet à mâcher précis ;
- `/ingredienten/` et `/eiwit/` filtrent par composition ;
- `/levensfase/` et `/voor-gevoelige-honden/` partent du chien ;
- une future page comparative sélectionne réellement des produits.

Un type de page n’impose jamais son plan. Le hub `/soorten/` oriente ; une page fille doit apporter une décision distincte et ne pas être une simple porte vers des produits.

## Couche custom : preuve et sécurité

Adapter la preuve au claim. Vérifier en priorité : ration énergétique, fréquence, taille et texture, risques d’étouffement ou d’ingestion, allégations dentaires, allergies/intolérances, âge, pathologies, composition, additifs, statut biologique et claims marketing.

Préférer selon le sujet : réglementation et autorités néerlandaises/européennes, organisations vétérinaires ou scientifiques, documentation fabricant pour un fait produit. Un retailer ou une marque ne suffit pas pour une conclusion générale de santé.

Ne jamais déduire `biologisch = gezonder`, `natuurlijk = beter`, `graanvrij = hypoallergeen` ou une efficacité dentaire sans preuve adaptée.

## Contrôle du cluster

Comparer la cible aux pages les plus proches : tâche lecteur, rôle, critères, ordre du raisonnement, tableaux, CTA, conclusions et formulations. Les composants visuels peuvent se répéter ; l’architecture éditoriale ne doit pas être clonée.

Documenter pour chaque audit : rôle, intention, job, valeur existante à préserver, frontières, preuves, inconnues, risques, cannibalisation, portée de correction et prochaine étape.

## Publish review

Relire la version rendue et le dossier de preuve, puis exécuter :

```bash
npm run build
npm run check
node scripts/check_snacks.mjs
```

Réexécuter les gates substantiels d’intention, JTBD, factualité, valeur sans affiliation, naturalité, anti-AI, SEO, technique et différenciation du cluster. Conserver `noindex,follow` même en cas de PASS.
