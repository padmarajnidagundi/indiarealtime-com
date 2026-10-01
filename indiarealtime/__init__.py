"""
IndiaRealTime Python SDK

Live India data aggregator - access mandi prices, fuel rates, AQI, weather, cricket scores, and more.

Example:
    >>> from indiarealtime import IndiaRealTime
    >>> irt = IndiaRealTime()
    >>> prices = irt.mandi_prices(commodity="wheat", state="Punjab")
    >>> print(prices)

"""

from .client import IndiaRealTime
from .models import (
    MandiPrice,
    FuelPrice,
    AirQuality,
    Weather,
    Earthquake,
    CricketScore,
    CurrencyRate,
    GoldPrice,
)

__version__ = "0.1.0"
__author__ = "Padmaraj Nidagundi"
__license__ = "MIT"

__all__ = [
    "IndiaRealTime",
    "MandiPrice",
    "FuelPrice",
    "AirQuality",
    "Weather",
    "Earthquake",
    "CricketScore",
    "CurrencyRate",
    "GoldPrice",
]
