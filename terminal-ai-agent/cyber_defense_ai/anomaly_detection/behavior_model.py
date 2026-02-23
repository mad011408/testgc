"""
Behavior Model - Models normal vs anomalous behavior.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class BehaviorBaseline:
    entity: str
    metrics: Dict[str, float]
    sample_count: int


@dataclass
class BehaviorDeviation:
    entity: str
    metric: str
    expected: float
    actual: float
    deviation_score: float
    severity: str


class BehaviorModel:
    """Models normal behavior for anomaly detection."""

    def __init__(self, threshold: float = 3.0):
        self.threshold = threshold
        self._baselines: Dict[str, BehaviorBaseline] = {}

    def add_baseline(self, baseline: BehaviorBaseline) -> None:
        self._baselines[baseline.entity] = baseline

    def check(self, entity: str, metrics: Dict[str, float]) -> List[BehaviorDeviation]:
        """Check metrics against baseline for deviations."""
        deviations = []
        baseline = self._baselines.get(entity)
        if not baseline:
            return deviations
        for metric, value in metrics.items():
            expected = baseline.metrics.get(metric)
            if expected is None:
                continue
            std = baseline.metrics.get(f"{metric}_std", 1.0) or 1.0
            diff = abs(value - expected) / std if std else abs(value - expected)
            if diff > self.threshold:
                severity = "critical" if diff > 5 else "high" if diff > 4 else "medium"
                deviations.append(BehaviorDeviation(
                    entity=entity, metric=metric,
                    expected=expected, actual=value,
                    deviation_score=diff, severity=severity,
                ))
        return deviations
