"""
Glob Handler - Glob patterns.
"""

from pathlib import Path
from typing import Any, List, Optional


class GlobHandler:
    """Glob pattern operations."""

    def glob(self, path: str, pattern: str) -> List[str]:
        """Glob search (stub)."""
        return [str(p) for p in Path(path).rglob(pattern)]
