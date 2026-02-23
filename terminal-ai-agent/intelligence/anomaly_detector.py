"""
Anomaly Detector - Detects anomalies in generic data streams.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Anomaly:
    index: int
    value: Any
    expected: float
    deviation: float
    severity: str


class AnomalyDetector:
    """Detects anomalies using statistical methods."""

    def __init__(self, threshold_std: float = 3.0):
        self.threshold_std = threshold_std

    def detect(self, values: List[float]) -> List[Anomaly]:
        """Detect anomalies in value stream (stub)."""
        if not values:
            return []
        mean = sum(values) / len(values)
        std = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5 or 1.0
        anomalies = []
        for i, v in enumerate(values):
            if std > 0 and abs(v - mean) > self.threshold_std * std:
                anomalies.append(Anomaly(i, v, mean, abs(v - mean) / std, "high"))
        return anomalies
