"""
Relative Path - Relative path handling.
"""

from pathlib import Path
from typing import Any, Optional


class RelativePath:
    """Relative path operations."""

    def relative_to(self, path: str, base: str) -> str:
        """Get relative path (stub)."""
        return str(Path(path).relative_to(base))
