# Behoeften — analyse et revue finale

Scope exclusif : `/voor-gevoelige-honden/` et ses pages filles. Le libellé de navigation est « Behoeften » ; ne pas créer de répertoire `/behoeften/`.

Ce fichier est un **orchestrateur**, pas un agent ou une méthode de qualité inventée. Lire `AGENTS.md`, `DESIGN.md`, `behoeften-workflow.config.yaml`, puis exécuter les skills locaux pertinents.

## Modes

- `AUDIT` (page existante) : inspecter contenu réel, code HTML, intention, liens voisins, citations et preuves ; ne pas réécrire.
- `CLUSTER_AUDIT` : comparer les six URLs et les sections `/soorten/`, `/ingredienten/`, `/eiwit/`, `/levensfase/`, `/gidsen/` ; relever cannibalisation et lacunes ; ne pas réécrire.
- `PUBLISH_REVIEW` : revue indépendante après rédaction et correction, avec décision `PASS — READY_FOR_HUMAN_VALIDATION` ou `FAIL — KEEP_NOINDEX`.

## Réutiliser, sans les dupliquer, les skills existants

`content-audit` → `search-intent` → `jobs-to-be-done` (si pertinent) → `content-refresh` (si mise à jour) → `fact-check` → `evidence-based-reviews` (si recommandation expérientielle) → `affiliate-value` (si achat) → `internal-linking-audit` → `anti-ai-slop` → `seo-onpage` / `seo-technical` → `editorial-qa`.

Les skills `usage-analysis-workflow` et `usage-content-workflow` des repos de référence fournissent la logique de séparation audit/production, mais contiennent des exemples sur des appareils numériques : ne **pas** appliquer leur contenu sectoriel au chien.

## Contrôles propres au sujet

1. **Frontière éditoriale** : une page Behoeften aide à évaluer les contraintes d'un chien et les questions à poser avant de choisir une friandise ; `/soorten/` classe des types de snacks, `/eiwit/` une source de protéines, `/ingredienten/` les formulations, et `/gidsen/` les explications générales.
2. **Sécurité et preuves** : aucune allégation diagnostique, thérapeutique ou de prévention sans preuve appropriée ; ne pas affirmer que « hypoallergeen », « graanvrij », « mono-eiwit », « vetarm » ou « biologisch » rend un produit sûr pour tous les chiens. Préciser les limites d'une lecture d'étiquette et renvoyer au vétérinaire pour suspicion d'allergie, régime d'éviction, troubles persistants ou maladie.
3. **Information produit** : pas de composition, certification biologique, dosage, kcal, disponibilité, prix, propriété « hypoallergénique », test clinique ou essai personnel inventés. Toute affirmation spécifique à un produit exige une source documentée et datée.
4. **Utilité** : spécificité du besoin, critères concrets, exclusions, cas défavorables, alternatives, distinction entre information et conseil médical ; éviter les podiums affiliés déguisés.
5. **Structure et design** : préserver l'identité éditoriale, les composants et les images existants ; pas de plan H2 ou quota de mots standardisé ; contrôler le HTML rendu, métadonnées, canonical, internal linking, robots et responsive si environnement disponible.

## Rapport d'audit requis

Pour chaque URL : intention et rôle ; contenu à préserver ; problèmes avec preuves ; risques vétérinaires ; cannibalisation ; décision `KEEP | LIGHT_UPDATE | DEEP_REWRITE | MERGE | NOINDEX` ; changements ciblés ; sources insuffisantes ; statut robots ; prochaine étape.

En `PUBLISH_REVIEW`, inclure les vérifications effectuées et les échecs bloquants. Ne jamais publier ni indexer automatiquement.
