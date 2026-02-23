"""
Kqueue Watcher - kqueue (BSD).
"""

from pathlib import Path
from typing import Any, Callable, List, Optional


class KqueueWatcher:
    """kqueue-based watcher (BSD)."""

    def watch(self, path: str) -> bool:
        """Watch with kqueue (stub)."""
        return True
