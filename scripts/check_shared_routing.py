#!/usr/bin/env python3
"""Check shared-agent identity and coverage of the site's content entry points."""
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
subprocess.run(['python', str(ROOT / 'scripts/sync_shared_agents.py'), '--check'], check=True)
routing = json.loads((ROOT / '.agents/workflow-routing.json').read_text())
locked = json.loads((ROOT / routing['reference_lock']).read_text())['files']
errors = []
covered = set()
for route in routing['routes']:
    prefix = route['prefix'].strip('/')
    covered.add(prefix)
    entry = ROOT / prefix / 'AGENTS.md'
    if (ROOT / prefix).is_dir():
        if not entry.is_file():
            errors.append(f'{prefix}: missing active instructions')
        elif any(skill not in entry.read_text() for skill in route['skills']):
            errors.append(f'{prefix}: active instructions disagree with routing')
    for skill in route['skills']:
        if f'.agents/skills/{skill}/SKILL.md' not in locked:
            errors.append(f'{prefix}: {skill} is not an original shared agent')
for skills in routing['other_workflows'].values():
    for skill in skills:
        if f'.agents/skills/{skill}/SKILL.md' not in locked:
            errors.append(f'{skill}: not an original shared agent')
for directory in ROOT.iterdir():
    if directory.is_dir() and (directory / 'index.html').is_file() and directory.name not in covered:
        errors.append(f'{directory.name}: unrouted content directory')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(routing["routes"])} content mappings and design use original shared agents.')
print('Routing and identity only; no claim of editorial execution or publication approval.')
