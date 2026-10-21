#!/usr/bin/env python3
"""Verify or copy the pinned original agents without editing their contents."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / '.agents/shared-agents.lock.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, help='Local reference checkout at the pinned commit')
    parser.add_argument('--sync', action='store_true', help='Copy original bytes from the verified source')
    parser.add_argument('--check', action='store_true', help='Check the locked shared files (default)')
    args = parser.parse_args()
    lock = json.loads(LOCK.read_text())
    files = lock['files']
    if not files:
        parser.error('The locked shared agent set is empty')
    if args.sync and not args.source:
        parser.error('--sync requires --source; no generated substitute is allowed')
    for name in files:
        relative = Path(name)
        if relative.is_absolute() or '..' in relative.parts or not name.startswith('.agents/skills/'):
            parser.error(f'Invalid shared agent path: {name}')
    if args.source:
        source = args.source.resolve()
        commit = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
        if commit != lock['source_commit']:
            parser.error(f'Source commit mismatch: {commit}; expected {lock["source_commit"]}')
        tracked = set(subprocess.check_output(
            ['git', '-C', str(source), 'ls-tree', '-r', '--name-only', 'HEAD', '--', '.agents/skills'], text=True
        ).splitlines())
        if tracked != set(files):
            parser.error('Source file inventory differs from the locked original agent package')
        bad = [name for name, expected in files.items() if digest(source / name) != expected]
        if bad:
            parser.error('Source bytes differ from the pinned original: ' + ', '.join(bad))
        if args.sync:
            for name in files:
                target = ROOT / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source / name, target)
    bad = [name for name, expected in files.items() if digest(ROOT / name) != expected]
    if bad:
        for name in bad:
            print(f'FAIL: missing or modified shared file: {name}')
        return 1
    print(f'PASS: {len(files)} shared files exactly match {lock["source_repository"]}@{lock["source_commit"]}')
    print('File identity only: this does not certify skill execution or content quality.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
