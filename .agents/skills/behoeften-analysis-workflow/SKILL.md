---
name: behoeften-analysis-workflow
description: Audit indépendant, cluster audit et contrôle de publication des pages /voor-gevoelige-honden/, adapté du workflow Usage des trois dépôts de référence.
metadata:
  sources:
    - MarcW88/bloc-notes-numerique/.agents/skills/usage-analysis-workflow/SKILL.md
    - MarcW88/aspirateurs-chantier/.agents/skills/usage-analysis-workflow/SKILL.md
    - MarcW88/cafetiere-italienne/.agents/skills/usage-analysis-workflow/SKILL.md
---
# Behoeften Analysis Workflow

## Contrat
Ce SKILL est l'orchestrateur complet des **analyses**. Les méthodes spécialisées appartiennent aux skills préexistants de ce dépôt : ne les réinventer ni les simuler. Lire intégralement chaque skill applicable AVANT son étape. Les documents d'exécution sont persistés dans `.content/behoeften/runs/<slug>/`, pas seulement résumés à posteriori.

## Modes
- `AUDIT` : page existante et comparaison de son cluster ; retourner `KEEP | LIGHT_UPDATE | DEEP_REWRITE | MERGE | NOINDEX`, sans éditer HTML.
- `CLUSTER_AUDIT` : rôle autonome, trous, chevauchements, différences de structures et sources de chaque URL.
- `PUBLISH_REVIEW` : relecture indépendante APRES production et corrections ; retourner `PASS — READY_FOR_HUMAN_VALIDATION` ou `FAIL — KEEP_NOINDEX`. Un PASS n'est ni validation vétérinaire ni autorisation d'indexation.

## AUDIT : vraie chaîne de skills et preuves
1. Lire `AGENTS.md`, `DESIGN.md`, `behoeften-workflow.config.yaml`, HTML existant, guide connexe et pages voisines. Capturer les constats et exemples précis dans `01-audit.md`.
2. `content-audit` et `seo-content-audit` : relever structure actuelle, passages valables, problèmes et décision proportionnée. Performance GSC/analytics seulement si données fournies ; déclarer explicitement l'absence.
3. `search-intent` et `seo-keyword` : consulter SERP NL actuelle quand accès web disponible ; sinon indiquer « SERP NON VERIFIEE » et bloquer une prétention de validation SEO concurrentielle. Distinguer besoin de choix de snack, guide définitionnel `/gidsen/`, source de protéines `/eiwit/`, type `/soorten/`, ingrédients `/ingredienten/`.
4. `jobs-to-be-done` : observer situation, tâche, résultat et compromis ; qualifier hypothèses vs faits, ne pas inventer de verbatim.
5. `content-refresh` si mise à jour, `affiliate-value` si le choix d'achat est influencé : décrire la valeur sans liens commerciaux.
6. `fact-check` : pour chaque claim médical, nutritionnel, fabrication et ingrédient, produire `03-claims.json` avec source, statut CONFIRMED/PARTIAL/UNVERIFIED/CONTRADICTED et date. Vérifier les sources réellement accessibles ; une simple URL affichée ne prouve rien.
7. `evidence-based-reviews` uniquement en présence de véritables affirmations d'expérience. Sans preuve, bannir les tests personnels, taux, classements, tolérances et témoignages inventés.
8. `internal-linking-audit`, `anti-ai-slop`, `seo-onpage`, `seo-technical`, `editorial-qa` : identifier cannibalisation, répétitions, template artificiel, robots, canonical, liens et adéquation besoin.

## Revue finale indépendante
Relire le résultat HTML ET le brief sans adopter automatiquement les conclusions de l'agent rédacteur. Décrire les échecs substantiels dans `05-review.md` et lister les corrections observées dans `06-corrections.md`. Une page dont les affirmations sensibles sont non vérifiées, dont l'intention n'est pas justifiée, ou dont les sources ne sont pas contrôlées est FAIL. Toute vérification absente reste explicitement ouverte.

## Distinguer les niveaux de qualité
Le validateur Node.js contrôle seulement **l'intégrité des artefacts**, l'alignement JSON→HTML et le maintien de `noindex`. Il ne peut ni exécuter un skill d'écriture ni attester qu'un fait vétérinaire est vrai. Ne jamais présenter CI verte comme un PASS éditorial.
