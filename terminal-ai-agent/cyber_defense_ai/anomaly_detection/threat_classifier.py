"""
Threat Classifier - Classifies threats by type and severity.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional


class ThreatType(str, Enum):
    MALWARE = "malware"
    PHISHING = "phishing"
    DDoS = "ddos"
    BRUTE_FORCE = "brute_force"
    DATA_EXFIL = "data_exfil"
    LATERAL_MOVEMENT = "lateral_movement"
    UNKNOWN = "unknown"


@dataclass
class ThreatClassification:
    type: ThreatType
    severity: str
    confidence: float
    indicators: List[str]
    recommended_action: str


class ThreatClassifier:
    """Classifies threats based on indicators."""

    def __init__(self):
        self._indicators: Dict[str, ThreatType] = {}

    def classify(
        self,
        indicators: List[str],
        context: Optional[Dict[str, Any]] = None,
    ) -> ThreatClassification:
        """Classify threat from indicators (stub)."""
        threat_type = ThreatType.UNKNOWN
        severity = "medium"
        confidence = 0.5
        if any("ddos" in i.lower() for i in indicators):
            threat_type = ThreatType.DDoS
            severity = "high"
            confidence = 0.8
        elif any("brute" in i.lower() or "ssh" in i.lower() for i in indicators):
            threat_type = ThreatType.BRUTE_FORCE
            severity = "medium"
            confidence = 0.7
        return ThreatClassification(
            type=threat_type,
            severity=severity,
            confidence=confidence,
            indicators=indicators,
            recommended_action="Investigate and isolate",
        )
