"""
Fnmatch Handler - fnmatch patterns.
"""

from pathlib import Path
from typing import Any, List, Optional
import fnmatch


class FnmatchHandler:
    """fnmatch pattern operations."""

    def filter(self, paths: List[str], pattern: str) -> List[str]:
        """Filter paths by fnmatch (stub)."""
        return [p for p in paths if fnmatch.fnmatch(Path(p).name, pattern)]
