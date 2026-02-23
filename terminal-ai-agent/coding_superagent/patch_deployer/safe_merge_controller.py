"""
Safe Merge Controller - Controls safe merge workflows.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class MergeCheck:
    name: str
    passed: bool
    message: str


@dataclass
class MergeResult:
    allowed: bool
    checks: List[MergeCheck]
    message: str


class SafeMergeController:
    """Ensures safe merge with pre-merge checks."""

    def __init__(self, required_checks: Optional[List[str]] = None):
        self.required_checks = required_checks or ["test", "lint"]

    def can_merge(self, branch: str, checks: Dict[str, bool]) -> MergeResult:
        """Determine if merge is safe."""
        results = []
        for name, passed in checks.items():
            results.append(MergeCheck(name=name, passed=passed, message="OK" if passed else "Failed"))
        allowed = all(c.passed for c in results) and all(
            name in checks and checks[name] for name in self.required_checks
        )
        return MergeResult(
            allowed=allowed,
            checks=results,
            message="Merge allowed" if allowed else "Merge blocked",
        )
