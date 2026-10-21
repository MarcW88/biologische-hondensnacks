# Shared editorial agents: one reference, separate site context

## What was wrong here

All 66 files from Bloc-notes numérique's `.agents/skills/` were already present
with identical bytes. However, `gidsen/AGENTS.md` explicitly prohibited the
original Guide orchestrators and routed work through a separate vendor workflow.
Identical installed files did not mean identical active agents.

Aspirateurs-chantier also has different Guide orchestrators: its analysis and
content SKILL files are not byte-identical to the current Bloc-notes originals.
They cannot both be called the same canonical version.

## Reference used for this site

Repository: `MarcW88/bloc-notes-numerique`.
Commit: `5b798c38648fdc32a9bbb0f2f6742b2dca9b7951`.
Inventory: `.agents/shared-agents.lock.json` (66 original shared files).

The original files are unchanged. Guide routing now names the original
`guide-analysis-workflow` and `guide-content-workflow`. The former vendor
orchestration files are compatibility pointers, not alternative methods.
Language, subject matter, site URLs, route mapping and command integration are
kept outside the original agents in `.agents/site-context.md`.

The source workflow invokes `python validate_guide_quality.py`. This site's
adapter forwards that command to its existing Guide HTML publish checker.
It is a site integration check, not an assertion that the two repositories'
HTML validators or editorial results are identical.

## Repeating this on a future site

1. Choose this exact reference commit, or explicitly request an updated version.
2. Copy the whole `.agents/skills/` package, including references, scripts and
   licenses; do not paraphrase, shorten, translate or rename its files.
3. Reuse the locked inventory and `scripts/sync_shared_agents.py` to verify bytes
   or copy them from a reference checkout. Keep site parameters in a separate
   context file and connect the site's `AGENTS.md` to the original agents.
4. Check that no more-specific `AGENTS.md` or older workflow overrides the route.
   Add the site's build/validator command adapters where the original workflow
   invokes project-specific commands; do not replace its editorial method.
5. For each content task, actually execute the original sequence and persist
   its real evidence, brief, draft and QA outputs. Copying files is not execution.

Commands, from the target site:

```sh
python scripts/sync_shared_agents.py --source /path/to/reference --sync
python scripts/sync_shared_agents.py --source /path/to/reference --check
```

Both commands require a source checkout at the locked commit. `--sync` copies
original bytes only; it does not generate replacements. CI also checks against
that reference and fails if a shared file is missing or altered.

A short request for future tasks can therefore be:

> Install and activate the shared agents from the locked Bloc-notes reference.
> Preserve every original file byte-for-byte; put only site context outside
> them. Verify identity and active routing before running the workflow.

## What has and has not been validated

PASS: all 66 original shared files match the reference. PASS: the existing HTML
checks pass for the 10 guides. No guide article was rewritten in this migration,
and no editorial PASS, search-performance improvement or successful execution
of the full content workflow is claimed. Older terse audit records remain
historical inputs; they are not substituted for new evidence and reviews.
