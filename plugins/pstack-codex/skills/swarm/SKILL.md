---
name: swarm
description: Fan out N parallel workers, drain them, and return one report. Use for
  /swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.

# Swarm

Fan out N parallel native Codex workers. They may cover separate slices, race the same brief, or mix both. The parent waits, aggregates, and returns one report.

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive it from the shape. N is total workers, not the native concurrency limit.
4. Use the configured native agent role and inherit the parent model and effort by default. A requested model race may override only with combinations verified by live Codex enumeration. Omit unsupported model or effort arguments. A rejected override is a capability failure, not permission to invent another slug. Report the limitation and preserve the required coverage.
5. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result.

## Phase B: Fan out

Spawn through the available native agent tool using the configured `poteto-agent` role. Respect the tool's concurrency ceiling and dispatch additional workers in waves. Drain each wave before launching another. Do not use Cursor Task flags or assume a private cloud VM.

For a non-default branch, prepare an isolated worktree at the brief's exact SHA and give the worker its absolute path. Read-only lanes may share immutable inputs, but separate outputs and stateful runtime resources.
Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and rerun that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

Keep a compact result table, one-line evidenced issues, and explicit gaps or dropouts.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used.
