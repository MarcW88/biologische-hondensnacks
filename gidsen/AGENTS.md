# Guides — shared agents from Bloc-notes numérique

For every task under `/gidsen/`, read `.agents/site-context.md` from the
repository root and run the original shared workflows, without rewriting them:

- Audit, cluster audit and publication review:
  `.agents/skills/guide-analysis-workflow/SKILL.md`.
- Creation or rewriting, after the audit decision for an existing page:
  `.agents/skills/guide-content-workflow/SKILL.md`.

Read these files in full, then read and execute the specialist skills they call
from `.agents/skills/`. Their references are part of the copied agent package.
Verify the package first with `python scripts/sync_shared_agents.py --check`.

The only site adaptations are in `.agents/site-context.md`: Dutch language,
dog-snack subject, URL/path mapping, source types and existing build commands.
Do not create another method, shorten the chain or substitute vendor variants.
The old `.agents/workflows/guide-*.md` files are compatibility pointers only;
`.agents/guide-vendor/` is not the authoritative guide stack for this site.

Persist the actual audit, evidence, brief, drafting and review outputs. Never
claim that a skill ran or that a guide passed without its supporting outputs.
Keep existing noindex until explicit human approval and an indexation instruction.
