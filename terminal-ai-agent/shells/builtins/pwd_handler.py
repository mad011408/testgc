"""
PWD Handler - Handles pwd command.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import os


@dataclass
class PwdResult:
    cwd: str
    physical: bool


class PwdHandler:
    """Handles pwd (print working directory) builtin."""

    def __init__(self, cwd: Optional[str] = None):
        self._cwd = cwd or os.getcwd()

    def handle(self, args: List[str], env: Optional[Dict[str, str]] = None) -> PwdResult:
        """Handle pwd command (stub)."""
        physical = "-P" in args or "--physical" in args
        path = os.path.realpath(self._cwd) if physical else self._cwd
        return PwdResult(cwd=path, physical=physical)
