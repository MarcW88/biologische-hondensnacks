# Guide content workflow — `/gidsen/`

This is project orchestration, **not a skill**. It runs only after `guide-analysis.md` has determined that a guide needs `LIGHT_UPDATE` or `DEEP_REWRITE`, or when creating a genuinely new guide.

All reusable methodology must come from the pinned third-party skills materialized under `.agents/guide-vendor/`.

## Normal sequence

`guide-analysis / AUDIT → evidence → persisted brief → writing → post-write verification → guide-analysis / PUBLISH_REVIEW`

Do not remove `noindex,follow` automatically.

## 1. Inputs

Read before drafting:

- target page and neighboring guide/category pages;
- `.content/guides/<slug>.md` audit record;
- `.content/briefs/<slug>.md` if it exists;
- semantic/GSC data if actually available;
- current SERP where intent/format needs verification;
- authoritative sources needed for unstable or regulated claims.

Preserve useful supported material identified by the audit. Do not rewrite valid sections merely for stylistic novelty.

## 2. Evidence register before prose

Run `fact-check` before drafting and maintain a small evidence register in the brief/review record.

For each claim that materially supports the article's answer, capture:

- claim;
- source;
- source type/authority;
- date checked when freshness matters;
- conditions/scope;
- uncertainty or exception.

For dog nutrition, health and regulatory topics, commercial category pages are not sufficient evidence for central claims.

An unsupported claim is removed, qualified, or explicitly left unknown.

## 3. Reader job, role and depth

Use `seo-keyword`, `seo-content-audit` findings and the search-intent guidance inside `content-brief-authoring` to confirm:

- primary query family;
- dominant intent;
- reader's job-to-be-done;
- role of this URL inside the site;
- adjacent questions owned by another guide or category;
- the amount of explanation needed to answer the question responsibly.

There is no fixed word count. Depth is determined by what the reader must understand, verify or decide. Do not pad to hit a number and do not truncate merely because the direct answer is short.

## 4. Persist a real brief

Use `content-brief-authoring` as the planning owner. Save the result to `.content/briefs/<slug>.md` before final drafting.

The project brief must contain at least:

- primary topic/query and supporting query family;
- audience and reader job;
- page role and boundaries with neighboring URLs;
- unique value/differentiation;
- evidence register and required entities;
- claims that must not be made;
- internal-link plan;
- source-integration plan;
- proposed structure derived from the research;
- success criteria for the page itself (clarity, verifiability, role), not invented traffic targets.

Ignore any generic quota in an upstream template when it is not justified here. No mandatory number of words, H2s, links, sources, FAQs or tables.

## 5. Structure from evidence, not from a template

The structure must be generated after the evidence and brief exist.

A section is justified only when it answers a real follow-up question, explains a distinction, supplies evidence, handles an exception, gives a verification method, or helps the reader decide.

Useful patterns when warranted:

- direct answer near the top;
- “what this means / what it does not mean” distinction;
- decision table when two terms/choices are genuinely being compared;
- label/checklist steps when the reader can verify something on-pack;
- examples or counterexamples when they clarify scope;
- source notes attached to factual sections;
- final decision guidance without turning into product ranking.

Do not repeat the same pattern mechanically across all guides.

## 6. Draft with public writing skills

Use `content-and-copy` as the main drafting skill from the persisted brief.

Then use the pinned writing package deliberately:

1. `humanizer` over the visible article;
2. `general-writing` for minimal clarity edits;
3. its embedded helpers (`better-usage`, `writing-cadence`, `academic-voice`, `non-autoregressive-writing-pass`) only when relevant;
4. `anti-ai-slop` as a separate final detection/review pass.

Writing rules for this site:

- natural Dutch, not translated French;
- no fake veterinarian voice or first-hand testing;
- no invented owner anecdotes, studies, statistics or product experience;
- no “biologisch = gezonder” or “natuurlijk = beter” leap without evidence;
- no promotional adjectives that do not add information;
- no affiliate CTA simply because the site monetizes by affiliation;
- the guide must remain useful if all affiliate links disappear.

## 7. Source integration

Do not make the reader wait until a generic source dump at the bottom to discover where important facts came from.

For evidence-sensitive claims:

- name or link the relevant authority in the paragraph or a nearby source note;
- use a final `Bronnen en verificatie` section as a reference list, not as the only evidence signal;
- distinguish legislation/regulator/control body from industry guidance;
- make clear when a source explains practice rather than creates the legal rule;
- never imply that FEDIAF is a biological certification authority.

For a stable, obvious statement that does not materially support the decision, inline sourcing is optional. For thresholds, dates, legal scope, health/safety claims and disputed descriptors, visible attribution is expected.

## 8. Internal linking

Plan links in the brief using `content-brief-authoring`'s internal-link strategy.

Use the specialized `internal-linking-audit` only if its GSC MCP is actually available. Otherwise verify repository-observable links and state the limitation in the audit record.

A link should answer the next logical question. No link quota.

## 9. Post-write verification

After the copy is stable:

1. rerun `fact-check` on claims as actually phrased;
2. run `editorial-qa`, especially brief adherence, citation discipline, structure/clarity and AI-content audit;
3. run `seo-onpage`;
4. run `seo-technical`;
5. run `seo-geo`;
6. verify internal links;
7. run `anti-ai-slop` again if substantial edits happened after its first pass.

Any factual edit after fact-check reopens the relevant claim.

## 10. Handoff

Update `.content/guides/<slug>.md` with:

- final decision/scope;
- brief path;
- evidence and unresolved claims;
- substantive changes;
- final fact-check;
- editorial-QA status;
- SEO/GEO status;
- internal-link status;
- technical/build status.

Then return to `.agents/workflows/guide-analysis.md` in `PUBLISH_REVIEW` mode.
