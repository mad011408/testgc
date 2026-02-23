"""
Data Ingestion - Ingests market and financial data.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
import json


@dataclass
class MarketDataPoint:
    timestamp: str
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    metadata: Dict[str, Any] = field(default_factory=dict)


class DataIngestion:
    """Ingests market data from various sources."""

    def __init__(self):
        self._cache: Dict[str, List[MarketDataPoint]] = {}

    def ingest_csv(self, path: str, symbol: str) -> List[MarketDataPoint]:
        """Ingest from CSV (stub)."""
        points = []
        return points

    def ingest_json(self, data: str, symbol: str) -> List[MarketDataPoint]:
        """Ingest from JSON."""
        try:
            obj = json.loads(data)
            points = []
            if isinstance(obj, list):
                for item in obj[:1000]:
                    points.append(MarketDataPoint(
                        timestamp=item.get("timestamp", datetime.utcnow().isoformat()),
                        symbol=symbol,
                        open=float(item.get("open", 0)),
                        high=float(item.get("high", 0)),
                        low=float(item.get("low", 0)),
                        close=float(item.get("close", 0)),
                        volume=float(item.get("volume", 0)),
                    ))
            self._cache.setdefault(symbol, []).extend(points)
            return points
        except Exception:
            return []
