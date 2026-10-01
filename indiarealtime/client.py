"""
Main IndiaRealTime API client
"""

import requests
from typing import Optional, List, Dict, Any
from .models import (
    MandiPrice,
    FuelPrice,
    AirQuality,
    Weather,
    CricketScore,
)


class IndiaRealTime:
    """
    Python client for IndiaRealTime API

    Provides access to live India data: mandi prices, fuel rates, AQI,
    weather, earthquakes, cricket scores, and more.

    Args:
        api_key (str, optional): API key for higher rate limits. Defaults to None.
        base_url (str, optional): Base URL for API. Defaults to https://api.indiarealtime.com
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Example:
        >>> irt = IndiaRealTime()
        >>> prices = irt.mandi_prices(commodity="wheat")
        >>> aqi = irt.air_quality(city="Delhi")
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.indiarealtime.com",
        timeout: int = 10,
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"X-API-Key": api_key})

    def _request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict:
        """Make HTTP request to API"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API request failed: {str(e)}")

    # Mandi / Agricultural Prices

    def mandi_prices(
        self,
        commodity: Optional[str] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        limit: int = 50,
    ) -> List[MandiPrice]:
        """
        Get current mandi prices for agricultural commodities

        Args:
            commodity: Commodity name (e.g., 'wheat', 'rice', 'onion')
            state: State name
            city: City/market name
            limit: Max results to return

        Returns:
            List of MandiPrice objects
        """
        params = {
            "commodity": commodity,
            "state": state,
            "city": city,
            "limit": limit,
        }
        params = {k: v for k, v in params.items() if v is not None}

        data = self._request("v1/mandi/prices", params)
        return [MandiPrice(**item) for item in data.get("results", [])]

    def mandi_commodities(self, state: Optional[str] = None) -> List[str]:
        """Get list of commodities tracked for a state"""
        params = {"state": state} if state else {}
        data = self._request("v1/mandi/commodities", params)
        return data.get("commodities", [])

    # Fuel Prices

    def fuel_prices(
        self,
        fuel_type: str = "petrol",
        state: Optional[str] = None,
        city: Optional[str] = None,
    ) -> List[FuelPrice]:
        """
        Get current fuel prices by state/city

        Args:
            fuel_type: 'petrol', 'diesel', or 'lpg'
            state: State name
            city: City name

        Returns:
            List of FuelPrice objects
        """
        params = {
            "type": fuel_type,
            "state": state,
            "city": city,
        }
        params = {k: v for k, v in params.items() if v is not None}

        data = self._request("v1/fuel/prices", params)
        return [FuelPrice(**item) for item in data.get("results", [])]

    # Air Quality

    def air_quality(
        self,
        city: Optional[str] = None,
        state: Optional[str] = None,
    ) -> List[AirQuality]:
        """
        Get current air quality data (AQI)

        Args:
            city: City name
            state: State name

        Returns:
            List of AirQuality objects
        """
        params = {
            "city": city,
            "state": state,
        }
        params = {k: v for k, v in params.items() if v is not None}

        data = self._request("v1/environment/aqi", params)
        return [AirQuality(**item) for item in data.get("results", [])]

    # Weather

    def weather_alerts(self, state: Optional[str] = None) -> List[Weather]:
        """
        Get current weather alerts

        Args:
            state: State name

        Returns:
            List of Weather objects
        """
        params = {"state": state} if state else {}
        data = self._request("v1/weather/alerts", params)
        return [Weather(**item) for item in data.get("results", [])]

    # Cricket

    def cricket_scores(self, limit: int = 10) -> List[CricketScore]:
        """
        Get live cricket scores

        Args:
            limit: Max results to return

        Returns:
            List of CricketScore objects
        """
        data = self._request("v1/sport/cricket/scores", {"limit": limit})
        return [CricketScore(**item) for item in data.get("results", [])]

    # Currency

    def currency_rates(
        self, base: str = "INR", symbols: Optional[List[str]] = None
    ) -> Dict[str, float]:
        """
        Get currency exchange rates

        Args:
            base: Base currency (default: INR)
            symbols: List of target currencies

        Returns:
            Dict mapping currency code to rate
        """
        params = {"base": base}
        if symbols:
            params["symbols"] = ",".join(symbols)

        data = self._request("v1/finance/currency", params)
        return data.get("rates", {})

    # Health Check

    def health(self) -> Dict[str, Any]:
        """
        Check API health and uptime

        Returns:
            Dict with status, last_updated, and uptime info
        """
        return self._request("v1/health")

    def source_status(self, source: Optional[str] = None) -> Dict[str, Any]:
        """
        Check status of individual data sources

        Args:
            source: Specific source to check

        Returns:
            Dict with source statuses and timestamps
        """
        params = {"source": source} if source else {}
        return self._request("v1/sources/status", params)
