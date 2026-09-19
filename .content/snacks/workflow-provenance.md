# Provenance du workflow Snacks

Date de contrôle : 2026-09-19

## Principe

Les deux skills `snack-analysis-workflow` et `snack-content-workflow` sont des orchestrateurs spécifiques au routage `/soorten/`. Ils ne redéfinissent pas les méthodes d’audit, d’intention, de JTBD, de preuve, de brief, de rédaction ou de QA.

## Source réutilisée

Architecture étudiée : `MarcW88/cafetiere-italienne`, branche `main`.

Les briques suivantes sont déjà versionnées dans `.agents/skills/` et proviennent de dépôts GitHub existants. Elles sont appelées séparément par les orchestrateurs Snacks :

- `seo-content-audit`, `seo-keyword`, `content-refresh`, `content-brief-authoring`, `content-and-copy`, `seo-onpage`, `seo-technical`, `editorial-qa` : adaptations issues de `rampstackco/claude-skills` ;
- `jobs-to-be-done` : `wondelai/skills` ;
- `fact-check` : `notque/vexjoy-agent` ;
- `humanizer` et `general-writing` : `msimchowitz/writing-skills` ;
- `anti-ai-slop` : `jmlozano1990/Cowork-Starter-Kit` ;
- `internal-linking-audit` : `FlorianBruniaux/google-search-console-mcp` ;
- `evidence-based-reviews` : workflow réutilisé depuis les dépôts existants de l’écosystème du propriétaire.

Les skills spécialisés ne sont pas copiés dans les orchestrateurs. La couche custom se limite aux frontières de catégories du site, aux risques de preuve propres aux snacks pour chiens, à l’intégration du dépôt et au publish review du cluster.

## Contrôle de parité

Les versions locales de `seo-content-audit`, `seo-keyword`, `content-brief-authoring`, `content-and-copy`, `evidence-based-reviews`, `internal-linking-audit`, `humanizer`, `general-writing`, `anti-ai-slop`, `seo-onpage` et `seo-technical` ont été comparées aux fichiers du dépôt `cafetiere-italienne` lors de la mise en place. Elles sont byte-identiques pour cette sélection.

Les skills `search-intent`, `fact-check` et `affiliate-value` de `cafetiere-italienne` contiennent des adaptations au café moka ; les versions génériques déjà présentes dans ce dépôt ont été conservées afin de ne pas importer de règles métier inadéquates.
