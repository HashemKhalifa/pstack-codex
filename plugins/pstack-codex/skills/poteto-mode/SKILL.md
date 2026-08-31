---
name: poteto-mode
description: Route a non-trivial engineering task through a rigorous, evidence-first
  Codex workflow. Use when the user says poteto-mode, pstack, go deep first, rigorous
  engineering workflow, or asks to investigate, design, implement, and verify a task
  with explicit authority boundaries. Do not trigger for casual questions or one-step
  formatting.
---

# Poteto Mode for Codex

Apply pstack's core idea: go deep enough to identify the real path, then make
the smallest change that proves the intended outcome.

Repository instructions and user authority always outrank this skill. This
fork never authorizes PR creation, merge, deployment, force-push, destructive
cleanup, external messages, broker actions, or trading.

Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before using any bundled
playbook or sibling skill.

## Start

1. State the intended outcome and current authority boundary.
2. Name the real terminal path: entrypoint, authoritative input, final
   artifact, verifier, and acceptance gate.
3. Choose one workflow below. Do not stack every workflow by default.
4. Track multi-step work in the repository's task ledger when required.

## Route

- Read-only code explanation or investigation: use `how` and the
  repository's semantic code-investigation workflow.
- New design crossing a boundary: use `architect`.
- Bug with a cheap local regression target: use `tdd`.
- Change-impact or test-selection question: use `blast-radius`.
- Diff, plan, or artifact challenge: use `interrogate` or the
  `adversarial-review` skill.
- Final prose cleanup: use `unslop` after preserving every material
  fact and caveat.

## Full upstream playbook inventory

The complete upstream resources are bundled under `playbooks/`, `references/`,
and `scripts/`. Route to the closest playbook after applying the Codex port
contract:

- investigation, bug fix, performance, hillclimb, runtime forensics, and trace
  forensics;
- feature, refactoring, prototype, visual parity, and authoring a skill;
- eval, babysit, shipping, autonomous run, orchestrate, autopilot full,
  autopilot stack, session pickup, pause safely, multi-phase plan, opening a
  PR, and worktree cleanup.

Playbook presence is not action authority. Cursor-only commands and external
writes must be translated or stopped per `CODEX_PORT.md`.

## Principles

- Model the domain before writing conditionals.
- Subtract obsolete paths before adding machinery.
- Validate at external and authority boundaries.
- Separate shared mutable state before adding coordination.
- Reproduce symptoms and fix the owning root cause.
- Sequence work into small units with executable evidence.
- Prove the real path, not a proxy, before reporting completion.
- Keep implementation, validation, deployment, runtime activation, outcome
  evidence, and operational authority separate.

## Delegation

Delegate only when the user or applicable project/skill instructions request
it and the lanes are independent. Give each writer exclusive file ownership.
Use read-only reviewers for challenge lanes. The lead verifies artifacts and
does not pass through a subagent's self-report as evidence.

## Finish

Report the outcome first, then:

- exact files or artifacts changed;
- RED and GREEN evidence when TDD applied;
- validation that ran and what did not run;
- unresolved findings and the next executable evidence;
- authority explicitly not granted.
