# Guide audit — biologische-of-natuurlijke-hondensnacks

## Page

- URL: `https://biologische-hondensnacks.nl/gidsen/biologische-of-natuurlijke-hondensnacks/`
- Repository path: `gidsen/biologische-of-natuurlijke-hondensnacks/index.html`
- Brief: `.content/briefs/biologische-of-natuurlijke-hondensnacks.md`
- Indexation: `noindex,follow` retained
- Primary query: `biologische of natuurlijke hondensnacks`
- Supporting intent: `biologisch vs natuurlijk hondensnacks`, difference between organic certification and a natural product descriptor
- Reader job: understand the difference, verify the claim on-pack/online, and know what neither term proves about nutrition
- Keyword-data limitation: no verified current volume/KD dataset was available; none was invented.

## Analysis decision

**DEEP_REWRITE — preserve URL, preserve evidence, rebuild editorial depth.**

The previous rewrite was factually sourced but too compressed. Important evidence was concentrated in a final source block, the reasoning path was thin, and the page could still feel like a short affiliate explainer rather than an evidence-led guide.

The URL remains distinct from:

- `/gidsen/biologisch-keurmerk-hondensnacks/` — deeper verification of EU organic logo/control information;
- `/ingredienten/natuurlijke-hondensnacks/` — product/category exploration;
- `/gidsen/ingredienten-hondensnacks-lezen/` — general ingredient-list reading;
- `/gidsen/welke-hondensnacks-zijn-gezond/` — broader nutritional suitability.

This guide owns the **meaning, limits and verification of `biologisch` vs `natuurlijk`**.

## Evidence register

### C1 — 95% rule for organic term in sales description

- Status: VERIFIED
- Source: Regulation (EU) 2023/2419, Article 3(1)(a)
- URL: https://eur-lex.europa.eu/eli/reg/2023/2419/oj
- Scope retained in copy: at least 95% of **agricultural ingredients by weight** are organic, together with the other production conditions.

### C2 — below 95%

- Status: VERIFIED
- Source: Regulation (EU) 2023/2419, Article 3(1)(b), 3(3)-(5)
- Copy distinguishes an organic ingredient reference from calling the whole snack organic.

### C3 — hunting/fishing exception

- Status: VERIFIED
- Source: Regulation (EU) 2023/2419, Article 3(2)
- Included as an edge case because fish snacks are relevant to the site.

### C4 — EU organic logo and application date

- Status: VERIFIED
- Source: Regulation (EU) 2023/2419, Articles 4 and 6
- Copy states that the EU organic logo must appear on qualifying prepacked petfood and Article 4(2) applies since 1 May 2024.

### C5 — Dutch organic supervision

- Status: VERIFIED
- Sources:
  - https://www.skal.nl/waarschuwingsbrief
  - https://www.skal.nl/onderwerpen/import/aanduidingen/bio-checker/diervoeder
- Skal explicitly includes dog kibble/organic feed within relevant supervision scope.

### C6 — `natuurlijk` as product descriptor/claim

- Status: VERIFIED
- Source: NVWA, `Wat is een claim op diervoeder?`
- URL: https://www.nvwa.nl/onderwerpen/diervoeder/claims-op-diervoeders-en-petfood/wat-is-een-claim
- NVWA lists `natuurlijk`, `vers` and `light` as product descriptors.

### C7 — FEDIAF practical definition of `natural`

- Status: VERIFIED WITH SCOPE NOTE
- Sources:
  - https://www.fediaf.org/self-regulation/labelling/
  - https://fediaf.org/wp-content/uploads/2022/02/FEDIAF_labeling_code_2019_onlineOctober2019.pdf
- Scope note preserved in public copy: FEDIAF is practical sector/co-regulatory guidance used alongside legislation, not an organic certification body.

### C8 — claims must not mislead; medical claims prohibited

- Status: VERIFIED
- Sources:
  - https://www.nvwa.nl/onderwerpen/diervoeder/claims-op-diervoeders-en-petfood
  - https://www.nvwa.nl/onderwerpen/diervoeder/diervoeder-of-petfood-etiketteren
- Public copy does not create veterinary advice from these rules.

## Public-content changes

The second rewrite now includes:

- a direct answer plus explicit “what neither term proves” distinction;
- a comparison table for `biologisch`, `natuurlijk`, `zonder toevoegingen` and `gezond`;
- full explanation of the 95% rule with the agricultural-ingredient scope preserved;
- the below-95% ingredient-list case;
- the separate hunting/fishing rule;
- EU-logo timing and Skal context;
- NVWA classification of `natuurlijk` as a product descriptor;
- FEDIAF explanation with a visible scope disclaimer;
- four common interpretation errors;
- a five-step label verification method;
- a decision rule that separates certification, composition and nutritional suitability;
- visible source notes adjacent to evidence-sensitive claims;
- final `Bronnen en verificatie` section as reference list rather than sole attribution mechanism;
- links to the organic-label, ingredient-reading, healthy-snacks and natural-category pages only where they answer a next question.

No product ranking, affiliate CTA, fabricated test, veterinarian quote, user anecdote or health-superiority claim was added.

## SEO / intent review

- Title and H1 directly match the comparison intent.
- Meta describes difference + verification rather than generic benefits.
- Direct answer appears before long-form detail.
- The URL role is narrower than the natural-snack category and broader than the organic-logo verification page.
- Canonical remains self-referential.
- Breadcrumb schema uses only observable hierarchy.
- No FAQPage schema was added.
- `noindex,follow` remains deliberately in place pending human approval.

SEO status: **PASS FOR HUMAN REVIEW**.

## GEO / answer-engine review

- The opening answer is self-contained.
- Important entities are explicit: Regulation (EU) 2023/2419, EU organic logo, Skal, NVWA, FEDIAF.
- Threshold, date and scope are attributable in the body.
- “what it does / does not prove” structure reduces ambiguous extraction.
- Sources are attached near claims rather than hidden in a generic source dump.
- No unsupported numerical or health claim was introduced.

GEO status: **PASS FOR HUMAN REVIEW**.

## Editorial QA / AI-slop review

The new article was structured from the persisted brief rather than from a generic guide template.

Checked for:

- commercial throat-clearing;
- repeated “best/healthy/premium” framing;
- symmetric filler sections;
- fake experience;
- source dumping without attribution;
- automatic equation of organic/natural with health superiority;
- unnecessary FAQ padding;
- templated affiliate CTA.

Result: **PASS FOR HUMAN REVIEW**. Final human read remains required.

## Internal linking

Repository-observable links are implemented based on the reader's next question. The specialized third-party `internal-linking-audit` expects a GSC MCP that was not available in this task, so no GSC orphan/striking-distance findings were invented.

Status: **PASS WITH EXPLICIT MCP LIMITATION**.

## Technical status

- Dedicated guide content stylesheet added: `assets/guide-content.css`.
- Skill provenance: **PASS** — PR #4 workflow run `34824603666` successfully fetched/materialized every pinned public skill and reference.
- Guide HTML structure: **PASS**.
- Repository checks: **PASS**.
- Build: **PASS**.

## Final status

- Fact-check: PASS
- Brief adherence: PASS FOR HUMAN REVIEW
- Editorial QA: PASS FOR HUMAN REVIEW
- SEO: PASS FOR HUMAN REVIEW
- GEO: PASS FOR HUMAN REVIEW
- Internal linking: PASS WITH MCP LIMITATION
- Technical/provenance gate: PASS
- Indexation: `noindex,follow`

**READY_FOR_HUMAN_VALIDATION**
