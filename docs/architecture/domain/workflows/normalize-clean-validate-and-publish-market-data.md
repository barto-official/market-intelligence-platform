# Workflow: Normalize, Clean, Validate, and Publish Market Data

## Actors

- Market Intelligence Platform
- Data Processing Pipeline
- Data Quality Process
- Asset Registry
- Market Data Store
- Data Registry / Lineage Store
- Portfolio, Watchlist, Dashboard, and Analytics consumers

## Trigger

Raw provider data has been received from an ingestion workflow and needs to be transformed into trusted market data.

## Data types covered in this workflow

- Raw historical price data
- Raw latest price data
- Raw financial metrics
- Raw earnings data
- Raw asset metadata/reference data
- Later: raw real-time price messages

## Main path

1. Platform loads raw provider data from the ingestion output.
1. Platform records or confirms raw data persistence for replay and auditability.
1. Platform parses provider-specific fields.
1. Platform normalizes raw data into platform-standard schemas.
1. Platform resolves asset references against the internal asset registry.
1. Platform cleans data where safe and rule-based, such as formatting, type coercion, timestamp normalization, currency normalization where supported, and duplicate removal.
1. Platform validates schema, required fields, completeness, duplicate records, value ranges, timestamp consistency, and freshness.
1. Platform assigns a data quality status such as healthy, partial, degraded, stale, or failed.
1. Platform creates or updates dataset version metadata.
1. Platform records lineage from provider source to raw data, normalized data, validation results, and serving-ready output.
1. Platform publishes only valid or explicitly quality-labeled data for serving.
1. Portfolio, watchlist, dashboard, and analytics workflows consume the serving-ready data and its quality/freshness status.

## Alternative paths

- Data passes all checks and is marked healthy.
- Data is usable but incomplete and is marked partial.
- Data is available but stale and is marked stale.
- Data contains non-critical issues and is marked degraded.
- Data fails validation and is blocked from healthy serving.
- Some assets pass validation while others fail.
- Previously served data remains active while new data is rejected.
- A dataset is regenerated through replay or backfill.

## Failure paths

- Raw data cannot be loaded.
- Provider schema changed unexpectedly.
- Normalization fails.
- Asset reference cannot be resolved.
- Required fields are missing.
- Duplicate records cannot be safely resolved.
- Data contains impossible values, such as negative prices.
- Data is stale beyond the allowed threshold.
- Dataset version cannot be created.
- Lineage cannot be recorded.
- No trustworthy data is available for serving.

## Business outcome

The platform has trusted, normalized, traceable, and quality-labeled market data that can safely power watchlists, portfolios, dashboards, analytics, and future insight-generation workflows.

```mermaid
flowchart TD
    A[Raw provider data received] --> B[Load raw data]
    B --> C{Raw data available?}

    C -- No --> D[Record raw data load failure]
    D --> Z1[Data not published for serving]

    C -- Yes --> E[Persist or confirm raw source snapshot]
    E --> F[Parse provider-specific fields]
    F --> G[Normalize into platform-standard schema]

    G --> H{Normalization succeeds?}
    H -- No --> I[Record normalization failure]
    I --> Z1

    H -- Yes --> J[Resolve asset references using asset registry]
    J --> K{Asset references resolved?}

    K -- No --> L[Record unresolved asset mapping]
    L --> M[Mark affected records failed or degraded]

    K -- Yes --> N[Clean safe and rule-based issues]
    M --> N

    N --> O[Run schema, completeness, duplicate, range, timestamp, and freshness checks]
    O --> P{Validation result}

    P -- Healthy --> Q[Assign healthy data quality status]
    P -- Partial --> R[Assign partial data quality status]
    P -- Degraded --> S[Assign degraded data quality status]
    P -- Stale --> T[Assign stale data quality status]
    P -- Failed --> U[Assign failed data quality status and block healthy serving]

    Q --> V[Create or update dataset version]
    R --> V
    S --> V
    T --> V
    U --> W[Record validation failure and keep previous trusted data if available]

    V --> X[Record lineage from source to serving output]
    X --> Y[Publish quality-labeled data for serving]
    Y --> Z[Portfolio, watchlist, dashboard, and analytics consume data with quality status]

    W --> Z2[No new healthy serving data published]
```
