# IndiaRealTime - ইন্ডিয়া রিয়েল টাইম | লাইভ মান্ডি দর, জ্বালানির হার, AQI, আবহাওয়া সতর্কতা ও ক্রিকেট স্কোর

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/padmarajnidagundi/indiarealtime-com)
[![License: MIT](https://img.shields.io/github/license/padmarajnidagundi/indiarealtime-com)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/padmarajnidagundi/indiarealtime-com?style=social)](https://github.com/padmarajnidagundi/indiarealtime-com/stargazers)
[![Open issues](https://img.shields.io/github/issues/padmarajnidagundi/indiarealtime-com)](https://github.com/padmarajnidagundi/indiarealtime-com/issues)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](API/)

🌐 **ভাষা:** [English](README.md) · [हिन्दी](README.hi.md) · বাংলা · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [ಕನ್ನಡ](README.kn.md) · [മലയാളം](README.ml.md) · [ਪੰਜਾਬੀ](README.pa.md) · [ଓଡ଼ିଆ](README.or.md) · [অসমীয়া](README.as.md) · [اردو](README.ur.md) · [संस्कृतम्](README.sa.md) · [नेपाली](README.ne.md) · [कोंकणी](README.kok.md) · [मैथिली](README.mai.md)

**~২০টি স্বতন্ত্র WordPress প্লাগইন, প্রতিটি আলাদা একটি সরকারি ডেটা উৎসের জন্য, একসাথে একটি সাইট চালায় যা সারা ভারতে লাইভ মান্ডি দর, জ্বালানির দাম, বায়ুর গুণমান, আবহাওয়া সতর্কতা, ভূমিকম্প এবং ক্রিকেট স্কোর ট্র্যাক করে। এর পেছনের সরকারি API কাজ বন্ধ করে দিলেও এটি ভালো ডেটা দেওয়া চালিয়ে যায়।**

**লাইভ সাইট:** https://indiarealtime.com

## ওয়েবসাইট স্ক্রিনশট

| ওয়েব ভিউ | মোবাইল ভিউ |
|---|---|
| ![IndiaRealTime website web view](assets/website-webview.png) | ![IndiaRealTime website mobile view](assets/website-mobile.png) |

---

## 📱 IndiaRealTime সম্পর্কে

### সমস্যাটা কী

ডেটা আগে থেকেই আছে এবং বেশিরভাগই সরকারি ভাবে প্রকাশিত। শুধু এটা বিভিন্ন সরকারি ও PSU পোর্টালে ছড়িয়ে আছে, প্রতিটির নিজস্ব ফরম্যাট, আপডেটের সময়সূচি, এবং (প্রায়ই) নির্ভরযোগ্যতার সমস্যা।

পাঞ্জাবে মান্ডির দাম দেখতে চাওয়া একজন কৃষককে জানতে হবে Agmarknet বলে কিছু আছে। বাইরে যাওয়া নিরাপদ কিনা জানতে চাওয়া কাউকে জানতে হবে CPCB আলাদা ওয়েবসাইটে, আলাদা ফরম্যাটে AQI প্রকাশ করে। জ্বালানির দাম প্রতিদিন বদলায় এবং রাজ্যভেদে আলাদা (আলাদা VAT হার), কিন্তু প্রতিটি তেল কোম্পানি শুধু নিজের সংখ্যা, আলাদাভাবে, শুধু যেসব শহরে সেবা দেয় সেগুলোর জন্য প্রকাশ করে।

এর জন্য নতুন কোনো ডেটা সংগ্রহের দরকার নেই। শুধু কাউকে যা আগে থেকেই প্রকাশিত তা নিয়ে, ফরম্যাট স্বাভাবিক করে, মান্ডির দাম, জ্বালানির দাম, AQI, আবহাওয়া সতর্কতা ইত্যাদি এক জায়গায় রাখতে হবে যাতে একজন মানুষ পাঁচটি আলাদা সরকারি সাইটের পাঁচটি ট্যাব খোলার বদলে কয়েক সেকেন্ডে দেখে নিতে পারে। **এই ফাঁকটাই IndiaRealTime পূরণ করে।**

### বাস্তব ব্যবহারকারীদের গল্প

**🌾 রাজেশ - পাঞ্জাবের কৃষক**
> "আমি APMC লুধিয়ানায় গম বিক্রি করি। প্রতিদিন সকালে ভালো দামে দরদাম করতে আমাকে আশেপাশের বাজারের দাম জানতে ৩টি আলাদা ওয়েবসাইট দেখতে হতো। এখন বাজারে যাওয়ার আগে ১০ সেকেন্ডে indiarealtime দেখে নিই।"

**🚖 প্রিয়া - বেঙ্গালুরুর অটো চালক**
> "জ্বালানির দাম প্রতিদিন বদলায় আর আমার আয়ে প্রভাব ফেলে। আগে আমি বিভিন্ন শহরের বন্ধুদের ফোন করে দাম জানতাম। এখন একটাই অ্যাপে বেঙ্গালুরু জুড়ে পেট্রল/ডিজেলের দাম দেখে আমার রুট ঠিক করি।"

**👨‍👩‍👧 অমিত - দিল্লির অভিভাবক**
> "বাচ্চাদের বাইরে খেলতে দেওয়ার আগে আমাকে AQI দেখতে হয়। আগে আমি ৫টি আলাদা উৎস গুগল করতাম - Agmarknet, CPCB, আবহাওয়ার সাইট - সব আলাদা ফরম্যাটে। এখন এক ক্লিকেই জানি বাইরে যাওয়া নিরাপদ কিনা।"

### আমরা যা ট্র্যাক করি

| বিভাগ | উদাহরণ |
|---|---|
| দাম | মান্ডি (কৃষিপণ্য), জ্বালানি ও LPG রাজ্য/শহর অনুযায়ী, মূল্যবান ধাতু, মুদ্রা রূপান্তর, মিউচুয়াল ফান্ড NAV, FD হার, টোল হার |
| পরিবেশ | বায়ুর গুণমান (AQI, CPCB ব্যান্ড), আবহাওয়া সতর্কতা, ভূমিকম্প সতর্কতা |
| নাগরিক / সময় | ব্যাংক ছুটি, পিনকোড লুকআপ, টাইমজোন রূপান্তর |
| সংস্কৃতি | পঞ্জিকা ও মুহূর্ত সময়, ব্রত ক্যালেন্ডার, রাশিফল |
| খেলা | লাইভ ক্রিকেট স্কোর |

কভারেজ শহর/রাজ্য স্তরে বিস্তারিত, যেখানে মূল ডেটা তা সমর্থন করে। যেমন, জ্বালানির দাম শহরভিত্তিক ট্র্যাক করা হয়, জাতীয় গড় নয়।

এর পেছনের বিনামূল্যের ভারতীয় ডেটা API-র সম্পূর্ণ তালিকা, যেসব সরকারি API সাইট এখনও ব্যবহার করে না সেগুলো সহ, [API/](API/)-তে আছে।

### দর্শকদের জন্য এটি যেভাবে কাজ করে

- **অবস্থান অনুযায়ী ব্রাউজ করুন**: URL `/state/city/category/` প্যাটার্ন অনুসরণ করে (যেমন একটি রাজ্যের পেজ, তারপর শহরে গিয়ে, তারপর জ্বালানির দাম বা AQI-র মতো নির্দিষ্ট বিভাগে)। বেশিরভাগ বিভাগ জাতীয় ওভারভিউ এবং শহর-ভিত্তিক বিস্তারিত পেজ দুই আকারেই আছে।
- **দাম তুলনা করুন**: একটি প্রাইস-কম্পারিজন ভিউ একটি পণ্য বা জ্বালানির ধরন শহর/রাজ্যজুড়ে পাশাপাশি সাজায়, প্রতিটি শহরের পেজ আলাদাভাবে খোলার বদলে।
- **ক্যালকুলেটর**: একটি মেটালস ক্যালকুলেটর লাইভ সোনা/রূপার দাম ওজন ও বিশুদ্ধতা অনুযায়ী রূপান্তর করে, শুধু প্রতি-গ্রাম সংখ্যা দেখানোর বদলে।
- **শেয়ার কার্ড**: ডেটা পেজ একটি শেয়ারযোগ্য ইমেজ কার্ড (দাম, তারিখ, উৎস) তৈরি করে যা সামাজিক মাধ্যমের জন্য উপযুক্ত আকারের, যাতে স্ক্রিনশট ছাড়াই একটি তথ্য শেয়ার করা যায়।
- **লেখক হাব**: প্রতিটি নিবন্ধ একজন প্রকৃত লেখকের নামে, তাদের প্রোফাইল পেজসহ, ক্রেডিট করা হয়, নামহীন বাইলাইন নয়। `/authors/` সবাইকে তালিকাভুক্ত করে, `/author/<name>/` তাদের প্রকাশিত কাজ দেখায়।

---

## 🏗️ ওয়েব অ্যাপ্লিকেশনের আর্কিটেকচার

ভারতে বেশিরভাগ "লাইভ ডেটা" সাইট হয় দিনে একবার স্ক্র্যাপ করে তাকে রিয়েল-টাইম বলে, নয়তো একটি পেজ-বিল্ডার থিমে একগাদা অসংলগ্ন উইজেট জুড়তে থাকে যতক্ষণ না সেটা রক্ষণাবেক্ষণযোগ্য থাকে না। IndiaRealTime প্রায় ১৫টি আলাদা সরকারি ডেটা উৎস (সরকারি API, এক্সচেঞ্জ, আবহাওয়া ও ভূকম্পীয় ফিড) থেকে ডেটা নিয়ে প্রতিটিকে একটি মনোলিথের বদলে নিজস্ব ছোট, পরীক্ষাযোগ্য ইউনিটে পরিণত করে।

আপনি যদি একটি ডেটা-অ্যাগ্রিগেশন সাইট, প্লাগইন-ভিত্তিক আর্কিটেকচার, বা এমন কিছু তৈরি করছেন যেখানে "আপস্ট্রিম API শেষ পর্যন্ত মিথ্যা বলবে" একটি বাস্তব ডিজাইন সীমাবদ্ধতা, তাহলে এটি আপনার জন্যই লেখা।

### টেকনিক্যাল ডায়াগ্রাম

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

### ডিজাইন দর্শন

**প্রতিটি ডেটা উৎস একটি সম্পূর্ণ স্বতন্ত্র প্লাগইন**, কোনো শেয়ার করা ইনজেশন পাইপলাইন নয়। একটি প্লাগইনের নিজস্ব ফেচ শিডিউল, ক্যাশ, এবং ব্যর্থতা সামলানোর ব্যবস্থা আছে। কোনো সরকারি API তার রেসপন্স ফরম্যাট বদলালে বা ডাউন হয়ে গেলে, ঠিক একটি প্লাগইন ভাঙে। বাকি ~১৯টি সেবা দেওয়া চালিয়ে যায়। `irt-api-health-monitor` আছে কারণ এত সংখ্যক স্বতন্ত্র চলমান অংশ থাকলে, প্রতিটি প্লাগইনের লগ হাতে হাতে দেখার বদলে একটি জায়গা থেকে সবগুলো দেখা দরকার।

### স্ট্যাক

- **WordPress** (কাস্টম থিম, কোনো পেজ বিল্ডার নেই): PHP টেমপ্লেট, ভ্যানিলা JS/CSS
- **~২০টি কাস্টম প্লাগইন**, প্রতিটি ডেটা উৎসের জন্য একটি, প্রতিটির নিজস্ব ফেচ/ক্যাশ লেয়ার
- সংরক্ষণ ও ট্রানজিয়েন্ট ক্যাশিংয়ের জন্য **MySQL**; লোকাল ডেভের জন্য Docker Compose
- একটি ডেডিকেটেড প্লাগইনের (`irt-dataset-schema`) মাধ্যমে Schema.org স্ট্রাকচার্ড ডেটা
- ডেটা আপডেটে তাৎক্ষণিক সার্চ ইঞ্জিন ইনডেক্সিংয়ের জন্য IndexNow ইন্টিগ্রেশন

---

## 👨‍💻 ডেভেলপাররা কীভাবে এটি ব্যবহার করতে পারেন

আপনি যদি আপনার অ্যাপে এমন ফিচার তৈরি করছেন যাতে ভারতীয় বাজারের ডেটা, লাইভ প্রাইসিং, আবহাওয়া, বা AQI দরকার - তাহলে আপনি IndiaRealTime-কে Python প্যাকেজ, কমান্ড-লাইন টুল, বা REST API হিসেবে ব্যবহার করতে পারেন।

### ইনস্টলেশন

**Python SDK (প্রস্তাবিত)**
```bash
pip install indiarealtime
```

**📦 PyPI-তে দেখুন:** https://pypi.org/project/indiarealtime/

**সোর্স থেকে**
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com
pip install -e .
```

### বাস্তব ইন্টিগ্রেশন উদাহরণ

#### উদাহরণ ১: মান্ডির দাম দেখছেন কৃষক (CLI)
```bash
# Get wheat prices in Punjab
$ indiarealtime mandi --commodity wheat --state Punjab

Commodity  Market           State         City      Price (₹)  Unit
wheat      APMC Ludhiana    Punjab        Ludhiana  2450       Quintal
wheat      APMC Amritsar    Punjab        Amritsar  2420       Quintal
```

#### উদাহরণ ২: প্রাইস অ্যালার্ট বট তৈরি করছে স্টার্টআপ (Python)
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

#### উদাহরণ ৩: জ্বালানির দাম দেখছে ডেলিভারি অ্যাপ (REST API)
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

#### উদাহরণ ৪: AQI স্ক্র্যাপ করছে নিউজ ওয়েবসাইট (Python)
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

#### উদাহরণ ৫: হার দেখাচ্ছে ফাইন্যান্স ড্যাশবোর্ড (React)
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

### লোকাল ডেভেলপমেন্ট সেটআপ (Docker)
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com

# Start all services
docker-compose up

# WordPress at http://localhost:8080
# API Server at http://localhost:5000
# Monitoring at http://localhost:3000
```

### নিজে চেষ্টা করুন

`scripts/fetch-pincode.js` হলো ফেচ-অ্যান্ড-নরমালাইজ প্যাটার্নের একটি ছোট স্ট্যান্ডঅ্যালোন উদাহরণ যা সাইটের প্লাগইনগুলো ব্যবহার করে, উপরের তালিকার একটি কী-বিহীন API ব্যবহার করে:

```
node scripts/fetch-pincode.js 560001
```

### আরও উদাহরণ
- [অটো-ডকসহ FastAPI সার্ভার](examples/fastapi_server.py)
- [প্রাইস অ্যালার্টের জন্য Telegram বট](examples/telegram_bot.py)
- [Google Sheets অটো-আপডেট](examples/google_sheets_integration.py)
- [Next.js ড্যাশবোর্ড](examples/nextjs_mandi_dashboard.tsx)

সম্পূর্ণ সেটআপ নির্দেশনার জন্য দেখুন [examples/README.md](examples/)।

---

## ⚠️ প্রযুক্তিগত চ্যালেঞ্জ

### ইঞ্জিনিয়ারিং সিদ্ধান্ত ও শিক্ষা

এই চ্যালেঞ্জগুলোর প্রতিটি এত দীর্ঘ হয়ে গেছে যে এদের নিজস্ব পেজ প্রাপ্য:

- **[ইচ্ছাকৃতভাবে পুরনো ডেটা দেখানো](notes/stale-cache-fallback.md)**: সরকারি ও এক্সচেঞ্জ API নির্ভরযোগ্য নয়, তবুও সাইটকে নির্ভরযোগ্য দেখাতে হয়। কোনো আপস্ট্রিম API ব্যর্থ হলে, আমরা এরর দেখানো বা কিছু না দেখানোর বদলে শেষ ভালো ক্যাশ করা মান দেখাই।
- **[অ্যাক্সেসিবিলিটি এবং রং, দুটোই গুরুত্বপূর্ণ](notes/cvd-safe-aqi-colors.md)**: প্রতিটি সিমান্টিক রং WCAG কনট্রাস্ট এবং কালার-ভিশন-ডেফিসিয়েন্সি সিমুলেশনের বিরুদ্ধে পরীক্ষা করা হয় যাতে ডেটা সবার জন্য অ্যাক্সেসযোগ্য হয়।
- **[দুই ভাষা জুড়ে একই হ্যাশ পাওয়া](notes/cross-language-hash-parity.md)**: PHP এবং JavaScript ইন্টিজার ওভারফ্লোতে একমত নয়, তবুও লেখক অ্যাট্রিবিউশন এদের একমত থাকার উপর নির্ভরশীল।
- **[প্রতি রাজ্যের জন্য রিরাইট-রুল regex ছাড়াই লোকেশন রাউটিং](notes/location-routing-without-regex.md)**: প্রতি অঞ্চলের জন্য একটি রিরাইট রুলের বদলে প্রতিটি রাজ্য ও শহর পেজের জন্য একটাই রাউটিং পথ।
- **[~২০টি প্লাগইন একটি রক্ষণাবেক্ষণযোগ্যতার বাজি, বিনামূল্যের কিছু নয়](notes/plugin-per-source-tradeoff.md)**: ফল্ট আইসোলেশনের খরচ হলো সবকিছু সামঞ্জস্যপূর্ণ রাখতে বেশি পরিমাণ কাজের এলাকা।

---

## 🚀 এরপর কী

- ঐতিহাসিক দামের ট্র্যাকিং এখন শুধু জ্বালানি ও AQI-র জন্য আছে, মান্ডি/পণ্যের দামের জন্য এখনও নয়। সেখানে এটি বিস্তৃত করাই পরবর্তী প্রকৃত ডেটা ফাঁক যা পূরণ করতে হবে।
- উৎস অনুমতি দিলে আরও বিস্তারিত শহর কভারেজ।
- `STYLE-GUIDE.md`-এ অ্যাক্সেসিবিলিটি অডিট রঙের কনট্রাস্ট ছাড়িয়ে সম্পূর্ণ কীবোর্ড/স্ক্রিন-রিডার পাস পর্যন্ত বিস্তৃত করা।

---

## 👋 লেখক সম্পর্কে

এই রিপোজিটরি প্রজেক্টের একটি ওভারভিউ, সাইটের সোর্স নয়। WordPress কোডবেস এখনকার জন্য বন্ধ। তবে, [API তালিকা](API/) এবং `scripts/` ফোল্ডার PR-এর জন্য উন্মুক্ত - অনুপস্থিত API, সংশোধন, ফেচের আরও উদাহরণ, সবই স্বাগত।

আপনি যদি উপরের কোনো সমস্যার একটি সংস্করণ সমাধান করে থাকেন (স্টেল-ক্যাশ ফলব্যাক কৌশল, প্লাগইন-প্রতি-সোর্স আর্কিটেকচার, CVD-সেফ কালার সিস্টেম, ক্রস-ল্যাঙ্গুয়েজ হ্যাশ প্যারিটি), অথবা এখন একই দেয়ালে ধাক্কা খাচ্ছেন, একটি [ডিসকাশন](https://github.com/padmarajnidagundi/indiarealtime-com/issues) খুলুন। আমি সত্যিই নোট মেলাতে চাই।

**অবদান স্বাগত:** নতুন ডেটা উৎস প্লাগইন হিসেবে কীভাবে যোগ করবেন তার জন্য দেখুন [CONTRIBUTING.md](CONTRIBUTING.md), অথবা সাহায্যের অন্যান্য উপায়ের জন্য [CONTRIBUTORS_GUIDE.md](CONTRIBUTORS_GUIDE.md)।

কোনো প্রশ্ন বা আইডিয়া থাকলে, [GitHub Issues](https://github.com/padmarajnidagundi/indiarealtime-com/issues) বা ইমেইলের মাধ্যমে যোগাযোগ করুন।

<!-- TODO: contact / social links -->
