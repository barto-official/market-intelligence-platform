# ADR <NNNN>: <Decision Title>

| Metadata          | Value                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| **Date**          | YYYY-MM-DD                                                                                             |
| **Author**        | @<github user>, @<github user>                                                                         |
| **Status**        | `Proposed`, `Approved`, `Partially Implemented`, `Rejected`, `Implemented`, `Deprecated`, `Superseded` |
| **Tags**          | {your_tag}                                                                                             |
| **Related**       | \<links to PRs, RFCs, incidents, docs, diagrams, tickets>                                              |
| **Supersedes**    | \<ADR NNNN, if applicable>                                                                             |
| **Superseded by** | \<ADR NNNN, if applicable>      <br/>                                                                  |

## 1) Context & Problem Statement

Context: Describe the situation that led to this decision. Include the relevant constraints and “why now”.
Problem Statement:

List the concrete forces that matter. Examples:

- Latency target: \<p95/p99>
- Availability/SLO: \<e.g., 99.9%>
- Scale assumptions: \<req/s, events/s, users>
- Compliance/security constraints: \<PII, audit, residency>
- Team constraints: \<skills, on-call maturity, timeline>
- Cost constraints: <budget limits>
- Operational constraints: \<multi-region, DR, incident history>

## 2) Decision & Design

### Decision Statement

A one-paragraph statement of what we will do.

### Decision Details

Bullet the specific commitments. For example:

- We will use <X> for <Y>.
- We will expose <interfaces> via <mechanism>.
- We will enforce \<policies/constraints>.
- We will not support <Z> initially.

### Decision Scope

- **In scope:** <what this decision covers>
- **Out of scope:** <what this does not decide>
- **Assumptions:** <explicit assumptions>
- **Non-goals:** <explicit non-goals>

### Affected Architecture Views

- Example: C4 Container Diagram (Orders & Billing) (reference: `\docs\architecture\diagrams\my_diagram.jpg`)

### Why this option

Explain why the chosen option best satisfies the drivers. Tie explicitly to constraints/trade-offs.

### Trade-offs Accepted

List what you are knowingly paying:

- We accept \<risk/cost> to gain <benefit>.
- We accept <limitation> until <trigger>.

## 4) Options Considered

### Option A: <name>

- **Summary:** <what it is>
- **Pros:**
  - ...
- **Cons / Risks:**
  - ...
- **Operational Impact:** \<on-call, debugging, complexity>
- **Cost Impact:** \<infra + engineering>
- **Notes:** \<where it fits/doesn’t>

### Option B: <name>

(same structure)

### Option C: <name>

(same structure)

## 5) Consequences

### Positive Consequences

- ...

### Negative Consequences / New Risks

- ...

### Impact on Quality Attributes

- **Performance:** <expected effect>
- **Reliability/Availability:** <expected effect>
- **Security:** <expected effect>
- **Maintainability/Evolvability:** <expected effect>
- **Cost:** <expected effect>

## 6) Implementation Plan (Decision-to-Action)

### High-level Plan

1. ...
1. ...
1. ...

### Migration / Rollout Strategy (if applicable)

- Phases:
  - Phase 1: ...
  - Phase 2: ...
- Backward compatibility:
  - ...
- Rollback plan:
  - ...

### Operational Plan

- Observability (signals to add):
  - Logs:
  - Metrics:
  - Traces:
- Runbooks to create/update:
  - ...
- On-call ownership:
  - ...

## 7) Validation

### Success Criteria

Define measurable outcomes that validate the decision:

- <metric> baseline → target
- \<SLO/SLI> compliance target
- <cost ceiling>
- <operational KPI> (e.g., MTTR)

### How we will validate

- Load test approach:
- Failure testing / game days:
- Pilot scope and duration:

## 8) Revisit Triggers

This decision should be revisited if any of the following occur:

- Scale crosses: <threshold>
- Latency/throughput constraints change: <threshold>
- Incidents: \<pattern/frequency>
- Cost exceeds: <threshold>
- Org/team change: <new team topology>
- New requirements: \<e.g., multi-region active-active>
