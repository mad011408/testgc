"""
Path Normalizer - Path normalization.
"""

from pathlib import Path
from typing import Any, Optional


class PathNormalizer:
    """Path normalization operations."""

    def normalize(self, path: str) -> str:
        """Normalize path (stub)."""
        return str(Path(path))
