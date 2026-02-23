"""
File Copy - File copying.
"""

from pathlib import Path
from typing import Any, Optional
import shutil


class FileCopy:
    """File copying operations."""

    def copy(self, src: str, dst: str) -> bool:
        """Copy file (stub)."""
        try:
            shutil.copy2(src, dst)
            return True
        except Exception:
            return False
