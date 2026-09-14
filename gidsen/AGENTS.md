# Instructions scoped to `/gidsen/`

The root `AGENTS.md` was imported from another project and contains legacy `/guides/` instructions. For every file under this directory, **this file takes precedence**.

## Authoritative guide workflow

Use:

- `.agents/workflows/guides.md` as the entry point;
- `.agents/workflows/guide-analysis.md` for `AUDIT`, `CLUSTER_AUDIT` and `PUBLISH_REVIEW`;
- `.agents/workflows/guide-content.md` for `LIGHT_UPDATE`, `DEEP_REWRITE` and new-guide production.

These files are project orchestration, not skills.

Before any audit or edit, run:

```bash
python scripts/sync_guide_skills.py --sync --remote
```

Then use only the pinned third-party skills under `.agents/guide-vendor/` materialized from `.agents/guide-skills.lock.json`.

Do **not** use the legacy custom skill orchestrators:

- `.agents/skills/guide-analysis-workflow/`
- `.agents/skills/guide-content-workflow/`

Do **not** use a same-named local skill from `.agents/skills/` as a substitute for a pinned guide-vendor skill.

## Mandatory sequence for an existing guide

`AUDIT → decision → persisted brief when rewriting → evidence-led drafting → post-write fact-check/QA/SEO/GEO → PUBLISH_REVIEW`

A `DEEP_REWRITE` requires `.content/briefs/<slug>.md` before final drafting.

Every worked guide requires `.content/guides/<slug>.md` as its audit/review record.

## Editorial standard

No word-count, heading-count, FAQ, table, source or link quota is a proxy for quality. A guide should be as deep as the reader's question and evidence require.

Do not invent veterinary, nutrition, certification, safety, product-test or user-experience claims. For evidence-sensitive claims, attach visible attribution close to the claim instead of relying only on a source dump at the end.

A guide must remain useful if affiliate links disappear. Do not turn an explainer into a product ranking or commercial landing page.

Keep `noindex,follow` until human validation and an explicit instruction to change indexation.
