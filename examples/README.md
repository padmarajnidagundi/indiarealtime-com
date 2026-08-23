# Examples

Complete, runnable examples using IndiaRealTime SDK and APIs.

## Python Examples

### 1. CLI Tool
```bash
pip install indiarealtime
indiarealtime mandi --commodity wheat --state Punjab
indiarealtime aqi --city Delhi
indiarealtime fuel --type petrol --state Maharashtra
```

See [indiarealtime/cli.py](../indiarealtime/cli.py) for full CLI implementation.

### 2. FastAPI Server
A complete REST API server that proxies IndiaRealTime data:

```bash
pip install fastapi uvicorn indiarealtime
python examples/fastapi_server.py
```

Visit http://localhost:8000/docs for interactive API documentation.

Features:
- ✅ Real-time mandi prices
- ✅ Fuel prices by state/city
- ✅ Air quality data
- ✅ Weather alerts
- ✅ Cricket scores
- ✅ Currency rates
- ✅ CORS enabled for frontend use

### 3. Telegram Bot
Price alerts when commodities reach your target price:

```bash
pip install python-telegram-bot indiarealtime
python examples/telegram_bot.py
```

Features:
- ✅ Set price alerts
- ✅ Query AQI by city
- ✅ Hourly price checks
- ✅ Instant notifications

**Setup:**
1. Create bot on Telegram (@BotFather)
2. Add token to `telegram_bot.py`
3. Run and use `/alert` command

### 4. Google Sheets Integration
Automatically update Google Sheets with live data:

```bash
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client indiarealtime
python examples/google_sheets_integration.py
```

Features:
- ✅ Auto-update mandi prices
- ✅ Track fuel rates
- ✅ Monitor AQI in real-time
- ✅ Refresh hourly/daily

**Setup:**
1. Create Google Cloud project
2. Enable Sheets API
3. Download credentials JSON
4. Run script (auto-opens Google OAuth)

## JavaScript/React Examples

### 5. Next.js Dashboard
A full-stack Next.js application with live mandi prices:

```bash
cd examples/nextjs_mandi_dashboard
npm install
npm run dev
```

Visit http://localhost:3000

Features:
- ✅ Real-time price updates
- ✅ Commodity selector
- ✅ Responsive design
- ✅ TailwindCSS styling

Source: [examples/nextjs_mandi_dashboard.tsx](nextjs_mandi_dashboard.tsx)

### 6. React Component (Hook)
```javascript
import { useState, useEffect } from 'react';

function MandiPrices({ commodity }) {
  const [prices, setPrices] = useState([]);
  
  useEffect(() => {
    fetch(`/api/v1/mandi/prices?commodity=${commodity}`)
      .then(r => r.json())
      .then(data => setPrices(data.results));
  }, [commodity]);
  
  return (
    <table>
      <tbody>
        {prices.map(p => (
          <tr key={p.market}>
            <td>{p.market}</td>
            <td>₹{p.price}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

## Spreadsheets & Automation

### 7. Google Sheets Scripts
Add this to Google Sheets → Extensions → Apps Script:

```javascript
function updateMandiPrices() {
  const url = 'http://localhost:5000/api/v1/mandi/prices?limit=50';
  const response = UrlFetchApp.fetch(url);
  const data = JSON.parse(response.getContentText());
  
  const sheet = SpreadsheetApp.getActiveSheet();
  const range = sheet.getRange(1, 1, data.results.length + 1, 5);
  
  const values = [['Commodity', 'Market', 'State', 'City', 'Price']];
  data.results.forEach(p => {
    values.push([p.commodity, p.market, p.state, p.city, p.price]);
  });
  
  range.setValues(values);
}
```

Then set up a time-based trigger to run every hour.

## API Clients

### 8. cURL Examples
```bash
# Get mandi prices
curl https://api.indiarealtime.com/v1/mandi/prices?commodity=wheat

# Get fuel prices
curl https://api.indiarealtime.com/v1/fuel/prices?state=Maharashtra

# Get AQI
curl https://api.indiarealtime.com/v1/environment/aqi?city=Delhi

# Get currency rates
curl https://api.indiarealtime.com/v1/finance/currency?base=INR&symbols=USD,EUR
```

### 9. Postman Collection
Import [postman-collection.json](postman-collection.json) into Postman for pre-built requests.

## Real-World Use Cases

### Case 1: Farmer Dashboard
Tracks mandi prices for multiple commodities across states, sends SMS alerts when prices spike.

**Stack:** Python backend + React frontend + Telegram API

### Case 2: Weather Alert System
Monitors weather alerts and AQI, triggers automation (turn off AC during high AQI, etc.)

**Stack:** Node.js + IFTTT + Smart home API

### Case 3: Financial Dashboard
Tracks currency rates, gold prices, and mutual fund NAVs in real-time.

**Stack:** Next.js + Plotly.js + Recharts

### Case 4: Journalism/Research
Pulls historical commodity and fuel prices for trend analysis and reports.

**Stack:** Python + Jupyter + Pandas

---

## Testing Examples

All examples include tests. Run them with:

```bash
# Python examples
pytest examples/ -v

# React examples
npm test --prefix examples/nextjs_mandi_dashboard
```

## Contributing New Examples

Have a cool example? Send a PR! Requirements:
- Clear README
- Working code
- <100 lines preferred
- Dependency list
- Screenshot/demo

---

**Questions?** Open an issue or start a [GitHub Discussion](https://github.com/padmarajnidagundi/indiarealtime-com/discussions)
