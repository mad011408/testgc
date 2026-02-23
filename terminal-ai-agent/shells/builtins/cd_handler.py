"""
CD Handler - Handles cd command.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from pathlib import Path
import os


@dataclass
class CdResult:
    success: bool
    new_cwd: str
    error: Optional[str]


class CdHandler:
    """Handles cd (change directory) builtin."""

    def __init__(self, cwd: Optional[str] = None):
        self._cwd = cwd or os.getcwd()

    def handle(self, args: List[str], env: Optional[Dict[str, str]] = None) -> CdResult:
        """Handle cd command (stub)."""
        target = args[0] if args else str(Path.home())
        new_path = (Path(self._cwd) / target).resolve()
        if new_path.is_dir():
            return CdResult(success=True, new_cwd=str(new_path), error=None)
        return CdResult(success=False, new_cwd=self._cwd, error="Not a directory: " + target)
