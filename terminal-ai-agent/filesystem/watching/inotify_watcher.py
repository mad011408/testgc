"""
Inotify Watcher - inotify (Linux).
"""

from pathlib import Path
from typing import Any, Callable, List, Optional


class InotifyWatcher:
    """inotify-based watcher (Linux)."""

    def watch(self, path: str, events: Optional[List[str]] = None) -> bool:
        """Watch with inotify (stub)."""
        return True
