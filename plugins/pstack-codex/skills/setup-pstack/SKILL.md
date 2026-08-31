---
name: setup-pstack
description: Configure pstack's Codex custom agents, model inheritance, reasoning effort, and concurrency. Use for setup-pstack, configure pstack models, verify pstack agents, or change which Codex model handles pstack roles.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.

# Setup pstack for Codex

Configure Codex-native custom agents. Never write Cursor rules or invent model
slugs.

## Workflow

1. Inspect `.codex/agents/` and `.codex/config.toml` in the active repository,
   plus the user's Codex config only when personal configuration is requested.
2. Enumerate models and reasoning levels currently exposed by Codex. Treat that
   live list as authoritative.
3. Show the two upstream roles (`poteto-agent`, `comment-sicko`) and any local
   reviewer roles with their current model, effort, and sandbox values.
4. Default to inheriting the parent model and effort. Add explicit values only
   when the user requests a stable role mapping and the combination is supported.
5. Keep reviewers read-only. Do not weaken the parent permission or approval
   boundary in a custom agent file.
6. Validate every TOML file and report whether a new Codex task is required to
   load the changes.

For global defaults, use supported `[agents]` keys in Codex config. For
role-specific behavior, use standalone `.codex/agents/<agent>.toml`. Do not
create `.cursor/rules`, use Cursor model IDs, or silently substitute models.

Optionally offer `create-verification-skill` when the project lacks a real
surface-level verification harness.
