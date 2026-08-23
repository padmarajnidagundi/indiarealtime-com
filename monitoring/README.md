# Status Page Configuration

This directory contains the monitoring dashboard configuration for IndiaRealTime.

## Quick Start

```bash
npm install
npm start
```

Visit http://localhost:3000/status

## Features

- **Real-time Status**: See which APIs are up/down right now
- **Historical Uptime**: 30-day uptime graphs for each service
- **Response Times**: Monitor API latency trends
- **Incident Timeline**: Track outages and when they were resolved
- **Service Dependencies**: See which services depend on each other
- **Alerts**: Get notified of service degradation via email/Slack

## Configuration

### Environment Variables

```bash
# .env
WORDPRESS_API=https://indiarealtime.com
MONITORING_INTERVAL=5m
ALERT_THRESHOLD_UPTIME=95
ALERT_THRESHOLD_RESPONSE=2000
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
```

### Service Definitions

Edit `services.json`:

```json
{
  "services": [
    {
      "id": "mandi-prices",
      "name": "Mandi Prices",
      "endpoint": "https://api.indiarealtime.com/v1/mandi/prices",
      "method": "GET",
      "timeout": 10000,
      "alert_email": "admin@indiarealtime.com"
    }
  ]
}
```

## Dashboard Pages

### `/status`
Current status of all services. Green/Yellow/Red indicators.

### `/status/uptime`
30-day uptime percentage for each service.

### `/status/response-times`
API response time trends over 7 days.

### `/status/incidents`
Historical list of outages with root cause and resolution time.

### `/api/health`
Returns JSON with current health status for integration with other tools.

## Integration with GitHub

Automatically update repo status in GitHub by pushing status checks:

```bash
npm run deploy-status
```

This updates the GitHub status badge in your README.

## Alerts

### Slack
Sends real-time alerts to Slack channel when service degrades:

```
❌ Mandi Prices API is down
Response: 503 Service Unavailable
Started: 2026-08-23 14:32 IST
```

### Email
Configure email alerts for:
- Service going down
- Service recovering
- Response time spike
- Database issues

### PagerDuty / Opsgenie
Integrate with PagerDuty for critical alerts:

```bash
npm run configure-pagerduty
```

## Custom Checks

Add custom health checks in `checks/`:

```javascript
// checks/custom-mandi-price.js
module.exports = {
  id: 'mandi-price-logic',
  name: 'Mandi Price Data Validation',
  async run() {
    const prices = await fetch('/v1/mandi/prices');
    if (!prices.length) throw new Error('No prices returned');
    if (prices[0].price < 100) throw new Error('Price sanity check failed');
  }
};
```

## Monitoring Individual Plugins

Each WordPress plugin registers with the health check:

```bash
GET /v1/sources/status?source=mandi-prices
```

Returns:
```json
{
  "source": "mandi-prices",
  "status": "operational",
  "last_fetch": "2026-08-23T14:35:00Z",
  "data_freshness_hours": 0.5,
  "error_rate": 0,
  "average_response_ms": 450
}
```

## Testing

```bash
npm test
npm run test:e2e
```

## Deployment

### Docker
```bash
docker build -t indiarealtime-status .
docker run -p 3000:3000 indiarealtime-status
```

### Vercel
```bash
vercel deploy
```

### Self-hosted
```bash
npm run build
npm run start
```

---

**Questions?** See [Challenges > Monitoring](../notes/)
