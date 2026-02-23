"""
FS Controller - Filesystem controller.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from pathlib import Path


@dataclass
class FSState:
    cwd: str
    root: str
    operations_count: int


class FSController:
    """Controls filesystem operations and state."""

    def __init__(self):
        self._cwd = Path.cwd()
        self._ops_count = 0

    def get_state(self) -> FSState:
        """Get current FS state."""
        return FSState(cwd=str(self._cwd), root=str(self._cwd.root), operations_count=self._ops_count)
