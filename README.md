# pstack-codex

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

Codex custom agents are project-scoped. Clone this repository and launch Codex
from it to use the bundled `.codex/agents/*.toml` definitions, or copy those
files into another repository's `.codex/agents/` directory.

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
python3 -m unittest plugins/pstack-codex/scripts/test_validate_port.py
```

The validator fails closed unless all 45 pstack skills, both upstream agents,
required upstream resources, Codex frontmatter, port-contract references, and
validation evidence are present.

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
