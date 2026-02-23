"""
File Read - File reading.
"""

from pathlib import Path
from typing import Any, Optional


class FileRead:
    """File reading operations."""

    def read(self, path: str, encoding: str = "utf-8") -> str:
        """Read file (stub)."""
        try:
            return Path(path).read_text(encoding=encoding)
        except Exception:
            return ""
