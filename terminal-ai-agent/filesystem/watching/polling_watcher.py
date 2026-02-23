"""
Polling Watcher - Polling fallback.
"""

from pathlib import Path
from typing import Any, Callable, List, Optional
import time


class PollingWatcher:
    """Polling-based watcher (fallback)."""

    def __init__(self, interval: float = 1.0):
        self.interval = interval

    def watch(self, path: str, callback: Optional[Callable] = None) -> bool:
        """Watch via polling (stub)."""
        return True
