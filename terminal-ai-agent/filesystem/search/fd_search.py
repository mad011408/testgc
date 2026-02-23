"""
FD Search - fd-like search.
"""

from pathlib import Path
from typing import Any, List, Optional


class FdSearch:
    """fd-like fast search."""

    def search(self, path: str, pattern: str, case_sensitive: bool = False) -> List[str]:
        """fd-like search (stub)."""
        results = []
        for p in Path(path).rglob(pattern):
            if p.is_file():
                results.append(str(p))
        return results
