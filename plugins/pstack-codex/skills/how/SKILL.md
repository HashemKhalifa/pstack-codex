---
name: how
description: Explain how a code path or subsystem works from the real entrypoint through
  state transitions and outputs. Use for how does this work, trace this subsystem,
  map the execution path, or investigate behavior before changing it. In TraceDecay-indexed
  projects, use graph context before text search.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.


# pstack How

1. Restate the question and identify whether it is narrow or cross-cutting.
2. In a TraceDecay-indexed project, invoke `tracedecay:using-tracedecay`, then
   route concepts to context, symbols to search, and call relationships to
   callers/callees. Do not begin with raw grep.
3. Trace the real flow from trigger to effect. Include data shapes, state
   transitions, boundaries, and error paths.
4. Verify surprising claims against source or executable behavior.
5. Return: overview, key concepts, step-by-step flow, file/symbol map, gotchas,
   and any evidence limitation.

Stay read-only unless the user also asked for a change.
