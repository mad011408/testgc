"""
FSEvents Watcher - FSEvents (macOS).
"""

from pathlib import Path
from typing import Any, Callable, List, Optional


class FseventsWatcher:
    """FSEvents-based watcher (macOS)."""

    def watch(self, path: str, callback: Optional[Callable] = None) -> bool:
        """Watch with FSEvents (stub)."""
        return True
