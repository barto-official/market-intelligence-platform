# ADR 0004: Use Modular Monolith with Separate Batch Ingestion Jobs

| Metadata          | Value                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------- |
| **Date**          | 2026-04-30                                                                            |
| **Author**        | @barto-official                                                                       |
| **Status**        | `Proposed`                                                                            |
| **Tags**          | architecture, architecture-style, modular-monolith, batch-ingestion, c2               |
| **Related**       | `docs/architecture/0002-system-context.md`, `docs/architecture/0002-strategic-ddd.md` |
| **Supersedes**    | N/A                                                                                   |
| **Superseded by** | N/A                                                                                   |

## 1) Context & Problem Statement

Context: The platform has multiple domain areas. The first implementation scope is narrower: market data foundation, asset universe, portfolio/watchlist context, data quality, and basic application experience.

Problem Statement: We need an initial architecture style that supports clear domain boundaries without introducing unnecessary distributed-system complexity.

Forces:

- One developer / small-team project initially.
- Need fast iteration and low operational overhead.
- Need clean boundaries for future evolution.
- Batch-first market data ingestion is preferred over streaming-first architecture.
- Broker execution, recommendations, and automation are future-gated.
- Data quality, lineage, observability, and reproducibility must be first-class.
- Microservices would add deployment, networking, observability, and data-consistency complexity too early.

## 2) Decision & Design

### Decision Statement

We will start with a **modular monolith** for product-facing backend capabilities, plus **separate batch-oriented ingestion jobs** for market data ingestion and processing.

### Decision Details

- We will implement the product-facing backend as one deployable application.
- Internal modules will represent domain boundaries, such as:
  - users/auth
  - assets
  - portfolio/watchlists
  - market data
  - data registry/lineage
  - feedback
  - trust/compliance
  - insights later
  - recommendations later
- We will run ingestion outside the request/response path.
- We will use batch ingestion as the default ingestion mode.
- We will defer streaming-first architecture.
- We will defer microservices.
- We will allow shared physical storage initially, but maintain logical data ownership by module/context.
- We will design module boundaries so future extraction remains possible.

### Decision Scope

- **In scope:** initial architecture style, runtime separation between backend and ingestion jobs, module-boundary strategy.
- **Out of scope:** concrete frameworks, database choice, cloud provider, auth provider, observability vendor, detailed API design.
- **Assumptions:** first users and workloads do not require independent service scaling.
- **Non-goals:** no microservices, no streaming-first architecture, no broker execution architecture in the initial platform.

### Affected Architecture Views

- `docs/architecture/03-domain-decomposition.md`
- `docs/architecture/05-container-architecture.md`
- `docs/architecture/diagrams/c2-container-architecture.drawio`

### Why this option

A modular monolith gives clear boundaries with low operational complexity. Separate ingestion jobs keep long-running data workflows out of user-facing API paths. This fits the current project stage while preserving an evolution path toward services later.

### Trade-offs Accepted

- We accept less independent scaling in exchange for simpler deployment and debugging.
- We accept one backend deployable in exchange for faster iteration.
- We accept possible future extraction work to avoid premature microservices now.
- We accept shared physical persistence initially, with strict logical ownership rules.

## 4) Options Considered

### Option A: Modular monolith + separate batch ingestion jobs

- **Summary:** One product-facing backend with internal modules, plus separate batch ingestion jobs.
- **Pros:**
  - Low operational complexity.
  - Fast iteration.
  - Clear domain boundaries without distributed systems.
  - Easier local development and testing.
  - Compatible with future extraction.
- **Cons / Risks:**
  - Requires discipline to avoid module coupling.
  - Harder to scale individual modules independently.
  - Shared database can blur ownership if unmanaged.
- **Operational Impact:** Low to medium.
- **Cost Impact:** Low.
- **Notes:** Accepted.

### Option B: Microservices from the start

- **Summary:** Each bounded context becomes an independently deployed service.
- **Pros:**
  - Independent deployment and scaling.
  - Stronger runtime isolation.
