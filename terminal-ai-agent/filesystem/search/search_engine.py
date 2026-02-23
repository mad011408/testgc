"""
Search Engine - Search engine core.
"""

from pathlib import Path
from typing import Any, List, Optional


class SearchEngine:
    """File search engine."""

    def __init__(self, root: Optional[str] = None):
        self.root = Path(root) if root else Path.cwd()

    def search(self, query: str, path: Optional[str] = None) -> List[str]:
        """Search files (stub)."""
        return []
