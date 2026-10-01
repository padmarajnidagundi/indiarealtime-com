"""
Data models for IndiaRealTime API responses
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class MandiPrice:
    """Mandi commodity price data"""

    commodity: str
    market: str
    state: str
    city: str
    price: float  # Per unit (usually per quintal)
    currency: str = "INR"
    unit: str = "Quintal"
    updated_at: Optional[str] = None
    source: str = "Agmarknet"

    def __str__(self) -> str:
        return f"{self.commodity} @ {self.market}: ₹{self.price}/{self.unit}"


@dataclass
class FuelPrice:
    """Fuel price by location"""

    fuel_type: str  # petrol, diesel, lpg
    state: str
    city: str
    price: float  # Per liter or per kg
    currency: str = "INR"
    unit: str = "Liter"
    updated_at: Optional[str] = None
    source: str = "IOCL/BPCL/HPCL"

    def __str__(self) -> str:
        return f"{self.fuel_type.upper()} in {self.city}: ₹{self.price}/{self.unit}"


@dataclass
class AirQuality:
    """Air quality index data"""

    city: str
    state: str
    aqi: int  # 0-500
    aqi_category: str  # Good, Moderate, Poor, etc.
    pm25: float  # µg/m³
    pm10: float  # µg/m³
    no2: Optional[float] = None
    so2: Optional[float] = None
    co: Optional[float] = None
    o3: Optional[float] = None
    updated_at: Optional[str] = None
    source: str = "CPCB"

    def __str__(self) -> str:
        return f"{self.city}: AQI {self.aqi} ({self.aqi_category})"


@dataclass
class Weather:
    """Weather alert data"""

    state: str
    alert_type: str  # Warning, Watch, Advisory
    description: str
    issued_at: Optional[str] = None
    valid_until: Optional[str] = None
    severity: str = "Moderate"  # Low, Moderate, High, Severe
    source: str = "IMD"

    def __str__(self) -> str:
        return f"{self.alert_type}: {self.description}"


@dataclass
class Earthquake:
    """Earthquake data"""

    magnitude: float
    latitude: float
    longitude: float
    depth: float  # km
    location: str
    state: str
    timestamp: str
    felt_reports: Optional[int] = None
    source: str = "USGS"

    def __str__(self) -> str:
        return f"M{self.magnitude} {self.location} at {self.depth}km"


@dataclass
class CricketScore:
    """Live cricket score"""

    match_id: str
    teams: str  # e.g., "India vs Australia"
    format: str  # Test, ODI, T20
    status: str  # Live, Upcoming, Completed
    score_team1: str  # e.g., "150/3"
    score_team2: Optional[str] = None
    current_over: Optional[str] = None
    updated_at: Optional[str] = None
    source: str = "CricAPI"

    def __str__(self) -> str:
        return f"{self.teams} - {self.score_team1}"


@dataclass
class CurrencyRate:
    """Currency exchange rate"""

    base: str  # e.g., "INR"
    target: str  # e.g., "USD"
    rate: float
    updated_at: Optional[str] = None
    source: str = "RBI"

    def __str__(self) -> str:
        return f"1 {self.base} = {self.rate:.2f} {self.target}"


@dataclass
class GoldPrice:
    """Gold/precious metal price"""

    metal: str  # gold, silver, etc.
    purity: str  # 24K, 22K, etc.
    price_per_gram: float
    currency: str = "INR"
    city: Optional[str] = None
    updated_at: Optional[str] = None
    source: str = "IBJA"

    def __str__(self) -> str:
        return f"{self.metal.upper()} ({self.purity}): ₹{self.price_per_gram}/g"


@dataclass
class ApiHealth:
    """API health status"""

    service: str
    status: str  # operational, degraded, down
    last_check: str
    uptime_percentage: float
    response_time_ms: int

    def __str__(self) -> str:
        return f"{self.service}: {self.status} ({self.uptime_percentage:.1f}% uptime)"
