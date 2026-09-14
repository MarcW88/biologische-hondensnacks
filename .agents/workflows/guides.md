# Guide workflow — `/gidsen/`

This file is orchestration only. It is **not a skill** and must not contain a replacement methodology for any specialist skill.

## Non-negotiable provenance rule

Before auditing, creating, or rewriting a guide, run:

```bash
python scripts/sync_guide_skills.py --sync --remote
```

Only skills materialized under `.agents/guide-vendor/` from `.agents/guide-skills.lock.json` may be used for `/gidsen/` work.

- Custom skills are forbidden.
- Floating branches/tags are forbidden; every source is pinned to a 40-character commit SHA.
- A local `.agents/skills/...` file with the same skill name does **not** override the guide-vendor copy.
- If an upstream file cannot be fetched or its `name:` does not match the lockfile, stop. Do not silently fall back to a local custom skill.
- `internal-linking-audit` is optional because its upstream expects a specific GSC MCP. If that MCP is unavailable, use only the internal-link checks already present in `seo-onpage` and state the data limitation.

## Workflow order

### A. Diagnostic — before substantive rewriting

1. `seo-technical`
   - crawlability, indexability, canonical, sitemap, rendering, structured data and page-experience blockers;
   - distinguish blockers from nice-to-have technical work.
2. `seo-content-audit`
   - decide whether the current page should be kept, updated, merged, redirected or removed;
   - check overlap/cannibalisation with other `/gidsen/` pages and relevant category pages.
3. `seo-keyword`
   - confirm the primary query, secondary query family and actual intent;
   - do not invent search volumes or difficulty when no keyword data is available.
4. `seo-onpage` — baseline audit of the existing page.
5. `seo-geo` — baseline AI-search/GEO audit of the existing page.

The diagnostic output must state what is known, what is missing, and the smallest justified scope of change. A page is not deeply rewritten merely because it is short or old.

### B. Evidence — before and after drafting

Use `fact-check` for every externally verifiable claim that will survive into the final guide. For dog nutrition, health, allergies, digestion, puppy feeding, calorie/quantity guidance, organic certification or safety claims, prefer primary regulatory, veterinary, scientific or manufacturer documentation as appropriate. Do not turn general information into individualized veterinary advice.

Unknown or unsupported claims remain unknown, are qualified, or are removed. Model memory is never evidence.

### C. Writing and revision

Use the pinned writing package from `msimchowitz/writing-skills`:

1. `general-writing` as the editorial owner;
2. `humanizer` in its embedded mode;
3. `better-usage`, `academic-voice`, `writing-cadence`, and `non-autoregressive-writing-pass` only through the Humanizer/general-writing pipeline when those skills call them. Do not run them a second time merely to satisfy a checklist.
4. `anti-ai-slop` as a final, separate authenticity check after factual content is stable.

Writing rules:

- Preserve every supported fact and meaningful qualification.
- No invented experience, product testing, veterinarian quote, study, statistic or owner anecdote.
- No fixed word count, heading count, FAQ count, table quota, source quota or internal-link quota.
- Do not force every guide into the same section order.
- Answer the dominant reader question early when that improves clarity, but do not flatten the page into repetitive answer blocks.
- Keep Dutch natural and specific. Avoid translated French structures and generic affiliate-copy language.
- The guide must remain useful if every affiliate link disappears.

### D. Final quality gates

Run these after the final text is stable:

1. `fact-check` again on the final copy.
2. `seo-onpage` again on the final page.
3. `seo-geo` again on the final page.
4. `internal-linking-audit` only when its required MCP is available; otherwise use `seo-onpage` internal-link checks and record the limitation.
5. `anti-ai-slop` final check; if no notable tells exist, do not manufacture edits.
6. Repository checks:

```bash
python scripts/sync_guide_skills.py --remote
npm ci
npm run check
npm run build
```

A machine PASS means only that the detectable gates passed. It does not replace human editorial validation.

## Required guide deliverable

For each guide worked on, keep a concise audit record in `.content/guides/<slug>.md` with:

- URL / slug;
- primary query and intent;
- content-audit decision and rewrite scope;
- key evidence/sources and unresolved claims;
- SEO baseline findings;
- GEO baseline findings;
- material changes made;
- final fact-check status;
- final SEO/GEO status;
- internal-linking status or explicit MCP limitation;
- `READY_FOR_HUMAN_VALIDATION` only when no blocker remains.

This audit record is evidence of the workflow; it must not be copied into the public article.
