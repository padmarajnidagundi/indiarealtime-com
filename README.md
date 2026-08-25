# IndiaRealTime - India Real Time | Live Mandi Prices, Fuel Rates, AQI, Weather Alerts & Cricket Scores

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/padmarajnidagundi/indiarealtime-com)
[![License: MIT](https://img.shields.io/github/license/padmarajnidagundi/indiarealtime-com)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/padmarajnidagundi/indiarealtime-com?style=social)](https://github.com/padmarajnidagundi/indiarealtime-com/stargazers)
[![Open issues](https://img.shields.io/github/issues/padmarajnidagundi/indiarealtime-com)](https://github.com/padmarajnidagundi/indiarealtime-com/issues)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](API/)

🌐 **Languages:** English · [हिन्दी](README.hi.md) · [বাংলা](README.bn.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [ಕನ್ನಡ](README.kn.md) · [മലയാളം](README.ml.md) · [ਪੰਜਾਬੀ](README.pa.md) · [ଓଡ଼ିଆ](README.or.md) · [অসমীয়া](README.as.md) · [اردو](README.ur.md) · [संस्कृतम्](README.sa.md) · [नेपाली](README.ne.md) · [कोंकणी](README.kok.md) · [मैथिली](README.mai.md)

## 🗂️ 19 Verticals, One Real Use Case Each

| Vertical | What You Get | Real India Use Case |
|---|---|---|
| Mandi Prices | Live agricultural commodity prices by market, state, and city | A Punjab wheat farmer compares APMC Ludhiana vs. Amritsar rates before deciding where to sell |
| Fuel Prices | Daily petrol/diesel rates by city and state | A Bengaluru cab driver checks rates across zones to plan the cheapest refuel stop |
| LPG Prices | Domestic and commercial cylinder rates by city | A household checks this month's cylinder price before booking a refill |
| Gold Rates | Live gold rates by weight and purity (22K/24K) | A Mumbai family shopping for a wedding checks today's 22K rate before visiting the jeweller |
| Silver Rates | Live silver rates by weight | An investor tracks silver price swings before buying coins for Dhanteras |
| Currency Exchange | INR conversion rates against major currencies | An NRI in Dubai checks the INR/AED rate before wiring money home |
| Mutual Fund NAVs | Daily NAV for tracked mutual fund schemes | A first-time investor in Pune checks their SIP fund's NAV before the monthly top-up |
| FD Rates | Fixed deposit interest rates by bank | A retiree in Chennai compares FD rates across banks before renewing a deposit |
| Toll Rates | Highway toll rates by route | A trucker planning a Delhi–Mumbai run checks toll costs to budget the trip |
| Air Quality Index | AQI and CPCB pollution bands by city | A Delhi parent checks AQI before deciding if the kids can play outside |
| Weather Alerts | Government weather warnings by state | A Kerala fisherman checks storm alerts before heading out to sea |
| Earthquake Alerts | Recent seismic activity | A Shillong resident checks recent tremors after feeling one |
| Bank Holidays | State-wise bank holiday calendar | A Kolkata shop owner checks if the bank is open before sending an urgent payment |
| Pincode Lookup | Address/post office lookup by pincode | An online seller verifies a buyer's pincode before confirming a shipment |
| Timezone Conversion | IST to global timezone conversion | A Bengaluru developer scheduling a call with a US client converts IST to EST instantly |
| Panchang & Muhurat | Daily panchang and auspicious timings | A family checks today's muhurat before fixing a housewarming date |
| Vrat Calendar | Fasting-day calendar (Ekadashi and others) | A devotee checks the next Ekadashi date to plan their fast |
| Rashifal | Daily horoscope by zodiac sign | A reader checks today's rashifal before starting the day |
| Live Cricket Scores | Real-time match scores and updates | A commuter on a train checks the live score without opening a heavier app |

**~20 independent WordPress plugins, one per public data source, feed a single site that tracks live mandi prices, fuel prices, air quality, weather alerts, earthquakes, and cricket scores across India. It keeps serving good data even when the government API behind it doesn't.**

**Live site:** https://indiarealtime.com

## Website screenshots

| Web view | Mobile view |
|---|---|
| ![IndiaRealTime website web view](assets/website-webview.png) | ![IndiaRealTime website mobile view](assets/website-mobile.png) |

---

## 📱 About IndiaRealTime

### The Problem

The data itself already exists and is mostly public. It's just scattered across dozens of separate government and PSU portals, each with its own format, update cadence, and (often) reliability problems.

A farmer checking today's mandi price has to know Agmarknet exists. Someone checking whether it's safe to go outside needs to know CPCB publishes AQI, on a different site, in a different format. Fuel prices change daily and vary by state (different VAT rates), but each oil marketing company only publishes its own numbers, separately, for the cities it serves.

None of that requires new data to be collected. It requires someone to fetch what's already public, normalize the formats, and put mandi prices, fuel prices, AQI, weather alerts, and the rest in one place a person can actually check in a few seconds instead of five open tabs across five different government sites. **That's the gap IndiaRealTime fills.**

### Real User Stories

**🌾 Rajesh - Farmer in Punjab**
> "I sell wheat at APMC Ludhiana. Every morning I had to visit 3 different websites to check prices in nearby markets to negotiate better rates. Now I check indiarealtime in 10 seconds before heading to the market."

**🚖 Priya - Auto Driver in Bangalore**
> "Fuel prices change daily and affect my earnings. I used to call friends in different cities to know rates. Now I check one app, see petrol/diesel prices across Bangalore to plan my routes."

**👨‍👩‍👧 Amit - Parent in Delhi**
> "Before letting my kids play outside, I need to check AQI. I used to google 5 different sources - Agmarknet, CPCB, weather sites - all showing different formats. Now one click and I know if it's safe to go out."

### What We Track

| Category | Examples |
|---|---|
| Prices | Mandi (agricultural commodity), fuel & LPG by state/city, precious metals, currency conversion, mutual fund NAVs, FD rates, toll rates |
| Environment | Air quality (AQI, CPCB bands), weather alerts, earthquake alerts |
| Civic / time | Bank holidays, pincode lookups, timezone conversion |
| Culture | Panchang & muhurat timings, vrat calendar, rashifal |
| Sport | Live cricket scores |

Coverage is city/state-granular where the underlying data supports it. Fuel prices, for instance, are tracked per city, not a national average.

The full list of free India data APIs behind this, including the government ones the site doesn't use yet, is in [API/](API/).

### How It Works for Visitors

- **Browse by location**: URLs follow a `/state/city/category/` pattern (e.g. a state page, drilling into a city, drilling into a specific data category like fuel prices or AQI). Most categories exist both as a national overview and a per-city detail page.
- **Compare prices**: a price-comparison view lines up a commodity or fuel type across cities/states side by side instead of making you open each city page separately.
- **Calculators**: a metals calculator converts live gold/silver rates by weight and purity instead of just showing a per-gram number.
- **Share cards**: data pages generate a shareable image card (price, date, source) sized for social platforms, so a fact can be shared without a screenshot.
- **Author hub**: every article is attributed to a real author with a profile page, not an anonymous byline. `/authors/` lists them, `/author/<name>/` shows their published work.

---

## 🏗️ Architecture of the Web Application

Most "live data" sites in India either scrape once a day and call it real-time, or bolt a dozen unrelated widgets onto a page-builder theme until it can't be maintained. IndiaRealTime pulls from ~15 different public data sources (government APIs, exchanges, weather and seismic feeds) and turns each one into its own small, testable unit instead of one monolith.

If you're building a data-aggregation site, a plugin-based architecture, or anything where "the upstream API will eventually lie to you" is a real design constraint, this is written for you.

### Technical Diagram

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

### Design Philosophy

**Each data source is a fully independent plugin**, not a shared ingestion pipeline. A plugin owns its own fetch schedule, cache, and failure handling. If one government API changes its response format or goes down, exactly one plugin breaks. The other ~19 keep serving. `irt-api-health-monitor` exists because with that many independent moving parts, you need one place that watches all of them rather than checking each plugin's logs by hand.

### Stack

- **WordPress** (custom theme, no page builder): PHP templates, vanilla JS/CSS
- **~20 custom plugins**, one per data source, each with its own fetch/cache layer
- **MySQL** for storage and transient caching; Docker Compose for local dev
- Schema.org structured data via a dedicated plugin (`irt-dataset-schema`)
- IndexNow integration for near-instant search engine indexing on data updates

---

## 👨‍💻 How Developers Can Use It

If you're building features into your app that need Indian market data, live pricing, weather, or AQI - you can use IndiaRealTime as a Python package, command-line tool, or REST API.

### Installation

**Python SDK (recommended)**
```bash
pip install indiarealtime
```

**📦 View on PyPI:** https://pypi.org/project/indiarealtime/

**From source**
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com
pip install -e .
```

### Real-Life Integration Examples

#### Example 1: Farmer Checking Mandi Prices (CLI)
```bash
# Get wheat prices in Punjab
$ indiarealtime mandi --commodity wheat --state Punjab

Commodity  Market           State         City      Price (₹)  Unit
wheat      APMC Ludhiana    Punjab        Ludhiana  2450       Quintal
wheat      APMC Amritsar    Punjab        Amritsar  2420       Quintal
```

#### Example 2: Startup Building Price Alert Bot (Python)
```python
from indiarealtime import IndiaRealTime

irt = IndiaRealTime()

# Get current wheat prices
prices = irt.mandi_prices(commodity="wheat", state="Punjab", limit=5)

for price in prices:
    print(f"📊 {price.market}: ₹{price.price}/{price.unit}")
    
    # Alert if price drops below ₹2400
    if price.price < 2400:
        send_sms_alert(f"Wheat at {price.market} is ₹{price.price}!")
```

#### Example 3: Delivery App Checking Fuel Prices (REST API)
```javascript
// Fetch fuel prices for driver earnings calculation
fetch('http://localhost:5000/v1/fuel/prices?state=Maharashtra&type=diesel')
  .then(r => r.json())
  .then(data => {
    data.results.forEach(price => {
      console.log(`Diesel in ${price.city}: ₹${price.price}/L`);
    });
  });
```

#### Example 4: News Website Scraping AQI (Python)
```python
from indiarealtime import IndiaRealTime
import requests

irt = IndiaRealTime()
aqi = irt.air_quality(city="Delhi")

if aqi[0].aqi > 300:
    # Post alert headline
    headline = f"🚨 Air Quality SEVERE in {aqi[0].city}: AQI {aqi[0].aqi}"
    post_to_website(headline)
```

#### Example 5: Finance Dashboard Showing Rates (React)
```jsx
import { useState, useEffect } from 'react';

function CurrencyRates() {
  const [rates, setRates] = useState({});
  
  useEffect(() => {
    fetch('/api/v1/finance/currency?base=INR&symbols=USD,EUR,GBP')
      .then(r => r.json())
      .then(d => setRates(d.rates));
  }, []);
  
  return (
    <div>
      <h2>INR Exchange Rates</h2>
      <p>1 INR = ${rates.USD?.toFixed(4)} USD</p>
      <p>1 INR = €{rates.EUR?.toFixed(4)} EUR</p>
    </div>
  );
}
```

### Local Development Setup (Docker)
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com

# Start all services
docker-compose up

# WordPress at http://localhost:8080
# API Server at http://localhost:5000
# Monitoring at http://localhost:3000
```

### Try It Yourself

`scripts/fetch-pincode.js` is a small standalone example of the fetch-and-normalize pattern the site's plugins use, pointed at one no-key-needed API from the list above:

```
node scripts/fetch-pincode.js 560001
```

### More Examples
- [FastAPI Server with auto-docs](examples/fastapi_server.py)
- [Telegram Bot for price alerts](examples/telegram_bot.py)
- [Google Sheets auto-update](examples/google_sheets_integration.py)
- [Next.js Dashboard](examples/nextjs_mandi_dashboard.tsx)

See [examples/README.md](examples/) for complete setup instructions.

---

## ⚠️ Technical Challenges

### Engineering Decisions & Lessons

Each of these challenges got long enough to deserve its own page:

- **[Serving stale data on purpose](notes/stale-cache-fallback.md)**: Government and exchange APIs are not reliable, and the site still has to look reliable. When an upstream API fails, we serve the last good cached value instead of erroring.
- **[Accessibility and color are load-bearing](notes/cvd-safe-aqi-colors.md)**: Every semantic color is checked against WCAG contrast and color-vision-deficiency simulation so data is accessible to everyone.
- **[A hash has to agree across two languages](notes/cross-language-hash-parity.md)**: PHP and JavaScript disagree on integer overflow, and author attribution depends on them agreeing anyway.
- **[Location routing without a rewrite-rule regex per state](notes/location-routing-without-regex.md)**: One routing path for every state and city page instead of one rewrite rule per region.
- **[~20 plugins is a maintainability bet, not a free lunch](notes/plugin-per-source-tradeoff.md)**: Fault isolation costs more surface area to keep consistent.

---

## 🚀 What's Next

- Historical price tracking currently exists for fuel and AQI, not yet for mandi/commodity prices. Extending it there is the next real data gap to close.
- More granular city coverage as sources allow it.
- Broadening the accessibility audit in `STYLE-GUIDE.md` past color contrast to full keyboard/screen-reader passes.

---

## 👋 About the Author

This repo is a project overview, not the site's source. The WordPress codebase is closed for now. However, the [API list](API/) and the `scripts/` folder are fair game for PRs — missing APIs, corrections, more fetch examples all welcome.

If you've solved a version of any of the problems above (stale-cache fallback strategies, plugin-per-source architectures, CVD-safe color systems, cross-language hash parity), or you're hitting the same wall right now, open a [discussion](https://github.com/padmarajnidagundi/indiarealtime-com/issues). I genuinely want to compare notes.

**Contributions welcome:** See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add new data sources as plugins, or [CONTRIBUTORS_GUIDE.md](CONTRIBUTORS_GUIDE.md) for other ways to help.

If you have questions or ideas, reach out via [GitHub Issues](https://github.com/padmarajnidagundi/indiarealtime-com/issues) or email.

<!-- TODO: contact / social links -->
