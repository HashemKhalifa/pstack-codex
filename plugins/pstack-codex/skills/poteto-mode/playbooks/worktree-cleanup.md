> Follow [the Codex port contract](../../../CODEX_PORT.md). Cleanup requires the user's matching authorization and exact target inspection.

### Worktree and simulator cleanup

1. Record disk usage, then run `scripts/worktree-audit.sh <repo>`. It reads worktree paths from Git with NUL-safe records, uses cached refs, and never fetches, deletes, or scans private sessions. The chat-evidence column is unknown unless separately established from an explicitly identified run.
2. Treat every bucket as review advice. `verify-ancestry` proves only ancestry against a cached trunk ref. It does not prove current usage, absence of ignored files, or authorization to delete. Verify current remote state separately when authorized. A merged PR does not prove later branch commits are preserved.
3. Inspect every candidate's absolute path, status, untracked and ignored files, branch tip, active processes, and ownership. Use current conversation or run-scoped TraceDecay evidence for active work. If usage is unknown, hold the tree. Do not crawl private session stores.
4. Hold all tracked changes, untracked files, ignored artifacts that may matter, and in-use worktrees. Untracked data is never disposable by inference. Present the exact proposed removal set and the evidence for each path before any required confirmation.
5. Remove only authorized, inspected, clean, unused worktrees with `git worktree remove <absolute-path>`. A refusal is a reason to inspect and hold, not to add `--force` or run recursive deletion. Keep branch refs unless their removal was separately authorized.
6. For simulator cleanup, inventory the exact device or runtime IDs and active usage first. Apply the same authorization and preservation gate; do not delete every simulator or clear unrelated application state by default.
7. Re-list worktrees and disk usage. Report space reclaimed, targets removed, and the reason for each held target.
