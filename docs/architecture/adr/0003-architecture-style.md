# ADR 0003: Modular Monolith, Batch Ingestion, and Hexagonal Codebase Architecture

| Metadata          | Value                                                                                                      |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| **Date**          | 2026-04-30                                                                                                 |
| **Author**        | @barto-official                                                                                            |
| **Status**        | `Proposed`                                                                                                 |
| **Tags**          | architecture, architecture-style, modular-monolith, hexagonal     |
| **Related**       | `docs/architecture/adr/0002-system-context.md`, `docs/architecture/diagrams/c2-target-architecture.drawio.svg`, `docs/architecture/domain/ddd-exercise.md` |
| **Supersedes**    | N/A                                                                                                        |
| **Superseded by** | N/A                                                                                                        |

## 1) Context & Problem Statement

We need an initial architecture that supports clear domain boundaries without introducing unnecessary distributed-system complexity — both at **runtime** (how the system is deployed and operated) and at **codebase level** (how the application is organized internally).

At runtime, the platform must serve user-facing APIs, run long-running batch ingestion pipelines, and eventually support additional entry points (notifications, streaming consumers).

At codebase level, the platform integrates many external systems (market data providers, auth, and later brokers and event sources), enforces trust-critical domain rules (freshness, quality, provenance), and must remain testable and evolvable as bounded contexts grow. We need an internal structure that keeps domain logic isolated from infrastructure without imposing excessive ceremony on early delivery.

**Forces:**

- Need fast iteration and low operational overhead.
- Need clean boundaries for future evolution — at deployment and at code level.
- Data ingestion is a high priority — batch-only at the beginning, streaming as a later add-on.
- Many external dependencies that must not leak provider models into domain logic.
- Multiple entry points over time: HTTP API, batch jobs, and later event consumers.
- Microservices would add deployment, networking, observability, and data-consistency complexity too early.
- A purely layered codebase (controllers → services → repositories) risks obscuring domain ownership across independent contexts.

## 2) Decision & Design

### Decision Statement

We will start with a **modular monolith** for product-facing backend capabilities. Internally, each domain module will follow **Hexagonal Architecture (Ports & Adapters)**.

### Runtime Architecture

The product-facing backend is one deployable application, internally organized by domain modules aligned with bounded contexts. Each module owns its domain concepts and exposes explicit interfaces to other modules.
- We will implement the product-facing backend as one deployable application.
- Internal modules will represent domain boundaries.
- We will use batch ingestion as the default ingestion mode.
- We will defer streaming-first architecture.
- We will defer microservices.
- We will design module boundaries so future extraction remains possible.

| Need                                           | Why it fits the requirements          |
| ---------------------------------------------- | ------------------------------------- |
| Fast iteration                                 | One backend deployable                |
| Clear domain boundaries                        | Modules align with DDD-light contexts |
| Lower operational complexity                   | No distributed services yet           |
| Future extraction path                         | Modules can later become services     |
| Easier local development                       | One backend app + workers             |
| Stronger maintainability than layered monolith | Domain-oriented code organization     |


### Decision Scope

- **In scope:** initial runtime architecture style (modular monolith), internal codebase structure (hexagonal modules per bounded context), dependency rules, adapter/port conventions, cross-module boundary strategy.
- **Out of scope:** concrete web framework, ORM, dependency-injection library, database choice, cloud provider, auth provider, observability vendor, detailed API design.
- **Assumptions:** first users and workloads do not require independent service scaling; bounded contexts from strategic DDD exercise guide module boundaries (see `ddd-exercise.md` for reference, not as a formal ADR).
- **Non-goals:** no microservices, no streaming-first architecture, no broker execution architecture in the initial platform, no global Clean Architecture layering from day one.

### Affected Architecture Views

- `docs/architecture/diagrams/c2-target-architecture.drawio.svg`

<img src="../diagrams/c2-target-architecture.drawio.svg" alt="C1 target architecture" width="1000" />

### Why this option

