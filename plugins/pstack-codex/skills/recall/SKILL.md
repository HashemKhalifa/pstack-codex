---
name: recall
description: Reconstruct recent working context from Codex session history, durable project facts, and current repository state. Use for recall my work on X, catch me up, what have I been working on, or where did I leave off.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.

# Recall

Return a tight, current-state brief. Do not scan Cursor transcript directories
or private host databases.

1. Pin the topic, workspace, and time window. Default "recent" to seven days.
2. In a TraceDecay-enabled project, use
   `tracedecay:managing-session-context` and `tracedecay_message_search` for
   prior sessions. Use `tracedecay:project-memory` for durable facts.
3. Search only the active project unless the user explicitly names another
   registered project. Keep raw transcripts out of the main context.
4. Check surfaced branches, commits, tasks, PRs, and artifacts against current
   read-only state. History is not current truth.
5. Use `why` for source-control, issue, documentation, or incident context that
   is outside the user's own session history.

Output:

- **Capsule:** at most five bullets.
- **Threads:** one line each with an evidence-backed status.
- **Problems:** at most five recurring or unresolved issues.
- **Next move:** the single most useful safe action.

Cite session IDs or source artifacts. Sanitize private context before public
output.
