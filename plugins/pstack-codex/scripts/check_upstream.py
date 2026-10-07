#!/usr/bin/env python3
"""Compare a supplied upstream checkout without fetching or copying files."""
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]


def changed_paths(checkout, base, head):
    result = subprocess.run(
        ["git", "-C", str(checkout), "diff", "--name-status", base, head, "--", "pstack"],
        check=True, capture_output=True, text=True,
    )
    return dict(line.split("\t", 1)[::-1] for line in result.stdout.splitlines())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path, help="existing cursor/plugins checkout")
    parser.add_argument("--head", help="optional next source revision to classify")
    args = parser.parse_args()
    source = json.loads((ROOT / "UPSTREAM.json").read_text())
    recorded = {row["source"]: row["status"] for row in source["delta_inventory"]}
    actual = changed_paths(args.checkout, source["previous_commit"], source["commit"])
    if recorded != actual:
        print("Pinned inventory mismatch")
        print(json.dumps({"missing_or_changed": {p: s for p, s in actual.items() if recorded.get(p) != s},
                          "extra": sorted(recorded.keys() - actual.keys())}, indent=2))
        return 1
    print(f"Pinned inventory verified: {len(actual)} source paths at {source['version']}")
    if args.head:
        changes = changed_paths(args.checkout, source["commit"], args.head)
        print(json.dumps({"from": source["commit"], "to": args.head,
                          "unclassified_changes": changes}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
