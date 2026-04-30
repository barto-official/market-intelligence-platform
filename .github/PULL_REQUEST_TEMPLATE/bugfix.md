## Bug Summary

<!--
Short description of the bug in user/system terms.

Example:
"Fix crash when creating a user without a profile photo."
-->

## Context / Links

<!--
Background and references:

- Links to issues / tickets / incident reports (e.g. Fixes #123)
- When did this regress? Known versions affected?
-->

## Root Cause Analysis

<!--
What was the actual root cause?

- Logic error? Race condition? Missing validation? Incorrect config?
- Why was this not caught earlier (if known)?
-->

## Fix Description

<!--
What is the fix, at a high level?

- How does this change address the root cause?
- Why is this approach correct and robust?
-->

## Scope / Impact

<!--
Who is affected and how?

- Affected components / services
- User-facing impact (error, wrong behaviour, data loss)
- Environments impacted: dev / staging / production
-->

## Regression Risk

<!--
Where could this fix cause new issues?

- Other code paths sharing this logic
- Performance implications
- Boundary / edge cases that are now different
-->

## Reproduction & Verification

### Steps to Reproduce (Before Fix)

<!--
Clear, minimal steps to reproduce the bug on the previous version.
-->

### Steps to Verify (After Fix)

<!--
Exact steps or test cases used to confirm behaviour is now correct.
Include commands and/or manual steps.
-->

## Testing

- [ ] New unit tests added
- [ ] Existing tests updated
- [ ] Integration / end-to-end tests run
- [ ] Manual verification performed

**Details:**

<!--
E.g.
- `pytest tests/foo/test_bar.py::TestBug123`
- Manual: follow "Steps to Verify" above in staging
-->

## Observability & Follow-up

<!--
Monitoring and longer-term actions.

- Metrics / logs / alerts updated?
- Any follow-up tasks (e.g. add regression test suite, refactor, write RCA doc)?
-->

## Checklist

- [ ] Root cause is clearly documented
- [ ] Fix is minimal and targeted (no unrelated changes)
- [ ] Regression tests added or expanded
- [ ] No secrets or sensitive data committed
- [ ] Bug is linked to issue / incident (e.g. Fixes #123)

## Documentation

<!--
List documentation updates required and their status.
-->

Does this PR change any of the following?

- [ ] Public APIs or contracts
- [ ] Error handling or failure modes
- [ ] Configuration or defaults
- [ ] Performance characteristics
- [ ] Operational behavior

Documentation updates:

- [ ] Docstrings updated
- [ ] Reference docs updated
- [ ] Guides/runbooks updated
- [ ] No documentation changes required (explain below)

Explanation:
