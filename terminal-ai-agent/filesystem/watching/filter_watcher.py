"""
Filter Watcher - Filtered watching.
"""

from pathlib import Path
from typing import Any, Callable, List, Optional


class FilterWatcher:
    """Filtered file watcher."""

    def watch(self, path: str, pattern: str = "*") -> bool:
        """Watch with filter (stub)."""
        return True
