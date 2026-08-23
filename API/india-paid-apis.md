# Paid India Data APIs

Commercial data sources and premium tiers for each category IndiaRealTime covers. These are premium/paid APIs that offer more comprehensive data, higher rate limits, better uptime guarantees, or dedicated support compared to free alternatives.

| Category | Source | Endpoint / access | Pricing Model | Key Features |
|---|---|---|---|---|
| Mandi (commodity) prices | Agmarknet Premium | [data.gov.in](https://www.data.gov.in/catalog/current-daily-price-various-commodities-various-markets-mandi) | Pay-per-call, Pro plans available | Higher rate limits, historical data, custom reports |
| Currency conversion | XE.com API | [xecdapi.xe.com](https://www.xe.com/xecurrencydata/) | Monthly subscription | Real-time rates, 150+ currencies, enterprise SLA |
| Currency conversion (alt) | Oanda fxTrade | [developer.oanda.com](https://developer.oanda.com/) | Monthly: $50-500+ | Live streaming rates, 300+ instruments, account integration |
| Stock market data | NSE EQ Live Data Feed | [nseindia.com/products/data-services](https://www.nseindia.com/products/data-services.jsp) | Monthly: ₹5,000-50,000+ | Real-time quotes, order book, trades, OI data |
| Stock market data (alt) | BSE Real-time API | [bseindia.com/bsedatalinkconnect](https://www.bseindia.com/bsedatalinkconnect/) | Custom pricing | Live L1/L2/L3 feeds, basket data, corporate actions |
| Precious metals (gold/silver) | IBJA Rates API | Contact for premium | Custom enterprise pricing | Certified IBJA hallmark rates, live updates, historical |
| Fuel/LPG prices | Oil Company Direct API | Direct contract with IOCL/BPCL/HPCL | Custom enterprise pricing | Real-time pump prices, dealer networks, bulk ordering |
| FD rates | RBI Credit Information Bureau | [cibil.com/api](https://www.cibil.com/) | Per-query, monthly plans | Interest rates, product catalogs, rate history across lenders |
| Toll rates | NHAI FASTag API | [www.nhai.gov.in/fast-tag](https://www.nhai.gov.in/en/fast-tag) | Enterprise contract | Live toll rates, lane data, real-time collection data |
| Air quality (AQI) | Ambee | [ambeehealth.com/api/aqi](https://www.ambeehealth.com/api/aqi/) | Starting ₹2,000/month | Real-time hyperlocal AQI, 24hr+ historical, health index |
| Air quality (alt) | Breezometer | [breezometer.com/air-quality-api](https://www.breezometer.com/air-quality-api) | Starting $200/month | Detailed pollutants, health score, pollen, fire data |
| Weather alerts | IMD Dedicated Feed | [mausam.imd.gov.in/premium](https://mausam.imd.gov.in/) | Enterprise contracts available | Official IMD alerts, regional warnings, seasonal forecasts |
| Weather alerts (alt) | OpenWeatherMap Pro | [openweathermap.org/api](https://openweathermap.org/api) | Starting $9.99/month | High-resolution forecasts, real-time alerts, historical data |
| Earthquake alerts | USGS Premium Access | [earthquake.usgs.gov](https://earthquake.usgs.gov/fdsnws/) | Enterprise contracts | Dedicated endpoints, 24/7 support, advanced filtering |
| Earthquake alerts (alt) | Risk.net Seismic Feed | Contact for pricing | Custom enterprise | Analyzed risk data, engineering parameters, IoT integration |
| Bank holidays | RBI Calendar Pro | Direct from RBI | By request, government only | Validated holiday calendars, advance announcements, updates |
| Pincode lookup | India Post Premium | [indiapost.gov.in](https://indiapost.gov.in/) | Per-transaction, bulk discounts | Complete postal data, delivery zones, tracking, rate cards |
| Pincode lookup (alt) | AddressAPI | [addressapi.in](https://www.addressapi.in/) | Starting ₹500/month | Standardized addresses, geocoding, pincode-to-coordinates |
| Panchang / muhurat / vrat / rashifal | Prokerala API | [prokerala.com/api](https://www.prokerala.com/) | ₹1,000-5,000/month | Validated Hindu calendar, remedies, detailed predictions |
| Panchang (alt) | drikpanchang.com API | Direct contact | Custom pricing | Comprehensive calendar, event data, consultation bookings |
| Live cricket scores | CricketAPI Pro | [cricketapi.com](https://www.cricketapi.com/) | ₹500-2,000/month | Live ball-by-ball, commentary, stats, fantasy integration |
| Live cricket scores (alt) | Cricbuzz Cricket API | [cricbuzz.com/api](https://cricbuzz.com/) | Enterprise rates | Official commentary, schedules, rankings, media rights |
| GST data | Indian GST API | [api.vatbox.com](https://www.vatbox.com/) | Starting $99/month | GST filing, compliance checks, rate lookups by HSN/SAC |
| GST data (alt) | NIC e-Services API | [services.nic.in](https://services.nic.in/) | Government contract | Official GST SEZS data, filing confirmations, audit trails |
| Real estate prices | NoBroker API | [nobroker.in/api](https://www.nobroker.in/) | Monthly subscription | Property listings, price trends, area insights, analytics |
| Real estate prices (alt) | Zomato Restaurant Data | [zomato.com/api](https://www.zomato.com/api) | Starting ₹5,000/month | Merchant data, order integrations, delivery partners |
| Transport / Transit | Uber Eats API | [developer.uber.com](https://developer.uber.com/) | Revenue share model | Restaurant integration, order tracking, driver data |
| News / Media | NewsAPI India | [newsapi.org](https://newsapi.org/) | Starter: $20/month | Real-time news filtering by location, language, keyword |

## Premium Tier Benefits

- **Higher Rate Limits**: 10,000-1,000,000+ requests/day instead of 100-1,000
- **Historical Data**: Access to 1-10+ years of historical records vs. real-time only
- **Dedicated Support**: 24/7 email/chat support, SLA guarantees
- **Custom Data Formats**: JSON, XML, CSV, or custom feeds
- **Webhook Support**: Real-time push notifications instead of polling
- **Authentication**: OAuth 2.0, API keys, certificate-based or VPN access
- **Compliance**: GDPR/CCPA-ready, audit logs, data residency options

## How to use this list

These APIs are ideal for production deployments requiring reliability, comprehensive data, and regulatory compliance. Free alternatives from `india-free-apis.md` can often be used with fallback/caching strategies for non-critical features. Mix both lists based on your SLA requirements and budget.

Know a paid India API that should be on this list? Open an issue or a PR against this file.
