# Free India Data APIs

Public/free data sources for each category IndiaRealTime covers. "Free" means a no-cost tier exists; check each source's rate limits and ToS before production use. Government sources are the ones this project prefers. Third-party fallbacks are marked where no official free API exists.

| Category | Source | Endpoint / access | Auth | Notes |
|---|---|---|---|---|
| Mandi (commodity) prices | Agmarknet via data.gov.in | [data.gov.in/catalog/current-daily-price...](https://www.data.gov.in/catalog/current-daily-price-various-commodities-various-markets-mandi) | Free API key (self-register) | Shared demo key caps at 10 records/request |
| Mandi prices (alt) | APISetu (Agri-Coop) | [directory.apisetu.gov.in/api-collection/agricoop](https://directory.apisetu.gov.in/api-collection/agricoop) | Free API key | Govt API gateway, same underlying data |
| Mutual fund NAVs | AMFI | [amfiindia.com/spages/NAVAll.txt](https://www.amfiindia.com/spages/NAVAll.txt) | None | Plain text, all AMCs, daily |
| Fuel/LPG prices | No official free API | n/a | n/a | State oil companies (IOCL/BPCL/HPCL) publish per-city rates on their own sites only, so this is scraped in practice |
| Precious metals (gold/silver) | No official free API | n/a | n/a | Third-party freemium (e.g. metals-api.com, goldapi.io); no govt source |
| Currency conversion | RBI reference rate via data.gov.in | search "RBI reference rate" on [data.gov.in](https://www.data.gov.in) | Free API key | Third-party fallback: [open.er-api.com](https://www.exchangerate-api.com/docs/free) (free, no key) |
| FD rates | No unified free API | n/a | n/a | Published per-bank individually, no aggregator |
| Toll rates | NHAI toll plaza data | search "NHAI toll" on [data.gov.in](https://www.data.gov.in) | Free API key | Static/periodic dataset, not live |
| Air quality (AQI) | CPCB real-time AQI via data.gov.in | [data.gov.in/resource/real-time-air-quality-index-various-locations](https://www.data.gov.in/resource/real-time-air-quality-index-various-locations) | Free API key | Official source; station coverage varies by city |
| Air quality (alt) | WAQI | [aqicn.org/api](https://aqicn.org/api/) | Free token | Aggregates CPCB and others, easier JSON |
| Air quality (alt) | OpenAQ | [docs.openaq.org](https://docs.openaq.org/) | Free API key | Aggregates CPCB, global format |
| Weather alerts | No official free IMD API | n/a | n/a | IMD (mausam.imd.gov.in) has no public API; fallback is [OpenWeatherMap](https://openweathermap.org/api) free tier |
| Earthquake alerts | NCS (no public API) | [seismo.gov.in/data-portal](https://seismo.gov.in/data-portal) | n/a | Portal/app only, no documented free API |
| Earthquake alerts (fallback) | USGS, filtered to India bbox | [earthquake.usgs.gov/fdsnws/event/1/](https://earthquake.usgs.gov/fdsnws/event/1/) | None | Global feed; filter `minlatitude/maxlatitude/minlongitude/maxlongitude` to India |
| Bank holidays | RBI holiday list via data.gov.in | search "bank holidays" on [data.gov.in](https://www.data.gov.in) | Free API key | Updated yearly |
| Pincode lookup | India Post via postalpincode.in | [api.postalpincode.in/pincode/{code}](https://www.postalpincode.in/Api-Details) | None | Official India Post data, no key needed |
| Timezone conversion | Stdlib only | n/a | n/a | India is a single fixed offset (UTC+5:30, no DST), so no API is needed |
| Panchang / muhurat / vrat / rashifal | No official free API | n/a | n/a | Third-party freemium only (e.g. Prokerala API); typically scraped |
| Live cricket scores | CricAPI | [cricapi.com](https://cricapi.com/) | Free tier key | Free tier is rate-limited |
| Live cricket scores (alt) | Cricbuzz (via RapidAPI) | [rapidapi.com/.../cricbuzz-cricket](https://rapidapi.com/) | Free tier key | Freemium, unofficial |

## How to use this list

Each row maps to one plugin in the `~20 independent WordPress plugins` architecture (see repo [README](../README.md)). Rows with no official free API are the ones where the site's stale-cache fallback strategy matters most, since the fetcher is more likely to break or get rate-limited.
