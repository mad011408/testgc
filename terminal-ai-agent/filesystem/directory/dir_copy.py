"""
Dir Copy - Directory copying.
"""

from pathlib import Path
from typing import Any, Optional
import shutil


class DirCopy:
    """Directory copying operations."""

    def copy(self, src: str, dst: str) -> bool:
        """Copy directory (stub)."""
        try:
            shutil.copytree(src, dst)
            return True
        except Exception:
            return False
