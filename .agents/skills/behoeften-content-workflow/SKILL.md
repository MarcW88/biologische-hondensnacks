---
name: behoeften-content-workflow
description: Exécution de recherche, brief, rédaction néerlandaise, relecture et correction des pages Behoeften, basée sur les workflows Usage des dépôts de référence.
metadata:
  sources:
    - MarcW88/bloc-notes-numerique/.agents/skills/usage-content-workflow/SKILL.md
    - MarcW88/aspirateurs-chantier/.agents/skills/usage-content-workflow/SKILL.md
    - MarcW88/cafetiere-italienne/.agents/skills/usage-content-workflow/SKILL.md
---
# Behoeften Content Workflow

## Prérequis obligatoires
Lire `AGENTS.md`, `DESIGN.md`, `behoeften-workflow.config.yaml`, le skill `behoeften-analysis-workflow`, les skills spécialisés cités ci-dessous, ainsi que `01-audit.md` pour chaque page existante. **Ne pas écrire tant que l'audit n'a pas choisi DEEP_REWRITE ou LIGHT_UPDATE**. KEEP n'édite pas ; MERGE/NOINDEX requiert une décision humaine.

## Pipeline exécuté, pas seulement déclaré
1. `search-intent`, `seo-keyword`, `jobs-to-be-done` : questions de recherche, contraintes et différenciation vs `/gidsen/`, `/eiwit/`, `/soorten/`. Enregistrer résultats réellement observés et données manquantes.
2. `fact-check` et `evidence-based-reviews` conditionnel : consulter références primaires, autorités vétérinaires ou fabricants ; extraire les affirmations avec statuts dans `03-claims.json`. Pas de faux produit, témoignage ou examen médical.
3. `content-brief-authoring` : créer `02-brief.md` AVANT prose. Il comprend intention, lecteur et décision, JTBD, preuves, limites, différenciation interne, plan spécifiquement motivé, maillage et critères de réussite. Pas de longueur artificielle.
4. `content-and-copy` : écrire un article NL apportant des critères vérifiables, scénarios utiles, contre-indications et alternatives ; pas de remplissage, pas de classement affilié forcé. Persist `04-draft.md` (extraits / choix structurants), puis `.content/behoeften/<slug>.json` avec `article_html`.
5. Seconde passe distincte `fact-check` → `affiliate-value` si achat → `internal-linking-audit` → `natural-writing` et `general-writing` → `humanizer` → `anti-ai-slop` → `seo-onpage` / `seo-technical` → `editorial-qa`.
6. Exécuter `behoeften-analysis-workflow / PUBLISH_REVIEW`. Enregistrer `05-review.md`. Si FAIL, corriger le contenu, expliquer chaque correction dans `06-corrections.md`, puis reprendre la revue ; jamais déclarer PASS sur l'absence de vérifications.
7. Appliquer le JSON éditorial au HTML avec `node scripts/apply_behoeften_content.mjs`, puis `--check`, `node scripts/check_behoeften.mjs` et `npm run check`. Vérifier les différences, le rendu mobile/desktop quand l'environnement le permet, les liens et le noindex. Ne pas fusionner ni indexer sans demande explicite.

## Particularités vétérinaires
- Une friandise à source protéique unique n'est pas par définition hypoallergénique.
- Distinguer régime d'éviction vétérinaire, formulation commerciale à ingrédients limités et préférence d'achat.
- Ne pas déduire composition, certification, calorimétrie, absence de contamination croisée ou tolérance individuelle sans preuve.
- Les symptômes persistants ou la suspicion d'allergie relèvent du vétérinaire. Les sources et dates doivent rester visibles dans le dossier et, lorsque pertinent, sur la page.

## Interdictions méthodologiques
Aucun script statique de génération ne « joue » ces skills. La CI contrôle des fichiers et invariants ; l'agent doit réellement lire les instructions, rechercher, rédiger, faire une seconde revue et conserver la preuve des passages. Les preuves manquantes ne peuvent pas être inventées pour satisfaire le validateur.
