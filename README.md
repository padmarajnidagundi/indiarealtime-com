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

## What's technically interesting here

**One WordPress plugin per data source, not one plugin for everything.**
Fuel prices, gas prices, air quality, mutual fund NAVs, metals, currency, bank holidays, cricket scores, earthquakes, weather alerts, panchang/muhurat timings, pincode lookups, timezone conversion — each is its own self-contained plugin with its own fetch/cache/render cycle. A source going down or changing its response shape breaks one plugin, not the site. It also means each fetcher can be reasoned about, tested, and rate-limited independently — `irt-api-health-monitor` watches all of them from one place instead of guessing.

**Accessibility and color aren't an afterthought bolted on at the end.**
The design tokens (`ir-tokens.css`) are WCAG-contrast-verified *and* checked against color-vision deficiency (CVD) simulation — every semantic color (success/warning/danger, AQI severity bands) has a documented contrast ratio, not just a hex code someone liked. The AQI band colors specifically match the official CPCB bands rather than an arbitrary gradient, because getting that wrong on an air-quality site has real consequences for people who rely on it.

**A hand-rolled hash has to agree across two languages.**
The author-attribution system computes a hash on both the PHP backend and the JS frontend to keep author identity consistent — which means the JS implementation has to reproduce PHP's 32-bit integer overflow behavior exactly (`Math.imul`), or the two sides silently disagree. Small, unglamorous, and the kind of bug that only shows up in production with real data.

**No page builder, no bloat.** The theme is hand-written PHP templates and vanilla JS/CSS — chosen deliberately over Elementor/Gutenberg-block sprawl for page-speed reasons on a site where the entire point is "load fast, show current data."

## Data covered

Mandi (agricultural commodity) prices · fuel & LPG prices by state/city · air quality (AQI) · weather alerts · earthquake alerts · cricket scores · mutual fund NAVs · precious metals · currency conversion · bank holidays · panchang & muhurat timings · pincode data · toll rates · fixed deposit rates

## Stack

- **WordPress** (custom theme, no page builder) — PHP templates, vanilla JS/CSS
- **~20 custom plugins**, one per data source, each with its own fetch/cache layer
- **MySQL** for storage; Docker Compose for local dev
- Schema.org structured data via a dedicated plugin (`irt-dataset-schema`) so pages are machine-readable, not just human-readable
- IndexNow integration for near-instant search engine indexing on data updates

## Status

Actively developed. This repo is a project overview, not the source — the codebase is closed for now. If you're working on something similar (data aggregation, WordPress plugin architecture, accessibility tooling) and want to compare notes, open an issue or reach out.

<!-- TODO: contact / social links -->
