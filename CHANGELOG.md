# Changelog

All notable changes to pstack-codex are documented here. Release versions and
notes are calculated from Conventional Commits and verified by semantic-release.

## 1.0.0 (2026-08-31)

### Features

- Port all 45 pstack skills to Codex-native skill packages.
- Add the adversarial-review skill with skeptic, architecture, and minimalism lenses.
- Register five custom Codex agents: `poteto-agent`, `comment-sicko`,
  `pstack_skeptic`, `pstack_architect`, and `pstack_minimalist`.
- Add marketplace installation, structural validation, isolated evals, and live
  persistent-parent agent smoke tests.
- Add semantic-release version verification, release notes, GitHub releases,
  contributor attribution, and pull-request validation.

### Bug Fixes

- Restore missing source references required by the ported skills.
- Translate Cursor-specific commands and assumptions to Codex-native behavior.
- Document and validate the Codex project-trust requirement for custom agents.
- Make custom-agent definitions self-contained and verify all named agents spawn.
- Replace ephemeral agent-smoke parents with durable Codex tasks.
- Align the changelog preset and accept generated and linked semantic-release headings.

### Contributors

- [Lauren Tan (@poteto)](https://github.com/poteto)
- [Cursor Agent (@cursoragent)](https://github.com/cursoragent)
- [Hashem Khalifa (@HashemKhalifa)](https://github.com/HashemKhalifa)

[1.0.0]: https://github.com/HashemKhalifa/pstack-codex/releases/tag/v1.0.0