A modular monolith gives clear runtime boundaries with low operational complexity. Separate ingestion jobs keep long-running data workflows out of user-facing API paths. Hexagonal modules inside each deployable unit keep domain logic testable and provider-independent, align with anti-corruption needs, and support multiple entry points without duplicating rules. Together, this fits the current project stage while preserving evolution paths toward richer internal layering (Clean) and eventual service extraction.

### Codebase Architecture (Internal Application Set-up)

Each domain module inside the monolith (and inside ingestion jobs) follows **Hexagonal Architecture**. The domain core contains entities, value objects, and domain services — free of framework, database, and provider dependencies. **Ports** define the module's boundaries: primary (driving) ports for use cases invoked by the outside world, and secondary (driven) ports for infrastructure the domain needs (repositories, external APIs, messaging). **Adapters** implement those ports: HTTP routes and batch job runners as primary adapters; database repositories and external provider clients as secondary adapters.

Organize the repository **by bounded context first**, then hexagonal structure inside each module.

### Why Hexagonal Architecture over Clean Architecture

Hexagonal Architecture and Clean Architecture share the same core idea — protect domain logic from external concerns via dependency inversion — but they emphasize different things. For this project at its current stage, Hexagonal is the better primary choice.

Hexagonal Architecture foregrounds **ports and adapters** and the interaction with the outside world. That maps directly to our needs: swapping market data providers, adding new entry points (API today, batch job now, event consumer later), and enforcing anti-corruption boundaries at adapter edges. It is less prescriptive about the number and naming of internal layers, which suits a modular monolith where some contexts are rich in rules (data quality, insight delivery) and others are simpler (user access, watchlist CRUD).

Clean Architecture prescribes a more rigid concentric model (entities → use cases → interface adapters → frameworks). That structure pays off when orchestration complexity is high and teams are large enough to maintain consistent layering everywhere. For a small team building incrementally, applying full Clean Architecture globally tends to produce empty use-case classes, boilerplate folder hierarchies, and friction in contexts that do not yet need that ceremony. The cost is paid upfront; the benefit arrives later — if at all — in modules that never grew complex enough to need it.

Hexagonal Architecture is also a better fit for Python, where ecosystem conventions favor pragmatic module boundaries over strict four-layer taxonomies. Ports as protocols or abstract base classes, adapters as concrete implementations, and domain tests that run without a database or network are straightforward to adopt and review.

In short: Hexagonal gives us the isolation and testability we need now, with less structural overhead than Clean Architecture, while remaining compatible with Clean's principles wherever a module's complexity justifies them.

### Future Migration from Hexagonal toward Clean Architecture

This decision does not foreclose Clean Architecture. Hexagonal modules can evolve toward Clean layering **locally**, inside a bounded context, when complexity and team size justify it — without rewriting the whole codebase.

**Evolution of internal layering**

1. **Start (now):** Hexagonal modules with domain, ports, and adapters. Add application services only where orchestration exceeds what a single port method can express cleanly.
2. **Grow (per module):** When a context accumulates multi-step workflows, branching policies, or cross-aggregate coordination (e.g. insight generation, impact assessment, execution readiness), extract an explicit **application/use-case layer** between primary ports and the domain. Primary adapters call use cases; use cases call domain entities and secondary ports. This is Clean Architecture applied locally, not globally.
3. **Mature (selective):** Contexts with heavy orchestration, audit requirements, or multiple teams may adopt full Clean layering (entities, use cases, presenters, gateways). Simpler contexts remain hexagonal. The monolith becomes a **heterogeneous modular structure** — hexagonal by default, Clean where earned.
4. **Extract (if needed):** When a module is extracted to a separate service, its ports become the service's public contract. The internal layering choice (hexagonal or Clean) travels with the module; extraction does not require a global rewrite.

Revisit the internal architecture style per module when: orchestration logic spreads into adapters, domain tests require increasingly heavy setup, or a context gains a dedicated sub-team. Until those triggers fire, the default remains hexagonal.

### Trade-offs Accepted

