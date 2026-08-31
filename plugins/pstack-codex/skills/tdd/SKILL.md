---
name: tdd
description: Apply focused red-green TDD to a bug or behavior change with an executable
  local test target. Use when the user asks for TDD, a failing regression test, red-green
  evidence, or when repository rules require TDD for the touched path.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.


# pstack TDD

1. Identify intended behavior, current behavior, and the nearest observable
   terminal boundary.
2. Add the smallest focused test that fails for the intended reason.
3. Run it before production edits and preserve the RED evidence.
4. Make the smallest production change that satisfies the behavior.
5. Rerun the focused test and preserve the GREEN evidence.
6. Select nearby validation from dependency and affected-test evidence.

Do not weaken assertions to fit the implementation. If a failing test is not
practical, explain why before editing and use the closest executable check.
Repository-specific Rust, Go, risk, and trading TDD rules remain mandatory.

Report the exact RED, GREEN, nearby validation, and anything not run.
