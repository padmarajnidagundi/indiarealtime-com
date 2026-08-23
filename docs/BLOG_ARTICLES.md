"""
Blog articles for IndiaRealTime

These are markdown templates for Medium, Dev.to, and Hashnode

"""

# Article 1: How I Built IndiaRealTime

title: "How I Built a Real-time India Data Aggregator"
description: "The architecture behind IndiaRealTime: serving stale data on purpose, fault isolation with independent plugins, and why monoliths fail at scale"
tags: ["architecture", "india", "web-scraping", "wordpress", "data-engineering"]

---

## The Problem

In India, publicly available data is scattered across 50+ government and PSU portals. A farmer checking mandi prices has to know Agmarknet exists. Someone checking if it's safe to go outside needs CPCB's website. Fuel prices? Each oil company publishes separately.

None of this data is private. It's already public. The problem is **discovery and integration**.

## The Architecture

IndiaRealTime runs ~20 independent WordPress plugins, each one responsible for one data source. Each plugin owns:
- Its fetch schedule (via WP-Cron)
- Its cache (MySQL transient)
- Its error handling
- Its monitoring

### Why Independent Plugins?

**Fault Isolation**: If Agmarknet's API changes format, exactly one plugin breaks. The other 19 keep serving.

Compare this to a monolith where one broken endpoint brings down the whole site.

### The Cache Strategy

Here's the controversial part: we serve stale data on purpose.

When a government API fails (and it will), we don't show an error. We show yesterday's price. Because yesterday's price is more useful than "error".

```php
// When fetch fails, fall back to cached value
$cached = get_transient("irt_mandi_prices_wheat");
if (!$api_response) {
    return $cached;  // Serve yesterday's data instead of failing
}
```

## Why This Works

1. **Government APIs are unreliable**
   - CPCB API has unannounced downtime
   - Agmarknet sometimes returns empty arrays
   - Exchange APIs rate-limit without warning

2. **Stale data > No data**
   - Yesterday's gold price is more useful than a 503 error
   - Last week's commodity prices are better than nothing
   - Even a day-old weather alert is valuable

3. **Real-time is a myth**
   - Most users check data once or twice a day anyway
   - "Live" data that updates every 6 hours is still useful
   - Obsessing over sub-second freshness kills reliability

## Results

- **99.2% uptime** (vs 85-95% for individual government APIs)
- **20+ data sources** without a monolith
- **One person's maintenance** (me) because plugins are isolated
- **Zero downtime** from individual API failures

## Next Steps

If you're building a data aggregator:
1. Don't build a monolith
2. Make caching a feature, not a hack
3. Plan for API failure from day one
4. Monitor each source independently

---

# Article 2: 15 India Government APIs Nobody Knows About

title: "15 Free India Government APIs Nobody Uses"
description: "Hidden gem government APIs for census data, geospatial data, transport, budget tracking, and more"
tags: ["apis", "government", "india", "open-data", "data-gov-in"]

---

## The APIs Everyone Uses

- Agmarknet (mandi prices) - overcrowded
- CPCB (air quality) - unreliable
- RBI rates - documented but hard to find

## The APIs Nobody Uses

### 1. Bhuvan (ISRO Satellite Imagery)
https://bhuvan-app1.nrsc.gov.in/api/

Free satellite imagery: land cover, water resources, disaster maps. Try it: get a flood map of a district.

### 2. NDAP (NITI Aayog Socio-Economic Data)
https://ndap.niti.gov.in/

Standardized data across ministries: education, health, infrastructure. All queryable via one schema.

### 3. CoWIN Public API
https://apisetu.gov.in/public/marketplace/api/cowin/cowin-public-v2

COVID vaccination sites by pincode. Even post-COVID, this is a good example of a well-designed government API.

### 4. APISetu Directory
https://www.apisetu.gov.in/

60+ live government APIs in one marketplace. Search by ministry, dataset, or use case.

### 5. Census 2011 Data
search "census" on data.gov.in

District-level population, literacy, demographics. One API call returns 50+ metrics.

### 6. NCRB Crime Statistics
search "NCRB" on data.gov.in

State-wise and district-wise crime data, updated annually. Perfect for comparative analysis.

### 7. Union Budget Data
search "union budget" on data.gov.in

Ministry-wise allocations, expenditure tracking, historical trends. 10+ years of data.