- We accept less independent scaling in exchange for simpler deployment and debugging.
- We accept one backend deployable in exchange for faster iteration.
- We accept possible future extraction work to avoid premature microservices now.
- We accept shared physical persistence initially, with strict logical ownership rules.
- We accept some structural discipline per module (ports, adapters, folder conventions) in exchange for long-term testability and swappable infrastructure.
- We accept that not every module will need the same internal depth; simpler contexts stay lightweight rather than forcing uniform Clean layering.

## 3) Options Considered

### Runtime architecture options

1. **Layered monolith** — a single backend application organized mostly by technical layers (`controllers/`, `services/`, `repositories/`). Simple, familiar, fast to start, and easy to deploy. Not suitable here because our domains are fairly independent and matter more than generic technical layers. If everything is organized as generic services and repositories, the system can easily become a "service soup" where domain ownership is unclear.

2. **Microservices** — each major domain becomes an independently deployed service. Professional and aligned with domain distribution, but technical overkill at the beginning. Switch to microservices only when independent scaling, reliability isolation, team ownership, deployment cadence, compliance boundaries, or traffic patterns require it.
| Trigger                      | Example                                             |
| ---------------------------- | --------------------------------------------------- |
| Independent scaling          | inference service needs GPUs; backend does not      |
| Different reliability needs  | broker execution needs stricter isolation           |
| Different team ownership     | data/ML team owns models; app team owns UX/backend  |
| Different deployment cadence | model inference deploys separately                  |
| Strong compliance boundary   | execution must be separated from insight generation |
| High traffic domain          | market data serving needs separate scaling          |

Full microservices from the start would add:
- network failures
- service discovery
- distributed tracing
- contract versioning
- distributed transactions
- cross-service authorization
- more deployment pipelines
- more observability complexity
- harder local development

3. **Coarse-grained services / SOA-like architecture** — a middle ground between modular monolith and microservices: a few major runtime units instead of many tiny services. Separates fundamentally different runtime concerns but risks over-splitting too early and making later refactoring harder. Best target runtime architecture when scaling triggers are met.

4. **Event-driven architecture** — parts of the system communicate by producing and consuming events. Especially useful for data ingestion, notification requests, and feedback loops. However, it requires mature handling of event schemas, idempotency, ordering, retries, dead-letter queues, replay, deduplication, observability, and schema evolution. If introduced too early, we may spend more time building event plumbing than product and data foundation. **Use selectively, only in parts where it makes the most sense.**

### Codebase architecture options

1. **Hexagonal Architecture / Ports & Adapters per bounded context (chosen)** — organize by domain module first; inside each module, domain at the center with explicit ports and adapters. Primary adapters for HTTP, batch jobs, and later event consumers; secondary adapters for databases and external providers. Pros: natural anti-corruption layers, multiple entry points without duplicated logic, testable domain core, low ceremony for simple modules, aligns with Python conventions. Cons: requires discipline to keep adapters thin and ports stable; shared kernel can become a coupling point if allowed to grow unchecked.

2. **Clean Architecture globally** — apply concentric layers (entities → use cases → interface adapters → frameworks) uniformly across all modules. Pros: strong separation of concerns, explicit use-case classes, scales well for complex orchestration and larger teams. Cons: high upfront ceremony for a small team; empty or trivial use-case classes in simple CRUD contexts; rigid folder taxonomy that may slow early iteration; less natural fit for Python project conventions. Better adopted selectively inside complex modules later than as a global day-one standard.

3. **Layered monolith (codebase)** — same as runtime layered monolith but at code level: organize primarily by technical layer rather than domain. Pros: fastest initial scaffolding. Cons: domain ownership obscured, cross-cutting changes touch many layers, harder to extract modules or swap providers, directly conflicts with DDD-light bounded context strategy. Rejected.

4. **Flat feature folders without ports** — organize by feature but allow direct imports of ORM models, HTTP clients, and provider SDKs from anywhere. Pros: fastest to write first code. Cons: provider schema leakage, untestable domain logic, tight coupling that makes future hexagonal or Clean migration expensive. Rejected for trust-critical and provider-heavy domains; acceptable only for throwaway spikes outside production paths.

