"""
History Handler - Handles history command.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class HistoryEntry:
    index: int
    command: str
    timestamp: Optional[str]


class HistoryHandler:
    """Handles history builtin."""

    def __init__(self, max_size: int = 1000):
        self._history: List[str] = []
        self._max_size = max_size

    def add(self, command: str) -> None:
        """Add command to history."""
        self._history.append(command)
        if len(self._history) > self._max_size:
            self._history.pop(0)

    def handle(self, args: List[str], env: Optional[Dict[str, str]] = None) -> List[HistoryEntry]:
        """Handle history command (stub)."""
        return [HistoryEntry(i + 1, cmd, None) for i, cmd in enumerate(self._history[-100:])]
