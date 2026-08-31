# Reviewer Prompt

Give each reviewer:

1. Exact frozen target and intent.
2. One complete lens from `reviewer-lenses.md`.
3. Relevant principles from `principles.md`.
4. Repository rules and explicit authority boundaries.
5. Available test, diff, runtime, or artifact evidence.

Require this output:

- numbered findings ordered by severity;
- `file:line` or exact artifact reference;
- concrete failure scenario;
- severity and confidence;
- cheapest verification or remediation route;
- explicit `NO FINDINGS` when the lane is clean.

The reviewer is read-only and must not edit, merge, deploy, or mutate external
state.
