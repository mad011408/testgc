"""
Path Resolver - Path resolution.
"""

from pathlib import Path
from typing import Any, Optional


class PathResolver:
    """Path resolution operations."""

    def resolve(self, path: str, base: Optional[str] = None) -> str:
        """Resolve path (stub)."""
        p = Path(path)
        if base:
            p = Path(base) / path
        return str(p.resolve())
