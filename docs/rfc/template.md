# RFC `<NNNN>: <Title>`

| Metadata           | Value                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------- |
| **Date**           | YYYY-MM-DD                                                                              |
| **Author**         | @<github user>, @<github user>                                                          |
| **Status**         | `Draft`, `In Review`, `Accepted`, `Rejected`, `Implemented`, `Deprecated`, `Superseded` |
| **Tags**           | {tag1}, {tag2}, {tag3}                                                                  |
| **Reviewers**      | @<github user>, @<github user>                                                          |
| **Related**        | \<links to PRs, ADRs, incidents, docs, diagrams, tickets>                               |
| **Related Issues** | \<Issue: {number}>                                                                      |
| **Related ADRs**   | <ADR links once accepted>                                                               |
| **Supersedes**     | \<RFC NNNN, if applicable>                                                              |
| **Superseded by**  | \<RFC NNNN, if applicable>                                                              |

## 1) Summary

### Problem (one paragraph)

What is the problem and why does it matter now?

### Proposed direction (one paragraph)

What are we proposing at a high level (even if not finalized)?

### Decision deadline (optional)

By when do we need a decision, and who decides if consensus is not reached?

## 2) Context

### Background

What led to this RFC? Include relevant history and current pain points.

### Drivers / Forces

List the concrete forces that matter. Examples:

- Performance/latency targets: \<p95/p99>
- Availability/SLOs: \<99.9% etc>
- Scale assumptions: \<req/s, events/s, data volume>
- Security/compliance: \<PII, audit, residency>
- Operational constraints: \<multi-region, DR, on-call maturity>
- Team constraints: \<skills, timeline, staffing>
- Cost constraints: <budget ceilings>

## 3) Goals and Non-goals

### Goals

- ...
- ...

### Non-goals

- ...
- ...

### Out of scope

- ...

## 4) Requirements (Optional)

### Functional requirements

- ...

### Non-functional requirements (quality attributes)

- Performance:
- Reliability/Availability:
- Security/Privacy:
- Operability/Observability:
- Scalability:
- Maintainability/Evolvability:
- Cost:

### Constraints

- Hard constraints (must):
  - ...
- Soft constraints (prefer):
  - ...

## 5) Proposed Design

### Overview

Describe the proposed architecture/design. Keep it structured:

- Components involved
- Interfaces/contracts impacted
- Data flow and ownership
- Failure handling approach

### Detailed Design (Optional — pick only needed parts)

Break into subsections as needed:

- API changes
- Event schemas/topics
- Data model changes
- Algorithms/policies
- Concurrency/backpressure
- Timeouts/retries/idempotency
- Security model (authn/authz, secrets, network)

### Data Model and Ownership (Optional)

- System of record:
- Read models / derived data:
- Schema evolution policy:
- Migration/backfill approach:

### Observability and Operations

- Logs:
- Metrics:
- Tracing:
- Dashboards/alerts:
- Runbooks:
- On-call ownership:

### Failure modes and resilience

- Expected failure modes
- Mitigations (retry, circuit breaker, bulkhead, fallback)
- Degradation strategy
- Recovery strategy (RTO/RPO if relevant)

## 6) Alternatives Considered

### Option A: <name>

- **Summary:** ...
- **Pros:**
  - ...
- **Cons / Risks:**
  - ...
- **Operational Impact:** ...
- **Cost Impact:** ...
- **Notes:** ...

### Option B: <name>

(same)

### Option C: <name>

(same)

## 7) Trade-offs and Rationale

### Why this approach

Tie back explicitly to the drivers/requirements.

### Trade-offs accepted

- We accept \<cost/risk> to gain <benefit>.
- We accept <limitation> until <trigger>.

## 8) Rollout / Migration Plan

### Approach

- Phase 1:
- Phase 2:
- Phase 3:

### Backward compatibility

- Versioning strategy:
- Deprecation strategy:

### Rollback plan

- How to roll back safely:
- Data rollback considerations:

## 9) Risks and Mitigations

- Risk:
  - Mitigation:
- Risk:
  - Mitigation:

## 10) Validation Plan

### Success criteria

- <metric> baseline → target
- <SLO compliance target>
- <cost ceiling>
- <operational KPI> (e.g., MTTR)

### Testing strategy

- Unit/integration:
- Load/performance:
- Failure testing / game days:
- Security testing:

### Pilot plan (if applicable)

- Scope:
- Duration:
- Exit criteria:

## 11) Open Questions

- [ ] Question 1
- [ ] Question 2

## 12) Decision and Outcome (fill when Accepted/Rejected)

### Decision

Accepted / Rejected on YYYY-MM-DD by \<decider(s)>.

### Outcome summary

What was chosen and why (short).

### Follow-ups

- ADR(s) to write:
- Implementation tasks:
- Documentation updates:
