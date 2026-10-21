# Site context — shared agents remain unchanged

Reference: `MarcW88/bloc-notes-numerique` at the exact commit recorded in
`.agents/shared-agents.lock.json`. Methodology, sequence, conditional stages,
references and quality gates come from its unmodified `.agents/skills/` files.

## Allowed site adaptations

| Source context | This site |
|---|---|
| bloc-notes-numeriques.fr | biologische-hondensnacks.nl |
| French prose | Dutch prose (`nl`); keep names of workflow decisions unchanged |
| Digital notebooks / E Ink examples | Dog snacks, ingredients, labelling and feeding contexts; research topic-specific facts instead of mechanically substituting nouns |
| `/guides/` | `/gidsen/` |
| `/comparatifs/` | Comparative product-selection role; distinguish this from snack-family explanations under `/soorten/` |
| `/usages/` | Reader circumstances and needs, including `/voor-gevoelige-honden/` and `/levensfase/` |
| `/marques/` | `/merken/`; keep ingredient/protein explanations under `/ingredienten/` and `/eiwit/` distinct |
| Technology/vendor factual sources | Appropriately authoritative veterinary, nutrition, labelling and regulatory sources; no invented product experience |

These are context mappings, not replacement instructions for research, briefs,
writing or quality. Do not simplify an explanation because it concerns dog food.
Use examples, mechanisms, exceptions and decision reasoning when the reader's
question requires them, exactly as the shared workflow requires.

## Existing site plumbing

- Rendered guide files: `gidsen/<slug>/index.html`. Preserve existing authored
  content through `npm run build`; do not add a generic content generator.
- New briefs: `.content/briefs/<slug>.md`; new publication reviews:
  `.content/reviews/<slug>.md`. Read prior `.content/guides/<slug>.md` records as
  historical input, not proof of a completed present-day audit.
- `python validate_guide_quality.py` is the site command adapter to the existing
  `node scripts/check_guides.mjs --publish` validator. These are machine checks,
  not editorial or factual approval. Also run `npm run check` and `npm run build`.
- All current guides remain `noindex,follow`. Copying a workflow or passing a
  machine check never grants publication/indexation approval.

## Provenance and reuse

`python scripts/sync_shared_agents.py --check` verifies every locked shared file.
To copy or restore the exact agents from a local checkout of the reference:

`python scripts/sync_shared_agents.py --source /absolute/path/to/reference --sync`

The checkout must match the pinned source commit. To compare against it without
writing: use `--source /absolute/path/to/reference --check`. Do not update the
pin, rewrite a shared file or switch reference repositories without an explicit
request. A future site can reuse the same lock, script and shared files, then
supply its own site context and routing instructions.

## Routage complet de tous les types de contenus

Le manifeste `.agents/workflow-routing.json` et les points d’entrée des rubriques
activent les mêmes agents originaux pour tous les types de contenus.
`/soorten/`, `/ingredienten/` et `/eiwit/` relèvent de Guide pour expliquer et
arbitrer des critères ; une sélection comparative de produits relève toujours de
Comparison. `/levensfase/` et `/voor-gevoelige-honden/` relèvent de Usage.
`/merken/`, `/producten/` et `/kauwsnacks/` relèvent de Brand lorsqu’ils documentent
un écosystème ou un produit précis. Un changement de tâche peut imposer le
handoff prévu dans le workflow original, même dans une rubrique donnée.

Trust : `/a-propos/` devient `/over-ons/` ; `/transparence-affiliation/` devient
`/transparantie-affiliatie/` ; contact et mentions gardent leur chemin.
Les méthodes d’évaluation et politiques de comparaison relèvent également de
Trust, sans créer une page absente uniquement pour reproduire l’arborescence.
Comparison et Deal restent disponibles avec leurs agents complets même si le
site n’a pas encore de rubrique dédiée. Ne pas créer de contenus pour valider
artificiellement le routage.

Conserver les registres originaux `.content/usages/`, `.content/trust/`,
`.content/deals/`, les briefs et preuves demandés par chaque workflow. Les anciens
registres snack/behoeften servent d’entrée historique, pas de validation courante.
Toute commande technique absente ou incompatible est un blocage à documenter et
à résoudre avant PUBLISH_REVIEW, jamais un contrôle implicitement réussi.

## Dépendances installées et commandes locales

Les 66 fichiers d’origine restent verrouillés et inchangés. Les auxiliaires
manquants proviennent de leurs dépôts exacts et sont verrouillés séparément dans
`.agents/support-files.lock.json` (source, commit, chemin et SHA256).
Contrôle complet : `python scripts/check_agent_installation.py`.

- Maillage : `scripts/internal_link_audit.py`, copie exacte de dageno-agents.
  Les exports HTML doivent résoudre `<base href>` : utiliser
  `scripts/export_audit_html.py`, puis le mode import original. Aucun fichier du
  site n’est modifié par cet export. Ne pas utiliser les résultats erronés d’un
  fetcher qui ignore le base HTML.
- SEO technique : les deux références manquantes sont installées à leur chemin.
- Anti-ai-slop : paquet auxiliaire complet ; cohérence vérifiée avec
  `python .agents/skills/anti-ai-slop/tools/validators/check_all.py --root
  .agents/skills/anti-ai-slop --profile pack-self --format markdown`.
- Écriture : références cadence et compatibility-examples restaurées.
- SEO drift : seuils et prérequis d’origine disponibles ; les scripts et références
  complémentaires sont sous `.agents/support/seranking/`. Se placer dans ce
  répertoire pour les commandes qui utilisent ses chemins relatifs. SE Ranking
  MCP est un prérequis externe à connecter pour la fonctionnalité correspondante ;
  Google et Firecrawl exigent leurs propres accès lorsqu’ils sont utilisés.
- Commandes `validate_brands.py`, `validate_comparisons.py`,
  `validate_usage_workflow.py`, `validate_deal_workflow.py`,
  `validate_trust_workflow.py` : adaptateurs machine locaux au HTML néerlandais.
  Ils ne reprennent pas les catalogues/URLs français de Bloc-notes et ne valent
  jamais validation éditoriale. Leur échec sur un brouillon signifie contenu à
  compléter, pas dépendance absente. Registres et preuves restent ceux demandés
  par les agents originaux. Ils ne modifient aucune page ni son indexation.
- Playwright : `npm run visual:install` ; l’adaptateur runtime peut utiliser le
  navigateur de secours installé si l’archive habituelle est indisponible.
  Le script du skill original reste inchangé. `npm run visual:site` et
  `npm run test:design` passent par cet adaptateur.

Les anciens générateurs Python des Actions héritées sont une application
française distincte et ne font pas partie de l’installation des agents. Ils ne
sont ni remplacés par de faux générateurs ni certifiés par le contrôle
installation. Le contrôle commun disponible via shared-site-readiness vérifie
installation, build et structure ; il ne génère pas de nouveaux articles.
