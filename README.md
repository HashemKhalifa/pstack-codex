# pstack-codex

[![CI](https://github.com/HashemKhalifa/pstack-codex/actions/workflows/ci.yml/badge.svg)](https://github.com/HashemKhalifa/pstack-codex/actions/workflows/ci.yml)
[![GitHub release](https://img.shields.io/github/v/release/HashemKhalifa/pstack-codex)](https://github.com/HashemKhalifa/pstack-codex/releases)
[![semantic-release](https://img.shields.io/badge/semantic--release-conventionalcommits-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

A complete Codex port of Cursor's verified pstack marketplace package, plus a
Codex-safe fork of `poteto/noodle`'s adversarial-review skill.

This repository contains:

- all 45 pstack skills and their bundled resources;
- the two upstream pstack subagents, converted to Codex custom-agent TOML;
- three additional read-only adversarial reviewer agents;
- the standalone `adversarial-review` skill;
- an explicit Codex capability and authority translation contract.

## Install the plugin

```sh
codex plugin marketplace add HashemKhalifa/pstack-codex
codex plugin add pstack-codex@pstack-codex
```

Start a new Codex task after installation so the skill catalog reloads.

## Use the custom agents

Codex custom agents are project-scoped and project `.codex/` layers load only
after the exact project is trusted. Clone this repository, mark its exact path
trusted when Codex prompts, and start a fresh task from the clone.

For manual configuration, add the destination's absolute path to
`~/.codex/config.toml`:

```toml
[projects."/absolute/path/to/project"]
trust_level = "trusted"
```

To use the agents in another repository, install the plugin, copy
`.codex/agents/*.toml` into that repository, trust the destination's exact
path, and start a fresh Codex task. The agent definitions are self-contained;
the plugin supplies the associated pstack skills.

The upstream roles are:

- `poteto-agent`
- `comment-sicko`

The port also includes `pstack_skeptic`, `pstack_architect`, and
`pstack_minimalist` as read-only review specialists.

## Standalone adversarial review

The Codex-safe `adversarial-review` fork lives at
`.agents/skills/adversarial-review/`. Codex discovers it automatically when
launched from this repository. Copy the directory into another repository's
`.agents/skills/` directory for project-local use.

## Verify the port

```sh
python3 plugins/pstack-codex/scripts/validate_port.py
python3 -m unittest discover -s plugins/pstack-codex/scripts -p 'test_*.py'
python3 plugins/pstack-codex/scripts/smoke_agents.py
```

The structural validator fails closed unless all 45 pstack skills, all five
agents, required upstream resources, Codex frontmatter, port-contract
references, and validation evidence are present. The smoke command is the live
terminal gate: every named agent must be discovered and successfully spawned.

## Releases and changelog

[`semantic-release`](https://github.com/semantic-release/semantic-release)
analyzes Conventional Commits merged to `main`, selects the next SemVer version,
updates [`CHANGELOG.md`](CHANGELOG.md), synchronizes the plugin manifest, tags
the release, and publishes the GitHub Release. See
[`RELEASING.md`](RELEASING.md) for the PR-only release workflow.

## Contributors

Upstream authors and Codex-port maintainers are recorded in
[`CONTRIBUTORS.md`](CONTRIBUTORS.md). The list is derived from the public Git
history of the exact imported paths.

## Safety and portability

Read [`plugins/pstack-codex/CODEX_PORT.md`](plugins/pstack-codex/CODEX_PORT.md).
It translates Cursor-specific model, subagent, slash-command, `/loop`,
Graphite, transcript, and UI-control behavior into Codex-native equivalents.
It does not grant merge, deployment, destructive, external-write, broker,
order, or trading authority.

## Provenance

- pstack source: `cursor/plugins` commit
  `fd878692de15a3069c21c8f429eb0b9f2fe178fa`, version `0.14.5`.
- adversarial-review source: `poteto/noodle` commit
  `82d2921c52370f23f29086de81ccfb600939c037`.
- upstream licensing: MIT. See [`LICENSE`](LICENSE).

This is an independent port, not an official Cursor or OpenAI repository.
