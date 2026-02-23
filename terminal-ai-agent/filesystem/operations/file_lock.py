"""
File Lock - File locking.
"""

from pathlib import Path
from typing import Any, Optional


class FileLock:
    """File locking operations."""

    def lock(self, path: str, exclusive: bool = True) -> bool:
        """Lock file (stub)."""
        return True
