"""File analyzer module."""
from pathlib import Path
from typing import Any, Dict


class FileAnalyzer:
    def analyze(self, path: str) -> Dict[str, Any]:
        p = Path(path)
        return {"exists": p.exists(), "size": p.stat().st_size if p.exists() else 0}
