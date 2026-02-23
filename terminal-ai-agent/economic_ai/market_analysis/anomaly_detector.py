"""
Anomaly Detector - Detects anomalies in market data.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AnomalyResult:
    timestamp: str
    symbol: str
    value: float
    expected: float
    deviation: float
    severity: str  # low, medium, high, critical


class AnomalyDetector:
    """Detects anomalies in price/volume data."""

    def __init__(self, threshold_std: float = 3.0):
        self.threshold_std = threshold_std

    def detect(self, values: List[float], timestamps: Optional[List[str]] = None) -> List[AnomalyResult]:
        """Detect anomalies using std deviation (stub)."""
        if not values:
            return []
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values) if values else 0
        std = variance ** 0.5 if variance else 0
        anomalies = []
        ts = timestamps or [""] * len(values)
        for i, (v, t) in enumerate(zip(values, ts)):
            if std > 0 and abs(v - mean) > self.threshold_std * std:
                severity = "high" if abs(v - mean) > 4 * std else "medium"
                anomalies.append(AnomalyResult(
                    timestamp=t, symbol="", value=v, expected=mean,
                    deviation=abs(v - mean) / std if std else 0, severity=severity,
                ))
        return anomalies
