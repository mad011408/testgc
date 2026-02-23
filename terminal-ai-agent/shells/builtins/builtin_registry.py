"""
Builtin Registry - Registry of shell builtin handlers.
"""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Type


@dataclass
class BuiltinEntry:
    name: str
    handler: Any
    aliases: List[str]


class BuiltinRegistry:
    """Registry of shell builtin command handlers."""

    def __init__(self):
        self._builtins: Dict[str, BuiltinEntry] = {}

    def register(self, name: str, handler: Any, aliases: Optional[List[str]] = None) -> None:
        """Register builtin handler."""
        entry = BuiltinEntry(name=name, handler=handler, aliases=aliases or [])
        self._builtins[name] = entry
        for a in entry.aliases:
            self._builtins[a] = entry

    def get(self, name: str) -> Optional[BuiltinEntry]:
        """Get builtin by name."""
        return self._builtins.get(name)

    def is_builtin(self, name: str) -> bool:
        """Check if command is builtin."""
        return name in self._builtins

    def list_builtins(self) -> List[str]:
        """List all builtin names."""
        seen = set()
        result = []
        for k, v in self._builtins.items():
            if v.name not in seen:
                result.append(v.name)
                seen.add(v.name)
        return result
