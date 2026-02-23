"""
Dir Walk - Directory walking.
"""

import os
from pathlib import Path
from typing import Any, Generator, List, Optional


class DirWalk:
    """Directory walking operations."""

    def walk(self, path: str, top_down: bool = True) -> Generator[tuple, None, None]:
        """Walk directory tree (stub)."""
        for root, dirs, files in os.walk(path, topdown=top_down):
            yield (root, dirs, files)
