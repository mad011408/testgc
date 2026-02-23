"""
Dir Size - Directory size calculation.
"""

from pathlib import Path
from typing import Any, Optional


class DirSize:
    """Directory size operations."""

    def size(self, path: str, follow_symlinks: bool = False) -> int:
        """Calculate directory size (stub)."""
        total = 0
        try:
            for p in Path(path).rglob("*"):
                if p.is_file():
                    total += p.stat().st_size
        except Exception:
            pass
        return total
