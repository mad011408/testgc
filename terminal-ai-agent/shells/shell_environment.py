"""
Shell Environment - Manages shell environment variables.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import os


@dataclass
class EnvVar:
    name: str
    value: str
    exported: bool


class ShellEnvironment:
    """Manages shell environment variables."""

    def __init__(self, initial: Optional[Dict[str, str]] = None):
        self._env: Dict[str, str] = dict(initial) if initial else dict(os.environ)

    def get(self, name: str, default: str = "") -> str:
        """Get environment variable."""
        return self._env.get(name, default)

    def set(self, name: str, value: str) -> None:
        """Set environment variable."""
        self._env[name] = value

    def unset(self, name: str) -> None:
        """Unset environment variable."""
        self._env.pop(name, None)

    def export_all(self) -> Dict[str, str]:
        """Get all env vars."""
        return dict(self._env)
