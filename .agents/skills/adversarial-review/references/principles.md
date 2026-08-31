# Review Principles

- **Foundational thinking.** Check whether the data model and ownership shape
  match the real access and lifecycle patterns.
- **Boundary discipline.** Validate external data and authority at boundaries;
  keep internal logic typed and explicit.
- **Subtract before adding.** Remove obsolete paths and speculative machinery
  before adding new layers.
- **Make operations idempotent.** Retries and partial prior runs should
  converge safely.
- **Separate shared state.** Prefer isolated ownership before locks or
  serialized coordination.
- **Prove it works.** Verify the real entrypoint, authoritative input, final
  artifact, verifier, and acceptance gate. Compilation and self-report are
  proxies.
- **Fix root causes.** Reproduce and trace the failure to the owning boundary;
  do not silence symptoms with guards.
- **Guard context.** Keep raw exploration in reviewer lanes and return concise
  evidence to the lead.
- **Respect authority.** Read-only review does not grant implementation,
  deployment, runtime, merge, broker, order, scientific, or trading authority.
