---
name: architect
description: Design types, ownership, signatures, and module boundaries before implementation.
  Use for architect this, design this integration, choose a data model, or non-trivial
  code that crosses a function, service, storage, or authority boundary.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.


# pstack Architect

1. Ground the existing path with `pstack-how` and semantic graph evidence.
2. Write the caller's desired usage and authoritative data shape first.
3. Identify ownership, lifecycle, concurrency, error, and authority boundaries.
4. Produce at least two structurally distinct sketches only when the choice is
   genuinely open. Compare interface depth, state validity, and testability.
5. Choose the smallest design that fully meets the current requirement.
6. Define the executable RED that proves the missing terminal boundary before
   implementation begins.

Do not implement unless the user's request includes implementation. Do not add
compatibility layers or speculative configuration when the repository does not
require them.

Return the caller usage, type/data sketch, module map, rejected alternative,
chosen rationale, terminal-path checklist, and validation plan.
