"""
Risk Analyzer - Analyzes deployment and change risk.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class RiskFactor:
    name: str
    level: RiskLevel
    score: float
    description: str
    mitigation: Optional[str] = None


@dataclass
class RiskReport:
    overall_level: RiskLevel
    overall_score: float
    factors: List[RiskFactor] = field(default_factory=list)
    recommendation: str = ""


class RiskAnalyzer:
    """Analyzes risk for deployments and changes."""

    def __init__(self, thresholds: Optional[Dict[str, float]] = None):
        self.thresholds = thresholds or {"critical": 0.9, "high": 0.7, "medium": 0.4}

    def analyze_deployment(
        self,
        change_type: str,
        affected_services: List[str],
        breaking_changes: bool = False,
        has_rollback: bool = True,
    ) -> RiskReport:
        """Analyze deployment risk."""
        factors = []
        scores = []

        if breaking_changes:
            f = RiskFactor("breaking_changes", RiskLevel.HIGH, 0.8, "Breaking changes detected", "Ensure backward compatibility")
            factors.append(f)
            scores.append(f.score)

        if not has_rollback:
            f = RiskFactor("no_rollback", RiskLevel.CRITICAL, 0.95, "No rollback plan", "Add rollback checkpoint")
            factors.append(f)
            scores.append(f.score)

        n_services = len(affected_services)
        if n_services > 10:
            f = RiskFactor("wide_impact", RiskLevel.MEDIUM, 0.6, f"Affects {n_services} services")
            factors.append(f)
            scores.append(f.score)

        avg_score = sum(scores) / len(scores) if scores else 0.2
        if avg_score >= self.thresholds["critical"]:
            level = RiskLevel.CRITICAL
        elif avg_score >= self.thresholds["high"]:
            level = RiskLevel.HIGH
        elif avg_score >= self.thresholds["medium"]:
            level = RiskLevel.MEDIUM
        else:
            level = RiskLevel.LOW

        rec = "Proceed with caution" if level in (RiskLevel.HIGH, RiskLevel.CRITICAL) else "Proceed"
        return RiskReport(overall_level=level, overall_score=avg_score, factors=factors, recommendation=rec)
