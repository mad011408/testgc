"""
Log Intelligence - Extracts insights from logs.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import re


@dataclass
class LogInsight:
    type: str
    message: str
    severity: str
    count: int
    sample: str


class LogIntelligence:
    """Analyzes logs for patterns and anomalies."""

    def analyze(self, logs: str) -> List[LogInsight]:
        """Analyze log text for insights."""
        insights = []
        error_count = len(re.findall(r"error|exception|failed", logs, re.I))
        if error_count:
            insights.append(LogInsight(
                type="error",
                message=f"{error_count} error-like lines",
                severity="high",
                count=error_count,
                sample=logs[:200],
            ))
        return insights
