# Guide analysis workflow — `/gidsen/`

This is project orchestration, **not a skill**. It may define site-specific routing and quality gates, but all reusable specialist methodology must come from the third-party skills materialized in `.agents/guide-vendor/`.

## Purpose

Audit one guide or a relevant guide cluster before writing. The workflow decides whether the page should be kept, lightly updated, deeply rewritten, merged, or kept out of the index. It also performs the final publish review after production.

Normal sequence for an existing guide:

`AUDIT → decision → guide-content workflow when needed → PUBLISH_REVIEW`

Never remove `noindex,follow`, merge, redirect, or delete solely because this workflow returns PASS.

## Modes

### `AUDIT`

Read the page, relevant neighboring guides/categories, available semantic data, current SERP when intent is uncertain, and current sources for unstable facts. Return one decision:

- `KEEP`
- `LIGHT_UPDATE`
- `DEEP_REWRITE`
- `MERGE`
- `NOINDEX`

### `CLUSTER_AUDIT`

Compare a coherent set of `/gidsen/` pages to detect:

- overlapping reader jobs or search intent;
- artificial fragmentation of one topic;
- missing sub-questions that deserve their own URL;
- guide/category overlap;
- structurally cloned pages;
- repeated conclusions or commercial CTAs that do not belong to the question.

### `PUBLISH_REVIEW`

Run after the content workflow. Return exactly one of:

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

A PASS is not permission to index or merge automatically.

## Required inputs

Use what is available, and state important unknowns instead of inventing them:

- `gidsen/AGENTS.md`;
- `.agents/workflows/guides.md`;
- target page;
- `.content/briefs/<slug>.md` when present;
- `.content/guides/<slug>.md` audit/review record;
- nearest guide/category pages by intent;
- keyword/GSC data if actually available;
- current SERP if format or intent can have changed;
- primary/authoritative sources for unstable or regulated claims.

## Specialist skill chain

All paths below refer to `.agents/guide-vendor/<skill>/...`.

1. **`seo-content-audit`** — determine whether the URL deserves KEEP / update / consolidation / removal.
2. **`seo-keyword`** — establish the primary query family, intent and overlap. Never invent search volume or difficulty.
3. **`content-brief-authoring`** — use its search-intent, entity-coverage and internal-linking references to articulate the reader job and expected answer shape. Do not blindly apply its word-count examples or quotas.
4. **`seo-onpage`** — baseline title, meta, H1, content coverage, links, canonical and schema.
5. **`seo-technical`** — robots/indexability, crawlability, rendering and structured-data blockers.
6. **`seo-geo`** — assess whether the page contains extractable, attributable, self-contained answers and meaningful entities.
7. **`fact-check`** — verify the claims that matter to the page's central answer.
8. **`editorial-qa`** — use in `PUBLISH_REVIEW` for brief adherence, citation discipline, structure/clarity, AI-content review and SEO/AEO QA.
9. **`anti-ai-slop`** — detect generic, interchangeable, over-smoothed prose; do not use it as an authorship detector.

The optional `internal-linking-audit` may be used only when its expected GSC MCP is available. Otherwise use the internal-linking strategy from `content-brief-authoring` plus repository-observable checks from `seo-onpage` and state the limitation.

## Site-specific analysis layer

This layer is routing logic, not a replacement skill.

### 1. What job does the guide perform?

Classify the dominant job only to expose risks; never turn the class into a template.

- `EXPLAINER`: distinguish concepts, mechanisms, labels, ingredients or rules.
- `CHOICE`: help the reader decide between options or criteria without ranking products.
- `HOW_TO`: allow a task to be carried out or checked reliably.

A guide may be hybrid.

### 2. Guide vs category boundary

A `/gidsen/` page should own a question or decision. A category/ingredient/protein page should own browsing of products or assortments.

If the useful answer becomes mainly “show me products with X”, route commercial exploration to the category and keep the guide educational.

### 3. Evidence risk for this niche

Treat the following as evidence-sensitive:

- organic certification and labelling;
- petfood claims and legal descriptors;
- calories, feeding quantities and obesity;
- allergies, intolerances, digestion and disease;
- puppy feeding and safety;
- dental, joint, skin/coat or other health effects;
- ingredient/additive claims.

Prefer, as appropriate: EU legislation, Dutch regulator/control body, veterinary/scientific sources, or manufacturer documentation for a product-specific fact. Commercial pages are not primary evidence for general health or regulatory claims.

### 4. Editorial integrity

A guide is not good because it is long. It is good when it makes the issue clearer, more verifiable or more decidable.

Check for:

- direct answer early enough for the intent;
- each major section adds a distinct piece of reasoning;
- distinctions between what a term **does** and **does not** guarantee;
- important exceptions and scope limits;
- sources attached to the claims they support, not merely dumped at the bottom;
- useful examples or decision checks when they genuinely clarify the question;
- no unsupported jump from “biological/natural” to “healthier/better”;
- no product ranking disguised as an explainer.

### 5. Cluster similarity

Compare the target with nearest guides. Shared visual components are fine. Flag editorial cloning when H2 functions, reasoning order, table placement, conclusion and CTA are repeated mechanically across topics.

## Decisions

### `KEEP`
Distinct job, supported claims, sufficient depth, no material correction needed.

### `LIGHT_UPDATE`
Architecture is sound; corrections are local (freshness, source, title/meta, missing distinction, link, example).

### `DEEP_REWRITE`
Use only for structural problems such as thin reasoning, unsupported central claims, unclear intent, heavy overlap, outdated procedure, category confusion, or an architecture that does not let the reader understand/decide.

Preserve supported facts and useful material from the current page.

### `MERGE`
Another URL owns substantially the same reader job. Recommend the target; do not merge automatically.

### `NOINDEX`
The page still lacks enough distinct value or evidence to be indexed. Do not delete automatically.

For every decision record:

- confidence;
- reader job and query family;
- page role and neighboring-page boundaries;
- existing value to preserve;
- evidence used;
- unknowns/blockers;
- cannibalisation risk;
- required scope of work;
- next step.

## PUBLISH_REVIEW gates

Run on the finished version:

1. provenance sync/check for third-party skills;
2. `fact-check` on the claims actually written;
3. `editorial-qa` against the persisted brief;
4. `seo-onpage`;
5. `seo-technical`;
6. `seo-geo`;
7. internal-link check (GSC skill only if available; otherwise repository/brief fallback);
8. `anti-ai-slop`;
9. `node scripts/check_guides.mjs`;
10. `npm run check` and `npm run build`.

Fail publish review when a central claim lacks adequate support, a page violates its role, a technical blocker remains, or the article still reads as generic/commercial filler rather than a source-led answer.
