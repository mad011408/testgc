"""
Path Builder - Path building.
"""

from pathlib import Path
from typing import Any, List, Optional


class PathBuilder:
    """Path building operations."""

    def build(self, *parts: str) -> str:
        """Build path from parts."""
        return str(Path(*parts))
