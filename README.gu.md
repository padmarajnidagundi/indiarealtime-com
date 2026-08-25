# IndiaRealTime

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/padmarajnidagundi/indiarealtime-com)
[![License: MIT](https://img.shields.io/github/license/padmarajnidagundi/indiarealtime-com)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/padmarajnidagundi/indiarealtime-com?style=social)](https://github.com/padmarajnidagundi/indiarealtime-com/stargazers)
[![Open issues](https://img.shields.io/github/issues/padmarajnidagundi/indiarealtime-com)](https://github.com/padmarajnidagundi/indiarealtime-com/issues)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](API/)

🌐 **ભાષા:** [English](README.md) · [हिन्दी](README.hi.md) · [বাংলা](README.bn.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · ગુજરાતી · [ಕನ್ನಡ](README.kn.md) · [മലയാളം](README.ml.md) · [ਪੰਜਾਬੀ](README.pa.md) · [ଓଡ଼ିଆ](README.or.md) · [অসমীয়া](README.as.md) · [اردو](README.ur.md) · [संस्कृतम्](README.sa.md) · [नेपाली](README.ne.md) · [कोंकणी](README.kok.md) · [मैथिली](README.mai.md)

**~20 સ્વતંત્ર WordPress પ્લગિન્સ, દરેક એક અલગ પબ્લિક ડેટા સ્રોત માટે, સાથે મળીને એક જ સાઇટ ચલાવે છે જે સમગ્ર ભારતમાં લાઇવ મંડી ભાવ, ઇંધણના ભાવ, હવાની ગુણવત્તા, હવામાન ચેતવણીઓ, ધરતીકંપ અને ક્રિકેટ સ્કોર ટ્રેક કરે છે. તેની પાછળની સરકારી API કામ કરવાનું બંધ કરી દે તો પણ આ સારો ડેટા આપવાનું ચાલુ રાખે છે.**

**લાઇવ સાઇટ:** https://indiarealtime.com

## વેબસાઇટ સ્ક્રીનશોટ

| વેબ વ્યૂ | મોબાઇલ વ્યૂ |
|---|---|
| ![IndiaRealTime website web view](assets/website-webview.png) | ![IndiaRealTime website mobile view](assets/website-mobile.png) |

---

## 📱 IndiaRealTime વિશે

### સમસ્યા શું છે

ડેટા પહેલેથી જ અસ્તિત્વમાં છે અને મોટાભાગે પબ્લિક છે. તે ફક્ત ડઝનેક અલગ-અલગ સરકારી અને PSU પોર્ટલ પર વિખેરાયેલો છે, દરેકનું પોતાનું ફોર્મેટ, અપડેટ થવાનો સમય, અને (ઘણીવાર) વિશ્વસનીયતાની સમસ્યાઓ.

પંજાબમાં મંડી ભાવ તપાસવા માંગતા ખેડૂતને ખબર હોવી જોઈએ કે Agmarknet નામનું કંઈક અસ્તિત્વમાં છે. બહાર જવું સુરક્ષિત છે કે નહીં તે જાણવા માંગતા કોઈને ખબર હોવી જોઈએ કે CPCB અલગ વેબસાઇટ પર, અલગ ફોર્મેટમાં AQI પ્રકાશિત કરે છે. ઇંધણના ભાવ દરરોજ બદલાય છે અને રાજ્ય પ્રમાણે અલગ હોય છે (અલગ VAT દર), પરંતુ દરેક ઓઇલ કંપની ફક્ત પોતાના આંકડા, અલગ-અલગ, ફક્ત જે શહેરોમાં તે સેવા આપે છે તેના માટે જ પ્રકાશિત કરે છે.

આ માટે નવો ડેટા એકત્ર કરવાની જરૂર નથી. ફક્ત કોઈએ જે પહેલેથી પબ્લિક છે તે લાવવું, ફોર્મેટ સામાન્ય બનાવવું, અને મંડી ભાવ, ઇંધણના ભાવ, AQI, હવામાન ચેતવણીઓ વગેરેને એક જ જગ્યાએ મૂકવું જરૂરી છે જેથી કોઈ વ્યક્તિ પાંચ અલગ સરકારી સાઇટના પાંચ ટેબ ખોલવાને બદલે થોડી સેકન્ડોમાં જોઈ શકે. **આ જ ખામી IndiaRealTime પૂરી કરે છે.**

### સાચા વપરાશકર્તાઓની વાર્તાઓ

**🌾 રાજેશ - પંજાબમાં ખેડૂત**
> "હું APMC લુધિયાણામાં ઘઉં વેચું છું. દરરોજ સવારે સારા ભાવે સોદો કરવા માટે મારે નજીકના બજારોમાં ભાવ જોવા 3 અલગ વેબસાઇટ જોવી પડતી હતી. હવે બજારમાં જતાં પહેલાં હું 10 સેકન્ડમાં indiarealtime પર જોઈ લઉં છું."

**🚖 પ્રિયા - બેંગલુરુમાં ઓટો ડ્રાઇવર**
> "ઇંધણના ભાવ દરરોજ બદલાય છે અને મારી કમાણી પર અસર કરે છે. પહેલાં હું અલગ-અલગ શહેરોમાં મિત્રોને ફોન કરીને ભાવ જાણતી હતી. હવે હું એક જ એપ પર બેંગલુરુભરમાં પેટ્રોલ/ડીઝલના ભાવ જોઈને મારો રૂટ નક્કી કરું છું."

**👨‍👩‍👧 અમિત - દિલ્હીમાં વાલી**
> "મારા બાળકોને બહાર રમવા મોકલતાં પહેલાં મારે AQI જોવું પડે છે. પહેલાં હું 5 અલગ સ્રોત ગૂગલ કરતો - Agmarknet, CPCB, હવામાન સાઇટ્સ - બધા અલગ ફોર્મેટમાં. હવે એક જ ક્લિકમાં ખબર પડે છે કે બહાર જવું સુરક્ષિત છે કે નહીં."

### અમે શું ટ્રેક કરીએ છીએ

| શ્રેણી | ઉદાહરણો |
|---|---|
| ભાવ | મંડી (કૃષિ પેદાશ), ઇંધણ અને LPG રાજ્ય/શહેર પ્રમાણે, કિંમતી ધાતુઓ, ચલણ રૂપાંતરણ, મ્યુચ્યુઅલ ફંડ NAV, FD દર, ટોલ દર |
| પર્યાવરણ | હવાની ગુણવત્તા (AQI, CPCB બેન્ડ), હવામાન ચેતવણીઓ, ધરતીકંપ ચેતવણીઓ |
| નાગરિક / સમય | બેંક રજાઓ, પિનકોડ લુકઅપ, ટાઇમઝોન રૂપાંતરણ |
| સંસ્કૃતિ | પંચાંગ અને મુહૂર્ત સમય, વ્રત કેલેન્ડર, રાશિફળ |
| રમત | લાઇવ ક્રિકેટ સ્કોર |

મૂળ ડેટા જ્યાં પરવાનગી આપે ત્યાં કવરેજ શહેર/રાજ્ય સ્તરે ઝીણવટભર્યું છે. ઉદાહરણ તરીકે, ઇંધણના ભાવ રાષ્ટ્રીય સરેરાશ નહીં, દરેક શહેર પ્રમાણે ટ્રેક કરવામાં આવે છે.

આની પાછળની મફત ભારતીય ડેટા API ની સંપૂર્ણ યાદી, સાઇટ હજુ સુધી ઉપયોગ ન કરતી હોય તેવી સરકારી API સહિત, [API/](API/) માં છે.

### મુલાકાતીઓ માટે આ કેવી રીતે કામ કરે છે

- **સ્થાન પ્રમાણે બ્રાઉઝ કરો**: URL `/state/city/category/` પેટર્ન અનુસરે છે (દા.ત. રાજ્ય પેજ, પછી શહેરમાં જવું, પછી ઇંધણ ભાવ કે AQI જેવી કોઈ ચોક્કસ કેટેગરીમાં). મોટાભાગની કેટેગરીઓ રાષ્ટ્રીય ઓવરવ્યૂ અને શહેર-વિશિષ્ટ વિગત પેજ બંને સ્વરૂપે અસ્તિત્વમાં છે.
- **ભાવ સરખાવો**: પ્રાઇસ-કમ્પેરિઝન વ્યૂ કોઈ ચીજવસ્તુ કે ઇંધણ પ્રકારને શહેરો/રાજ્યોમાં સાથે-સાથે બતાવે છે, દરેક શહેરનું પેજ અલગ ખોલવાને બદલે.
- **કેલ્ક્યુલેટર**: એક મેટલ્સ કેલ્ક્યુલેટર ફક્ત પ્રતિ-ગ્રામ આંકડો બતાવવાને બદલે લાઇવ સોના/ચાંદીના દરને વજન અને શુદ્ધતા પ્રમાણે રૂપાંતરિત કરે છે.
- **શેર કાર્ડ**: ડેટા પેજ સોશિયલ પ્લેટફોર્મ માટે યોગ્ય કદનું શેર કરી શકાય તેવું ઇમેજ કાર્ડ (ભાવ, તારીખ, સ્રોત) બનાવે છે, જેથી સ્ક્રીનશોટ વગર જ કોઈ હકીકત શેર થઈ શકે.
- **લેખક હબ**: દરેક લેખને એક સાચા લેખકને, તેમના પ્રોફાઇલ પેજ સાથે, ક્રેડિટ આપવામાં આવે છે, અનામી બાયલાઇન નહીં. `/authors/` બધાની યાદી બતાવે છે, `/author/<name>/` તેમનું પ્રકાશિત કામ બતાવે છે.

---

## 🏗️ વેબ એપ્લિકેશનનું આર્કિટેક્ચર

ભારતમાં મોટાભાગની "લાઇવ ડેટા" સાઇટ્સ કાં તો દિવસમાં એકવાર સ્ક્રેપ કરીને તેને રીયલ-ટાઇમ કહે છે, અથવા તે મેઇન્ટેન કરી શકાય તેવી ન રહે ત્યાં સુધી પેજ-બિલ્ડર થીમ પર ડઝનેક અસંબંધિત વિજેટ્સ ઉમેરતી રહે છે. IndiaRealTime લગભગ 15 અલગ પબ્લિક ડેટા સ્રોતો (સરકારી API, એક્સચેન્જ, હવામાન અને ધરતીકંપ ફીડ) માંથી ડેટા લે છે અને દરેકને એક મોનોલિથને બદલે તેની પોતાની નાની, ટેસ્ટ કરી શકાય તેવી યુનિટમાં ફેરવે છે.

જો તમે ડેટા-એગ્રિગેશન સાઇટ, પ્લગિન-આધારિત આર્કિટેક્ચર, અથવા એવું કંઈક બનાવી રહ્યા છો જ્યાં "અપસ્ટ્રીમ API આખરે દગો દેશે" એ એક સાચી ડિઝાઇન મર્યાદા છે, તો આ તમારા માટે જ લખાયું છે.

### ટેકનિકલ ડાયાગ્રામ

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

### ડિઝાઇન ફિલોસોફી

**દરેક ડેટા સ્રોત એક સંપૂર્ણ સ્વતંત્ર પ્લગિન છે**, શેર કરેલી ઇન્જેશન પાઇપલાઇન નહીં. એક પ્લગિનનું પોતાનું ફેચ શેડ્યૂલ, કેશ, અને ફેલ્યોર હેન્ડલિંગ હોય છે. જો કોઈ સરકારી API તેનું રિસ્પોન્સ ફોર્મેટ બદલે અથવા ડાઉન થાય, તો બરાબર એક પ્લગિન તૂટે છે. બાકીના ~19 સેવા આપવાનું ચાલુ રાખે છે. `irt-api-health-monitor` એટલા માટે છે કારણ કે આટલા બધા સ્વતંત્ર ફરતા ભાગો સાથે, દરેક પ્લગિનના લોગ જાતે તપાસવાને બદલે તે બધાને એક જ જગ્યાએથી જોતી વ્યવસ્થા જોઈએ.

### સ્ટેક

- **WordPress** (કસ્ટમ થીમ, પેજ બિલ્ડર નહીં): PHP ટેમ્પ્લેટ, વેનિલા JS/CSS
- **~20 કસ્ટમ પ્લગિન્સ**, દરેક ડેટા સ્રોત માટે એક, દરેકનું પોતાનું ફેચ/કેશ લેયર
- સ્ટોરેજ અને ટ્રાન્ઝિયન્ટ કેશિંગ માટે **MySQL**; લોકલ ડેવ માટે Docker Compose
- એક સમર્પિત પ્લગિન (`irt-dataset-schema`) દ્વારા Schema.org સ્ટ્રક્ચર્ડ ડેટા
- ડેટા અપડેટ પર લગભગ તાત્કાલિક સર્ચ એન્જિન ઇન્ડેક્સિંગ માટે IndexNow ઇન્ટિગ્રેશન

---

## 👨‍💻 ડેવલપર્સ આનો ઉપયોગ કેવી રીતે કરી શકે

જો તમે તમારી એપમાં ભારતીય બજાર ડેટા, લાઇવ પ્રાઇસિંગ, હવામાન, અથવા AQI જોઈતા ફીચર્સ બનાવી રહ્યા છો - તો તમે IndiaRealTime ને Python પેકેજ, કમાન્ડ-લાઇન ટૂલ, અથવા REST API તરીકે વાપરી શકો છો.

### ઇન્સ્ટોલેશન

**Python SDK (ભલામણ કરેલ)**
```bash
pip install indiarealtime
```

**📦 PyPI પર જુઓ:** https://pypi.org/project/indiarealtime/

**સોર્સમાંથી**
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com
pip install -e .
```

### વાસ્તવિક ઇન્ટિગ્રેશન ઉદાહરણો

#### ઉદાહરણ 1: મંડી ભાવ તપાસતો ખેડૂત (CLI)
```bash
# Get wheat prices in Punjab
$ indiarealtime mandi --commodity wheat --state Punjab

Commodity  Market           State         City      Price (₹)  Unit
wheat      APMC Ludhiana    Punjab        Ludhiana  2450       Quintal
wheat      APMC Amritsar    Punjab        Amritsar  2420       Quintal
```

#### ઉદાહરણ 2: પ્રાઇસ એલર્ટ બોટ બનાવતું સ્ટાર્ટઅપ (Python)
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

#### ઉદાહરણ 3: ઇંધણના ભાવ તપાસતી ડિલિવરી એપ (REST API)
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

#### ઉદાહરણ 4: AQI સ્ક્રેપ કરતી ન્યૂઝ વેબસાઇટ (Python)
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

#### ઉદાહરણ 5: દરો બતાવતું ફાઇનાન્સ ડેશબોર્ડ (React)
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

### લોકલ ડેવલપમેન્ટ સેટઅપ (Docker)
```bash
git clone https://github.com/padmarajnidagundi/indiarealtime-com.git
cd indiarealtime-com

# Start all services
docker-compose up

# WordPress at http://localhost:8080
# API Server at http://localhost:5000
# Monitoring at http://localhost:3000
```

### જાતે અજમાવો

`scripts/fetch-pincode.js` એ ફેચ-એન્ડ-નોર્મલાઇઝ પેટર્નનું એક નાનું સ્ટેન્ડઅલોન ઉદાહરણ છે જે સાઇટના પ્લગિન્સ વાપરે છે, ઉપરની યાદીમાંથી કી વગરની એક API પર લાગુ કરેલું:

```
node scripts/fetch-pincode.js 560001
```

### વધુ ઉદાહરણો
- [ઓટો-ડોક્સ સાથે FastAPI સર્વર](examples/fastapi_server.py)
- [પ્રાઇસ એલર્ટ માટે Telegram બોટ](examples/telegram_bot.py)
- [Google Sheets ઓટો-અપડેટ](examples/google_sheets_integration.py)
- [Next.js ડેશબોર્ડ](examples/nextjs_mandi_dashboard.tsx)

સંપૂર્ણ સેટઅપ સૂચનાઓ માટે [examples/README.md](examples/) જુઓ.

---

## ⚠️ ટેકનિકલ પડકારો

### એન્જિનિયરિંગ નિર્ણયો અને પાઠ

આમાંનો દરેક પડકાર એટલો લાંબો થઈ ગયો કે તેને પોતાનું પેજ મળવું જોઈએ:

- **[જાણીજોઈને જૂનો ડેટા આપવો](notes/stale-cache-fallback.md)**: સરકારી અને એક્સચેન્જ API વિશ્વસનીય નથી, છતાં સાઇટે વિશ્વસનીય દેખાવું જ પડે. જ્યારે કોઈ અપસ્ટ્રીમ API નિષ્ફળ જાય, ત્યારે અમે એરર આપવા કે કંઈ ન બતાવવાને બદલે છેલ્લું સારું કેશ કરેલું મૂલ્ય આપીએ છીએ.
- **[એક્સેસિબિલિટી અને રંગ, બંને મહત્વના](notes/cvd-safe-aqi-colors.md)**: દરેક સિમેન્ટિક રંગને WCAG કોન્ટ્રાસ્ટ અને કલર-વિઝન-ડેફિશિયન્સી સિમ્યુલેશન સામે તપાસવામાં આવે છે જેથી ડેટા બધા માટે એક્સેસિબલ રહે.
- **[બે ભાષાઓમાં એકસમાન હેશ મેળવવો](notes/cross-language-hash-parity.md)**: PHP અને JavaScript ઇન્ટિજર ઓવરફ્લો પર સહમત નથી, છતાં લેખક એટ્રિબ્યુશન તેમના સહમત રહેવા પર જ આધાર રાખે છે.
- **[દરેક રાજ્ય માટે રીરાઇટ-રૂલ regex વગર લોકેશન રાઉટિંગ](notes/location-routing-without-regex.md)**: દરેક પ્રદેશ માટે એક રીરાઇટ રૂલને બદલે દરેક રાજ્ય અને શહેર પેજ માટે એક જ રાઉટિંગ પાથ.
- **[~20 પ્લગિન્સ એક મેઇન્ટેનેબિલિટી હોડ છે, મફતની વસ્તુ નહીં](notes/plugin-per-source-tradeoff.md)**: ફોલ્ટ આઇસોલેશનની કિંમત એટલે બધું સુસંગત રાખવા માટે વધુ સપાટી વિસ્તાર.

---

## 🚀 આગળ શું

- ઐતિહાસિક ભાવ ટ્રેકિંગ હાલમાં ફક્ત ઇંધણ અને AQI માટે અસ્તિત્વમાં છે, મંડી/કોમોડિટી ભાવ માટે હજુ નહીં. તેને ત્યાં સુધી વિસ્તારવું એ આગળનો ખરો ડેટા ગેપ છે જે પૂરવાનો છે.
- સ્રોતો પરવાનગી આપે તેમ વધુ ઝીણવટભરી શહેર કવરેજ.
- `STYLE-GUIDE.md` માંનું એક્સેસિબિલિટી ઓડિટ રંગ કોન્ટ્રાસ્ટથી આગળ સંપૂર્ણ કીબોર્ડ/સ્ક્રીન-રીડર પાસ સુધી વિસ્તારવું.

---

## 👋 લેખક વિશે

આ રિપોઝિટરી પ્રોજેક્ટનું ઓવરવ્યૂ છે, સાઇટનો સોર્સ નહીં. WordPress કોડબેઝ હાલ પૂરતું બંધ છે. જોકે, [API યાદી](API/) અને `scripts/` ફોલ્ડર PR માટે ખુલ્લા છે - ખૂટતી API, સુધારા, ફેચના વધુ ઉદાહરણો, બધું આવકાર્ય છે.

જો તમે ઉપરની કોઈપણ સમસ્યાનું કોઈ સ્વરૂપ ઉકેલ્યું હોય (સ્ટેલ-કેશ ફોલબેક વ્યૂહરચના, પ્લગિન-પર-સોર્સ આર્કિટેક્ચર, CVD-સેફ કલર સિસ્ટમ, ક્રોસ-લેંગ્વેજ હેશ પેરિટી), અથવા તમે અત્યારે એ જ દીવાલ સામે લડી રહ્યા છો, તો એક [ડિસ્કશન](https://github.com/padmarajnidagundi/indiarealtime-com/issues) ખોલો. મારે ખરેખર નોંધો સરખાવવી છે.

**યોગદાનનું સ્વાગત છે:** નવા ડેટા સ્રોતોને પ્લગિન તરીકે કેવી રીતે ઉમેરવા તે માટે [CONTRIBUTING.md](CONTRIBUTING.md) જુઓ, અથવા મદદના અન્ય રસ્તાઓ માટે [CONTRIBUTORS_GUIDE.md](CONTRIBUTORS_GUIDE.md) જુઓ.

જો તમારી પાસે પ્રશ્નો કે વિચારો હોય, તો [GitHub Issues](https://github.com/padmarajnidagundi/indiarealtime-com/issues) અથવા ઇમેઇલ દ્વારા સંપર્ક કરો.

<!-- TODO: contact / social links -->
