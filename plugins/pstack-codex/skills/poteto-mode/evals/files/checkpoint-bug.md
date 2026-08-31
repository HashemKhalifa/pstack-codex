# Synthetic checkpoint bug

Intent: resuming an interrupted importer must continue after the last durably
written record without duplicating it.

Observed behavior: after writing record 42 and persisting checkpoint `42`, a
restart imports record 42 again. `resumeFromCheckpoint()` returns the stored
index directly and the loop starts at that value.

Existing test surface: `resume.test.ts` has a cheap unit fixture for a stored
checkpoint and an output array. No production edit has been made.
