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
