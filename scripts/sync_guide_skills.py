#!/usr/bin/env python3
"""Validate and materialize the pinned third-party skills used for /gidsen/.

This script is orchestration/verification code, not an editorial skill. It refuses
custom or floating skill sources and downloads only immutable GitHub commit URLs.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / ".agents" / "guide-skills.lock.json"
REQUIRED = {
    "seo-technical",
    "seo-content-audit",
    "seo-keyword",
    "seo-onpage",
    "seo-geo",
    "fact-check",
    "content-brief-authoring",
    "content-and-copy",
    "editorial-qa",
    "internal-linking-audit",
    "humanizer",
    "general-writing",
    "writing-cadence",
    "non-autoregressive-writing-pass",
    "better-usage",
    "academic-voice",
    "anti-ai-slop",
}
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def die(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def safe_rel(value: str, label: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        die(f"unsafe {label}: {value}")
    return path


def load_lock() -> dict:
    if not LOCK.exists():
        die(f"missing lockfile: {LOCK.relative_to(ROOT)}")
    data = json.loads(LOCK.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        die("unsupported guide skill lock schema")
    policy = data.get("policy", {})
    if policy.get("allow_custom_skills") is not False:
        die("allow_custom_skills must be false")
    if policy.get("allow_unpinned_refs") is not False:
        die("allow_unpinned_refs must be false")
    return data


def validate_entry(entry: dict) -> None:
    name = entry.get("name", "")
    repo = entry.get("repository", "")
    commit = entry.get("commit", "")
    root = entry.get("root", "")
    files = entry.get("files", [])

    if not name or not isinstance(name, str):
        die("skill without a valid name")
    if not REPO_RE.fullmatch(repo):
        die(f"{name}: invalid repository {repo!r}")
    if repo.split("/", 1)[0].lower() == "marcw88":
        die(f"{name}: custom MarcW88 repository is forbidden for guide skills")
    if not COMMIT_RE.fullmatch(commit):
        die(f"{name}: commit must be an immutable 40-char SHA")
    safe_rel(root, f"root for {name}")
    if not isinstance(files, list) or "SKILL.md" not in files:
        die(f"{name}: files must include SKILL.md")
    for rel in files:
        safe_rel(rel, f"file for {name}")


def raw_url(entry: dict, rel: str) -> str:
    root = str(safe_rel(entry["root"], "skill root"))
    rel_path = str(safe_rel(rel, "skill file"))
    return (
        "https://raw.githubusercontent.com/"
        f"{entry['repository']}/{entry['commit']}/{root}/{rel_path}"
    )


def fetch_text(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "biologische-hondensnacks-guide-skill-validator/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status != 200:
                die(f"upstream returned HTTP {response.status}: {url}")
            return response.read().decode("utf-8")
    except (urllib.error.URLError, UnicodeDecodeError) as exc:
        die(f"cannot fetch upstream {url}: {exc}")


def verify_skill_name(name: str, content: str, url: str) -> None:
    if not content.startswith("---\n"):
        die(f"{name}: upstream SKILL.md has no YAML frontmatter: {url}")
    match = re.search(r"(?m)^name:\s*['\"]?([^'\"\n]+)['\"]?\s*$", content)
    if not match:
        die(f"{name}: upstream SKILL.md has no name field: {url}")
    upstream_name = match.group(1).strip()
    if upstream_name != name:
        die(f"{name}: upstream name is {upstream_name!r}: {url}")


def destination(vendor_dir: Path, entry: dict, rel: str) -> Path:
    return vendor_dir / entry["name"] / Path(*safe_rel(rel, "destination").parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sync",
        action="store_true",
        help="download pinned upstream files into .agents/guide-vendor",
    )
    parser.add_argument(
        "--remote",
        action="store_true",
        help="verify every pinned upstream file is reachable even without --sync",
    )
    args = parser.parse_args()

    data = load_lock()
    entries = data.get("skills", [])
    if not isinstance(entries, list):
        die("skills must be a list")

    names = [entry.get("name") for entry in entries]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        die(f"duplicate skill entries: {', '.join(duplicates)}")

    missing = REQUIRED - set(names)
    extra = set(names) - REQUIRED
    if missing:
        die(f"missing required guide skills: {', '.join(sorted(missing))}")
    if extra:
        die(f"unexpected guide skills: {', '.join(sorted(extra))}")

    vendor_rel = data["policy"].get("vendor_directory", ".agents/guide-vendor")
    vendor_dir = ROOT / Path(*safe_rel(vendor_rel, "vendor_directory").parts)

    for entry in entries:
        validate_entry(entry)
        if not (args.sync or args.remote):
            continue
        for rel in entry["files"]:
            url = raw_url(entry, rel)
            content = fetch_text(url)
            if rel == "SKILL.md":
                verify_skill_name(entry["name"], content, url)
            if args.sync:
                target = destination(vendor_dir, entry, rel)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")
                print(f"SYNC {entry['name']}: {rel}")
            else:
                print(f"OK   {entry['name']}: {rel}")

    print(
        f"PASS: {len(entries)} guide skills are third-party, commit-pinned, "
        "and policy-complete"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
