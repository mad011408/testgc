"""
Test Executor - Runs and reports test results.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class TestResult:
    name: str
    status: str  # passed, failed, skipped
    duration_seconds: float
    message: Optional[str] = None
    output: Optional[str] = None


@dataclass
class TestRun:
    total: int
    passed: int
    failed: int
    skipped: int
    duration_seconds: float
    results: List[TestResult] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


class TestExecutor:
    """Executes tests and aggregates results."""

    def __init__(self, test_runner: str = "pytest"):
        self.test_runner = test_runner

    async def run_tests(
        self,
        path: str = ".",
        pattern: str = "test_*.py",
        extra_args: Optional[List[str]] = None,
    ) -> TestRun:
        """Run tests (stub - in production uses subprocess)."""
        # subprocess.run([self.test_runner, path, "-v", f"--tb=short"])
        return TestRun(total=0, passed=0, failed=0, skipped=0, duration_seconds=0.0)

    def parse_output(self, output: str) -> TestRun:
        """Parse test runner output into TestRun."""
        results = []
        total = 0
        passed = 0
        failed = 0
        skipped = 0
        for line in output.splitlines():
            if "passed" in line.lower():
                passed = int(line.split()[0]) if line.split() else 0
                total = passed
            if "failed" in line.lower() and "passed" not in line:
                failed = int(line.split()[0]) if line.split() else 0
                total += failed
        return TestRun(total=total, passed=passed, failed=failed, skipped=skipped, duration_seconds=0, results=results)
