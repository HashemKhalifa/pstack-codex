---
name: blast-radius
description: Determine what a proposed or completed change can break beyond the diff
  and select affected tests from graph evidence. Use for blast radius, what could
  this break, impact analysis, affected callers, or verification without running the
  full suite.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.


# pstack Blast Radius

1. Resolve the changed symbols and behavior delta.
2. Use the repository impact workflow. In TraceDecay-indexed projects, invoke
   `tracedecay:assessing-impact` before guessing tests or running a broad suite.
3. Follow callers, serialized shapes, database/API contracts, feature flags,
   and cross-language readers that a simple text search misses.
4. Name the one or two facts the change's safety depends on.
5. Prove each fact as far as practical: source, impossible failure path,
   focused executable check, or live reproduction.
6. Mark any fact that did not reach executable proof as unproven.

Return the behavior delta, affected paths, proven safety facts, real risks,
cleared risks, focused tests, and remaining evidence gap.
