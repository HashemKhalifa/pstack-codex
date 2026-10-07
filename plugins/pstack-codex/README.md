# pstack-codex

A project-scoped Codex port of Cursor's complete pstack plugin, sourced from
`cursor/plugins` commit `12d587dfb20741cafc376c42c696c5f6e2a64487`
(upstream pstack version `0.15.5`).

Included inventory:

- all 53 marketplace skills and their bundled references, playbooks, scripts,
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
