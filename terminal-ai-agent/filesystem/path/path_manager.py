"""
Path Manager - Path management.
"""

from pathlib import Path
from typing import Any, List, Optional


class PathManager:
    """Path management operations."""

    def __init__(self, base: Optional[str] = None):
        self.base = Path(base) if base else Path.cwd()

    def join(self, *parts: str) -> Path:
        """Join path parts."""
        return self.base.joinpath(*parts)
