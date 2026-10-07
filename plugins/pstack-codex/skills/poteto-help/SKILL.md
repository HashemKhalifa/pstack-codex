---
name: poteto-help
description: Guide users through pstack setup, choose a skill or playbook, and diagnose a workflow that drifted. Use for poteto-help or questions about using pstack.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.

# Poteto help

Answer the help question without starting an implementation. If the user asks
for work, route to poteto-mode and execute within the existing authorization.
Read the selected skill before explaining it. Link the public file under
https://github.com/HashemKhalifa/pstack-codex/tree/main/plugins/pstack-codex.

## Setup

Use setup-pstack to inspect a trusted project's five native agent roles and the
live model and effort list. Inherit the parent by default. Validate TOML and run
smoke_agents.py before calling setup complete. Installation does not create
model overrides, scheduler jobs, or global standing instructions.

## Choose a workflow

| Request | Skill or playbook |
|---|---|
| Investigate, build, and prove a non-trivial change | poteto-mode |
| Explain current code or historical decisions | how or why |
| Design caller usage and ownership | architect |
| Compare isolated candidates | arena |
| Cover independent checks or race workers | swarm |
| Challenge a frozen diff | interrogate or adversarial-review |
| Check effects outside a diff | blast-radius |
| Validate a performance claim | benchmark-checklist |
| Stop a recurring mistake structurally | correct |
| Capture personal working conventions | automate-me |
| Capture named maintainers' public engineering conventions | automate-maintainer |
| Discover a repository's active core contributors | automate-team |
| Resume recent work | recall or the session-pickup playbook |
| Get PR checks and threads to merge-ready | babysit playbook |
| Land an explicitly authorized verified chain | shipping playbook |

Architect stops at a design unless implementation is requested. Babysit does
not grant merge authority. Review findings do not grant acceptance authority.
Each writer needs its own worktree; spawning alone does not isolate files.
A blocked verification lane is a gap, not a pass. Use supported automation only
for an explicitly requested future wakeup, and report unavailable capabilities.

Give one concrete example prompt and the relevant source link. Keep the answer
short unless the user requests a full map.
