# IndiaRealTime

**~20 independent WordPress plugins, one per public data source, feed a single site that tracks live mandi prices, fuel prices, air quality, weather alerts, earthquakes, and cricket scores across India. It keeps serving good data even when the government API behind it doesn't.**

**Live site:** https://indiarealtime.com
**License:** [MIT](LICENSE)

## Website screenshots

| Web view | Mobile view |
|---|---|
| ![IndiaRealTime website web view](assets/website-webview.png) | ![IndiaRealTime website mobile view](assets/website-mobile.png) |

If you're building a data-aggregation site, a plugin-based architecture, or anything where "the upstream API will eventually lie to you" is a real design constraint, this is written for you. See [Challenges](https://github.com/padmarajnidagundi/indiarealtime-com/issues) below.

---

## Why India needs this

The data itself already exists and is mostly public. It's just scattered across dozens of separate government and PSU portals, each with its own format, update cadence, and (often) reliability problems. A farmer checking today's mandi price has to know Agmarknet exists. Someone checking whether it's safe to go outside needs to know CPCB publishes AQI, on a different site, in a different format. Fuel prices change daily and vary by state (different VAT rates), but each oil marketing company only publishes its own numbers, separately, for the cities it serves.

None of that requires new data to be collected. It requires someone to fetch what's already public, normalize the formats, and put mandi prices, fuel prices, AQI, weather alerts, and the rest in one place a person can actually check in a few seconds instead of five open tabs across five different government sites. That's the gap this project sits in.

## Why this exists (the engineering side)

Most "live data" sites in India either scrape once a day and call it real-time, or bolt a dozen unrelated widgets onto a page-builder theme until it can't be maintained. IndiaRealTime pulls from ~15 different public data sources (government APIs, exchanges, weather and seismic feeds) and turns each one into its own small, testable unit instead of one monolith.

## What we cover

| Category | Examples |
|---|---|
| Prices | Mandi (agricultural commodity), fuel & LPG by state/city, precious metals, currency conversion, mutual fund NAVs, FD rates, toll rates |
| Environment | Air quality (AQI, CPCB bands), weather alerts, earthquake alerts |
| Civic / time | Bank holidays, pincode lookups, timezone conversion |
| Culture | Panchang & muhurat timings, vrat calendar, rashifal |
| Sport | Live cricket scores |

Coverage is city/state-granular where the underlying data supports it. Fuel prices, for instance, are tracked per city, not a national average.

## How the site works, for visitors

- **Browse by location**: URLs follow a `/state/city/category/` pattern (e.g. a state page, drilling into a city, drilling into a specific data category like fuel prices or AQI). Most categories exist both as a national overview and a per-city detail page.
- **Compare prices**: a price-comparison view lines up a commodity or fuel type across cities/states side by side instead of making you open each city page separately.
- **Calculators**: a metals calculator converts live gold/silver rates by weight and purity instead of just showing a per-gram number.
- **Share cards**: data pages generate a shareable image card (price, date, source) sized for social platforms, so a fact can be shared without a screenshot.
- **Author hub**: every article is attributed to a real author with a profile page, not an anonymous byline. `/authors/` lists them, `/author/<name>/` shows their published work.

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

The core decision: **each data source is a fully independent plugin**, not a shared ingestion pipeline. A plugin owns its own fetch schedule, cache, and failure handling. If one government API changes its response format or goes down, exactly one plugin breaks. The other ~19 keep serving. `irt-api-health-monitor` exists because with that many independent moving parts, you need one place that watches all of them rather than checking each plugin's logs by hand.

## Challenges worth mentioning

Each of these got long enough to deserve its own page:

- [Serving stale data on purpose](notes/stale-cache-fallback.md): government and exchange APIs are not reliable, and the site still has to look reliable.
- [Accessibility and color are load-bearing](notes/cvd-safe-aqi-colors.md): every semantic color is checked against WCAG contrast and color-vision-deficiency simulation.
- [A hash has to agree across two languages](notes/cross-language-hash-parity.md): PHP and JavaScript disagree on integer overflow, and author attribution depends on them agreeing anyway.
- [Location routing without a rewrite-rule regex per state](notes/location-routing-without-regex.md): one routing path for every state and city page instead of one rewrite rule per region.
- [~20 plugins is a maintainability bet, not a free lunch](notes/plugin-per-source-tradeoff.md): fault isolation costs more surface area to keep consistent.

## Stack

- **WordPress** (custom theme, no page builder): PHP templates, vanilla JS/CSS
- **~20 custom plugins**, one per data source, each with its own fetch/cache layer
- **MySQL** for storage and transient caching; Docker Compose for local dev
- Schema.org structured data via a dedicated plugin (`irt-dataset-schema`)
- IndexNow integration for near-instant search engine indexing on data updates

## What's next

- Historical price tracking currently exists for fuel and AQI, not yet for mandi/commodity prices. Extending it there is the next real data gap to close.
- More granular city coverage as sources allow it.
- Broadening the accessibility audit in `STYLE-GUIDE.md` past color contrast to full keyboard/screen-reader passes.

## Talk to me

This repo is a project overview, not the source. The codebase is closed for now, so there's nothing to PR against. But if you've solved a version of any of the problems above (stale-cache fallback strategies, plugin-per-source architectures, CVD-safe color systems, cross-language hash parity), or you're hitting the same wall right now, open a [discussion](https://github.com/padmarajnidagundi/indiarealtime-com/issues). Genuinely want to compare notes.

<!-- TODO: contact / social links -->
