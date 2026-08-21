# IndiaRealTime

**Live, India-specific data — mandi prices, fuel prices, air quality, weather alerts, cricket scores, earthquake alerts, and more — updated continuously and served as a fast WordPress site.**

🔗 **Live site:** https://indiarealtime.com

<!-- TODO: add 2-4 screenshots or a GIF here, e.g.
![AQI dashboard](assets/aqi-dashboard.png)
![Fuel price city page](assets/fuel-prices.gif)
-->

---

## Why this exists

Most "live data" sites in India either scrape once a day and call it real-time, or bolt a dozen unrelated widgets onto a page-builder theme until it can't be maintained. IndiaRealTime pulls from ~15 different public data sources (government APIs, exchanges, weather and seismic feeds) and turns each one into its own small, testable unit instead of one monolith.

## What we cover

| Category | Examples |
|---|---|
| Prices | Mandi (agricultural commodity), fuel & LPG by state/city, precious metals, currency conversion, mutual fund NAVs, FD rates, toll rates |
| Environment | Air quality (AQI, CPCB bands), weather alerts, earthquake alerts |
| Civic / time | Bank holidays, pincode lookups, timezone conversion |
| Culture | Panchang & muhurat timings, vrat calendar, rashifal |
| Sport | Live cricket scores |

Coverage is city/state-granular where the underlying data supports it — fuel prices, for instance, are tracked per city, not just a national average.

## How the site works, for visitors

- **Browse by location**: URLs follow a `/state/city/category/` pattern (e.g. a state page, drilling into a city, drilling into a specific data category like fuel prices or AQI). Most categories exist both as a national overview and a per-city detail page.
- **Compare prices**: a price-comparison view lines up a commodity or fuel type across cities/states side by side instead of making you open each city page separately.
- **Calculators**: a metals calculator converts live gold/silver rates by weight and purity rather than just showing a per-gram number.
- **Share cards**: data pages generate a shareable image card (price, date, source) sized for social platforms, so a fact can be shared without a screenshot.
- **Author hub**: every article is attributed to a real author with a profile page, not an anonymous byline — `/authors/` lists them, `/author/<name>/` shows their published work.

## Architecture

```
Public data sources (govt APIs, exchanges, weather/seismic feeds, ~15 total)
        │
        ▼
One WordPress plugin per source  ──►  WP-Cron fetch on its own schedule
  (fetch → validate → normalize)       (e.g. every 6h for commodities/AQI,
        │                               daily for fuel prices)
        ▼
WP transient cache (MySQL-backed)  ◄── on fetch failure, keep serving the
        │                               last good cached value instead of
        ▼                               erroring or showing nothing
Custom theme templates (PHP)
  render location/category pages
        │
        ▼
irt-dataset-schema → schema.org JSON-LD  +  irt-api-health-monitor watches
  (machine-readable structured data)       all fetchers from one dashboard
        │
        ▼
IndexNow ping on update → search engines re-crawl fresh data within minutes,
  not on their own schedule
```

The core decision: **each data source is a fully independent plugin**, not a shared ingestion pipeline. A plugin owns its own fetch schedule, cache, and failure handling. If one government API changes its response format or goes down, exactly one plugin breaks — the other ~19 keep serving. `irt-api-health-monitor` exists because with that many independent moving parts, you need one place that watches all of them rather than checking each plugin's logs by hand.

## Challenges worth mentioning

**Government and exchange APIs are not reliable, and the site still has to look reliable.**
Fuel price and commodity sources fail, rate-limit, or return malformed data often enough that "just show what the API returned" isn't viable. The fix was a stale-while-revalidate style cache: fetch fails silently fall back to the last successfully cached value (comment in the code literally says *"serving yesterday's cached transient value"*), with a short-lived failure flag so retries don't hammer a source that's already down. Visitors see a slightly-stale number instead of a broken page.

**Accessibility and color are load-bearing, not decorative.**
Every semantic color — success/warning/danger states, the AQI severity scale — is checked against WCAG contrast ratios *and* color-vision-deficiency (CVD) simulation, and documented with the actual ratio next to the hex code. The AQI bands specifically match the official CPCB scale rather than an arbitrary gradient, because an air-quality site getting a color wrong has real consequences for someone deciding whether to go outside.

**A hash has to agree across two languages.**
Author attribution computes a hash on the PHP backend and again in JS on the frontend. PHP and JavaScript disagree on integer overflow by default, so the JS side has to explicitly use `Math.imul` to reproduce PHP's 32-bit wraparound — otherwise the two sides silently compute different values and attribution breaks in a way that's invisible until someone checks production data.

**Location-based routing without a rewrite-rule regex per state.**
Every Indian state and city page shares one routing path (`ir_state` / `ir_sub` / `ir_sub2` query vars parsed from the URL) instead of a hand-written WordPress rewrite rule per region — necessary at this scale, but it means URL parsing has its own edge cases (trailing slashes, category vs. city ambiguity) that get covered by dedicated test files rather than caught by hand.

**~20 plugins is a maintainability bet, not a free lunch.**
The upside is fault isolation and independent scheduling; the tradeoff is more surface area to keep consistent — shared conventions (transient naming, cache durations, failure-flag patterns) have to be enforced by discipline and code review rather than a shared framework, since each plugin is deliberately self-contained.

## Stack

- **WordPress** (custom theme, no page builder) — PHP templates, vanilla JS/CSS
- **~20 custom plugins**, one per data source, each with its own fetch/cache layer
- **MySQL** for storage and transient caching; Docker Compose for local dev
- Schema.org structured data via a dedicated plugin (`irt-dataset-schema`)
- IndexNow integration for near-instant search engine indexing on data updates

## Status

Actively developed. This repo is a project overview, not the source — the codebase is closed for now. If you're working on something similar (data aggregation, WordPress plugin architecture, accessibility tooling) and want to compare notes, open an issue or reach out.

<!-- TODO: contact / social links -->
