#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import tomllib


EXPECTED_SKILLS = {
    "architect",
    "arena",
    "automate-me",
    "blast-radius",
    "bro",
    "create-verification-skill",
    "figure-it-out",
    "how",
    "interrogate",
    "maintain-verification-skill",
    "make-bot-ui",
    "no-comments",
    "poteto-mode",
    "principle-boundary-discipline",
    "principle-build-the-lever",
    "principle-encode-lessons-in-structure",
    "principle-exhaust-the-design-space",
    "principle-experience-first",
    "principle-fix-root-causes",
    "principle-foundational-thinking",
    "principle-guard-the-context-window",
    "principle-laziness-protocol",
    "principle-make-operations-idempotent",
    "principle-migrate-callers-then-delete-legacy-apis",
    "principle-minimize-reader-load",
    "principle-model-the-domain",
    "principle-never-block-on-the-human",
    "principle-outcome-oriented-execution",
    "principle-prove-it-works",
    "principle-redesign-from-first-principles",
    "principle-separate-before-serializing-shared-state",
    "principle-sequence-verifiable-units",
    "principle-subtract-before-you-add",
    "principle-type-system-discipline",
    "recall",
    "reflect",
    "setup-pstack",
    "show-me-your-work",
    "swarm",
    "tdd",
    "teach",
    "technical-writing",
    "typescript-best-practices",
    "unslop",
    "why",
}

EXPECTED_AGENTS = {"comment-sicko", "poteto-agent"}
EXPECTED_EVIDENCE = {"validation/2026-08-31-pstack-script-tests.md"}
EXPECTED_UPSTREAM_RESOURCES = {
    "skills/architect/references/design-red-flags.md",
    "skills/architect/references/rationale-template.md",
    "skills/architect/references/runner-prompt.md",
    "skills/how/references/critic-prompt.md",
    "skills/how/references/critique-rubric.md",
    "skills/how/references/explainer-prompt.md",
    "skills/how/references/explorer-prompt.md",
    "skills/interrogate/references/code-quality-review.md",
    "skills/interrogate/references/lead-judgment.md",
    "skills/interrogate/references/reviewer-prompt.md",
    "skills/interrogate/references/rubric.md",
}
ALLOWED_FRONTMATTER = {"name", "description", "allowed-tools", "license", "metadata"}
FRONTMATTER_KEY = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s|$)")


def _frontmatter(skill_path: Path) -> tuple[dict[str, str], set[str], str]:
    text = skill_path.read_text()
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing closing frontmatter delimiter")

    values: dict[str, str] = {}
    keys: set[str] = set()
    for line in text[4:end].splitlines():
        match = FRONTMATTER_KEY.match(line)
        if not match:
            continue
        key = match.group(1)
        keys.add(key)
        values[key] = line.split(":", 1)[1].strip().strip("'\"")
    return values, keys, text[end + 5 :]


def validate_port(plugin_root: Path, repo_root: Path) -> list[str]:
    errors: list[str] = []
    skills_root = plugin_root / "skills"
    actual_skills = {
        path.name
        for path in skills_root.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    }
    if actual_skills != EXPECTED_SKILLS:
        errors.append(
            f"skill inventory mismatch: missing={sorted(EXPECTED_SKILLS - actual_skills)} "
            f"extra={sorted(actual_skills - EXPECTED_SKILLS)}"
        )

    for skill_name in sorted(EXPECTED_SKILLS & actual_skills):
        skill_path = skills_root / skill_name / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"{skill_name}: missing SKILL.md")
            continue
        try:
            values, keys, body = _frontmatter(skill_path)
        except ValueError as error:
            errors.append(f"{skill_name}: {error}")
            continue
        if values.get("name") != skill_name:
            errors.append(f"{skill_name}: frontmatter name is {values.get('name')!r}")
        unsupported = sorted(keys - ALLOWED_FRONTMATTER)
        if unsupported:
            errors.append(f"{skill_name}: unsupported frontmatter keys {unsupported}")
        if not values.get("description"):
            errors.append(f"{skill_name}: missing description")
        if "CODEX_PORT.md" not in body:
            errors.append(f"{skill_name}: missing Codex port contract reference")

    if not (plugin_root / "CODEX_PORT.md").is_file():
        errors.append("missing CODEX_PORT.md")

    missing_resources = sorted(
        resource
        for resource in EXPECTED_UPSTREAM_RESOURCES
        if not (plugin_root / resource).is_file()
    )
    if missing_resources:
        errors.append(f"missing upstream resources: {missing_resources}")

    missing_evidence = sorted(
        evidence for evidence in EXPECTED_EVIDENCE if not (plugin_root / evidence).is_file()
    )
    if missing_evidence:
        errors.append(f"missing validation evidence: {missing_evidence}")

    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"invalid plugin manifest: {error}")
    else:
        if manifest.get("name") != "pstack-codex":
            errors.append("plugin manifest name must be pstack-codex")
        if manifest.get("skills") != "./skills/":
            errors.append("plugin manifest must expose ./skills/")

    actual_agents: set[str] = set()
    for agent_path in sorted((repo_root / ".codex" / "agents").glob("*.toml")):
        try:
            agent = tomllib.loads(agent_path.read_text())
        except (OSError, tomllib.TOMLDecodeError) as error:
            errors.append(f"{agent_path.name}: invalid TOML: {error}")
            continue
        name = agent.get("name")
        if isinstance(name, str):
            actual_agents.add(name)
        for required in ("name", "description", "developer_instructions"):
            if not agent.get(required):
                errors.append(f"{agent_path.name}: missing {required}")

    missing_agents = sorted(EXPECTED_AGENTS - actual_agents)
    if missing_agents:
        errors.append(f"missing upstream Codex agents: {missing_agents}")

    return errors


def main() -> int:
    plugin_root = Path(__file__).resolve().parents[1]
    repo_root = plugin_root.parents[1]
    errors = validate_port(plugin_root, repo_root)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"pstack Codex port valid: {len(EXPECTED_SKILLS)} skills, {len(EXPECTED_AGENTS)} upstream agents")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