- **Cons / Risks:**
  - Premature complexity.
  - Distributed transactions and network failures.
  - More CI/CD, observability, API versioning, and operational overhead.
- **Operational Impact:** High.
- **Cost Impact:** High.
- **Notes:** Rejected for initial platform.

### Option C: Streaming/event-driven architecture first

- **Summary:** Use streams/events as the central integration style from the beginning.
- **Pros:**
  - Good for future real-time data and alerts.
  - Scales well for event-driven workflows.
- **Cons / Risks:**
  - Too complex for the current batch-first stage.
  - Harder debugging and replay semantics.
  - Requires more infrastructure and operational maturity.
- **Operational Impact:** High.
- **Cost Impact:** Medium to high.
- **Notes:** Deferred.

### Option D: Serverless-first architecture

- **Summary:** Use serverless functions and managed services for backend and jobs.
- **Pros:**
  - Low infrastructure management.
  - Good for small workloads.
- **Cons / Risks:**
  - Can fragment the architecture.
  - Harder local development and portability.
  - Vendor lock-in risk.
- **Operational Impact:** Medium.
- **Cost Impact:** Low to medium.
- **Notes:** Not selected for initial architecture.

## 5) Consequences

### Positive Consequences

- Simpler initial architecture.
- Faster development loop.
- Lower operational burden.
- Clear internal module boundaries.
- Easier testing and debugging.
- Future service extraction remains possible.

### Negative Consequences / New Risks

- Module coupling may grow if boundaries are not enforced.
- Individual capabilities cannot be deployed independently.
- Shared database ownership must be controlled.
- Future extraction may require refactoring.

### Impact on Quality Attributes

- **Performance:** Good enough for current workload; ingestion separated from API path.
- **Reliability/Availability:** Simpler system reduces failure modes.
- **Security:** Centralized authorization is simpler initially.
- **Maintainability/Evolvability:** Good if module boundaries are enforced.
- **Cost:** Lower infrastructure and operational cost.

## 6) Implementation Plan (Decision-to-Action)

### High-level Plan

1. Define backend as one modular monolith.
1. Implement domain contexts as internal modules/packages.
1. Create separate batch ingestion job/container.
1. Keep ingestion outside user request paths.
1. Document logical ownership of data by module/context.
1. Reflect this decision in the C2 container diagram.

### Migration / Rollout Strategy (if applicable)

- Phases:
  - Phase 1: Modular backend + batch ingestion job.
  - Phase 2: Add stronger module boundaries and internal interfaces.
  - Phase 3: Extract services only if revisit triggers are met.
- Backward compatibility:
  - Not applicable.
- Rollback plan:
  - Not applicable; this is the initial architecture style.

### Operational Plan

- Observability:
  - Logs: backend and ingestion jobs emit structured logs.
  - Metrics: API latency/errors, ingestion run status, data quality status.
  - Traces: add later if needed across API/data flows.
- Runbooks to create/update:
  - ingestion failure runbook
  - stale data runbook
  - deployment rollback runbook
- On-call ownership:
  - single owner initially.

## 7) Validation

### Success Criteria

- First implementation slices can be built without service orchestration overhead.
- Backend modules remain logically separated.
- Ingestion jobs do not block or degrade API requests.
- Local development remains simple.
- C2 diagram clearly separates frontend, backend, ingestion, storage, and external systems.

### How we will validate

- Architecture review of module boundaries.
- Code review for cross-module coupling.
- Integration tests for core flows.
- Basic operational tests for ingestion failure and stale data.

## 8) Revisit Triggers

This decision should be revisited if any of the following occur:

- A module needs independent scaling.
- A module needs independent deployment.
- Multiple teams need separate ownership.
- Ingestion workloads interfere with API performance.
- Failure blast radius becomes unacceptable.
- Broker execution becomes active.
- Recommendations/automation become active.
- Compliance requires runtime isolation.
- Streaming/real-time requirements become core.
- Shared database ownership becomes a persistent source of defects.
