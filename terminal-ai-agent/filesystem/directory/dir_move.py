"""
Dir Move - Directory moving.
"""

from pathlib import Path
from typing import Any, Optional
import shutil


class DirMove:
    """Directory moving operations."""

    def move(self, src: str, dst: str) -> bool:
        """Move directory (stub)."""
        try:
            shutil.move(src, dst)
            return True
        except Exception:
            return False
