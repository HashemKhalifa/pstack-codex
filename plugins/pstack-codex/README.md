# pstack-codex

A project-scoped Codex port of Cursor's complete pstack plugin, sourced from
`cursor/plugins` commit `fd878692de15a3069c21c8f429eb0b9f2fe178fa`
(upstream pstack version `0.14.5`).

Included inventory:

- all 45 marketplace skills and their bundled references, playbooks, scripts,
  and assets;
- both upstream subagent roles, converted to Codex custom-agent TOML;
- three additional read-only adversarial reviewer agents used by the
  Codex-safe `adversarial-review` fork.

Project custom agents live in `.codex/agents/` because Codex custom agents use
standalone TOML rather than Cursor's plugin `agents/*.md` format.

Host-specific behavior is translated, not silently enabled. Read
[`CODEX_PORT.md`](CODEX_PORT.md) before any upstream workflow. It gates:

- Cursor `/loop`, cloud-agent, Bugbot, Graphite, and `cursor-team-kit` seams;
- transcript recall through TraceDecay instead of Cursor-private paths;
- PR, merge, force-push, reset, cleanup, deployment, external-write, and
  trading authority;
- unavailable model identifiers through inherited Codex model settings.

The fork preserves pstack's MIT license and complete skill inventory without
broadening the BOT repository's authority boundaries.
