# ADR 0002: Define Target System Boundary for Market Intelligence Platform

| Metadata          | Value                                                            |
| ----------------- | ---------------------------------------------------------------- |
| **Date**          | 2026-04-30                                                       |
| **Author**        | @barto-official                                                  |
| **Status**        | `Accepted`                                                       |
| **Tags**          | architecture, system-context, c4                                 |
| **Related**       | `docs/architecture/diagrams/c1-target-system-context.drawio.svg` |
| **Supersedes**    | N/A                                                              |
| **Superseded by** | N/A                                                              |

## 1) Context & Problem Statement

The project needs a clear definition of goals, no-goals, boundaries, scopes, and architecture context. This prevents from scope explosion, technology-first design, and misaligned implementation.

The architecture needs a clear boundary that answers:

- What is the system under design?
- Which capabilities belong inside the platform?
- Which actors and systems are external dependencies?
- Which external dependencies are current versus future/deferred?
- How do we prevent future-facing context diagrams from creating MVP scope creep?

## 2) Decision

The Market Intelligence Platform helps active retail investors maintain investing context
and eventually translate market, news, and geopolitical events into portfolio-aware,
risk-aware insights. The solution will be built iteratively but the first architecture and system scope should be defined up-front for better planning and scaling of the project.

The plan for the release cycle include:

**Version 0.0.1 —** Foundation Portfolio + Historical Equity Data

- Data:
  - Batch & Historical Data Ingestion (only equities): Price
  - Analytical and Operational Databases
- Application:
  - Portfolio & Watchlist management
  - Authorization & Authentication
  - Minimal user account
- Analytics:
  - Dashboard with Historical Data based on portfolio
- Operations:
  - Structured logging

**Version 0.0.2** — Expanded Batch Data + Governance

- Data:
  - Batch & Historical Data Ingestion (equities, commodities, crypto): financial metrics, earnings, other dimension data (tbd),
  - Batch & Historical Data Ingestion (commodities, crypto): price
  - Data Quality & Governance
- Application
  - Improved User Account Management
- Analytics:
  - Improved dashboard with metrics and asset detail views

**Version 0.0.3** — Multi-Asset Batch Analytics

- Data:
  - Batch & Historical Data Ingestion (other assets): price, financial metrics, earnings, other dimension data (tbd)
  - Ingestion of Geopolitical Data & Events
- Analytics
  - Real-time dashboard
  - Cross-asset dashboard
  - Portfolio exposure by asset class
  - Basic historical analytics

**Version 0.0.4** — Real-Time Price Foundation

- Data:
  - Real-Time price ingestion of existing assets
- Analytics:
  - Real-time dashboard
- Operations:
  - Real-time ingestion monitoring
  - Alerts for stale streams and ingestion failures

**Version 0.0.4** — News & Geopolitical Event Ingestion

- Data:

  - Geopolitical data ingestion
  - News/event ingestion
  - Event taxonomy
  - Event quality/status metadata

- Analytics:

  - Event timeline
  - Basic event filtering
  - Basic asset/event tagging where reliable

Version 0.0.6 — Event Relevance & Notifications

- Analytics & Insights:

  - Event-to-asset relevance v1
  - Portfolio/watchlist relevance matching
  - Basic event explanations
  - Source links and confidence labels

- Application:

  - Price volatility notifications
  - Geopolitical/event notifications
  - Notification preferences

- Feedback:

  - Relevant / not relevant feedback
  - Data/event issue feedback

**Version 1.0.0 — Decision Intelligence v1**

- Analytics & Insights:

  - Batch price forecasting v1
  - Geopolitical/event impact assessment v1
  - Portfolio-aware risk narratives
  - Explanation and source traceability
  - Confidence/uncertainty communication
  - Evaluation dashboards
  - Calibration tracking

- Feedback:

  - Feedback loop for relevance and trust
  - Outcome tracking for insights

- Operations:

  - Production-grade observability
  - Tracing
  - Runbooks
  - Alerting

**Version 1.1.0 — Portfolio Optimization v1**

- Analytics & Insights:
  - Portfolio optimization v1
  - Scenario-based portfolio analysis
  - Risk/return trade-off views
  - Constraints and user preferences
  - Paper recommendations only
  - No automatic broker execution

**Version 1.2.0 — Broker Integration / Paper Trading**

