"""
Path Matcher - Pattern matching.
"""

from pathlib import Path
from typing import Any, List, Optional
import fnmatch


class PathMatcher:
    """Path pattern matching operations."""

    def match(self, path: str, pattern: str) -> bool:
        """Match path against pattern (stub)."""
        return fnmatch.fnmatch(Path(path).name, pattern)
