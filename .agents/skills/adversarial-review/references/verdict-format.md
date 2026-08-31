# Verdict Format

```md
## Intent
<stated outcome and exact target>

## Verdict: REVIEW_CLEAN | FINDINGS | INCONCLUSIVE
<one-line judgment>

## Verified findings
1. **[severity] Title** (`file:line`)
   - Failure scenario: <what breaks>
   - Lens: <reviewer>
   - Evidence: <what was checked>
   - Recommendation: <bounded action>

## Cleared challenges
- <important risk checked and disproved>

## Review limitations
- <missing evidence, scope, or reviewer lane>

## Lead judgment
- Act now: <accepted findings>
- Future hardening: <real but out-of-scope concerns>
- Dismissed: <false positives and why>

## Authority boundary
<what this review does not authorize>
```
