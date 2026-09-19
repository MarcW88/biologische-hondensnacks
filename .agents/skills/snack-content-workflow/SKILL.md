---
name: snack-content-workflow
description: Crée ou corrige une page néerlandaise sous /soorten/ après snack-analysis-workflow. Orchestre les skills GitHub existants pour l’intention, le JTBD, les preuves, le brief, la rédaction, la QA et le publish review sans imposer de template de page.
metadata:
  adapted_for: biologische-hondensnacks.nl
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "routing /soorten/ + snack-family boundaries + repository integration"
---

# Snack Content Workflow

## Rôle

Seul workflow de production pour `/soorten/`.

Séquence : `snack-analysis-workflow / AUDIT` → correction autorisée → `snack-analysis-workflow / PUBLISH_REVIEW`.

- `KEEP` : ne pas réécrire.
- `LIGHT_UPDATE` : respecter le scope de l’audit.
- `DEEP_REWRITE` : reconstruire en préservant les éléments valides.
- `MERGE` ou `NOINDEX` : attendre une décision humaine sur l’URL.

## Production fondée sur les skills existants

1. Confirmer intention, requêtes, rôle et chevauchements avec `seo-keyword`, `search-intent`, `seo-content-audit` et, pour l’existant, `content-refresh`.
2. Utiliser `jobs-to-be-done` pour relier le type de snack aux circonstances, au progrès recherché, aux frictions, aux alternatives et aux contre-indications. Sans données comportementales, conserver les motivations en hypothèses.
3. Construire avant la prose un registre de preuves avec `fact-check`. Appeler `evidence-based-reviews` seulement pour un jugement expérientiel réel.
4. Utiliser `affiliate-value` si la page influence l’achat ; elle doit rester utile sans produit ni lien affilié.
5. Persister `.content/snacks/briefs/<slug>.md` avec `content-brief-authoring` : rôle, frontières, intention, job, critères, preuves, inconnues, claims interdits, maillage, angle et plan justifié.
6. Rédiger avec `content-and-copy` en néerlandais naturel. La structure vient du brief, jamais d’un modèle Snacks fixe.
7. Après rédaction : `fact-check`, `internal-linking-audit`, `humanizer`, `general-writing`, `anti-ai-slop`, `seo-onpage`, `seo-technical`, `editorial-qa`, puis lecture complète du rendu.

Toute reformulation qui crée ou renforce un fait rouvre le fact-check correspondant.

## Intégration au dépôt

Les pages HTML sous `/soorten/` sont des fichiers éditoriaux préservés par `scripts/build-preserving-guides.mjs`. Modifier la page réelle, mettre à jour les artefacts `.content/snacks/`, puis vérifier que le build ne remplace pas le contenu.

Conserver `noindex,follow`. Ne pas inventer produits, disponibilités, prix, tests, mesures, avis, bénéfices santé ou expériences.

## Handoff

Mettre à jour `.content/snacks/reviews/<slug>.md` avec les contrôles réellement effectués, les preuves, les inconnues, les changements, les résultats machine et les éventuels blockers. Passer ensuite à `snack-analysis-workflow / PUBLISH_REVIEW`.

Le résultat final est uniquement :

- `PASS — READY_FOR_HUMAN_VALIDATION` ;
- `FAIL — KEEP_NOINDEX`.
