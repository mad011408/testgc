"""
File Delete - File deletion.
"""

from pathlib import Path
from typing import Any, Optional


class FileDelete:
    """File deletion operations."""

    def delete(self, path: str) -> bool:
        """Delete file (stub)."""
        try:
            Path(path).unlink(missing_ok=True)
            return True
        except Exception:
            return False
