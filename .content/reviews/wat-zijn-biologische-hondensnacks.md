# Guide correction and publication review — 22 October 2026

URL: https://biologische-hondensnacks.nl/gidsen/wat-zijn-biologische-hondensnacks/
Consumed audit: `.content/reviews/wat-zijn-biologische-hondensnacks-reaudit-2026-10-21.md`.
Decision: LIGHT_UPDATE. User explicitly requested corrections using the original workflow.

## Production workflow

Original `guide-content-workflow` applied. The original agents and their support
files were not edited. Site context supplies Dutch language and the authored HTML
integration. Existing HTML is the authored source preserved and explicitly loaded
by scripts/build-preserving-guides.mjs; corrected content is retained through build.

Separate pass outputs are in `.content/runs/wat-zijn-biologische-hondensnacks/2026-10-22/`:

1. Intent/content-audit/content-refresh handoff: scope and preservation decisions.
2. Research and fact-check ledger before drafting, in `.content/evidence/`.
3. content-brief-authoring: updated page-specific brief before writing.
4. content-and-copy: concrete production explanation; narrower legal background;
   fictional denominator example; existing useful passages preserved.
5. Post-writing fact-check: checked claims actually written; arithmetic verified;
   publication date is an actual update date, not a fabricated September check.
6. internal-linking-audit: original script, actual exported HTML, four existing
   contextual destinations confirmed. Zero remaining suggested links among candidates.
7. Humanizer embedded, including usage/cadence/global revision; then general-writing
   and its evaluation checklist. Separate outputs document actual wording repairs.
8. anti-ai-slop detection: LOW; no claim of AI authorship, no HIGH signal.
9. seo-onpage/seo-technical/applicable seo-best-practices and editorial-qa.
   No Laravel/React prescriptions or word/title/source quotas imposed.
10. Rendered reading: original Playwright script, mobile and desktop captures inspected.

Conditional: evidence-based-reviews not required because no experiential product
judgment; SEO drift not executed because no registered performance baseline;
generated image NOT_NEEDED. No fake product packaging, test, brand or review added.

## Final gate: guide-analysis-workflow / PUBLISH_REVIEW

Machine gate: `python validate_guide_quality.py` PASS, ten guides checked.
Repository check: PASS, 52 HTML pages. Build preserves authored corrected article.

| Substantive gate | Result | Evidence |
|---|---|---|
| Task and early answer | PASS | Plain definition, production mechanisms and limits |
| Guide/category boundary | PASS | No product ranking or brand-centred review |
| Central factual claims | PASS within written scope | Commission, official USDA/Defra reports, NVWA, FEDIAF; dated evidence ledger |
| No invented experience | PASS | No physical-test or product-specific experience claim |
| Practical explanation | PASS | Cultivation, livestock treatment and processing linked to label interpretation |
| Restrictions/unknowns | PASS | Not zero pesticides/medicines/additives; not a dietary guarantee; threshold only one condition |
| Independent value | PASS | Useful without affiliate links; no merchant rewrite found |
| Cluster distinction | PASS | Production explanation here; comparison of terms and packaging controls remain on neighbours |
| Generic-output patterns | PASS | Concrete examples replace circular framework-only definition; no HIGH finding |
| Metadata/links/schema | PASS within observable scope | Title/H1/URL/canonical/noindex unchanged; four contextual links verified; honest BreadcrumbList |
| Rendered reading | PASS | Two captures inspected, HTTP 200, no horizontal overflow or browser errors |

**PASS — READY_FOR_HUMAN_VALIDATION**

This decision is produced in the final analysis mode, after content and QA passes.
It is not a declaration of human approval or authorisation to index the article.
`noindex,follow` and the visible human-validation notice remain.

## Evidence and limits

The earlier direct-access EUR-Lex blocker was addressed through accessible official
explanatory documents: USDA E42023-0049 and Defra PE-CONS 33/23 REV 1 corroborate
claims about the EU regulation and logo date. The EU regulation remains cited as
the legal source. No UK-only rule is presented as Dutch law. This is not an exhaustive
legal-compliance certification of a real product or a claim about future amendments.

Google Search Console, field Core Web Vitals and Rich Results Test were not executed.
Missing site-level robots/sitemap recorded by the audit remain outside this bounded
article edit. The article remains deliberately noindex. No ranking improvement is claimed.
Some counters in the source visual script target French CSS selectors; zero such
counters is not used as proof of missing headings or tables on this Dutch page.
The actual rendered page and DOM were read.

## What changed

Simpler definition; a sourced production explanation; a fictional 76/80 example
with a precise denominator; less repetition of legal background; ingredient-reading
link in the body; supporting sources and an honest update date. Existing source
precision, complementary role and nutritional limitations were preserved.
