"""
Unset Handler - Handles unset command.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class UnsetResult:
    success: bool
    unset_vars: List[str]
    error: Optional[str]


class UnsetHandler:
    """Handles unset builtin."""

    def __init__(self, env: Optional[Dict[str, str]] = None):
        self._env = env or {}

    def handle(self, args: List[str], env: Optional[Dict[str, str]] = None) -> UnsetResult:
        """Handle unset command (stub)."""
        unset_vars = []
        for name in args:
            if name in self._env:
                del self._env[name]
                unset_vars.append(name)
        return UnsetResult(success=True, unset_vars=unset_vars, error=None)
