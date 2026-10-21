#!/usr/bin/env python3
"""Site command adapter; editorial gates remain in the shared Guide agents."""
from pathlib import Path
import subprocess

if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    raise SystemExit(subprocess.call(
        ['node', str(root / 'scripts/check_guides.mjs'), '--publish'], cwd=root
    ))
