---
name: automate-me
description: Create or update a personal Codex mode skill from recurring, evidence-backed working preferences. Use for automate me, create my mode skill, update my mode skill, or turn my working style into a reusable Codex skill.
---

> Codex port: Read [../../CODEX_PORT.md](../../CODEX_PORT.md) before following this workflow. The port contract overrides host-specific mechanics in this file.

# Automate me

Create one focused `<handle>-mode` skill through Codex `skill-creator`.

1. Look for an existing mode under repository `.agents/skills/` and personal
   `~/.agents/skills/` locations. Update an existing skill unless the user asks
   to replace it.
2. Use the `recall` workflow and TraceDecay session search for recent evidence.
   Do not scan unrelated projects or private Cursor transcript folders.
3. Promote a preference only when it recurs across sessions or the user states
   it directly. Treat one-off behavior as weak evidence.
4. Ask a small number of questions only for genuine preference choices that
   evidence cannot settle.
5. Invoke Codex `skill-creator` to draft, validate, and evaluate the skill.
   Place project skills under `.agents/skills/<handle>-mode/` unless the user
   requests personal scope.
6. Apply `unslop` without removing examples, boundaries, or trigger language.
7. Run paired evals when behavior is objectively testable. For subjective tone,
   generate the review viewer and ask the user for a vibe check.

Do not create a PR, push, or merge unless the user explicitly requests it.
Do not store secrets or transient task state in the mode skill.
