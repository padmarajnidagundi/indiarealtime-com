# IndiaRealTime - इंडिया रिअल टाइम | लाइव्ह मंडी भाव, इंधन दर, AQI, हवामान इशारे आणि क्रिकेट स्कोअर

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/padmarajnidagundi/indiarealtime-com)
[![License: MIT](https://img.shields.io/github/license/padmarajnidagundi/indiarealtime-com)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/padmarajnidagundi/indiarealtime-com?style=social)](https://github.com/padmarajnidagundi/indiarealtime-com/stargazers)
[![Open issues](https://img.shields.io/github/issues/padmarajnidagundi/indiarealtime-com)](https://github.com/padmarajnidagundi/indiarealtime-com/issues)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](API/)

🌐 **भाषा:** [English](README.md) · [हिन्दी](README.hi.md) · [বাংলা](README.bn.md) · मराठी · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [ಕನ್ನಡ](README.kn.md) · [മലയാളം](README.ml.md) · [ਪੰਜਾਬੀ](README.pa.md) · [ଓଡ଼ିଆ](README.or.md) · [অসমীয়া](README.as.md) · [اردو](README.ur.md) · [संस्कृतम्](README.sa.md) · [नेपाली](README.ne.md) · [कोंकणी](README.kok.md) · [मैथिली](README.mai.md)

**~२० स्वतंत्र WordPress प्लगइन्स, प्रत्येक एका वेगळ्या सार्वजनिक डेटा स्रोतासाठी, मिळून एक अशी साइट चालवतात जी संपूर्ण भारतभर लाइव्ह मंडी भाव, इंधनाचे दर, हवेची गुणवत्ता, हवामान इशारे, भूकंप आणि क्रिकेट स्कोअर ट्रॅक करते. यामागील सरकारी API बंद पडली तरी ती चांगला डेटा देत राहते.**

**लाइव्ह साइट:** https://indiarealtime.com

## वेबसाइट स्क्रीनशॉट

| वेब व्ह्यू | मोबाइल व्ह्यू |
|---|---|
| ![IndiaRealTime website web view](assets/website-webview.png) | ![IndiaRealTime website mobile view](assets/website-mobile.png) |

---

## 📱 IndiaRealTime बद्दल

### समस्या काय आहे

डेटा आधीच अस्तित्वात आहे आणि बहुतांशी सार्वजनिक आहे. फक्त तो अनेक वेगवेगळ्या सरकारी आणि PSU पोर्टल्सवर विखुरलेला आहे, प्रत्येकाचा स्वतःचा फॉरमॅट, अपडेटची वेळ, आणि (अनेकदा) विश्वासार्हतेच्या अडचणी.

पंजाबमध्ये मंडी भाव तपासणाऱ्या शेतकऱ्याला Agmarknet नावाचं काहीतरी अस्तित्वात आहे हे माहीत असायला हवं. बाहेर जाणं सुरक्षित आहे का हे तपासणाऱ्या कोणालाही माहीत असायला हवं की CPCB वेगळ्या वेबसाइटवर, वेगळ्या फॉरमॅटमध्ये AQI प्रकाशित करते. इंधनाचे दर रोज बदलतात आणि राज्यानुसार वेगळे असतात (वेगवेगळे VAT दर), पण प्रत्येक तेल कंपनी फक्त स्वतःचे आकडे, वेगवेगळे, फक्त जिथे सेवा देते त्या शहरांसाठी प्रकाशित करते.

यासाठी नवीन डेटा गोळा करण्याची गरज नाही. फक्त कोणीतरी आधीच सार्वजनिक असलेलं आणून, फॉरमॅट सामान्य करून, मंडी भाव, इंधनाचे दर, AQI, हवामान इशारे वगैरे एका ठिकाणी ठेवायला हवेत जेणेकरून एखादी व्यक्ती पाच वेगवेगळ्या सरकारी साइट्सचे पाच टॅब उघडण्याऐवजी काही सेकंदांत तपासू शकेल. **हीच उणीव IndiaRealTime भरून काढते.**

### खऱ्या वापरकर्त्यांच्या गोष्टी

**🌾 राजेश - पंजाबमधील शेतकरी**
> "मी APMC लुधियानामध्ये गहू विकतो. दररोज सकाळी चांगल्या दरात घासाघीस करण्यासाठी मला जवळपासच्या बाजारातील भाव तपासण्यासाठी ३ वेगळ्या वेबसाइट पाहाव्या लागत. आता बाजारात जाण्याआधी मी १० सेकंदात indiarealtime वर तपासतो."

**🚖 प्रिया - बंगळुरूतील ऑटो चालक**
> "इंधनाचे दर रोज बदलतात आणि माझ्या कमाईवर परिणाम करतात. आधी मी वेगवेगळ्या शहरांतल्या मित्रांना फोन करून दर विचारायचे. आता मी एका अ‍ॅपवर बंगळुरूभरातील पेट्रोल/डिझेलचे दर पाहून माझा मार्ग ठरवते."

**👨‍👩‍👧 अमित - दिल्लीतील पालक**
> "मुलांना बाहेर खेळायला पाठवण्याआधी मला AQI तपासावा लागतो. आधी मी ५ वेगळे स्रोत गूगल करत असे - Agmarknet, CPCB, हवामान साइट्स - सगळे वेगळ्या फॉरमॅटमध्ये. आता एका क्लिकमध्ये कळतं बाहेर जाणं सुरक्षित आहे का."

### आम्ही काय ट्रॅक करतो

| श्रेणी | उदाहरणे |
|---|---|
| भाव | मंडी (कृषी उत्पादन), इंधन आणि LPG राज्य/शहरानुसार, मौल्यवान धातू, चलन रूपांतरण, म्युच्युअल फंड NAV, FD दर, टोल दर |
| पर्यावरण | हवेची गुणवत्ता (AQI, CPCB बँड), हवामान इशारे, भूकंप इशारे |
| नागरी / वेळ | बँक सुट्ट्या, पिनकोड लुकअप, टाइमझोन रूपांतरण |
| संस्कृती | पंचांग व मुहूर्त वेळा, व्रत कॅलेंडर, राशीभविष्य |
| खेळ | लाइव्ह क्रिकेट स्कोअर |

कव्हरेज शहर/राज्य स्तरावर बारकाईने आहे, जिथे मूळ डेटा तसं करू देतो. उदाहरणार्थ, इंधनाचे दर प्रत्येक शहरानुसार ट्रॅक केले जातात, राष्ट्रीय सरासरी नाही.

यामागील मोफत भारतीय डेटा API ची संपूर्ण यादी, साइट अजून वापरत नसलेल्या सरकारी API सह, [API/](API/) मध्ये आहे.

### भेट देणाऱ्यांसाठी हे कसं काम करतं

- **स्थानानुसार ब्राउझ करा**: URL `/state/city/category/` अशा पॅटर्नमध्ये असतात (उदा. राज्य पान, नंतर शहरात जाणे, नंतर इंधन दर किंवा AQI सारख्या विशिष्ट श्रेणीत). बहुतेक श्रेणी राष्ट्रीय आढावा आणि शहर-विशिष्ट तपशील पान अशा दोन्ही स्वरूपात असतात.
- **भाव तुलना करा**: प्राइस-कंपॅरिझन व्ह्यू एखादी वस्तू किंवा इंधन प्रकार शहरे/राज्यांमध्ये एकत्र दाखवतो, प्रत्येक शहराचं पान वेगळं उघडण्याऐवजी.
- **कॅल्क्युलेटर**: मेटल्स कॅल्क्युलेटर लाइव्ह सोनं/चांदी दर वजन आणि शुद्धतेनुसार रूपांतरित करतो, फक्त प्रति-ग्रॅम आकडा दाखवण्याऐवजी.
- **शेअर कार्ड**: डेटा पानं सोशल प्लॅटफॉर्मसाठी योग्य आकाराचं शेअर करण्यायोग्य इमेज कार्ड (भाव, तारीख, स्रोत) तयार करतात, जेणेकरून स्क्रीनशॉटशिवाय एखादी माहिती शेअर करता येईल.
- **लेखक हब**: प्रत्येक लेख खऱ्या लेखकाच्या नावे, त्यांच्या प्रोफाइल पानासह, श्रेय दिला जातो, अनामिक बायलाइन नाही. `/authors/` सर्वांची यादी दाखवतं, `/author/<name>/` त्यांचं प्रकाशित काम दाखवतं.

---

## 🏗️ वेब अ‍ॅप्लिकेशनची आर्किटेक्चर

भारतातील बहुतेक "लाइव्ह डेटा" साइट्स एकतर दिवसातून एकदा स्क्रॅप करून त्याला रिअल-टाइम म्हणतात, किंवा पेज-बिल्डर थीमवर डझनभर असंबंधित विजेट्स जोडत राहतात जोवर ती मेंटेन करण्याजोगी राहत नाही. IndiaRealTime सुमारे १५ वेगवेगळ्या सार्वजनिक डेटा स्रोतांमधून (सरकारी API, एक्स्चेंज, हवामान व भूकंपीय फीड) डेटा घेतो आणि प्रत्येकाला एका मोनोलिथऐवजी स्वतःच्या लहान, चाचणीयोग्य युनिटमध्ये रूपांतरित करतो.

तुम्ही डेटा-अ‍ॅग्रिगेशन साइट, प्लगइन-आधारित आर्किटेक्चर, किंवा असं काहीतरी बनवत असाल जिथे "अपस्ट्रीम API शेवटी फसवणार" ही खरी डिझाइन मर्यादा आहे, तर हे तुमच्यासाठी लिहिलं आहे.

### तांत्रिक आकृती

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

### डिझाइन तत्त्वज्ञान

**प्रत्येक डेटा स्रोत हा पूर्णपणे स्वतंत्र प्लगइन आहे**, शेअर केलेली इनजेशन पाइपलाइन नाही. एका प्लगइनचं स्वतःचं फेच शेड्युल, कॅश, आणि फेल्युअर हँडलिंग असतं. एखाद्या सरकारी API ने आपला रिस्पॉन्स फॉरमॅट बदलला किंवा ती डाउन झाली, तर नेमकं एकच प्लगइन तुटतं. बाकीचे ~१९ सेवा देत राहतात. `irt-api-health-monitor` अस्तित्वात आहे कारण इतक्या स्वतंत्र हलत्या भागांसह, प्रत्येक प्लगइनचे लॉग स्वतः तपासण्याऐवजी सगळ्यांवर लक्ष ठेवणारी एक जागा हवी असते.

### स्टॅक

- **WordPress** (कस्टम थीम, पेज बिल्डर नाही): PHP टेम्प्लेट्स, वॅनिला JS/CSS
- **~२० कस्टम प्लगइन्स**, प्रत्येक डेटा स्रोतासाठी एक, प्रत्येकाचा स्वतःचा फेच/कॅश लेयर
- साठवणूक आणि ट्रान्झिएंट कॅशिंगसाठी **MySQL**; लोकल डेव्हसाठी Docker Compose
- एका समर्पित प्लगइनद्वारे (`irt-dataset-schema`) Schema.org स्ट्रक्चर्ड डेटा
- डेटा अपडेटवर तत्काळ सर्च इंजिन इंडेक्सिंगसाठी IndexNow इंटिग्रेशन

---

## 👨‍💻 डेव्हलपर्स याचा वापर कसा करू शकतात

तुम्ही तुमच्या अ‍ॅपमध्ये भारतीय बाजार डेटा, लाइव्ह प्राइसिंग, हवामान, किंवा AQI हवा असलेले फीचर्स बनवत असाल - तर तुम्ही IndiaRealTime ला Python पॅकेज, कमांड-लाइन टूल, किंवा REST API म्हणून वापरू शकता.

### इन्स्टॉलेशन

**Python SDK (शिफारस केलेलं)**
```bash
pip install indiarealtime
```

**📦 PyPI वर पहा:** https://pypi.org/project/indiarealtime/

**सोर्सवरून**
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com
pip install -e .
```

### खरी इंटिग्रेशन उदाहरणे

#### उदाहरण १: मंडी भाव तपासणारा शेतकरी (CLI)
```bash
# Get wheat prices in Punjab
$ indiarealtime mandi --commodity wheat --state Punjab

Commodity  Market           State         City      Price (₹)  Unit
wheat      APMC Ludhiana    Punjab        Ludhiana  2450       Quintal
wheat      APMC Amritsar    Punjab        Amritsar  2420       Quintal
```

#### उदाहरण २: प्राइस अलर्ट बॉट बनवणारं स्टार्टअप (Python)
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

#### उदाहरण ३: इंधन दर तपासणारं डिलिव्हरी अ‍ॅप (REST API)
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

#### उदाहरण ४: AQI स्क्रॅप करणारी न्यूज वेबसाइट (Python)
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

#### उदाहरण ५: दर दाखवणारा फायनान्स डॅशबोर्ड (React)
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

### लोकल डेव्हलपमेंट सेटअप (Docker)
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com

# Start all services
docker-compose up

# WordPress at http://localhost:8080
# API Server at http://localhost:5000
# Monitoring at http://localhost:3000
```

### स्वतः वापरून पाहा

`scripts/fetch-pincode.js` हे साइटचे प्लगइन्स वापरतात त्या फेच-अँड-नॉर्मलाइझ पॅटर्नचं एक लहान स्वतंत्र उदाहरण आहे, वरील यादीतील की न लागणाऱ्या एका API वर लागू केलेलं:

```
node scripts/fetch-pincode.js 560001
```

### आणखी उदाहरणे
- [ऑटो-डॉक्ससह FastAPI सर्व्हर](examples/fastapi_server.py)
- [प्राइस अलर्टसाठी Telegram बॉट](examples/telegram_bot.py)
- [Google Sheets ऑटो-अपडेट](examples/google_sheets_integration.py)
- [Next.js डॅशबोर्ड](examples/nextjs_mandi_dashboard.tsx)

संपूर्ण सेटअप सूचनांसाठी [examples/README.md](examples/) पहा.

---

## ⚠️ तांत्रिक आव्हानं

### इंजिनिअरिंग निर्णय आणि धडे

यातील प्रत्येक आव्हान इतकं मोठं झालं की त्याला स्वतःचं पान द्यावं लागलं:

- **[जाणूनबुजून जुना डेटा दाखवणं](notes/stale-cache-fallback.md)**: सरकारी आणि एक्स्चेंज API विश्वासार्ह नसतात, तरीही साइटला विश्वासार्ह दिसावं लागतं. एखादी अपस्ट्रीम API अयशस्वी झाली की, आम्ही एरर देण्याऐवजी किंवा काहीच न दाखवण्याऐवजी शेवटचं चांगलं कॅश केलेलं मूल्य दाखवतो.
- **[अ‍ॅक्सेसिबिलिटी आणि रंग, दोन्ही महत्त्वाचे](notes/cvd-safe-aqi-colors.md)**: प्रत्येक सिमँटिक रंग WCAG कॉन्ट्रास्ट आणि कलर-व्हिजन-डेफिशियन्सी सिम्युलेशनविरुद्ध तपासला जातो जेणेकरून डेटा सर्वांसाठी अ‍ॅक्सेसिबल राहील.
- **[दोन भाषांमध्ये एकसारखा हॅश जुळवणं](notes/cross-language-hash-parity.md)**: PHP आणि JavaScript इंटिजर ओव्हरफ्लोवर असहमत असतात, तरीही लेखक अ‍ॅट्रिब्युशन त्यांनी सहमत राहण्यावर अवलंबून आहे.
- **[प्रत्येक राज्यासाठी रिराइट-रूल regex शिवाय लोकेशन राउटिंग](notes/location-routing-without-regex.md)**: प्रत्येक प्रदेशासाठी एक रिराइट रूल बनवण्याऐवजी प्रत्येक राज्य व शहर पानासाठी एकच राउटिंग मार्ग.
- **[~२० प्लगइन्स ही मेंटेनेबिलिटीची पैज आहे, फुकटची गोष्ट नाही](notes/plugin-per-source-tradeoff.md)**: फॉल्ट आयसोलेशनची किंमत म्हणजे सगळं सुसंगत ठेवण्यासाठी लागणारं अधिक क्षेत्रफळ.

---

## 🚀 पुढे काय

- हिस्टॉरिकल प्राइस ट्रॅकिंग सध्या फक्त इंधन आणि AQI साठी आहे, मंडी/कमोडिटी भावांसाठी अजून नाही. तिथवर ते वाढवणं ही पुढची खरी डेटा उणीव आहे जी भरून काढायची आहे.
- स्रोत परवानगी देतील तसं अधिक बारकाईने शहर कव्हरेज.
- `STYLE-GUIDE.md` मधील अ‍ॅक्सेसिबिलिटी ऑडिट रंग कॉन्ट्रास्टच्या पलीकडे नेऊन पूर्ण कीबोर्ड/स्क्रीन-रीडर पासपर्यंत विस्तारणं.

---

## 👋 लेखकाबद्दल

हे रिपॉझिटरी प्रोजेक्टचा आढावा आहे, साइटचा सोर्स नाही. WordPress कोडबेस सध्या तरी बंद आहे. मात्र, [API यादी](API/) आणि `scripts/` फोल्डर PR साठी खुले आहेत - गहाळ API, दुरुस्त्या, फेचची आणखी उदाहरणं, सगळं स्वागतार्ह आहे.

तुम्ही वरीलपैकी कोणत्याही समस्येचं एखादं स्वरूप सोडवलं असेल (स्टेल-कॅश फॉलबॅक स्ट्रॅटेजी, प्लगइन-पर-सोर्स आर्किटेक्चर, CVD-सेफ कलर सिस्टम, क्रॉस-लँग्वेज हॅश पॅरिटी), किंवा तुम्ही आत्ता त्याच भिंतीशी झगडत असाल, तर एक [डिस्कशन](https://github.com/padmarajnidagundi/indiarealtime-com/issues) उघडा. मला खरोखर नोट्स जुळवायच्या आहेत.

**योगदानाचं स्वागत आहे:** नवीन डेटा स्रोत प्लगइन म्हणून कसे जोडायचे यासाठी [CONTRIBUTING.md](CONTRIBUTING.md) पहा, किंवा मदतीच्या इतर मार्गांसाठी [CONTRIBUTORS_GUIDE.md](CONTRIBUTORS_GUIDE.md) पहा.

काही प्रश्न किंवा कल्पना असतील, तर [GitHub Issues](https://github.com/padmarajnidagundi/indiarealtime-com/issues) किंवा ईमेलद्वारे संपर्क साधा.

<!-- TODO: contact / social links -->
