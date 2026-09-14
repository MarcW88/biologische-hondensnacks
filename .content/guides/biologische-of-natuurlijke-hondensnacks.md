# Guide audit — biologische-of-natuurlijke-hondensnacks

## Page

- URL: `https://biologische-hondensnacks.nl/gidsen/biologische-of-natuurlijke-hondensnacks/`
- Repository path: `gidsen/biologische-of-natuurlijke-hondensnacks/index.html`
- Status before work: placeholder, `noindex,follow`
- Primary query: `biologische of natuurlijke hondensnacks`
- Supporting intent: `biologisch vs natuurlijk hondensnacks`, difference between organic certification and a natural product descriptor
- Intent: informational / comparison
- Keyword-data limitation: no verified current search-volume or difficulty dataset is available in this task. No volume/KD has been invented.

## Content-audit decision

**UPDATE — deep rewrite, preserve URL and role.**

The URL has a distinct informational job, but the previous body was placeholder copy and contained no usable answer or evidence. The page remains separate from:

- `/gidsen/biologisch-keurmerk-hondensnacks/` — deeper verification of the EU organic logo, control body/code and certification;
- `/ingredienten/natuurlijke-hondensnacks/` — category/commercial exploration of natural snacks;
- `/gidsen/ingredienten-hondensnacks-lezen/` — broader ingredient-list reading.

The current guide owns the **difference and decision framework**, not the full certification manual or the natural-snack catalogue.

## Evidence and claim verification

### C1 — Organic petfood can use organic-production terms in the sales description only under the EU petfood-organic conditions, including at least 95% organic agricultural ingredients by weight.

- Status: VERIFIED
- Primary source: Regulation (EU) 2023/2419, Article 3(1)(a)
- Source: https://eur-lex.europa.eu/eli/reg/2023/2419/oj
- Note: this petfood-specific regulation is more precise than relying only on general Regulation (EU) 2018/848.

### C2 — If petfood has less than 95% organic agricultural ingredients, organic references can be limited to qualifying ingredients in the ingredient list when the other Article 3 conditions are met.

- Status: VERIFIED
- Primary source: Regulation (EU) 2023/2419, Article 3(1)(b), 3(3)-(5)
- Source: https://eur-lex.europa.eu/eli/reg/2023/2419/oj

### C3 — The EU organic-production logo is mandatory on prepacked petfood that meets Article 3(1)(a), with Article 4(2) applicable since 1 May 2024.

- Status: VERIFIED
- Primary source: Regulation (EU) 2023/2419, Articles 4 and 6
- Source: https://eur-lex.europa.eu/eli/reg/2023/2419/oj

### C4 — In the Netherlands, Skal explains and supervises organic indications for product categories covered by EU organic legislation, including dog food/organic feed.

- Status: VERIFIED
- Source: https://www.skal.nl/waarschuwingsbrief
- Supporting source: https://www.skal.nl/onderwerpen/import/aanduidingen/bio-checker/diervoeder

### C5 — `Natuurlijk` is not the same certification claim as `biologisch`; the petfood sector's FEDIAF code gives a specific interpretation for use of `natural` as a product descriptor.

- Status: VERIFIED WITH SCOPE NOTE
- Source: FEDIAF Code of Good Labelling Practice for Pet Food, section 5.2.4.1, publication October 2019
- Source: https://fediaf.org/wp-content/uploads/2022/02/FEDIAF_labeling_code_2019_onlineOctober2019.pdf
- Scope note: FEDIAF is an industry code used alongside legislation, not an organic certification scheme. NVWA explicitly lists the FEDIAF code among sector labelling guides.
- NVWA source: https://www.nvwa.nl/onderwerpen/diervoeder/diervoeder-of-petfood-etiketteren/regels

### C6 — Petfood labelling/marketing claims may not mislead and may not promise prevention or cure of disease.

- Status: VERIFIED
- Source: NVWA, `Diervoeder of petfood etiketteren`
- Source: https://www.nvwa.nl/onderwerpen/diervoeder/diervoeder-of-petfood-etiketteren

## SEO baseline and final pass

Baseline:
- title relevant but generic;
- duplicate/generic meta wording used on other templates;
- relevant H1 but no answer body;
- canonical missing;
- contextual internal links absent.

Implemented:
- page-specific 53-character title: `Biologische of natuurlijke hondensnacks: het verschil`;
- page-specific meta description;
- one H1 aligned with comparison intent;
- direct answer immediately below H1;
- self-canonical added;
- contextual links added to the organic-label guide, natural-snack category and ingredient-reading guide;
- `BreadcrumbList` JSON-LD added using only observable site hierarchy;
- `noindex,follow` deliberately retained pending human validation.

Final SEO status: **PASS FOR HUMAN REVIEW**. No search-volume/KD claim was used because no verified dataset was available.

## GEO baseline and final pass

Baseline:
- no extractable answer/definition;
- no authoritative source named;
- no evidence differentiating organic rules from a natural descriptor.

Implemented:
- self-contained distinction directly below the H1;
- exact 95% threshold used only in its verified EU context, with the hunting/fishing edge case acknowledged;
- Regulation (EU) 2023/2419, Skal, NVWA and FEDIAF named where they support different claims;
- sections written to remain understandable independently without forced FAQ formatting;
- source section links to primary/authoritative material;
- no FAQPage schema, fabricated quotation, invented statistic or `llms.txt` ranking claim.

Final GEO status: **PASS FOR HUMAN REVIEW**.

## Writing / AI-slop final pass

Checked for generic scene-setting, promotional adjectives, fake personal experience, symmetrical filler, unsupported health superiority, repetitive FAQ-shaped headings and excessive summary language.

Result:
- no fabricated vet quote, owner experience, study, test result or product recommendation;
- `biologisch` is not presented as automatically nutritionally superior;
- `natuurlijk` is not dismissed as meaningless, but its scope is distinguished from organic certification;
- no artificial word-count, source-count, FAQ, table or internal-link quota was applied;
- final text remains neutral and decision-oriented.

Final anti-slop status: **PASS**.

## Internal linking

- Repository-observable contextual links implemented.
- The specialised upstream `internal-linking-audit` expects its GSC MCP methods. That MCP was not available in this task, so no GSC-based orphan/striking-distance findings have been fabricated.
- Fallback: on-page internal-link checks only, as specified by the guide workflow.

## Final status

- Fact-check: PASS
- SEO: PASS FOR HUMAN REVIEW
- GEO: PASS FOR HUMAN REVIEW
- Anti-AI-slop/humanization: PASS
- Technical/static gate: pending CI on content PR
- Indexation: deliberately remains `noindex,follow`

**READY_FOR_HUMAN_VALIDATION**
