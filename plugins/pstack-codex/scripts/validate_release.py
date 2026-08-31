#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)


def extract_release_notes(changelog: str, version: str) -> str:
    date = r"\d{4}-\d{2}-\d{2}"
    bracketed_version = (
        rf"\[{re.escape(version)}\]"
        rf"(?:\([^)]+\))?"
        rf"(?: (?:- {date}|\({date}\)))?"
    )
    heading = re.compile(
        rf"^## (?:{bracketed_version}|{re.escape(version)} \({date}\))\s*$",
        re.MULTILINE,
    )
    match = heading.search(changelog)
    if not match:
        return ""
    next_heading = re.search(r"^## ", changelog[match.end() :], re.MULTILINE)
    end = match.end() + next_heading.start() if next_heading else len(changelog)
    return changelog[match.start() : end].strip() + "\n"


def set_manifest_version(root: Path, version: str) -> None:
    if not SEMVER.fullmatch(version):
        raise ValueError(f"version is not SemVer: {version}")
    manifest_path = root / "plugins" / "pstack-codex" / ".codex-plugin" / "plugin.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["version"] = version
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")


def validate_release(root: Path, tag: str) -> list[str]:
    errors: list[str] = []
    if not tag.startswith("v"):
        return ["release tag must start with v"]
    version = tag[1:]
    if not SEMVER.fullmatch(version):
        errors.append(f"release version is not SemVer: {version}")

    manifest_path = root / "plugins" / "pstack-codex" / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"invalid plugin manifest: {error}")
    else:
        manifest_version = manifest.get("version")
        if manifest_version != version:
            errors.append(
                f"manifest version {manifest_version!r} does not match tag {version!r}"
            )

    try:
        changelog = (root / "CHANGELOG.md").read_text()
    except OSError as error:
        errors.append(f"missing changelog: {error}")
    else:
        if not extract_release_notes(changelog, version):
            errors.append(f"changelog has no release section for {version}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a pstack-codex release")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument("--tag")
    operation.add_argument("--set-version")
    parser.add_argument("--notes-out", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    if args.set_version:
        try:
            set_manifest_version(root, args.set_version)
        except (OSError, json.JSONDecodeError, ValueError) as error:
            print(error)
            return 1
        print(f"plugin version set: {args.set_version}")
        return 0

    errors = validate_release(root, args.tag)
    if errors:
        for error in errors:
            print(error)
        return 1

    version = args.tag[1:]
    if args.notes_out:
        notes = extract_release_notes((root / "CHANGELOG.md").read_text(), version)
        args.notes_out.write_text(notes)
    print(f"release valid: {args.tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
