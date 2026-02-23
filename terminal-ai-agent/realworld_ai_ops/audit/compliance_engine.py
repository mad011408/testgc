"""
Compliance Engine - Checks and enforces compliance rules.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional


class ComplianceStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    WARN = "warn"
    SKIP = "skip"


@dataclass
class ComplianceCheck:
    id: str
    name: str
    status: ComplianceStatus
    message: str
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ComplianceReport:
    checks: List[ComplianceCheck] = field(default_factory=list)
    passed: int = 0
    failed: int = 0
    warnings: int = 0

    @property
    def compliant(self) -> bool:
        return self.failed == 0


class ComplianceEngine:
    """Runs compliance checks against resources and config."""

    def __init__(self):
        self._checks: Dict[str, Callable[..., ComplianceCheck]] = {}

    def register(self, check_id: str, check_fn: Callable[..., ComplianceCheck]) -> "ComplianceEngine":
        """Register compliance check."""
        self._checks[check_id] = check_fn
        return self

    def run_checks(self, context: Optional[Dict[str, Any]] = None) -> ComplianceReport:
        """Run all registered checks."""
        ctx = context or {}
        report = ComplianceReport()
        for check_id, fn in self._checks.items():
            try:
                result = fn(ctx)
                report.checks.append(result)
                if result.status == ComplianceStatus.PASS:
                    report.passed += 1
                elif result.status == ComplianceStatus.FAIL:
                    report.failed += 1
                elif result.status == ComplianceStatus.WARN:
                    report.warnings += 1
            except Exception as e:
                report.checks.append(ComplianceCheck(
                    id=check_id, name=check_id, status=ComplianceStatus.FAIL,
                    message=str(e), details={"error": type(e).__name__}
                ))
                report.failed += 1
        return report
