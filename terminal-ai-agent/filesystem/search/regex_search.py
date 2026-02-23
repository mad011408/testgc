"""
Regex Search - Regex search.
"""

import re
from pathlib import Path
from typing import Any, List, Optional


class RegexSearch:
    """Regex-based search."""

    def search(self, path: str, pattern: str) -> List[str]:
        """Search with regex (stub)."""
        results = []
        try:
            rx = re.compile(pattern)
            for p in Path(path).rglob("*"):
                if p.is_file():
                    try:
                        if rx.search(p.read_text(errors="ignore")):
                            results.append(str(p))
                    except Exception:
                        pass
        except re.error:
            pass
        return results
