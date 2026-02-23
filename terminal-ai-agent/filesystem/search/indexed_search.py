"""
Indexed Search - Indexed search.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional


class IndexedSearch:
    """Indexed file search."""

    def __init__(self):
        self._index: Dict[str, List[str]] = {}

    def index(self, path: str) -> None:
        """Build index (stub)."""
        pass

    def search(self, query: str) -> List[str]:
        """Search index (stub)."""
        return self._index.get(query, [])
