# Synthetic API rename proposal

Intent: rename internal field `filing_or_form4` to `event_source` because a new
caller also sends analyst notes.

Known shape:

- TypeScript writes the field into a JSON artifact.
- Python reads the artifact during offline evaluation.
- one external dashboard may consume the same JSON but no contract evidence is
  attached.
- the proposal adds `event_source` while retaining `filing_or_form4` as an
  indefinite compatibility alias.

No caller inventory, serialized fixture, or affected-test map is supplied.
