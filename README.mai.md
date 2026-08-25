# IndiaRealTime - इंडिया रियल टाइम | लाइव मंडी भाव, इंधन दर, AQI, मौसमक चेतावनी आ क्रिकेट स्कोर

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/padmarajnidagundi/indiarealtime-com)
[![License: MIT](https://img.shields.io/github/license/padmarajnidagundi/indiarealtime-com)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/padmarajnidagundi/indiarealtime-com?style=social)](https://github.com/padmarajnidagundi/indiarealtime-com/stargazers)
[![Open issues](https://img.shields.io/github/issues/padmarajnidagundi/indiarealtime-com)](https://github.com/padmarajnidagundi/indiarealtime-com/issues)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](API/)

🌐 **भाषा:** [English](README.md) · [हिन्दी](README.hi.md) · [বাংলা](README.bn.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [ಕನ್ನಡ](README.kn.md) · [മലയാളം](README.ml.md) · [ਪੰਜਾਬੀ](README.pa.md) · [ଓଡ଼ିଆ](README.or.md) · [অসমীয়া](README.as.md) · [اردو](README.ur.md) · [संस्कृतम्](README.sa.md) · [नेपाली](README.ne.md) · [कोंकणी](README.kok.md) · मैथिली

**~२० स्वतंत्र WordPress प्लगइन, हरेक अलग सार्वजनिक डेटा स्रोत लेल, मिलिकय एकहि साइट चलबैत अछि जे पूरा भारत मे लाइव मंडी भाव, इंधनक भाव, हवाक गुणवत्ता, मौसमक चेतावनी, भूकंप आ क्रिकेट स्कोर ट्रैक करैत अछि। एकर पाछाँ रहल सरकारी API काज करब बंद क' देलहुँ तैयो ई नीक डेटा देब जारी राखैत अछि।**

**लाइव साइट:** https://indiarealtime.com

## वेबसाइट स्क्रीनशॉट

| वेब व्यू | मोबाइल व्यू |
|---|---|
| ![IndiaRealTime website web view](assets/website-webview.png) | ![IndiaRealTime website mobile view](assets/website-mobile.png) |

---

## 📱 IndiaRealTime क बारे मे

### समस्या की अछि

डेटा पहिनहि सँ मौजूद अछि आ अधिकतर सार्वजनिक अछि। ई मात्र दर्जनों अलग-अलग सरकारी आ PSU पोर्टल पर बिखरल अछि, हरेकक अपन फॉर्मेट, अपडेट होबाक समय, आ (प्रायः) भरोसाक समस्या।

पंजाब मे मंडी भाव देखय चाहय बला किसान के बुझल रहबाक चाही जे Agmarknet नाम केर किछु अछि। बाहर जाएब सुरक्षित अछि की नहि ई जानय चाहय बला केओ के बुझल रहबाक चाही जे CPCB अलग वेबसाइट पर, अलग फॉर्मेट मे AQI प्रकाशित करैत अछि। इंधनक भाव रोज बदलैत अछि आ राज्य अनुसार अलग होइत अछि (अलग-अलग VAT दर), मुदा हरेक तेल कंपनी केवल अपन सेवा देल जाए बला शहर सभक लेल, अलग-अलग रूप सँ, अपनहि आँकड़ा प्रकाशित करैत अछि।

एकर लेल नव डेटा एकत्रित करबाक जरूरत नहि। मात्र केओ के जे पहिनहि सँ सार्वजनिक अछि ओकरा आनि, फॉर्मेट के सामान्य बनाकय, मंडी भाव, इंधनक भाव, AQI, मौसमक चेतावनी आदि के एकहि जगह राखय पड़त जाहि सँ केओ व्यक्ति पाँच अलग सरकारी साइटक पाँच टैब खोलबाक बदला किछु सेकेंड मे देखि सकय। **इएह कमी के IndiaRealTime पूर्ण करैत अछि।**

### असली उपयोगकर्ता सभक कहानी

**🌾 राजेश - पंजाबक किसान**
> "हम APMC लुधियाना मे गहुम बेचैत छी। हरेक भोर बेसी नीक भाव पर मोलभाव करबाक लेल हमरा लग्गुक बजार सभक भाव देखबाक लेल 3 गोट अलग वेबसाइट देखय पड़ैत छल। आब बजार जेबाक सँ पहिने हम 10 सेकेंड मे indiarealtime देखि लैत छी।"

**🚖 प्रिया - बेंगलुरुक ऑटो चालक**
> "इंधनक भाव रोज बदलैत अछि आ हमर कमाई पर असर पड़ैत अछि। पहिने हम अलग-अलग शहर मे रहनिहार मित्र सभ के फोन करिकय भाव जानैत रही। आब हम एकहि ऐप पर बेंगलुरु भर मे पेट्रोल/डीजलक भाव देखिकय अपन रस्ता योजना बनाबैत छी।"

**👨‍👩‍👧 अमित - दिल्लीक अभिभावक**
> "अपन बच्चा सभ के बाहर खेलय पठेबाक सँ पहिने हमरा AQI देखय पड़ैत अछि। पहिने हम 5 गोट अलग स्रोत गूगल करैत रही - Agmarknet, CPCB, मौसमक साइट - सभटा अलग फॉर्मेट मे। आब एक क्लिक मे बुझा जाइत अछि जे बाहर जाएब सुरक्षित अछि की नहि।"

### हमसभ की ट्रैक करैत छी

| श्रेणी | उदाहरण |
|---|---|
| भाव | मंडी (कृषि उत्पाद), इंधन आ LPG राज्य/शहर अनुसार, मूल्यवान धातु, मुद्रा रूपांतरण, म्यूचुअल फंड NAV, FD दर, टोल दर |
| पर्यावरण | हवाक गुणवत्ता (AQI, CPCB बैंड), मौसमक चेतावनी, भूकंपक चेतावनी |
| नागरिक / समय | बैंक छुट्टी, पिनकोड लुकअप, टाइमजोन रूपांतरण |
| संस्कृति | पंचांग आ मुहूर्तक समय, व्रत कैलेंडर, राशिफल |
| खेल | लाइव क्रिकेट स्कोर |

मूल डेटा जतय अनुमति दैत अछि ततय कवरेज शहर/राज्य स्तर पर बारीक अछि। जेना, इंधनक भाव राष्ट्रीय औसत नहि, हरेक शहर अनुसार ट्रैक कएल जाइत अछि।

एकर पाछाँ रहल मुफ्त भारतीय डेटा API सभक पूरा सूची, साइट जे सरकारी API सभक अखनो उपयोग नहि करैत अछि ओकरा सहित, [API/](API/) मे अछि।

### आगंतुक सभक लेल ई कोना काज करैत अछि

- **स्थान अनुसार ब्राउज करू**: URL सभ `/state/city/category/` पैटर्न के अनुसरण करैत अछि (जेना एक राज्य पृष्ठ, फेर एक शहर मे जाएब, फेर इंधनक भाव या AQI जेहन कोनो खास श्रेणी मे)। अधिकतर श्रेणी राष्ट्रीय अवलोकन आ शहर-विशेष विवरण पृष्ठ दुनू रूप मे अछि।
- **भावक तुलना करू**: एक भाव-तुलना दृश्य कोनो वस्तु या इंधन प्रकार के शहर/राज्य सभ मे संगे-संग देखबैत अछि, हरेक शहरक पृष्ठ अलग सँ खोलबाक बदला।
- **कैलकुलेटर**: एक धातु कैलकुलेटर मात्र प्रति-ग्राम आँकड़ा देखेबाक बदला लाइव सोन/चानीक दर के वजन आ शुद्धता अनुसार बदलैत अछि।
- **शेयर कार्ड**: डेटा पृष्ठ सभ सामाजिक प्लेटफॉर्म लेल उपयुक्त आकारक शेयर कएल जा सकय बला छवि कार्ड (भाव, तारीख, स्रोत) बनबैत अछि, जाहि सँ स्क्रीनशॉट बिना एक तथ्य शेयर कएल जा सकय।
- **लेखक हब**: हरेक लेख के एक असली लेखक के, हुनक प्रोफाइल पृष्ठ सहित, श्रेय देल जाइत अछि, गुमनाम बाइलाइन नहि। `/authors/` सभके सूचीबद्ध करैत अछि, `/author/<name>/` हुनक प्रकाशित काज देखबैत अछि।

---

## 🏗️ वेब एप्लिकेशनक आर्किटेक्चर

भारत मे अधिकतर "लाइव डेटा" साइट या त दिन मे एक बेर स्क्रैप कय एकरा रियल-टाइम कहैत अछि, या ई प्रबंधन योग्य नहि रहय धरि एक पेज-बिल्डर थीम पर दर्जनों असंबंधित विजेट जोड़ैत रहैत अछि। IndiaRealTime करीब 15 गोट अलग सार्वजनिक डेटा स्रोत सँ (सरकारी API, एक्सचेंज, मौसम आ भूकंपीय फीड) डेटा लैत अछि आ हरेक के एक मोनोलिथक बदला अपन छोट, परीक्षण योग्य इकाई मे बदलैत अछि।

जँ अहाँ एक डेटा-एग्रीगेशन साइट, प्लगइन-आधारित आर्किटेक्चर, या एहन किछु बना रहल छी जतय "अपस्ट्रीम API अंततः धोखा देत" ई एक असली डिजाइन सीमा अछि, त ई अहीं लेल लिखल गेल अछि।

### तकनीकी आरेख

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

### डिजाइन दर्शन

**हरेक डेटा स्रोत एक पूर्ण स्वतंत्र प्लगइन अछि**, साझा इंजेशन पाइपलाइन नहि। एक प्लगइनक अपन फेच शेड्यूल, कैश, आ विफलता प्रबंधन अछि। जँ कोनो सरकारी API अपन प्रतिक्रिया फॉर्मेट बदलि दैत अछि या बंद भऽ जाइत अछि, त ठीक एक प्लगइन टूटैत अछि। बाकी ~19 सेवा देब जारी राखैत अछि। एतेक स्वतंत्र चलैत भाग सभक संग, हरेक प्लगइनक लॉग हाथ सँ जाँचबाक बदला सभटा के एक जगह सँ देखय बला व्यवस्थाक जरूरत होयबाक कारणे `irt-api-health-monitor` अछि।

### स्टैक

- **WordPress** (कस्टम थीम, पेज बिल्डर नहि): PHP टेम्पलेट, वेनिला JS/CSS
- **~20 गोट कस्टम प्लगइन**, हरेक डेटा स्रोत लेल एक, हरेकक अपन फेच/कैश लेयर
- स्टोरेज आ ट्रांजिएंट कैशिंग लेल **MySQL**; लोकल डेव लेल Docker Compose
- एक समर्पित प्लगइन (`irt-dataset-schema`) क माध्यम सँ Schema.org संरचित डेटा
- डेटा अपडेट पर करीब तत्काल सर्च इंजन इंडेक्सिंग लेल IndexNow एकीकरण

---

## 👨‍💻 डेवलपर एकर उपयोग कोना कऽ सकैत छथि

जँ अहाँ अपन ऐप मे भारतीय बाजार डेटा, लाइव प्राइसिंग, मौसम, या AQI जरूरी बला फीचर बना रहल छी - त अहाँ IndiaRealTime के Python पैकेज, कमांड-लाइन टूल, या REST API के रूप मे उपयोग कऽ सकैत छी।

### इंस्टॉलेशन

**Python SDK (सिफारिश कएल)**
```bash
pip install indiarealtime
```

**📦 PyPI पर देखू:** https://pypi.org/project/indiarealtime/

**स्रोत सँ**
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com
pip install -e .
```

### असली एकीकरण उदाहरण

#### उदाहरण 1: मंडी भाव देखैत किसान (CLI)
```bash
# Get wheat prices in Punjab
$ indiarealtime mandi --commodity wheat --state Punjab

Commodity  Market           State         City      Price (₹)  Unit
wheat      APMC Ludhiana    Punjab        Ludhiana  2450       Quintal
wheat      APMC Amritsar    Punjab        Amritsar  2420       Quintal
```

#### उदाहरण 2: भाव अलर्ट बॉट बनबैत स्टार्टअप (Python)
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

#### उदाहरण 3: इंधनक भाव जाँचैत डिलीवरी ऐप (REST API)
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

#### उदाहरण 4: AQI स्क्रैप करैत न्यूज वेबसाइट (Python)
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

#### उदाहरण 5: दर देखबैत फाइनांस डैशबोर्ड (React)
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

### लोकल डेवलपमेंट सेटअप (Docker)
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com

# Start all services
docker-compose up

# WordPress at http://localhost:8080
# API Server at http://localhost:5000
# Monitoring at http://localhost:3000
```

### स्वयं कोशिश करू

`scripts/fetch-pincode.js` साइटक प्लगइन सभ उपयोग करैत बला फेच-आ-नॉर्मलाइज पैटर्नक एक छोट स्वतंत्र उदाहरण अछि, ऊपरक सूची सँ बिना-चाबी बला एक API पर लागू कएल गेल:

```
node scripts/fetch-pincode.js 560001
```

### आर उदाहरण
- [ऑटो-डॉक्स सहित FastAPI सर्वर](examples/fastapi_server.py)
- [भाव अलर्ट लेल Telegram बॉट](examples/telegram_bot.py)
- [Google Sheets ऑटो-अपडेट](examples/google_sheets_integration.py)
- [Next.js डैशबोर्ड](examples/nextjs_mandi_dashboard.tsx)

पूर्ण सेटअप निर्देश लेल [examples/README.md](examples/) देखू।

---

## ⚠️ तकनीकी चुनौती

### इंजीनियरिंग निर्णय आ सीख

एहि मे सँ हरेक चुनौती एतेक पैघ भऽ गेल जे एकरा अपन पृष्ठक जरूरत भऽ गेल:

- **[जानि-बूझिकय पुरान डेटा देब](notes/stale-cache-fallback.md)**: सरकारी आ एक्सचेंज API भरोसेमंद नहि होइत अछि, फेर सेहो साइट के भरोसेमंद देखाएब पड़ैत अछि। जखन कोनो अपस्ट्रीम API विफल होइत अछि, हमसभ त्रुटि देबाक या किछु नहि देखेबाक बदला अंतिम नीक कैश कएल मूल्य देखबैत छी।
- **[पहुँच आ रंग, दुनू महत्वपूर्ण](notes/cvd-safe-aqi-colors.md)**: डेटा सभक लेल सुलभ रहय ताहि लेल हरेक अर्थपूर्ण रंग के WCAG कंट्रास्ट आ रंग-दृष्टि-अभाव सिमुलेशनक विरुद्ध जाँचल जाइत अछि।
- **[दू भाषा मे मेल खाइत हैश](notes/cross-language-hash-parity.md)**: PHP आ JavaScript इंटीजर ओवरफ्लो पर सहमत नहि होइत अछि, फेर सेहो लेखक एट्रिब्यूशन हुनक सहमत रहला पर निर्भर अछि।
- **[हरेक राज्य लेल रीराइट-रूल regex बिना लोकेशन राउटिंग](notes/location-routing-without-regex.md)**: हरेक क्षेत्र लेल एक रीराइट नियमक बदला हरेक राज्य आ शहर पृष्ठ लेल एकहि राउटिंग रास्ता।
- **[~20 गोट प्लगइन एक रखरखाव योग्यता दाँव अछि, मुफ्त नहि](notes/plugin-per-source-tradeoff.md)**: दोष पृथक्करणक मोल कहबाक अर्थ सभटा के स्थिर रखबाक लेल बेसी सतह क्षेत्र।

---

## 🚀 आगू की

- ऐतिहासिक भाव ट्रैकिंग अखन मात्र इंधन आ AQI लेल अछि, मंडी/वस्तु भाव लेल अखनो नहि। ओकरा ओतय धरि विस्तार करब अगिला असली डेटा अंतर अछि, जकरा भरबाक अछि।
- स्रोत अनुमति देलहुँ अनुसार बेसी बारीक शहर कवरेज।
- `STYLE-GUIDE.md` मे रहल पहुँच ऑडिट के रंग कंट्रास्ट सँ आगू पूर्ण कीबोर्ड/स्क्रीन-रीडर पास धरि विस्तारित करब।

---

## 👋 लेखकक बारे मे

ई रिपॉजिटरी प्रोजेक्टक एक अवलोकन अछि, साइटक स्रोत नहि। WordPress कोडबेस अखनक लेल बंद अछि। मुदा, [API सूची](API/) आ `scripts/` फोल्डर PR लेल खुजल अछि - छूटल API, सुधार, फेचक आर उदाहरण, सभटाक स्वागत अछि।

जँ अहाँ ऊपर बतायल गेल कोनो समस्याक एक संस्करण हल कएने छी (stale-cache fallback रणनीति, plugin-per-source आर्किटेक्चर, CVD-safe रंग प्रणाली, cross-language hash parity), या अहाँ अखन ओहि दीवाल सँ जूझि रहल छी, त एक [चर्चा](https://github.com/padmarajnidagundi/indiarealtime-com/issues) खोलू। हमरा सचमुच नोट मिलाबय के अछि।

**योगदानक स्वागत अछि:** नव डेटा स्रोत के प्लगइनक रूप मे कोना जोड़य, एकर लेल [CONTRIBUTING.md](CONTRIBUTING.md) देखू, या मदति के आर तरीका लेल [CONTRIBUTORS_GUIDE.md](CONTRIBUTORS_GUIDE.md) देखू।

जँ अहाँक लग सवाल या विचार अछि, त [GitHub Issues](https://github.com/padmarajnidagundi/indiarealtime-com/issues) या ईमेल क माध्यम सँ संपर्क करू।

<!-- TODO: contact / social links -->
