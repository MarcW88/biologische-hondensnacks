#!/usr/bin/env python3
"""Check original package identity, supplemental dependencies, routing and commands."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'scripts/check_shared_routing.py')],check=True)
lock=json.loads((ROOT/'.agents/support-files.lock.json').read_text())['files']
errors=[]
for name,item in lock.items():
    p=ROOT/name
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256']:errors.append('missing/modified support: '+name)
for p in (ROOT/'.agents/skills').glob('*/SKILL.md'):
    for name in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)',p.read_text()):
        if '://' not in name and not (p.parent/name).exists():errors.append(f'{p.relative_to(ROOT)}: missing {name}')
for name in ['scripts/internal_link_audit.py','validate_guide_quality.py','validate_usage_workflow.py','validate_brands.py','validate_comparisons.py','validate_deal_workflow.py','validate_trust_workflow.py']:
    if not (ROOT/name).is_file():errors.append('missing workflow command: '+name)
if errors:raise SystemExit('\n'.join(errors))
print(f'PASS: {len(lock)} original support files, linked resources and active command entry points.')
print('External services still require their own credentials; this is not an editorial or publication approval.')
