---
name: setup-pstack
description: Configure pstack's Codex custom agents, model inheritance, reasoning effort, and concurrency. Use for setup-pstack, configure pstack models, verify pstack agents, or change which Codex model handles pstack roles.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.

# Setup pstack for Codex

Configure Codex-native custom agents. Never write Cursor rules or invent model
slugs.

## Workflow

1. Confirm the active repository's exact absolute path is trusted. Codex skips
   project `.codex/` layers, including custom agents, for untrusted projects.
   If it is not trusted, stop and ask the user to trust it through Codex or add
   the exact path under `[projects]` with `trust_level = "trusted"` in the user
   config.
2. Inspect `.codex/agents/` and `.codex/config.toml` in the active repository,
   plus the user's Codex config only when personal configuration is requested.
3. Enumerate models and reasoning levels currently exposed by Codex. Treat that
   live list as authoritative.
4. Show all five roles (`poteto-agent`, `comment-sicko`, `pstack_skeptic`,
   `pstack_architect`, and `pstack_minimalist`) with their current model,
   effort, and sandbox values.
5. Default to inheriting the parent model and effort. Add explicit values only
   when the user requests a stable role mapping and the combination is supported.
6. Keep reviewers read-only. Do not weaken the parent permission or approval
   boundary in a custom agent file.
7. Validate every TOML file, start a fresh task, and run
   `plugins/pstack-codex/scripts/smoke_agents.py`. Do not call setup complete
   until all five named agents spawn successfully.

For global defaults, use supported `[agents]` keys in Codex config. For
role-specific behavior, use standalone `.codex/agents/<agent>.toml`. Do not
create `.cursor/rules`, use Cursor model IDs, or silently substitute models.

Optionally offer `create-verification-skill` when the project lacks a real
surface-level verification harness.