## 4) Consequences

### Positive Consequences

- Simpler initial runtime architecture.
- Faster development loop.
- Lower operational burden.
- Clear internal module boundaries at runtime and in code.
- Domain logic testable without database or network.
- External providers swappable by changing adapters, not domain rules.
- Multiple entry points (API, batch job) share the same domain core.
- Easier debugging in a single deployable.
- Future service extraction and selective Clean layering remain possible.

### Negative Consequences / New Risks

- Modular boundaries can erode — for example, importing internal database models, writing to another module's tables, or bypassing ports.
- Module coupling may grow if hexagonal rules are not enforced in code review.
- Individual capabilities cannot be deployed independently at runtime.
- Shared database ownership must be controlled with strict logical ownership rules.
- Port and adapter boilerplate adds overhead in very simple modules.
- Future extraction or Clean migration inside a module requires deliberate refactoring, not automatic upgrade.
- Heterogeneous internal structure (hexagonal vs Clean per module) may confuse contributors unless documented per context.

### Impact on Quality Attributes

- **Performance:** Good enough for current workload; ingestion separated from API path.
- **Reliability/Availability:** Simpler runtime reduces failure modes; hexagonal isolation limits blast radius of provider or infrastructure changes within a module.
- **Security:** Centralized authorization is simpler initially; adapter boundaries provide clear points for auth and input validation.
- **Maintainability/Evolvability:** Strong positive if module and port boundaries are enforced; supports incremental migration to Clean layering where complexity warrants it.
- **Cost:** Lower infrastructure and operational cost; moderate upfront code structure cost per module.

## 5) Implementation Plan (Decision-to-Action)

### High-level Plan

1. Define backend as one modular monolith with hexagonal internal modules.
1. Scaffold domain modules aligned with phase-one bounded contexts (user access, investing, asset registry, market data ingestion, data quality, market data serving, portfolio analytics).
1. Establish port/adapter conventions and dependency rules in code review checklist.
1. Keep ingestion outside user request paths.
1. Add domain-level tests that run without infrastructure; integration tests at adapter boundaries.

### Migration / Rollout Strategy

- Phases:
  - Phase 1: Modular backend + batch ingestion job with hexagonal structure in phase-one contexts.
  - Phase 2: Strengthen module boundaries, enforce port-only cross-module access, add anti-corruption adapters for first external providers.
  - Phase 3: Introduce application/use-case layer selectively in modules where orchestration complexity grows (toward Clean Architecture locally).
  - Phase 4: Extract services only if runtime revisit triggers are met; ports become service contracts.
- Backward compatibility: not applicable — this is the initial architecture.
- Rollback plan: not applicable.

## 6) Validation

### Success Criteria

- First implementation slices can be built without service orchestration overhead.
- Backend modules remain logically separated at runtime and in code.
- Domain tests run without database or external network for core business rules.
- A market data provider can be replaced by changing adapters only, without domain changes.
- Ingestion jobs do not block or degrade API requests.
- Local development remains simple (one backend app).
- C2 diagram clearly separates frontend, backend, ingestion, storage, and external systems.
- Code review can detect cross-module coupling (direct DB model imports, adapter bypass).

### How we will validate

- Architecture review of module boundaries and port definitions.
- Code review for cross-module coupling and adapter thinness.
- Unit tests on domain logic; integration tests at adapter boundaries.
- Basic operational tests for ingestion failure and stale data.
- Provider swap exercise (mock or second adapter) to confirm port isolation.

## 7) Revisit Triggers

This decision should be revisited if any of the following occur:

**Runtime:**

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

**Codebase (internal architecture):**

- Orchestration logic consistently leaks into adapters despite port conventions.
- A module's workflow complexity makes hexagonal structure insufficient without a dedicated use-case layer (trigger for local Clean Architecture adoption).
- Domain tests routinely require heavy infrastructure setup, indicating port boundaries are too coarse.
- Cross-module coupling incidents recur despite code review.
- Team size grows to the point where uniform layering conventions would reduce onboarding friction.
