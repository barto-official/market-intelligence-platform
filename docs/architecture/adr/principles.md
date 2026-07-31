# Principles & Trade-offs

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
