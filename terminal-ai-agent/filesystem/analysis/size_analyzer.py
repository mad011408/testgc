"""
Size Analyzer - Size analysis.
"""

from pathlib import Path
from typing import Any, Dict, Optional


class SizeAnalyzer:
    """File/directory size analysis."""

    def analyze(self, path: str) -> Dict[str, Any]:
        """Analyze size (stub)."""
        p = Path(path)
        if p.is_file():
            return {"size": p.stat().st_size, "type": "file"}
        total = sum(f.stat().st_size for f in p.rglob("*") if f.is_file())
        return {"size": total, "type": "dir", "file_count": sum(1 for _ in p.rglob("*") if _.is_file())}
