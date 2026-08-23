#!/usr/bin/env python3
"""
FastAPI example server for IndiaRealTime

Usage:
    pip install fastapi uvicorn indiarealtime
    python api/example_fastapi.py
    
Then visit http://localhost:8000/docs for interactive API docs
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from indiarealtime import IndiaRealTime
from typing import Optional, List

app = FastAPI(
    title="IndiaRealTime API Proxy",
    description="FastAPI wrapper around IndiaRealTime SDK",
    version="1.0.0",
)

# Enable CORS for public use
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

irt = IndiaRealTime()


@app.get("/")
async def root():
    """API overview"""
    return {
        "name": "IndiaRealTime API Proxy",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
async def health():
    """Check API health"""
    try:
        status = irt.health()
        return {"status": "healthy", "details": status}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))


@app.get("/mandi/prices")
async def get_mandi_prices(
    commodity: Optional[str] = Query(None, description="Commodity name"),
    state: Optional[str] = Query(None, description="State name"),
    city: Optional[str] = Query(None, description="City/market name"),
    limit: int = Query(50, ge=1, le=500, description="Max results"),
):
    """Get mandi prices for agricultural commodities"""
    try:
        prices = irt.mandi_prices(
            commodity=commodity,
            state=state,
            city=city,
            limit=limit,
        )
        return {
            "count": len(prices),
            "results": [vars(p) for p in prices],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/fuel/prices")
async def get_fuel_prices(
    fuel_type: str = Query("petrol", regex="^(petrol|diesel|lpg)$"),
    state: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
):
    """Get fuel prices by location"""
    try:
        prices = irt.fuel_prices(fuel_type=fuel_type, state=state, city=city)
        return {
            "fuel_type": fuel_type,
            "count": len(prices),
            "results": [vars(p) for p in prices],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/environment/aqi")
async def get_aqi(
    city: Optional[str] = Query(None),
    state: Optional[str] = Query(None),
):
    """Get air quality index (AQI) data"""
    try:
        results = irt.air_quality(city=city, state=state)
        return {
            "count": len(results),
            "results": [vars(r) for r in results],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/weather/alerts")
async def get_weather_alerts(
    state: Optional[str] = Query(None),
):
    """Get weather alerts"""
    try:
        alerts = irt.weather_alerts(state=state)
        return {
            "count": len(alerts),
            "results": [vars(a) for a in alerts],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/sport/cricket/scores")
async def get_cricket_scores(
    limit: int = Query(10, ge=1, le=100),
):
    """Get live cricket scores"""
    try:
        scores = irt.cricket_scores(limit=limit)
        return {
            "count": len(scores),
            "results": [vars(s) for s in scores],
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/finance/currency")
async def get_currency_rates(
    base: str = Query("INR", min_length=3, max_length=3),
    symbols: Optional[str] = Query(None, description="Comma-separated currency codes"),
):
    """Get currency exchange rates"""
    try:
        symbol_list = symbols.split(',') if symbols else None
        rates = irt.currency_rates(base=base, symbols=symbol_list)
        return {
            "base": base,
            "rates": rates,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
