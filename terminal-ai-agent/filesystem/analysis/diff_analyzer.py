"""
Diff Analyzer - Diff analysis.
"""

from pathlib import Path
from typing import Any, List, Optional


class DiffAnalyzer:
    """File diff analysis."""

    def diff(self, path_a: str, path_b: str) -> List[str]:
        """Get diff (stub)."""
        try:
            a = Path(path_a).read_text()
            b = Path(path_b).read_text()
            return [line for line in a.splitlines() if line not in b.splitlines()]
        except Exception:
            return []
