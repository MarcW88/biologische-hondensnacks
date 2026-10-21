# Visual redesign — 21 October 2026

The design audit skill remains unchanged. This is an explicitly requested
implementation following its audit, not an automatic behavior of that skill.

## Visible changes

- Homepage rebuilt as an editorial opening: compact masthead, a readable serif
  headline and an illustrative still life in place of the large CSS dog.
- Four repeated need cards replaced by numbered reading routes with clear rules
  and less decorative framing.
- Finder redesigned as a quiet sage section with two-column choices; the tested
  guide routing, announcements and focus behavior remain intact.
- Ingredient-reading feature uses a typographic label illustration instead of
  fictional product values. The guide feature and related reads use asymmetric
  magazine layouts rather than a succession of identical cards.
- Shared article styles have more deliberate title/metadata spacing, quieter
  side notes, less rounded framing, readable table styling and stronger reading
  rhythm. Directory pages use simple editorial lists.
- Shared header and footer use smaller typography and flatter shapes while
  preserving the site's logo, cream/forest/terracotta palette and local fonts.

The image in `assets/editorial/snack-still-life.webp` is illustrative, not a
product test or endorsement. Its visible caption and provenance README make
that distinction explicit. No publisher data or product experience was invented.

## Checks

- Build, 52-page static check, 10-guide check and 3-page Snacks check: PASS.
- `npm run test:design`: PASS; 104 route/viewports, no axe A/AA violations
  detected, 97 Finder test combinations and menu/focus checks.
- Supplemental reflow: 260 observations across five widths, no overflow.
- Playwright source script: desktop and mobile captures for all 52 routes.
- Authored main bodies outside the homepage and all imported skills unchanged.
- Screenshot review includes homepage, directory, guides, Snacks and needs pages
  in both desktop and mobile. Automated checks are not a WCAG certification.

The inherited Trust and French hreflang workflows still reference absent files;
these separate configuration defects do not block the Pages deployment. Draft
content and noindex remain as before.
