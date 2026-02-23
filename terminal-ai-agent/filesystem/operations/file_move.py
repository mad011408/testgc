"""
File Move - File moving.
"""

from pathlib import Path
from typing import Any, Optional
import shutil


class FileMove:
    """File moving operations."""

    def move(self, src: str, dst: str) -> bool:
        """Move file (stub)."""
        try:
            shutil.move(src, dst)
            return True
        except Exception:
            return False
