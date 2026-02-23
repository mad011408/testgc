"""
Owner Handler - Owner handling.
"""

from pathlib import Path
from typing import Any, Optional


class OwnerHandler:
    """File owner operations."""

    def get_owner(self, path: str) -> str:
        """Get file owner (stub)."""
        return str(Path(path).owner()) if Path(path).exists() else ""
