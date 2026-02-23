"""
Regulatory Checker - Checks compliance with financial regulations.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ComplianceCheck:
    rule_id: str
    passed: bool
    message: str
    details: Dict[str, Any]


class RegulatoryChecker:
    """Checks trading and portfolio against regulations."""

    def check_position_limits(self, positions: Dict[str, float], limits: Dict[str, float]) -> List[ComplianceCheck]:
        """Check position limits."""
        results = []
        for asset, qty in positions.items():
            limit = limits.get(asset, float("inf"))
            passed = qty <= limit
            results.append(ComplianceCheck(
                rule_id="position_limit",
                passed=passed,
                message=f"{asset}: {qty} vs limit {limit}" if limit != float("inf") else "OK",
                details={"asset": asset, "position": qty, "limit": limit},
            ))
        return results