- Application:

  - Broker account connection
  - Holdings sync
  - Transaction import
  - Paper trade simulation
  - Trade intent model
  - User confirmation flow

- Trust & Compliance:

  - Audit trail
  - Execution disclaimers
  - Kill switch
  - Order preview
  - Risk warnings

**Version 2.0.0 — Semi-Automated Trading**

- Execution
  - Broker order submission
  - User-approved trade execution
  - Strict audit trail
  - Rollback/failure handling
  - Execution monitoring
  - Automation gates
  - LLM-based trading

## 3) Out Of Scope

- HFT execution infrastructure (colocation, ultra-low-latency order routing, microstructure optimizations)
- “Guaranteed returns” positioning or anything resembling it
- Full multi-asset coverage (start with equities/ETFs; add others only after quality is proven)
- Complex derivatives strategy automation before compliance, risk controls, and user sophistication gates
- Building a full broker-dealer stack from scratch (prefer partnerships/integrations)

## 3) Principles & Trade-offs

**User Success over Feature Breadth**

- Meaning: Users should get their job done with the minimum number of steps
- Deprioritizes: Add-on Features that don’t contribute to happy path
- How: Keep the product minimal, pragmatic, and efficient through minimal number of user-features (not system features that enhances the usability)

**Data quality, lineage and reproducibility as default**

- Meaning: What cannot be reproduced, don’t go to production.
- Practice: versioned datasets, model versions, immutable event records, deterministic backtests
- Deprioritizes: ad hoc analyses that cannot be reproduced.

**Batch first, streaming last**

- Meaning: The key focus is on deliver stable insights on historical data. Only then switch to streaming and HFT.
- Deprioritizes: premature HFT-grade infrastructure
- How: aim for “minutes” latency for intelligence first; only chase “seconds/milliseconds” when there’s a proven business case and execution path

**Explainability is a feature, not compliance**

- Meaning: the user should be informed **how** the information turns into insights and what are the drivers behind it
- Deprioritizes: purely predictive outputs without reasoning
- How: each insight shows drivers, counterpoints, and context (e.g. confidence intervals)

Insights before automation

- What: Users understand signals before trusting execution.
- How: The system does not introduce automation until the insights delivery is stable and effective.
- Deprioritizes: Fully autonomous trading in early stages.

**Observability as first class citizens**

- Meaning: The system and results should be monitored to solve the bugs quickly, iterate over possible problems, and reduce unknown unknowns.
- How: observability, metrics, tracing should be an essential component of each feature.
- Deprioritizes: Ad-hoc delivery without system thinking and proper monitoring.

**Personalization as a key to win the customer**

- Meaning: User preferences are the road to our success.
- How: personalize the insights and communication with the user.
- Deprioritizes: broad, one-size-fits-all news timelines

**Systems Thinking as the backbone**

- Meaning: Take decision and design with the future extensibility in mind.
- How: Refer to Quality Attributes and analyze trade-offs
- Deprioritizes: Shipping features without the overall system in mind.

**Frequent releases and testing as the main development driver**

- Meaning: Release new features quickly, get feedback, iterate.
- How: Set-up the infrastructure to enable quickly test and deploy new features in multiple environments
- Deprioritizes: Perfect, scalable infrastructure and omission of testing.

## 4) Quality Attributes & Guardrails

*Tiers express required rigor, not implementation order.*

**Scopes:**

- **Scopes 1 (must not fail):** data ingestion and storage, dataset/version registry, backtests, insight generation pipeline
- **Scopes 2:** UI rendering of insights, personalization, notifications, auth/permissions, recommendations
- **Scopes 3:** automation, extra features

Priorities:

- 1 \[Must\]
- 2 \[Should\]
- 3 \[Could\]

**Deployability & Release engineering & Testing \[QA-1\]**

- Intent: Ship frequently with confidence; reduce change risk as the system grows.

- Priority: 1

- Scope: All

- Guardrails

  - All services shall be built, tested, packaged, and deployed via an automated pipeline with no manual steps for standard releases. \[QA-1.1\]
  - Deployments shall use immutable artifacts (images/packages) with provenance: version, commit SHA, build time, and dependency manifest. \[QA-1.2\]
  - Changes require automated tests covering critical paths (ingestion → registry → backtest → insight). \[QA-1.3\]
  - Promotions to production shall pass defined quality gates: unit/integration tests, security scans, and deployment verification. \[QA-1.4\]
  - Feature flags for risky changes and experiments; quick rollback path is always available. \[QA-1.5\]

