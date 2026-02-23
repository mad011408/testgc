"""
Dir List - Directory listing.
"""

from pathlib import Path
from typing import Any, List, Optional


class DirList:
    """Directory listing operations."""

    def list(self, path: str, pattern: str = "*") -> List[str]:
        """List directory contents (stub)."""
        try:
            return [p.name for p in Path(path).glob(pattern)]
        except Exception:
            return []
