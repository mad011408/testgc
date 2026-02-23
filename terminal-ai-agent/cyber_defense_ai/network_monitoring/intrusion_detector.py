"""
Intrusion Detector - Detects intrusion attempts.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import re


@dataclass
class IntrusionAlert:
    id: str
    severity: str
    src_ip: str
    dst_ip: str
    rule: str
    description: str
    timestamp: str


class IntrusionDetector:
    """Detects intrusion attempts from traffic and logs."""

    def __init__(self):
        self._rules: List[Dict[str, Any]] = []
        self._alert_counter = 0

    def add_rule(self, pattern: str, severity: str, description: str) -> "IntrusionDetector":
        self._rules.append({"pattern": pattern, "severity": severity, "description": description})
        return self

    def analyze(self, log_line: str, src_ip: str = "", dst_ip: str = "") -> List[IntrusionAlert]:
        """Analyze log line for intrusion patterns."""
        alerts = []
        for rule in self._rules:
            if re.search(rule["pattern"], log_line, re.I):
                self._alert_counter += 1
                alerts.append(IntrusionAlert(
                    id=f"int-{self._alert_counter}",
                    severity=rule["severity"],
                    src_ip=src_ip,
                    dst_ip=dst_ip,
                    rule=rule["pattern"],
                    description=rule["description"],
                    timestamp="",
                ))
        return alerts