- Measures

  - Deployment frequency
  - Change failure rate (deployments causing incidents)
  - Lead time for changes (commit → production)
  - Mean time to restore (MTTR) for change-induced issues

- Trade-offs

  - Slower feature throughput early to build the release “muscle.”
  - Some experimental features are delayed until they can be shipped safely behind flags.

**Reliability of Pipelines \[QA-2\]**

- Intent: Inputs are available and timely; failures are visible and recoverable; pipelines handle unexpected failure gracefully.
- Priority: 1
- Scope: 1
- Guardrails
  - Failures must degrade gracefully: block incorrect outputs rather than produce silently wrong insights. \[QA-2.1\]
  - All pipelines have an idempotent mechanism \[QA-2.2\]
  - Backfill and replay are first-class capabilities \[QA-2.3\]
  - All pipelines can be run with full load and delta load \[QA-2.4\]
- Measures
  - Pipeline availability
  - Missed Execution Rate
  - Error rate
  - Mean Time to Detect (MTTD)
  - Retry success rate
- Trade-offs
  - Accept reduced source breadth initially to ensure reliability for selected sources.
  - Prefer resilient batch pipelines over premature streaming.

**Reproducibility and Lineage \[QA-3\]**

- Intent: Any production insight can be regenerated from recorded artifacts.
- Priority: 1
- Scope: 1
- Guardrails
  - No production insight without: dataset version, model version, code version, and immutable event inputs. \[QA-3.1\]
  - Deterministic backtests for the same inputs; randomness is controlled and recorded. \[QA-3.2\]
  - Lineage is captured end-to-end: source → features → model → insight. \[QA-3.3\]
- Measures
  - % of production insights reproducible on demand
  - % of “cannot reproduce” defects/incidents
  - Coverage of lineage metadata for Tier 1 outputs
- Trade-offs
  - Higher upfront discipline; experimentation is slightly slower.
  - Some ad hoc analyses remain “sandbox-only” by design.

**Data Quality, Integrity, and Correctness (No Silent Wrong Outputs) \[QA-4\]**

- Intent: Incorrect insights are prevented or clearly flagged; integrity is provable.
- Scope: 1
- Priority: 1
- Guardrails
  - Quality checks and reliability measures (e.g. confidence levels) on produced insights. \[QA-4.1\]
  - Data integrity constraints implemented for core data insights. \[QA-4.2\]
  - User-visible “quality status” when upstream quality is degraded.  \[QA-4.3\]
- Measures
  - Incidents of incorrect outputs (vs. availability incidents)
  - % of insights published with “healthy” quality status
  - Rate of schema/contract violations detected pre-production
- Trade-offs
  - Sometimes fewer insights delivered rather than questionable insights delivered.
  - Adds engineering work for validation and contracts.

**Observability (Fast Detection and Diagnosis) \[QA-5\]**

- Intent: Detect issues quickly, localize root cause, and shorten recovery time.
- Scope: All
- Priority: 2
- Guardrails
  - All architecture components implement metrics, tracing, and logging. \[QA-5.1\]
  - Alerting on golden signals plus correctness proxies (freshness, anomaly rates). \[QA-5.2\]
  - Post-incident learning is captured (runbooks, alerts tuned, failure mode prevented). \[QA-5.3\]
  - All data and ML pipeline should monitor performance. \[QA-5.4\]
  - All user-facing endpoints shall emit request rate, error rate, and latency (p50/p95/p99) metrics, labeled by {service, route, status class} \[QA-5.5\]
  - Logs shall be structured and adhere to the common template. \[QA-5.6\]
- Measures
  - MTTD and MTTR
  - Alert coverage: %
  - Correlation effectiveness (trace/log linkage)
  - % incidents with identified root cause and documented
- Trade-offs
  - Additional work per feature; slower initial shipping.
  - More operational discipline and on-call readiness.

**Explainability (Drivers and Uncertainty) \[QA-6\]**

- Intent: Users understand why an insight exists and when to distrust it.
- Priority: 2
- Scope: 1, 2
- Guardrails
  - Each insight shows: primary drivers, counterpoints/alternatives, and uncertainty (confidence bands or qualitative reliability). \[QA-6.1\]
  - Explainability is part of the definition of done for new insight types. \[QA-6.2\]
  - When explainability is weak, insights are labeled experimental or not promoted to production. \[QA-6.3\]
