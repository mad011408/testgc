"""
Dir Create - Directory creation.
"""

from pathlib import Path
from typing import Any, Optional


class DirCreate:
    """Directory creation operations."""

    def create(self, path: str, parents: bool = True) -> bool:
        """Create directory (stub)."""
        try:
            Path(path).mkdir(parents=parents, exist_ok=True)
            return True
        except Exception:
            return False
