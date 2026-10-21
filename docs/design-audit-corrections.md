# Design audit corrections — 21 October 2026

These changes address the design review of commit a4c699d. The imported
`.agents/skills/site-design-review/` directory remains byte-for-byte unchanged.
The GitHub Actions integration is deliberately adapted to this site's actual
routes; it is not presented as an unchanged copy of the source site's CI.

## Changes

- Use accessible terracotta text/button and muted text tokens; keep light
  contrasting accents on dark green and dark labels on oat backgrounds.
- Remove the 10 px dead zone between desktop navigation links and dropdowns.
  Preserve mobile submenu controls, Escape dismissal, and restore button focus.
- Add a keyboard skip link with a page-specific URL (the site uses a base URL),
  explicit focus styles, keyboard-focusable named table regions, and reduced
  motion rules. Give the informative CSS illustration an image role.
- Turn the Finder into a transparent guide router: each goal has a relevant
  destination; needs and protein answers add existing explanatory pages. It
  explicitly does not claim to select safe products or give feeding advice.
  Focus moves to each next heading and step/result changes are announced.
- Remove unfinished destinations from shared header/footer links, and label
  unavailable directory choices as “In voorbereiding”. Replace the homepage's
  empty product-data mockup with the existing label-reading guide. Keep draft
  content and noindex; do not fabricate publisher data or imagery.
- Replace the unsubstantiated global trust banner with the site's actual concept
  status. Only the available chicken protein page is promoted on the homepage.
- Self-host the existing Lora/Manrope Latin webfonts, with their original SIL OFL
  licenses, instead of requesting fonts from Google at runtime.
- Preserve existing editorial directories during builds, including puppy and
  protein pages. Shared navigation synchronization still applies to all pages.
- Accept both existing source-section HTML conventions in the Snacks validator,
  while requiring an external reference link. The earlier two failures were
  caused by markup detection, not by missing source lists.
- Discover all actual routes in `scripts/visual-review.mjs` and pass them to the
  unchanged imported visual script. Run design regression checks in Actions and
  retain visual diagnostics as artifacts.

## Validation

- `npm run build`: PASS; a repeated build leaves all 52 HTML files byte-identical.
- `npm run check`: PASS, 52 pages.
- `node scripts/check_guides.mjs`: PASS, 10 guides.
- `npm run check:snacks`: PASS, 3 brief-backed pages.
- `npm run test:design`: PASS, 104 route/viewports, no axe A/AA violations
  detected; 96 desktop Finder combinations plus one mobile combination;
  focus, available destinations, skip-link URLs and dropdown traversal checked.
- Supplemental responsive probes: PASS, 260 route/width observations at 390,
  768, 920, 1024 and 1440 px, with zero document horizontal overflows.
- `npm run visual:site`: source script screenshots at 1440 × 1000 and 390 × 844.
- `git diff --check` and binary comparison of the imported design skill: PASS.
- Authored article main bodies and all three client redirects are preserved;
  changes to existing main bodies are limited to the homepage and four directory
  indexes. Header/footer and accessibility entry-point changes are shared.

These are local checks, not a production deployment or accessibility
certification. Chromium 153 was provided outside the repository because the
standard download endpoint returned an invalid archive in this environment.
Actions uses the normal Playwright installation on the GitHub runner.

## Remaining editorial work

The 18 provisional content/product pages and four incomplete publisher/trust
pages still require real content or owner-confirmed details. They have not been
filled with invented information. Product/ingredient photography and verified
product comparisons also remain to be supplied. Consequently, passing the
technical checks does not validate the complete site for publication.
