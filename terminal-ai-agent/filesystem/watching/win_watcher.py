"""
Win Watcher - Windows file watcher.
"""

from pathlib import Path
from typing import Any, Callable, List, Optional


class WinWatcher:
    """Windows ReadDirectoryChangesW watcher."""

    def watch(self, path: str, callback: Optional[Callable] = None) -> bool:
        """Watch on Windows (stub)."""
        return True
