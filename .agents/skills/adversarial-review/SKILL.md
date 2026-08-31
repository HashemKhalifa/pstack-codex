---
name: adversarial-review
description: Run a read-only adversarial review of a diff, branch, exact commit, plan, or evidence packet through independent skeptic, architecture, and minimalism lenses. Use when the user asks for an adversarial review, red-team review, independent challenge, or wants reviewers to try to break a proposed change. Do not use this skill to edit code, merge, deploy, or grant acceptance authority.
---

# Adversarial Review

Challenge whether the reviewed artifact achieves its stated intent. Produce a
synthesized, evidence-backed review. Do not change the artifact.

This is a Codex-safe fork of `poteto/noodle`'s adversarial-review skill. The
upstream cross-model CLI requirement was replaced with native Codex subagents
because unattended `claude -p` or `codex exec` calls are not portable and can
violate repository model, quota, and audit policy.

## 1. Freeze scope and intent

State:

- the exact review target, including commit SHA or working-tree scope;
- the author's intended outcome;
- the applicable repository rules and acceptance boundary;
- evidence that is available and evidence that is missing.

If the target changes materially, stop and restart the review against the new
target. Never treat a review of stale bytes as current.

## 2. Load the review frame

Read [references/principles.md](references/principles.md) and
[references/reviewer-lenses.md](references/reviewer-lenses.md). Apply only the
principles relevant to the target.

Choose the smallest useful panel:

- Narrow, low-risk change: Skeptic.
- Multi-file or boundary change: Skeptic and Architect.
- Cross-cutting, authority-sensitive, or large change: Skeptic, Architect, and
  Minimalist.

## 3. Dispatch independent read-only reviewers

Use native Codex subagents when available. Prefer the project custom agents
`pstack_skeptic`, `pstack_architect`, and `pstack_minimalist`. If a named agent
is unavailable, use a default read-only subagent with the full corresponding
lens in its prompt.

Give every reviewer the same frozen target and intent. Keep their contexts
independent. Require concrete findings with file and line references, a failure
scenario, severity, and a verification route. Reviewers must not edit files,
run destructive commands, publish, merge, deploy, or mutate external systems.

Do not silently replace a failed reviewer. Record missing or incomplete lanes
as review limitations.

## 4. Verify findings

Deduplicate overlapping findings. Check each claimed path against the reviewed
artifact. Reject findings that are style preferences, rely on stale bytes, or
cannot name a concrete failure mode.

Severity:

- `high`: correctness, security, data-loss, authority, or contract failure that
  blocks the reviewed outcome;
- `medium`: material defect or test gap that should be fixed before adoption;
- `low`: bounded hardening or maintainability concern.

## 5. Render the review

Use [references/verdict-format.md](references/verdict-format.md).

Use these verdicts:

- `REVIEW_CLEAN`: no verified high or medium findings;
- `FINDINGS`: at least one verified high or medium finding;
- `INCONCLUSIVE`: required scope, evidence, or reviewer output is unavailable.

This verdict is advisory. It does not replace a repository-required independent
acceptance audit and grants no deployment, runtime, scientific, broker, order,
or trading authority.
