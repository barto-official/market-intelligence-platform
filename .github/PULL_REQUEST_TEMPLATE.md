## Summary

<!-- 1–3 sentences describing what this PR does in plain language. -->

## Context / Motivation

<!--
Why is this change needed?

- What is the problem or user need?
- Link to issues / tickets / docs (e.g. Closes #123, Related to #456).
-->

## Scope of Change

<!--
What is included in this PR? Be specific but concise.

Examples:
- New endpoints / APIs
- New components / modules
- Config / infra changes
- Data model / schema changes
-->

## Design / Implementation Notes

<!--
Highlight key design decisions and non-obvious choices.

- Architecture / patterns used (e.g. new service, interface, abstraction)
- Important trade-offs (simplicity vs flexibility, performance vs readability)
- Any deviations from existing conventions (and why)
-->

## Risk & Impact Assessment

<!--
What can go wrong? Consider:

- Breaking changes for API clients or consumers
- Data migration or schema compatibility issues
- Performance / latency impact
- Security / privacy / compliance considerations
-->

### Rollout Plan

<!--
How will this change be rolled out?

- Behind a feature flag?
- Staged or canary deployment?
- Co-ordination with other teams/services?
-->

### Rollback Plan

<!--
How can we safely undo this change if needed?

- Simple revert of this PR?
- Additional manual steps (e.g. data rollback, config revert)?
-->

## Testing

<!--
Describe how you tested this change.

Include commands, tools and scenarios where helpful.
-->

- [ ] Unit tests
- [ ] Integration tests
- [ ] End-to-end / manual tests
- [ ] Performance / load tests (if applicable)

## Observability

<!--
How will we know this works (or fails) in production?

- New metrics / logs / traces?
- Alerts or dashboards that should be updated?
-->

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
- [ ] Architecture

Documentation updates:

- [ ] Docstrings updated
- [ ] Reference docs updated
- [ ] Guides/runbooks updated
- [ ] No documentation changes required (explain below)
- [ ] Architecture-Decision Record (ADR)

Explanation:

## Checklist

- [ ] Code follows existing style and conventions
- [ ] Feature is behind a flag if risky
- [ ] No secrets, credentials or sensitive data committed
- [ ] Backwards compatibility considered (APIs, events, DB)
- [ ] Tests added/updated and passing
