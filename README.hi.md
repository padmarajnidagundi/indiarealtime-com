# IndiaRealTime

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/padmarajnidagundi/indiarealtime-com)
[![License: MIT](https://img.shields.io/github/license/padmarajnidagundi/indiarealtime-com)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/padmarajnidagundi/indiarealtime-com?style=social)](https://github.com/padmarajnidagundi/indiarealtime-com/stargazers)
[![Open issues](https://img.shields.io/github/issues/padmarajnidagundi/indiarealtime-com)](https://github.com/padmarajnidagundi/indiarealtime-com/issues)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](API/)

🌐 **भाषा:** [English](README.md) · हिन्दी · [বাংলা](README.bn.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [ಕನ್ನಡ](README.kn.md) · [മലയാളം](README.ml.md) · [ਪੰਜਾਬੀ](README.pa.md) · [ଓଡ଼ିଆ](README.or.md) · [অসমীয়া](README.as.md) · [اردو](README.ur.md) · [संस्कृतम्](README.sa.md) · [नेपाली](README.ne.md) · [कोंकणी](README.kok.md) · [मैथिली](README.mai.md)

**~20 स्वतंत्र WordPress प्लगइन, हर एक अलग सार्वजनिक डेटा स्रोत के लिए, मिलकर एक ऐसी साइट चलाते हैं जो पूरे भारत में लाइव मंडी भाव, ईंधन के दाम, वायु गुणवत्ता, मौसम अलर्ट, भूकंप और क्रिकेट स्कोर ट्रैक करती है। इसके पीछे की सरकारी API काम करना बंद कर दे, तब भी यह अच्छा डेटा देना जारी रखती है।**

**लाइव साइट:** https://indiarealtime.com

## वेबसाइट स्क्रीनशॉट

| वेब व्यू | मोबाइल व्यू |
|---|---|
| ![IndiaRealTime website web view](assets/website-webview.png) | ![IndiaRealTime website mobile view](assets/website-mobile.png) |

---

## 📱 IndiaRealTime के बारे में

### समस्या क्या है

डेटा पहले से मौजूद है और ज़्यादातर सार्वजनिक है। बस यह दर्जनों अलग-अलग सरकारी और PSU पोर्टलों में बिखरा हुआ है, हर एक का अपना फॉर्मेट, अपडेट होने का समय, और (अक्सर) भरोसेमंदी की दिक्कत।

पंजाब में मंडी भाव देखने वाले किसान को यह पता होना चाहिए कि Agmarknet नाम की कोई चीज़ मौजूद है। बाहर जाना सुरक्षित है या नहीं यह जानने वाले किसी व्यक्ति को पता होना चाहिए कि CPCB अलग वेबसाइट पर, अलग फॉर्मेट में AQI छापता है। ईंधन के दाम रोज़ बदलते हैं और राज्य के हिसाब से अलग होते हैं (अलग VAT दरें), लेकिन हर तेल कंपनी सिर्फ अपने आंकड़े, अलग-अलग, सिर्फ उन शहरों के लिए छापती है जहां वह सेवा देती है।

इसके लिए कोई नया डेटा जुटाने की ज़रूरत नहीं है। बस किसी को जो पहले से सार्वजनिक है उसे लाना है, फॉर्मेट सामान्य बनाना है, और मंडी भाव, ईंधन के दाम, AQI, मौसम अलर्ट वगैरह को एक जगह रखना है ताकि कोई व्यक्ति पांच अलग सरकारी साइटों के पांच टैब खोलने के बजाय कुछ सेकंड में देख सके। **यही कमी IndiaRealTime पूरी करता है।**

### असली उपयोगकर्ताओं की कहानियां

**🌾 राजेश - किसान, पंजाब**
> "मैं APMC लुधियाना में गेहूं बेचता हूं। हर सुबह बेहतर दाम पर मोलभाव करने के लिए मुझे आस-पास के बाज़ारों में भाव जानने के लिए 3 अलग वेबसाइट देखनी पड़ती थीं। अब मैं बाज़ार जाने से पहले 10 सेकंड में indiarealtime पर देख लेता हूं।"

**🚖 प्रिया - ऑटो ड्राइवर, बेंगलुरु**
> "ईंधन के दाम रोज़ बदलते हैं और मेरी कमाई पर असर डालते हैं। पहले मैं अलग-अलग शहरों में दोस्तों को फोन करके दाम पूछती थी। अब मैं एक ही ऐप पर बेंगलुरु में पेट्रोल/डीज़ल के दाम देखकर अपना रूट तय करती हूं।"

**👨‍👩‍👧 अमित - अभिभावक, दिल्ली**
> "अपने बच्चों को बाहर खेलने भेजने से पहले मुझे AQI देखना पड़ता है। पहले मैं 5 अलग स्रोत गूगल करता था - Agmarknet, CPCB, मौसम साइटें - सब अलग फॉर्मेट में। अब एक क्लिक में पता चल जाता है कि बाहर जाना सुरक्षित है या नहीं।"

### हम क्या ट्रैक करते हैं

| श्रेणी | उदाहरण |
|---|---|
| दाम | मंडी (कृषि उत्पाद), ईंधन और LPG राज्य/शहर के हिसाब से, कीमती धातुएं, मुद्रा रूपांतरण, म्यूचुअल फंड NAV, FD दरें, टोल दरें |
| पर्यावरण | वायु गुणवत्ता (AQI, CPCB बैंड), मौसम अलर्ट, भूकंप अलर्ट |
| नागरिक / समय | बैंक अवकाश, पिनकोड लुकअप, टाइमज़ोन रूपांतरण |
| संस्कृति | पंचांग और मुहूर्त समय, व्रत कैलेंडर, राशिफल |
| खेल | लाइव क्रिकेट स्कोर |

कवरेज शहर/राज्य स्तर पर बारीक है, जहां भी मूल डेटा इसकी अनुमति देता है। उदाहरण के लिए, ईंधन के दाम हर शहर के हिसाब से ट्रैक होते हैं, राष्ट्रीय औसत नहीं।

इसके पीछे मुफ्त भारतीय डेटा API की पूरी सूची, उन सरकारी API सहित जिनका साइट अभी इस्तेमाल नहीं करती, [API/](API/) में है।

### विज़िटर के लिए यह कैसे काम करता है

- **स्थान के हिसाब से ब्राउज़ करें**: URL `/state/city/category/` पैटर्न फॉलो करते हैं (जैसे राज्य पेज, फिर शहर में जाना, फिर ईंधन के दाम या AQI जैसी किसी खास श्रेणी में)। ज़्यादातर श्रेणियां राष्ट्रीय ओवरव्यू और शहर-विशेष डिटेल पेज दोनों रूपों में मौजूद हैं।
- **दाम तुलना करें**: एक प्राइस-कंपैरिज़न व्यू किसी वस्तु या ईंधन प्रकार को शहरों/राज्यों में साथ-साथ दिखाता है, हर शहर का पेज अलग से खोलने के बजाय।
- **कैलकुलेटर**: एक मेटल्स कैलकुलेटर लाइव सोना/चांदी दरों को वज़न और शुद्धता के हिसाब से बदलता है, सिर्फ प्रति-ग्राम आंकड़ा दिखाने के बजाय।
- **शेयर कार्ड**: डेटा पेज एक शेयर करने लायक इमेज कार्ड (दाम, तारीख, स्रोत) बनाते हैं जो सोशल प्लेटफॉर्म के लिए सही आकार का हो, ताकि स्क्रीनशॉट के बिना कोई तथ्य शेयर हो सके।
- **लेखक हब**: हर लेख एक असली लेखक को, उनके प्रोफ़ाइल पेज के साथ, क्रेडिट किया जाता है, गुमनाम बायलाइन नहीं। `/authors/` सबको सूचीबद्ध करता है, `/author/<name>/` उनका प्रकाशित काम दिखाता है।

---

## 🏗️ वेब एप्लिकेशन की आर्किटेक्चर

भारत में ज़्यादातर "लाइव डेटा" साइटें या तो दिन में एक बार स्क्रैप करके उसे रीयल-टाइम कह देती हैं, या एक पेज-बिल्डर थीम पर दर्जन भर असंबंधित विजेट तब तक जोड़ती रहती हैं जब तक वह मेंटेन करने लायक नहीं रहती। IndiaRealTime करीब 15 अलग सार्वजनिक डेटा स्रोतों (सरकारी API, एक्सचेंज, मौसम और भूकंपीय फीड) से डेटा लेता है और हर एक को एक मोनोलिथ के बजाय अपनी छोटी, टेस्ट करने लायक इकाई में बदल देता है।

अगर आप डेटा-एग्रीगेशन साइट, प्लगइन-आधारित आर्किटेक्चर, या ऐसा कुछ बना रहे हैं जहां "अपस्ट्रीम API आखिरकार धोखा देगी" एक असली डिज़ाइन बाधा है, तो यह आपके लिए लिखा गया है।

### तकनीकी डायग्राम

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

### डिज़ाइन दर्शन

**हर डेटा स्रोत एक पूरी तरह स्वतंत्र प्लगइन है**, साझा इनजेशन पाइपलाइन नहीं। एक प्लगइन का अपना फ़ेच शेड्यूल, कैश, और फेल्योर हैंडलिंग होता है। अगर कोई सरकारी API अपना रिस्पॉन्स फॉर्मेट बदल दे या डाउन हो जाए, तो ठीक एक प्लगइन टूटता है। बाकी ~19 सेवा देना जारी रखते हैं। `irt-api-health-monitor` इसीलिए है क्योंकि इतने सारे स्वतंत्र मूविंग पार्ट्स के साथ, आपको एक ऐसी जगह चाहिए जो हर प्लगइन के लॉग हाथ से जांचने के बजाय इन सबको देखे।

### स्टैक

- **WordPress** (कस्टम थीम, कोई पेज बिल्डर नहीं): PHP टेम्पलेट, वनीला JS/CSS
- **~20 कस्टम प्लगइन**, हर डेटा स्रोत के लिए एक, हर एक की अपनी फ़ेच/कैश लेयर
- स्टोरेज और ट्रांज़िएंट कैशिंग के लिए **MySQL**; लोकल डेव के लिए Docker Compose
- एक समर्पित प्लगइन (`irt-dataset-schema`) के ज़रिए Schema.org स्ट्रक्चर्ड डेटा
- डेटा अपडेट होने पर तुरंत सर्च इंजन इंडेक्सिंग के लिए IndexNow इंटीग्रेशन

---

## 👨‍💻 डेवलपर इसका इस्तेमाल कैसे कर सकते हैं

अगर आप अपने ऐप में ऐसे फीचर बना रहे हैं जिन्हें भारतीय बाज़ार डेटा, लाइव प्राइसिंग, मौसम, या AQI चाहिए - तो आप IndiaRealTime को Python पैकेज, कमांड-लाइन टूल, या REST API के रूप में इस्तेमाल कर सकते हैं।

### इंस्टॉलेशन

**Python SDK (सुझाया गया)**
```bash
pip install indiarealtime
```

**📦 PyPI पर देखें:** https://pypi.org/project/indiarealtime/

**सोर्स से**
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com
pip install -e .
```

### असली इंटीग्रेशन उदाहरण

#### उदाहरण 1: मंडी भाव देखता किसान (CLI)
```bash
# Get wheat prices in Punjab
$ indiarealtime mandi --commodity wheat --state Punjab

Commodity  Market           State         City      Price (₹)  Unit
wheat      APMC Ludhiana    Punjab        Ludhiana  2450       Quintal
wheat      APMC Amritsar    Punjab        Amritsar  2420       Quintal
```

#### उदाहरण 2: प्राइस अलर्ट बॉट बनाता स्टार्टअप (Python)
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

#### उदाहरण 3: ईंधन के दाम जांचता डिलीवरी ऐप (REST API)
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

#### उदाहरण 4: AQI स्क्रैप करती न्यूज़ वेबसाइट (Python)
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

#### उदाहरण 5: दरें दिखाता फाइनेंस डैशबोर्ड (React)
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

### खुद आज़माएं

`scripts/fetch-pincode.js` फ़ेच-और-नॉर्मलाइज़ पैटर्न का एक छोटा स्टैंडअलोन उदाहरण है जो साइट के प्लगइन इस्तेमाल करते हैं, ऊपर की सूची में से बिना-key वाली एक API पर लागू:

```
node scripts/fetch-pincode.js 560001
```

### और उदाहरण
- [ऑटो-डॉक्स वाला FastAPI सर्वर](examples/fastapi_server.py)
- [प्राइस अलर्ट के लिए Telegram बॉट](examples/telegram_bot.py)
- [Google Sheets ऑटो-अपडेट](examples/google_sheets_integration.py)
- [Next.js डैशबोर्ड](examples/nextjs_mandi_dashboard.tsx)

पूरी सेटअप जानकारी के लिए [examples/README.md](examples/) देखें।

---

## ⚠️ तकनीकी चुनौतियां

### इंजीनियरिंग फैसले और सबक

इनमें से हर चुनौती इतनी लंबी हो गई कि इसका अपना पेज बनाना पड़ा:

- **[जानबूझकर पुराना डेटा दिखाना](notes/stale-cache-fallback.md)**: सरकारी और एक्सचेंज API भरोसेमंद नहीं होतीं, फिर भी साइट को भरोसेमंद दिखना ज़रूरी है। जब कोई अपस्ट्रीम API फेल होती है, तो हम एरर देने या कुछ न दिखाने के बजाय आखिरी अच्छा कैश किया गया डेटा दिखाते हैं।
- **[एक्सेसिबिलिटी और रंग, दोनों ज़रूरी हैं](notes/cvd-safe-aqi-colors.md)**: हर सिमेंटिक रंग को WCAG कंट्रास्ट और कलर-विज़न-डेफिशिएंसी सिमुलेशन के खिलाफ जांचा जाता है ताकि डेटा सबके लिए सुलभ हो।
- **[दो भाषाओं में एक जैसा हैश बनाना](notes/cross-language-hash-parity.md)**: PHP और JavaScript इंटीजर ओवरफ़्लो पर असहमत होते हैं, फिर भी लेखक अट्रीब्यूशन इस बात पर निर्भर करता है कि वे सहमत रहें।
- **[हर राज्य के लिए रीराइट-रूल regex के बिना लोकेशन राउटिंग](notes/location-routing-without-regex.md)**: हर क्षेत्र के लिए एक रीराइट रूल बनाने के बजाय हर राज्य और शहर पेज के लिए एक ही राउटिंग रास्ता।
- **[~20 प्लगइन एक मेंटेनेबिलिटी दांव है, मुफ्त की चीज़ नहीं](notes/plugin-per-source-tradeoff.md)**: फॉल्ट आइसोलेशन की कीमत, चीज़ों को एक जैसा बनाए रखने के लिए ज़्यादा सतह क्षेत्र है।

---

## 🚀 आगे क्या है

- हिस्टोरिकल प्राइस ट्रैकिंग अभी सिर्फ ईंधन और AQI के लिए मौजूद है, मंडी/कमोडिटी दामों के लिए नहीं। इसे वहां तक बढ़ाना अगला असली डेटा गैप है जिसे भरना है।
- स्रोतों की इजाज़त के मुताबिक और बारीक शहर कवरेज।
- `STYLE-GUIDE.md` में एक्सेसिबिलिटी ऑडिट को कलर कंट्रास्ट से आगे पूरे कीबोर्ड/स्क्रीन-रीडर पास तक बढ़ाना।

---

## 👋 लेखक के बारे में

यह रिपॉज़िटरी प्रोजेक्ट का एक ओवरव्यू है, साइट का सोर्स नहीं। WordPress कोडबेस अभी के लिए बंद है। हालांकि, [API सूची](API/) और `scripts/` फोल्डर PR के लिए खुले हैं - छूटी हुई API, सुधार, और फ़ेच के और उदाहरण, सबका स्वागत है।

अगर आपने ऊपर बताई किसी समस्या को हल किया है (स्टेल-कैश फॉलबैक स्ट्रैटेजी, प्लगइन-पर-सोर्स आर्किटेक्चर, CVD-सेफ कलर सिस्टम, क्रॉस-लैंग्वेज हैश पैरिटी), या आप अभी उसी दीवार से जूझ रहे हैं, तो एक [डिस्कशन](https://github.com/padmarajnidagundi/indiarealtime-com/issues) खोलें। मैं सच में नोट्स मिलाना चाहता हूं।

**योगदान का स्वागत है:** नए डेटा स्रोत प्लगइन के रूप में कैसे जोड़ें, इसके लिए [CONTRIBUTING.md](CONTRIBUTING.md) देखें, या मदद के अन्य तरीकों के लिए [CONTRIBUTORS_GUIDE.md](CONTRIBUTORS_GUIDE.md) देखें।

अगर आपके पास सवाल या विचार हैं, तो [GitHub Issues](https://github.com/padmarajnidagundi/indiarealtime-com/issues) या ईमेल के ज़रिए संपर्क करें।

<!-- TODO: contact / social links -->
