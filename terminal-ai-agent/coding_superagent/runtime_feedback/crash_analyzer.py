"""
Crash Analyzer - Analyzes stack traces and crashes.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CrashReport:
    exception_type: str
    message: str
    stack_frames: List[Dict[str, Any]] = field(default_factory=list)
    root_cause: Optional[str] = None
    suggestions: List[str] = field(default_factory=list)


class CrashAnalyzer:
    """Analyzes crash reports and stack traces."""

    def parse_stack(self, traceback_str: str) -> CrashReport:
        """Parse stack trace into CrashReport (stub)."""
        lines = traceback_str.strip().split("\n")
        exc_type = "Exception"
        message = "Unknown"
        for line in reversed(lines):
            if line.startswith(("  ", "\t")):
                continue
            if ":" in line:
                parts = line.split(":", 1)
                exc_type = parts[0].strip()
                message = parts[1].strip() if len(parts) > 1 else ""
                break
        return CrashReport(
            exception_type=exc_type,
            message=message,
            suggestions=["Check input types", "Add error handling"],
        )
