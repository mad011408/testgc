"""
Source Handler - Handles source/dot command.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from pathlib import Path


@dataclass
class SourceResult:
    success: bool
    commands_executed: int
    error: Optional[str]


class SourceHandler:
    """Handles source/. builtin."""

    def __init__(self):
        pass

    def handle(self, args: List[str], env: Optional[Dict[str, str]] = None) -> SourceResult:
        """Handle source command (stub)."""
        if not args:
            return SourceResult(success=False, commands_executed=0, error="Missing filename")
        path = Path(args[0])
        if path.exists():
            return SourceResult(success=True, commands_executed=0, error=None)
        return SourceResult(success=False, commands_executed=0, error="File not found: " + args[0])
