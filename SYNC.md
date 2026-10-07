# Classified pstack sync

The baseline is Cursor pstack 0.15.5 at `12d587dfb20741cafc376c42c696c5f6e2a64487`, compared with the previous imported 0.14.5 commit `fd878692de15a3069c21c8f429eb0b9f2fe178fa`. This is a classified workflow sync, not byte-for-byte source parity. `UPSTREAM.json` records all 104 changed source paths and their decisions.

## Bounded upstream changes

| Affected paths under plugins/pstack-codex | Behavior | Validation |
| --- | --- | --- |
| skills/show-me-your-work/{SKILL.md,scripts/log.sh} | Append headers without truncating an existing trail; sanitize spreadsheet cells; supersede incorrect rows; audit only the current run's stretches. | log.test.mjs checks append preservation, empty-file headers, spaces, and formula escaping. |
| skills/swarm/SKILL.md | Results bind to exact target SHAs and measurement methods; retry a missing receipt once; remaining gaps cannot count as pass. | Native forward evaluation checks missing receipts and concurrency waves. |
| skills/poteto-mode/playbooks/{autopilot-full,autopilot-stack,shipping,babysit,opening-a-pr}.md | Code-ready fix rounds, independent live/audit verification, current patch verdicts, bottom-first stack preparation, confirmed merges, and forge-specific state. | Native scenario evaluation checks unauthorized merges, shared worktrees, stale patch verdicts, pending checks, and build-noise reuse. |
| skills/poteto-mode/playbooks/{multi-phase-plan,performance}.md and scripts/check-plan.mjs | Live evidence and fair trunk/head measurement; concrete perf budgets when trunk lacks the feature; plan checks accept inherited or configured worker models. | check-plan.test.mjs populates the actual shipped skeleton and rejects missing gates, evidence, placeholders, and cadence. |
| skills/principle-{attack-the-premise,test-behavior-not-implementation}/SKILL.md | Challenge a repeatedly failed premise; test observable behavior. | Structural skill discovery and native scenario evaluation. |
| skills/architect/references/*, skills/why/*, skills/blast-radius/SKILL.md, skills/technical-writing/SKILL.md | Schema-first design, decision lineage, downstream impact, and concise evidence-aware explanations. | Structural resource validation and relative-link review. |
| skills/how/references/{critic-prompt,critique-rubric}.md | Remove obsolete critique resources and validator expectations. The native How entrypoint already avoids critique. | Structural validator expects nine required upstream resources. |

## Selected ScriptedAlchemy additions

Source revision `c25afa251f1513b0b28cc089294d468c5e350444` is pinned separately. Later Cursor changes are not implied to be fully imported.

| Addition | Selection |
| --- | --- |
| automate-maintainer, automate-team | Mine repository-scoped public or authorized evidence into convention modes, retain attribution and uncertainty, and validate generated workflows. |
| benchmark-checklist, principle-explain-the-number | Keep benchmark methodology and units explicit; ground numerical choices in evidence. |
| correct | Verify a suspected mistaken premise before preserving or changing it. |
| poteto-help | New native help entrypoint inspired by the fork, matching this repository's actual skills and five-agent setup. |
| worktree-audit.sh | Port read-only cached-ref auditing, space-safe paths, conservative ancestry classification, and preservation of untracked data. Omit private session scanning. |
| check-plan.test.mjs, log.test.mjs | Adapt runnable behavior tests to this layout and the 0.15.5 cadence. |

The fork's loopback Codex bridge and Benny ledger are not installed. They add separate services, state, dependencies, and setup obligations without a demonstrated requirement here. Its model defaults, two global-agent installation, global role document, and guides that describe that setup are also excluded.

## Codex boundaries

The five existing agent TOMLs remain intact. Setup continues to enumerate live model and effort support, inherit parent configuration by default, and require all five live smoke probes. Optional budget preferences apply only to explicit supported overrides and preserve uncapped choices for reruns.

Cursor Task flags, automatic cloud VM isolation, Cursor role rules, and built-in goal/loop commands are replaced with native agents, explicit worktree ownership, recorded objectives, and actual available automation capabilities. Future scheduling requires an explicit request. Trail recovery uses run-scoped conversation evidence or TraceDecay, never a private session crawl. Merge and draft-state changes follow existing user and repository authorization.

## Repeatable validation

```sh
python3 -m unittest discover -s plugins/pstack-codex/scripts -p 'test_*.py'
python3 plugins/pstack-codex/scripts/validate_port.py
python3 plugins/pstack-codex/scripts/check_upstream.py /path/to/cursor-plugins
node --test plugins/pstack-codex/skills/poteto-mode/scripts/check-plan.test.mjs plugins/pstack-codex/skills/poteto-mode/scripts/worktree-audit.test.mjs plugins/pstack-codex/skills/show-me-your-work/scripts/log.test.mjs
cd plugins/pstack-codex/skills/poteto-mode/scripts
bun install --frozen-lockfile
bun test orch watch-pr
bun run typecheck
```

Run `smoke_agents.py` from a trusted checkout in a fresh native Codex task. A passing historical receipt is not proof that another installation has loaded the agents. Plugin updates become available after installation/update and a new task reload.
