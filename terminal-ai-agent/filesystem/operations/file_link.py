"""
File Link - File linking (symlink, hardlink).
"""

from pathlib import Path
from typing import Any, Optional


class FileLink:
    """File linking operations."""

    def symlink(self, src: str, dst: str) -> bool:
        """Create symlink (stub)."""
        try:
            Path(dst).symlink_to(src)
            return True
        except Exception:
            return False

    def hardlink(self, src: str, dst: str) -> bool:
        """Create hardlink (stub)."""
        try:
            Path(dst).hardlink_to(src)
            return True
        except Exception:
            return False
