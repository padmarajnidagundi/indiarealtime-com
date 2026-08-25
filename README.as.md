# IndiaRealTime

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/padmarajnidagundi/indiarealtime-com)
[![License: MIT](https://img.shields.io/github/license/padmarajnidagundi/indiarealtime-com)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/padmarajnidagundi/indiarealtime-com?style=social)](https://github.com/padmarajnidagundi/indiarealtime-com/stargazers)
[![Open issues](https://img.shields.io/github/issues/padmarajnidagundi/indiarealtime-com)](https://github.com/padmarajnidagundi/indiarealtime-com/issues)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](API/)

🌐 **ভাষা:** [English](README.md) · [हिन्दी](README.hi.md) · [বাংলা](README.bn.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [ಕನ್ನಡ](README.kn.md) · [മലയാളം](README.ml.md) · [ਪੰਜਾਬੀ](README.pa.md) · [ଓଡ଼ିଆ](README.or.md) · অসমীয়া · [اردو](README.ur.md) · [संस्कृतम्](README.sa.md) · [नेपाली](README.ne.md) · [कोंकणी](README.kok.md) · [मैथिली](README.mai.md)

**~20 টা স্বতন্ত্ৰ WordPress প্লাগইন, প্ৰতিটো এটা পৃথক ৰাজহুৱা ডেটা উৎসৰ বাবে, একেলগে এখন চাইট চলায় যিয়ে গোটেই ভাৰতত লাইভ মণ্ডি দাম, জ্বালানী দাম, বায়ুৰ গুণগত মান, বতৰৰ সতৰ্কবাণী, ভূমিকম্প আৰু ক্ৰিকেট স্ক‌ʼৰ ট্ৰেক কৰে। ইয়াৰ পিছৰ চৰকাৰী API এ কাম কৰা বন্ধ কৰি দিলেও ই ভাল ডেটা দিয়া অব্যাহত ৰাখে।**

**লাইভ চাইট:** https://indiarealtime.com

## ৱেবছাইট স্ক্ৰীণশ্বট

| ৱেব ভিউ | মবাইল ভিউ |
|---|---|
| ![IndiaRealTime website web view](assets/website-webview.png) | ![IndiaRealTime website mobile view](assets/website-mobile.png) |

---

## 📱 IndiaRealTime ৰ বিষয়ে

### সমস্যাটো কি

ডেটা ইতিমধ্যে আছে, বেছিভাগেই ৰাজহুৱা। ই মাত্ৰ বহুতো পৃথক চৰকাৰী আৰু PSU পৰ্টেলত সিঁচৰতি হৈ আছে, প্ৰতিটোৰে নিজৰ ফৰ্মেট, আপডেট হোৱাৰ সময়, আৰু (প্ৰায়ে) নিৰ্ভৰযোগ্যতাৰ সমস্যা।

পঞ্জাৱত মণ্ডি দাম চাব বিচৰা এজন কৃষকে জনা দৰকাৰ যে Agmarknet বুলি কিবা এটা আছে। বাহিৰলৈ যোৱাটো সুৰক্ষিত নে নাই জানিব বিচৰা যিকোনো মানুহে জনা দৰকাৰ যে CPCB এ পৃথক ৱেবছাইটত, পৃথক ফৰ্মেটত AQI প্ৰকাশ কৰে। জ্বালানীৰ দাম প্ৰতিদিনে সলনি হয় আৰু ৰাজ্যৰ ওপৰত নিৰ্ভৰ কৰি বেলেগ হয় (বেলেগ VAT হাৰ), কিন্তু প্ৰতিটো তেল কোম্পানীয়ে কেৱল নিজে সেৱা দিয়া চহৰসমূহৰ বাবে, পৃথক পৃথকভাৱে, নিজৰ সংখ্যাহে প্ৰকাশ কৰে।

ইয়াৰ বাবে নতুন ডেটা সংগ্ৰহ কৰাৰ প্ৰয়োজন নাই। কেৱল কোনোবাই ইতিমধ্যে ৰাজহুৱা হৈ থকাটো আনি, ফৰ্মেটবোৰ সাধাৰণ কৰি, মণ্ডি দাম, জ্বালানী দাম, AQI, বতৰৰ সতৰ্কবাণী আদি এঠাইতে ৰাখিব লাগিব যাতে এজন ব্যক্তিয়ে পাঁচখন পৃথক চৰকাৰী চাইটৰ পাঁচটা টেব খোলাৰ পৰিৱৰ্তে কেইছেকেণ্ডমানতে চাব পাৰে। **এই ফাঁকটোৱেই IndiaRealTime এ পূৰণ কৰে।**

### প্ৰকৃত ব্যৱহাৰকাৰীৰ কাহিনী

**🌾 ৰাজেশ - পঞ্জাৱৰ কৃষক**
> "মই APMC লুধিয়ানাত গম বিক্ৰী কৰোঁ। প্ৰতিদিনে ৰাতিপুৱা ভাল দামত দৰদাম কৰিবলৈ ওচৰৰ বজাৰবোৰৰ দাম চাবলৈ মোক 3খন পৃথক ৱেবছাইট চাব লাগিছিল। এতিয়া বজাৰলৈ যোৱাৰ আগতে মই 10 ছেকেণ্ডত indiarealtime চাই লওঁ।"

**🚖 প্ৰিয়া - বেংগালুৰুৰ অটো চালক**
> "জ্বালানীৰ দাম প্ৰতিদিনে সলনি হয় আৰু মোৰ উপাৰ্জনত প্ৰভাৱ পেলায়। আগতে মই বিভিন্ন চহৰৰ বন্ধুক ফোন কৰি দাম গম পাইছিলোঁ। এতিয়া মই এটা এপতে বেংগালুৰু সৰহভাগ পেট্ৰল/ডিজেলৰ দাম চাই মোৰ পথ পৰিকল্পনা কৰোঁ।"

**👨‍👩‍👧 অমিত - দিল্লীৰ অভিভাৱক**
> "মোৰ শিশুক বাহিৰত খেলিবলৈ পঠোৱাৰ আগতে মই AQI চাব লাগে। আগতে মই 5টা পৃথক উৎস গুগল কৰিছিলোঁ - Agmarknet, CPCB, বতৰৰ চাইট - সকলো পৃথক ফৰ্মেটত। এতিয়া এক ক্লিকতে জানিব পাৰোঁ বাহিৰলৈ যোৱাটো সুৰক্ষিত নে নাই।"

### আমি কি ট্ৰেক কৰোঁ

| শ্ৰেণী | উদাহৰণ |
|---|---|
| দাম | মণ্ডি (কৃষি পণ্য), জ্বালানী আৰু LPG ৰাজ্য/চহৰ অনুসৰি, বহুমূলীয়া ধাতু, মুদ্ৰা ৰূপান্তৰ, মিউচুৱেল ফাণ্ড NAV, FD হাৰ, টোল হাৰ |
| পৰিৱেশ | বায়ুৰ গুণগত মান (AQI, CPCB বেণ্ড), বতৰৰ সতৰ্কবাণী, ভূমিকম্প সতৰ্কবাণী |
| নাগৰিক / সময় | বেংক বন্ধ, পিনকোড লুকআপ, সময় অঞ্চল ৰূপান্তৰ |
| সংস্কৃতি | পঞ্জিকা আৰু মুহূৰ্ত সময়, ব্ৰত কেলেণ্ডাৰ, ৰাশিফল |
| খেল | লাইভ ক্ৰিকেট স্ক‌ʼৰ |

মূল ডেটাই অনুমতি দিয়া ঠাইত কভাৰেজ চহৰ/ৰাজ্য স্তৰত সূক্ষ্ম। উদাহৰণস্বৰূপে, জ্বালানীৰ দাম ৰাষ্ট্ৰীয় গড় নহয়, প্ৰতিটো চহৰ অনুসৰি ট্ৰেক কৰা হয়।

ইয়াৰ পিছত থকা বিনামূলীয়া ভাৰতীয় ডেটা API ৰ সম্পূৰ্ণ তালিকা, চাইটে এতিয়াও ব্যৱহাৰ নকৰা চৰকাৰী API সহ, [API/](API/) ত আছে।

### দৰ্শকৰ বাবে এইটো কেনেকৈ কাম কৰে

- **স্থান অনুসৰি ব্ৰাউজ কৰক**: URL সমূহে `/state/city/category/` আৰ্হি অনুসৰণ কৰে (যেনে এখন ৰাজ্যৰ পৃষ্ঠা, তাৰ পিছত এখন চহৰলৈ যোৱা, তাৰ পিছত জ্বালানী দাম বা AQI ৰ দৰে কোনো নিৰ্দিষ্ট শ্ৰেণীলৈ)। বেছিভাগ শ্ৰেণী ৰাষ্ট্ৰীয় পৰ্যালোচনা আৰু চহৰ-নিৰ্দিষ্ট বিৱৰণ পৃষ্ঠা দুয়োটা ৰূপত আছে।
- **দাম তুলনা কৰক**: এটা প্ৰাইছ-কম্পেৰিজন ভিউৱে এটা সামগ্ৰী বা জ্বালানীৰ প্ৰকাৰক চহৰ/ৰাজ্যসমূহত কাষে কাষে দেখুৱায়, প্ৰতিটো চহৰৰ পৃষ্ঠা পৃথকে খোলাৰ পৰিৱৰ্তে।
- **কেলকুলেটৰ**: এটা মেটেল কেলকুলেটৰে কেৱল প্ৰতি-গ্ৰাম সংখ্যা দেখুওৱাৰ পৰিৱৰ্তে লাইভ সোণ/ৰূপৰ হাৰক ওজন আৰু শুদ্ধতা অনুসৰি ৰূপান্তৰ কৰে।
- **শ্বেয়াৰ কাৰ্ড**: ডেটা পৃষ্ঠাসমূহে ছ‌ʼচিয়েল প্লেটফৰ্মৰ বাবে উপযুক্ত আকাৰৰ শ্বেয়াৰযোগ্য ছবি কাৰ্ড (দাম, তাৰিখ, উৎস) সৃষ্টি কৰে, যাতে স্ক্ৰীণশ্বট নোহোৱাকৈয়ে এটা তথ্য শ্বেয়াৰ কৰিব পাৰি।
- **লেখক হাব**: প্ৰতিটো লেখাক এজন প্ৰকৃত লেখকক, তেওঁলোকৰ প্ৰ‌ʼফাইল পৃষ্ঠাসহ, কৃতিত্ব দিয়া হয়, বেনামী বাইলাইন নহয়। `/authors/` এ সকলোকে তালিকাভুক্ত কৰে, `/author/<name>/` এ তেওঁলোকৰ প্ৰকাশিত কাম দেখুৱায়।

---

## 🏗️ ৱেব এপ্লিকেচনৰ আৰ্কিটেকচাৰ

ভাৰতত বেছিভাগ "লাইভ ডেটা" চাইটে হয় দিনটোত এবাৰ স্ক্ৰেপ কৰি তাক ৰিয়েল-টাইম বুলি কয়, নহলে ই পৰিচালনা কৰিব নোৱাৰালৈকে এটা পেজ-বিল্ডাৰ থীমত ডজন ডজন অসম্পৰ্কিত ৱিজেট যোগ কৰি থাকে। IndiaRealTime এ প্ৰায় 15 টা পৃথক ৰাজহুৱা ডেটা উৎসৰ পৰা (চৰকাৰী API, এক্সচেঞ্জ, বতৰ আৰু ভূমিকম্পীয় ফীড) ডেটা লয় আৰু প্ৰতিটোকে এটা মন‌ʼলিথৰ পৰিৱৰ্তে নিজৰ সৰু, পৰীক্ষাযোগ্য একক এককত পৰিণত কৰে।

আপুনি এটা ডেটা-এগ্ৰিগেচন চাইট, প্লাগইন-ভিত্তিক আৰ্কিটেকচাৰ, বা "আপষ্ট্ৰীম API এ শেষত ঠগিব" এইটো এটা প্ৰকৃত ডিজাইন সীমাবদ্ধতা হোৱা যিকোনো কিবা তৈয়াৰ কৰি থাকিলে, এইটো আপোনাৰ বাবেই লিখা হৈছে।

### কাৰিকৰী চিত্ৰ

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

### ডিজাইন দৰ্শন

**প্ৰতিটো ডেটা উৎস এটা সম্পূৰ্ণ স্বতন্ত্ৰ প্লাগইন**, শ্বেয়াৰ কৰা ইনজেশ্বন পাইপলাইন নহয়। এটা প্লাগইনৰ নিজৰ ফেচ সময়সূচী, কেশ্ব, আৰু ব্যৰ্থতা পৰিচালনা আছে। যিকোনো চৰকাৰী API এ তাৰ প্ৰতিক্ৰিয়া ফৰ্মেট সলনি কৰিলে বা বন্ধ হৈ গ‌ʼলে, ঠিক এটা প্লাগইনহে ভাঙে। বাকী ~19 টাই সেৱা দি থাকে। ইমান বেছি স্বতন্ত্ৰ চলি থকা অংশৰ সৈতে, প্ৰতিটো প্লাগইনৰ লগ হাতেৰে পৰীক্ষা কৰাৰ পৰিৱৰ্তে সেই সকলোকে এঠাইৰ পৰা চাই থকা এটা ব্যৱস্থাৰ প্ৰয়োজন হোৱাৰ বাবেই `irt-api-health-monitor` আছে।

### ষ্টেক

- **WordPress** (কাষ্টম থীম, পেজ বিল্ডাৰ নাই): PHP টেম্পলেট, ভেনিলা JS/CSS
- **~20 টা কাষ্টম প্লাগইন**, প্ৰতিটো ডেটা উৎসৰ বাবে এটা, প্ৰতিটোৰে নিজৰ ফেচ/কেশ্ব স্তৰ
- সংৰক্ষণ আৰু ট্ৰেনজিয়েণ্ট কেশ্বিংৰ বাবে **MySQL**; স্থানীয় ডেভৰ বাবে Docker Compose
- এটা উৎসৰ্গীকৃত প্লাগইন (`irt-dataset-schema`) ৰ জৰিয়তে Schema.org গঠনমূলক ডেটা
- ডেটা আপডেটত প্ৰায় তৎক্ষণাৎ চাৰ্চ ইঞ্জিন ইণ্ডেক্সিংৰ বাবে IndexNow একত্ৰীকৰণ

---

## 👨‍💻 ডেভেলপাৰসকলে ইয়াক কেনেকৈ ব্যৱহাৰ কৰিব পাৰে

আপুনি আপোনাৰ এপত ভাৰতীয় বজাৰ ডেটা, লাইভ প্ৰাইচিং, বতৰ, বা AQI ৰ প্ৰয়োজনীয় বৈশিষ্ট্য তৈয়াৰ কৰি থাকিলে - আপুনি IndiaRealTime ক Python পেকেজ, কমাণ্ড-লাইন সঁজুলি, বা REST API হিচাপে ব্যৱহাৰ কৰিব পাৰে।

### ইনষ্টলেচন

**Python SDK (পৰামৰ্শিত)**
```bash
pip install indiarealtime
```

**📦 PyPI ত চাওক:** https://pypi.org/project/indiarealtime/

**উৎসৰ পৰা**
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com
pip install -e .
```

### প্ৰকৃত সংহতিকৰণ উদাহৰণ

#### উদাহৰণ 1: মণ্ডি দাম চোৱা কৃষক (CLI)
```bash
# Get wheat prices in Punjab
$ indiarealtime mandi --commodity wheat --state Punjab

Commodity  Market           State         City      Price (₹)  Unit
wheat      APMC Ludhiana    Punjab        Ludhiana  2450       Quintal
wheat      APMC Amritsar    Punjab        Amritsar  2420       Quintal
```

#### উদাহৰণ 2: প্ৰাইচ এলাৰ্ট বট তৈয়াৰ কৰা ষ্টাৰ্টআপ (Python)
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

#### উদাহৰণ 3: জ্বালানী দাম পৰীক্ষা কৰা ডেলিভাৰী এপ (REST API)
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

#### উদাহৰণ 4: AQI স্ক্ৰেপ কৰা নিউজ ৱেবছাইট (Python)
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

#### উদাহৰণ 5: হাৰ দেখুওৱা ফাইনেন্স ডেশ্ববৰ্ড (React)
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

### স্থানীয় ডেভেলপমেণ্ট ছেটআপ (Docker)
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com

# Start all services
docker-compose up

# WordPress at http://localhost:8080
# API Server at http://localhost:5000
# Monitoring at http://localhost:3000
```

### নিজে চেষ্টা কৰক

`scripts/fetch-pincode.js` চাইটৰ প্লাগইনসমূহে ব্যৱহাৰ কৰা ফেচ-আৰু-নৰমেলাইজ আৰ্হিৰ এটা সৰু স্বতন্ত্ৰ উদাহৰণ, ওপৰৰ তালিকাৰ পৰা চাবিৰ প্ৰয়োজন নোহোৱা এটা API ত প্ৰয়োগ কৰা হৈছে:

```
node scripts/fetch-pincode.js 560001
```

### অধিক উদাহৰণ
- [অট‌ʼ-ডক্সসহ FastAPI চাৰ্ভাৰ](examples/fastapi_server.py)
- [প্ৰাইচ এলাৰ্টৰ বাবে Telegram বট](examples/telegram_bot.py)
- [Google Sheets অট‌ʼ-আপডেট](examples/google_sheets_integration.py)
- [Next.js ডেশ্ববৰ্ড](examples/nextjs_mandi_dashboard.tsx)

সম্পূৰ্ণ ছেটআপ নিৰ্দেশনাৰ বাবে [examples/README.md](examples/) চাওক।

---

## ⚠️ কাৰিকৰী প্ৰত্যাহ্বান

### অভিযান্ত্ৰিক সিদ্ধান্ত আৰু শিক্ষা

এই প্ৰতিটো প্ৰত্যাহ্বান ইমান দীঘল হৈ গ‌ʼল যে ইয়াক নিজৰ পৃষ্ঠাৰ প্ৰয়োজন হ‌ʼল:

- **[ইচ্ছাকৃতভাৱে পুৰণি ডেটা প্ৰদান কৰা](notes/stale-cache-fallback.md)**: চৰকাৰী আৰু এক্সচেঞ্জ API নিৰ্ভৰযোগ্য নহয়, তথাপিও চাইটক নিৰ্ভৰযোগ্য দেখা লাগে। যেতিয়া এটা আপষ্ট্ৰীম API বিফল হয়, আমি ভুল দিয়া বা একো নেদেখুওৱাৰ পৰিৱৰ্তে শেষৰ ভাল কেশ্ব কৰা মূল্য প্ৰদান কৰোঁ।
- **[সাধ্যতা আৰু ৰং, দুয়োটাই গুৰুত্বপূৰ্ণ](notes/cvd-safe-aqi-colors.md)**: ডেটা সকলোৰে বাবে সাধ্য হৈ থাকিবলৈ প্ৰতিটো অৰ্থপূৰ্ণ ৰংক WCAG কণ্ট্ৰাষ্ট আৰু ৰং-দৃষ্টি-অভাৱ চিমুলেচনৰ বিৰুদ্ধে পৰীক্ষা কৰা হয়।
- **[দুটা ভাষাত মিল খোৱা হেশ্ব](notes/cross-language-hash-parity.md)**: PHP আৰু JavaScript এ ইণ্টিজাৰ অ‌ʼভাৰফ্ল‌ʼত একমত নহয়, তথাপিও লেখক এট্ৰিবিউচন সিহঁতৰ একমত হোৱাৰ ওপৰতেই নিৰ্ভৰ কৰে।
- **[প্ৰতিটো ৰাজ্যৰ বাবে ৰিৰাইট-ৰুল regex অবিহনে স্থান ৰাউটিং](notes/location-routing-without-regex.md)**: প্ৰতিটো অঞ্চলৰ বাবে এটা ৰিৰাইট ৰুলৰ পৰিৱৰ্তে প্ৰতিটো ৰাজ্য আৰু চহৰ পৃষ্ঠাৰ বাবে এটাই ৰাউটিং পথ।
- **[~20 টা প্লাগইন এটা ৰক্ষণাবেক্ষণযোগ্যতাৰ বাজি, বিনামূলীয়া নহয়](notes/plugin-per-source-tradeoff.md)**: ফল্ট আইছ‌ʼলেচনৰ মূল্য মানে সকলো একে ধৰণে ৰাখিবলৈ অধিক পৃষ্ঠতলৰ ক্ষেত্ৰ।

---

## 🚀 আগলৈ কি

- ঐতিহাসিক দাম ট্ৰেকিং বৰ্তমান কেৱল জ্বালানী আৰু AQI ৰ বাবেহে আছে, মণ্ডি/সামগ্ৰীৰ দামৰ বাবে এতিয়াও নাই। তাকো তালৈ বিস্তাৰ কৰাটোৱেই পৰৱৰ্তী প্ৰকৃত ডেটা ফাঁক, যিটো পূৰণ কৰিব লাগিব।
- উৎসে অনুমতি দিয়াৰ দৰে অধিক সূক্ষ্ম চহৰ কভাৰেজ।
- `STYLE-GUIDE.md` ত থকা সাধ্যতা অডিটক ৰং কণ্ট্ৰাষ্টৰ বাহিৰেও সম্পূৰ্ণ কীব‌ʼৰ্ড/স্ক্ৰীণ-ৰীডাৰ পাছলৈকে বিস্তাৰ কৰা।

---

## 👋 লেখকৰ বিষয়ে

এই ৰিপ‌ʼজিটৰীটো প্ৰজেক্টৰ এটা পৰ্যালোচনা, চাইটৰ উৎস নহয়। WordPress ক‌ʼডবেছ এতিয়াৰ বাবে বন্ধ। অৱশ্যে, [API তালিকা](API/) আৰু `scripts/` ফ‌ʼল্ডাৰ PR ৰ বাবে খোলা - নথকা API, সংশোধন, ফেচৰ অধিক উদাহৰণ, সকলোৰে স্বাগতম।

আপুনি ওপৰৰ যিকোনো সমস্যাৰ এটা সংস্কৰণ সমাধান কৰিলে (ষ্টেল-কেশ্ব ফলবেক কৌশল, প্লাগইন-প্ৰতি-উৎস আৰ্কিটেকচাৰ, CVD-চেফ ৰং প্ৰণালী, ক্ৰছ-লেংগুৱেজ হেশ্ব পেৰিটি), বা আপুনি এতিয়া একেটা দেৱালৰ সন্মুখীন হৈ আছে, তেন্তে এটা [আলোচনা](https://github.com/padmarajnidagundi/indiarealtime-com/issues) খোলক। মই সঁচাকৈয়ে টোকা মিলাব বিচাৰোঁ।

**অৱদান স্বাগতম:** নতুন ডেটা উৎস প্লাগইন হিচাপে কেনেকৈ যোগ কৰিব লাগে তাৰ বাবে [CONTRIBUTING.md](CONTRIBUTING.md) চাওক, বা সহায় কৰাৰ অন্য উপায়ৰ বাবে [CONTRIBUTORS_GUIDE.md](CONTRIBUTORS_GUIDE.md) চাওক।

আপোনাৰ প্ৰশ্ন বা ধাৰণা থাকিলে, [GitHub Issues](https://github.com/padmarajnidagundi/indiarealtime-com/issues) বা ইমেইলৰ জৰিয়তে যোগাযোগ কৰক।

<!-- TODO: contact / social links -->