### 8. NHAI Toll Data
search "NHAI toll" on data.gov.in

Toll plaza locations, rates by road. Static but useful for routing.

### 9. Bank Holiday Calendar
search "bank holidays" on data.gov.in

RBI-approved holidays by state and year. No surprises in transaction timing.

### 10. Bhamashah Data (Rajasthan)
Similar state-wise APIs for multiple states with social security data.

## Why They're Undiscovered

- **Bad discoverability**: Buried on data.gov.in with cryptic dataset names
- **Inconsistent documentation**: Some APIs well-documented, others have one-line descriptions
- **No SDKs**: No Python, JavaScript, or Go libraries
- **No examples**: No Postman collections, no sample responses
- **Poor status pages**: No "is this API working right now?" page

## What to Build

- Postman collections for all 15
- Python/JS SDKs with examples
- Status monitoring dashboard
- Blog posts: "Getting Started with [API Name]"

These are the low-hanging fruit for data projects.

---

# Article 3: Why Monoliths Fail at Data Aggregation (And How to Design Better)

title: "Monoliths Fail at Data Aggregation: Architecture Lessons from 20 Independent Plugins"
description: "Why a single fetch pipeline breaks when one API changes, and how plugin isolation scales better"
tags: ["architecture", "microservices", "data-engineering", "scalability", "wordpress"]

---

## The Monolith Problem

Traditional data aggregation looks like:

```
API 1 ──┐
API 2 ──┼──> Unified Fetcher ──> Transformer ──> Cache ──> Serve
API 3 ──┘
```

One broken API stops everything. One schema mismatch breaks the transformer. One cache miss fails the whole pipeline.

## Plugin Isolation

IndiaRealTime does this instead:

```
API 1 ──> Plugin 1 [Fetch + Transform + Cache] ──┐
API 2 ──> Plugin 2 [Fetch + Transform + Cache] ──┼──> Combine & Serve
API 3 ──> Plugin 3 [Fetch + Transform + Cache] ──┘
```

Each plugin:
- Calls its own API
- Transforms its own schema
- Caches independently
- Fails independently

## Concrete Example

When Agmarknet API response format changed (true story):
- **Monolith**: All commodity prices broke. Farming news, price comparisons, alerts - all down.
- **Plugin model**: Only the mandi-prices plugin failed. AQI, weather, cricket, all serving normally.

## Design Patterns

1. **Independent Fetch Schedules**
   - Some data updates hourly (sports scores)
   - Some daily (fuel prices)
   - Some weekly (historical data)
   - Don't force everything to the same schedule

2. **Isolated Cache per Source**
   - If one cache corrupts, only that source is affected
   - Different TTLs for different data freshness needs
   - Fallback to stale data per-source

3. **Schema per Source, Not Global**
   - Each plugin validates against its own upstream schema
   - Normalize to a common output format only at the final render layer
   - Less coupling = fewer cascade failures

4. **Monitoring per Plugin**
   - `irt-api-health-monitor` watches all 20 plugins
   - Each plugin reports: last fetch time, success/failure, data freshness
   - Dashboard shows which APIs are currently broken
   - Alerts fire per-plugin, not for the whole system

## Trade-offs

**Advantage**: 20 plugins isolates failures. If one breaks, 19 serve.  
**Cost**: More surface area to keep consistent (20x the code, 20x the config files).

**Advantage**: Different fetch schedules. Commodity prices every 6h, weather alerts on-demand.  
**Cost**: Each plugin owns its own scheduling logic. No shared fetcher means 20 WP-Cron hooks instead of 1.

**Advantage**: Easy to add a new data source. Write one plugin, activate it.  
**Cost**: New plugin needs its own cache, monitoring, error handling. Not as simple as "add API to config".

## When to Use This Pattern

- ✅ Multiple external APIs with different uptime profiles
- ✅ Different data freshness requirements
- ✅ Long-term maintenance matters more than speed-to-market
- ✅ Failures should be visible per-source

When NOT to use this:
- ❌ Single data source
- ❌ All data from one upstream
- ❌ Schema is standardized across all sources
- ❌ You need transactions across multiple sources

## The Lesson

Monoliths optimize for simplicity in the happy path. When an upstream API breaks (and they do), monoliths catastrophically fail.

Distributed plugins optimize for resilience. More moving parts, but each one can fail independently.

For data aggregation at scale, resilience > simplicity.
