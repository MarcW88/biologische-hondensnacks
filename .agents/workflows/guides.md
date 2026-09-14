# Guide workflow — `/gidsen/`

This file is the routing entry point for guide work. It is **orchestration only**, not a skill.

Reusable methodology must come from the third-party, commit-pinned skills in `.agents/guide-skills.lock.json`. Project-specific workflow logic lives in:

- `.agents/workflows/guide-analysis.md`
- `.agents/workflows/guide-content.md`

## 0. Provenance gate

Before any guide audit, creation or rewrite, run:

```bash
python scripts/sync_guide_skills.py --sync --remote
```

Only the materialized copies under `.agents/guide-vendor/` may be used as guide skills.

- custom skills are forbidden as specialist methodology;
- floating branches/tags are forbidden;
- every upstream source is pinned to an immutable 40-character commit SHA;
- local `.agents/skills/...` copies do not override the vendor set;
- if an upstream skill or pinned reference cannot be fetched, stop rather than silently substituting a local custom file.

The workflows in `.agents/workflows/` are allowed to define **site routing, page boundaries, evidence sensitivity and handoff rules**. They are not presented as reusable skills.

## 1. Existing guide sequence

For an existing `/gidsen/` URL:

1. run `.agents/workflows/guide-analysis.md` in `AUDIT` mode;
2. record the decision and evidence in `.content/guides/<slug>.md`;
3. `KEEP` → stop unless a separate requested task remains;
4. `LIGHT_UPDATE` or `DEEP_REWRITE` → run `.agents/workflows/guide-content.md`;
5. persist/update `.content/briefs/<slug>.md` before final drafting;
6. run `.agents/workflows/guide-analysis.md` in `PUBLISH_REVIEW` mode;
7. keep `noindex,follow` until human validation and an explicit instruction to change indexation.

`MERGE` and `NOINDEX` require a human decision before structural action.

## 2. New guide sequence

For a genuinely new guide:

1. verify the URL has a distinct reader job and does not duplicate a category/guide;
2. run the evidence and planning stages of `guide-content.md`;
3. create `.content/briefs/<slug>.md`;
4. draft from the brief using the pinned public skills;
5. run `PUBLISH_REVIEW`;
6. keep `noindex,follow` until explicit human approval.

## 3. Required public skill stack

The current pinned set includes:

### Diagnostic / SEO

- `seo-technical`
- `seo-content-audit`
- `seo-keyword`
- `seo-onpage`
- `seo-geo`

### Evidence and planning

- `fact-check`
- `content-brief-authoring`

### Drafting

- `content-and-copy`
- `general-writing`
- `humanizer`
- `better-usage`
- `academic-voice`
- `writing-cadence`
- `non-autoregressive-writing-pass`

### Quality

- `editorial-qa`
- `anti-ai-slop`
- `internal-linking-audit` only when its expected MCP is available

The lockfile, not this prose list, is the source of truth for exact repositories, commits and included files.

## 4. Editorial standard for this site

A guide should not read like a short affiliate landing page with a source dump added at the end.

It should:

- answer the reader's question early;
- show the reasoning needed to understand or decide;
- distinguish what a label/ingredient/claim **does** and **does not** establish;
- expose meaningful exceptions, uncertainty and scope;
- attach important evidence to the claims it supports;
- use tables/checklists/examples only when they clarify the reader's task;
- remain useful if affiliate links are removed;
- avoid product rankings unless the page is explicitly a comparison/category page;
- avoid fixed word, H2, FAQ, table, source or internal-link quotas.

For pet nutrition, safety, health and organic/labelling claims, use appropriately authoritative current sources and never convert general information into individualized veterinary advice.

## 5. Required artifacts per worked guide

### Audit/review record

`.content/guides/<slug>.md`

Must contain:

- URL/slug;
- query family and reader job;
- analysis decision and scope;
- page-role boundaries;
- evidence/source register and unresolved claims;
- baseline SEO/GEO findings;
- material changes;
- final fact-check;
- editorial-QA status;
- final SEO/GEO status;
- internal-linking status/limitation;
- technical/build status;
- final `READY_FOR_HUMAN_VALIDATION` only when no blocker remains.

### Content brief

`.content/briefs/<slug>.md`

Required for every new guide and every `DEEP_REWRITE`; recommended for substantive `LIGHT_UPDATE` work. The brief must be based on evidence and page role, not a recycled content template.

## 6. Machine checks

After final content is stable:

```bash
python scripts/sync_guide_skills.py --remote
node scripts/check_guides.mjs
npm ci
npm run check
npm run build
```

A machine PASS only proves detectable gates. It does not replace editorial or factual review.
