# Reviewer Lenses

## Skeptic

Challenge correctness and completeness.

- Find inputs, states, sequences, and error paths that break the intent.
- Identify races, ordering assumptions, silent fallbacks, and unproven claims.
- Distinguish component checks from proof of the real terminal path.
- Require a concrete failure scenario and the cheapest executable verification.

## Architect

Challenge structural fitness.

- Trace ownership, boundaries, callers, data flow, and authority flow.
- Find coupling, leaked responsibility, invalid state models, and lifecycle gaps.
- Test assumptions about scale, concurrency, retries, and partial completion.
- Prefer a root-cause correction over a guard that hides the symptom.

## Minimalist

Challenge necessity and complexity.

- Find abstractions, configuration, compatibility paths, or orchestration that
  do not serve the stated intent.
- Ask what can be deleted while keeping the outcome.
- Separate required scope from adjacent hardening.
- Reject complexity justified only by hypothetical future use.
