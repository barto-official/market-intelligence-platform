# Workflow: Check Portfolio/Watchlist Market Position

## Actors

- Authenticated Investor
- Market Intelligence Platform
- Portfolio/Watchlist Context
- Market Data Foundation
- Data Quality/Freshness Process

## Trigger

The investor opens the platform to understand the current state of assets they care about.

## Main path

1. Investor signs in and opens the dashboard, portfolio view, or watchlist view.
1. Platform loads the investor's watchlists and/or portfolio positions.
1. Platform retrieves latest available validated market data and selected financial metrics for the relevant assets.
1. Platform calculates basic derived values, such as current position value and simple gain/loss where supported.
1. Platform displays assets, positions, prices, metrics, and freshness/quality indicators.
1. Investor reviews the current state and decides whether further investigation is needed.
1. Investor may open an asset detail view, update a position, add/remove assets, or report a data issue.

## Alternative paths

- Investor checks only watchlist, not portfolio.
- Investor checks only asset detail view.
- Platform shows partial data with explicit quality/freshness indicators.
- Investor uses the dashboard as a quick daily check-in rather than a deep analysis view.

## Failure paths

- Portfolio/watchlist cannot be loaded.
- Market data is stale, missing, or degraded.
- Position valuation cannot be calculated.
- Asset metadata is incomplete.
- User sees incorrect or confusing data and reports an issue.
- Authorization failure prevents access to user-owned investing context.

## Business outcome

The investor can quickly understand the current market state of assets they care about, with enough trust signals to know whether the displayed information is fresh, complete, and reliable.
