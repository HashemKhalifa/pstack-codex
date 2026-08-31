# Codex Port Contract

Read this before following any pstack skill in this plugin. It overrides
host-specific mechanics in upstream skill text while preserving the workflow's
intent.

## Precedence and authority

1. The user's request, repository `AGENTS.md`, and applicable Codex skills
   outrank pstack instructions.
2. A terminal phrase such as "finish" or "do not stop" requires persistence;
   it never grants merge, deploy, external-write, destructive, broker, order,
   or trading authority.
3. Ask or stop when new authority is required. Do not infer permission from an
   upstream playbook.

## Host translation

- Cursor `Task` or `subagent_type` means native Codex subagents. Delegate only
  when the user or applicable project/skill instructions request it.
- Cursor `/skill-name` means invoke the matching Codex skill by name (for
  example `$skill-name`) when it is installed. Do not emit or simulate an
  unsupported slash command.
- Cursor Plan Mode means Codex Plan mode when available. Do not simulate a mode
  change in prose.
- Cursor `/loop` or cloud wake chains mean a Codex heartbeat automation only
  when the user explicitly asks to monitor, wait, or continue later.
- Cursor transcript paths mean TraceDecay session/message search in indexed
  projects. Never scan private host databases directly.
- Cursor `create-skill` means Codex `skill-creator`.
- Cursor browser or control skills mean the available Codex browser, Chrome,
  computer-use, or terminal tools selected for the real surface.
- Cursor model names and role configuration map to available Codex custom
  agents. Omit an unavailable model and inherit the parent rather than
  substituting silently.
- Graphite, Bugbot, and `cursor-team-kit` are optional external dependencies.
  If unavailable, use the repository's supported Git, review, and verification
  paths or report the missing capability.

## Safety translation

- PR creation, ready-state changes, merges, force-pushes, deployments, service
  restarts, external messages, and automation creation require an explicit
  matching user request.
- Destructive cleanup requires exact read-only target resolution and the
  confirmation required by the host and repository.
- Never use `git reset --hard`, discard unrelated work, or copy over a dirty
  checkout merely because an upstream playbook suggests it.
- Reviewers are read-only. Review findings do not grant acceptance or runtime
  authority.
- In authority-sensitive repositories, separate implementation, validation,
  deployment, runtime activation, outcome evidence, and operational authority.

## Unsupported behavior

If a workflow depends on a capability that Codex cannot represent honestly,
state the unsupported seam and preserve the nearest safe partial result. Do not
pretend the original guarantee was met.