- Measures
  - User engagement with explanations (open rate, time spent, follow-up actions)
  - Support questions related to “why did I get this insight?”
  - “Trust” proxy metrics (save/share/act) correlated with explanation availability
- Trade-offs
  - Some high-performing but opaque models may be delayed.
  - More product and design effort per insight type.

**Maintainability and Extensibility \[QA-7\]**

- Intent: The system evolves without accumulating brittle one-offs; changes remain predictable.
- Priority: 1
- Scope: All
- Guardrails
  - Clear modular boundaries (ingestion, registry, backtest, insight generation, delivery).  \[QA-7.1\]
  - Avoid one-off pipelines unless they are explicitly time-boxed and scheduled for generalization.  \[QA-7.2\]
  - ADRs are produced for major decisions and stored in a repo.  \[QA-7.3\]
  - RFCs are used for new proposals and stored in a repo.  \[QA-7.4\]
  - Code is designed with best practices in mind.  \[QA-7.5\]
- Measures
  - Lead time for change
  - Change failure rate trend (should decrease over time)
  - Ratio of shared pipelines/components vs one-offs
  - Change amplification (blast radius of typical changes)
- Trade-offs
  - Some refactoring is planned work, not accidental work.
  - Slightly slower feature experimentation in exchange for long-term velocity.

**Performance (Minutes-Latency First; Streaming Later) \[QA-8\]**

- Intent: Deliver stable insight generation for historical/batch use-cases before real-time.
- Applies to: Tier 1 (mandatory for pipelines); Tier 2 (mandatory for UX responsiveness).
- Guardrails
  - Target “minutes” end-to-end latency for Tier 1 insights; streaming only with validated business case and measurable ROI.
  - Performance work focuses on predictability (p95) not just average speed.
  - Cost-awareness: performance improvements must consider compute cost per insight.
- Measures
  - p95 end-to-end insight generation latency (batch)
  - p95 UI time-to-first-insight (Tier 2)
  - Cost per insight run / compute budget adherence
- Trade-offs
  - Real-time features intentionally deferred.
  - Some complex insights may run slower initially, provided latency is predictable and communicated.

**Environment Constraints (Cloud-First) \[CNT-1\]**

- Intent: Operate efficiently and consistently in cloud environments; avoid split-mode complexity early.
- Applies to: All
- Guardrails
  - Default deployment target is cloud. \[CNT-1.1\]
  - Infrastructure defined as code; environments are reproducible (dev/stage/prod parity as feasible).  \[CNT-1.2\]
- Measures
  - Provisioning time for new environments
  - % infrastructure managed via IaC
- Trade-offs
  - Some enterprise deals requiring on-prem may be deferred or handled via a separate roadmap track.
  - Additional effort to standardize tooling and deployments.

**Scope 3: Automation (Explicit Gate)**

- Intent: No automation until insights are stable, explainable, and trusted.
- Gate (must be true before any automation ships):
  - Tier 1 reproducibility and correctness standards are met for the automated action domain.
  - Explainability and uncertainty are shown and understood by users.
  - Monitoring exists for model drift, anomalies, and negative outcomes; rollback exists.
- Measures
  - Automation opt-in rate and sustained usage
  - Outcome quality metrics (e.g., avoided loss, improved execution KPIs) with safeguards
  - Incident rate attributable to automation
- Trade-offs
  - Slower path to “full autonomy,” higher trust and lower reputational risk.

## 5) Design

We will name the target system **Market Intelligence Platform** in the C1 System Context diagram.

### Decision Scope

- **In scope:**

  - System boundary definition
  - C1 target-context naming
  - External actors and external software systems
  - Current versus future dependency classification
  - Relationship-level framing between the platform and external systems

- **Out of scope:**

  - Decision on Tooling

- **Non-goals:**

  - Do not decide how the platform is internally decomposed.
  - Do not decide which technologies are used.
  - Do not imply that all target-context integrations are MVP scope.
  - Do not model internal containers, databases, queues, workers, or services in this ADR.

### Affected Architecture Views

- C4 System Context Diagram:
  - `docs/architecture/diagrams/c1-target-system-context.drawio`

<img src="../diagrams/c1-target-system-context.drawio.svg" alt="C1 target system context" width="1000" />
