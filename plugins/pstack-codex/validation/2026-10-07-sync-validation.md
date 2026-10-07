# Classified sync validation

Runtime target commit: `a1d279dd0beda5e7b0730874d36da0f0c145932d`.
Native CLI: `codex-cli 0.159.3`.

| Gate | Outcome |
| --- | --- |
| Structural discovery | PASS, 53 skills and five agents |
| Python regression suite | PASS, 13 tests |
| Bundled orch/watch-pr suite | PASS, 52 tests |
| Strict helper typecheck | PASS |
| Published plan, log, worktree behavior | PASS, 11 Node tests |
| Bounded upstream inventory | PASS, all 104 changed source paths at 0.15.5 |
| Five-agent live smoke | PASS, exact child/parent sentinels for every native role |
| Release dry-run | PASS, calculates and verifies 1.1.0 on the proposed branch |
| Whitespace and relative resources | PASS; the source example URL placeholder is not a local resource |

The initial independent native review found stale generated plan paths, an unsafe copied VM-isolation claim, and no-op model-choice tests. All three were fixed. A focused recheck confirmed those corrections and independently reproduced rejection of a placeholder in the perf probe. Its remaining test-coverage finding was fixed by populating and mutating the actual perf probe, with an assertion that the intended command exists before mutation.

Live probes ran from the exact trusted checkout in fresh persistent native parent tasks, with read-only sandbox and strict configuration. Agent files, role permissions, and inherited model/effort settings remain unchanged. Command-line trust overrides alone did not activate project configuration discovery; the setup's documented exact-path trust requirement was applied. No extra role registry was needed.

The smoke receipt records the runtime target SHA. Later changes only tighten the perf test fixture and attach validation evidence; they do not change the tested runtime instructions or agent definitions. The CI run on the final PR head is the final structural/helper gate.

Git test fixtures used isolated Git configuration to avoid the user's global commit hooks. The worktree regression test covers canonical paths with spaces, cached-ref preservation, no fetch, and preservation of untracked files. Automation scheduling, live forge mutations, bridge/Benny installation, and cap writes were not exercised or claimed.
