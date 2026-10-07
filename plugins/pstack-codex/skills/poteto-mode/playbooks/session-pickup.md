> Follow [the Codex port contract](../../../CODEX_PORT.md). Native agents inherit parent configuration; independent writers require explicit worktrees. Merge, publication, and scheduling follow the user's authorization.

### Session pickup

**You own the resume point. Read the prior trail, don't redo it.**

1. Locate the prior trail from the current conversation, an explicitly identified prior run, its decision log, a pushed branch, or a run-scoped TraceDecay recall/export. Read metadata and recent decisions first. Do not glob or scan private session stores. Reduce a long identified trail in a read-only native agent and retain file and revision pointers. If history is unavailable, state that limit and recover only from repository evidence.
2. Reconstruct operational state. The branch and worktree, what already landed (`git log`, `git diff` against the base), the open todos, the decisions made. The prior trail is authoritative input. Resist the bias to re-derive it.
3. Diff done vs pending. Compare what shipped against what was planned, name the resume point, do not re-run the prior repro or redo completed work. A "let me verify from scratch" pass means you're treating the trail as untrustworthy when it's authoritative.
4. Route the remaining work to the matching playbook and pick the verdict: continue the execution, ship a finished recommendation, ratify or override a prior conclusion, or postmortem a failed run. The pickup playbook ends here. The routed playbook owns the rest.
5. Verify the inherited claims against the original goal on the real artifact (the **principle-prove-it-works** skill). A passing prior self-report is not the proof.

**Reply:** where the prior agent stopped, what you inherited vs redid (ideally nothing redone), the resume point, and the outcome.
