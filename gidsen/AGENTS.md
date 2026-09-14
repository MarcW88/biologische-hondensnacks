# Instructions scoped to `/gidsen/`

The root `AGENTS.md` was imported from another project and contains legacy `/guides/` instructions. For every file under this directory, **this file takes precedence**.

## Authoritative workflow

Use `.agents/workflows/guides.md`.

Before any audit or edit, run:

```bash
python scripts/sync_guide_skills.py --sync --remote
```

Then use only the pinned third-party skills under `.agents/guide-vendor/` that were materialized from `.agents/guide-skills.lock.json`.

Do **not** use the legacy custom orchestrators:

- `.agents/skills/guide-analysis-workflow/`
- `.agents/skills/guide-content-workflow/`

Do **not** use a same-named local skill from `.agents/skills/` as a substitute for a pinned guide-vendor skill.

## Mandatory guide chain

Diagnostic:
`seo-technical → seo-content-audit → seo-keyword → seo-onpage → seo-geo`

Evidence and writing:
`fact-check → general-writing/humanizer pipeline → anti-ai-slop`

Final gates:
`fact-check → seo-onpage → seo-geo → internal-linking-audit when its MCP is available → anti-ai-slop → npm check/build`

No word-count, heading-count, FAQ, table, source or link quotas may be used as a proxy for quality. Never invent veterinary, nutrition, certification, safety, product-test or user-experience claims.

Every worked guide must have a matching private audit record under `.content/guides/<slug>.md` as described in `.agents/workflows/guides.md`.
