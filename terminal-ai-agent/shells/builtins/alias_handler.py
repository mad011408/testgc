"""
Alias Handler - Handles alias command.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AliasEntry:
    name: str
    value: str


class AliasHandler:
    """Handles alias builtin."""

    def __init__(self):
        self._aliases: Dict[str, str] = {}

    def handle(self, args: List[str], env: Optional[Dict[str, str]] = None) -> List[AliasEntry]:
        """Handle alias command (stub)."""
        result = []
        if not args:
            return [AliasEntry(k, v) for k, v in self._aliases.items()]
        for arg in args:
            if "=" in arg:
                name, value = arg.split("=", 1)
                self._aliases[name] = value
                result.append(AliasEntry(name, value))
        return result
