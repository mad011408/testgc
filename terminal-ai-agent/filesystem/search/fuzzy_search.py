"""
Fuzzy Search - Fuzzy search.
"""

from pathlib import Path
from typing import Any, List, Optional


class FuzzySearch:
    """Fuzzy filename search."""

    def search(self, path: str, query: str) -> List[str]:
        """Fuzzy search (stub)."""
        return [str(p) for p in Path(path).rglob(f"*{query}*")]
