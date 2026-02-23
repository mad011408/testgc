"""
Base Shell - Abstract base shell implementation.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ShellResult:
    output: str
    exit_code: int
    success: bool


class BaseShell(ABC):
    """Abstract base shell implementation."""

    name: str = "base"
    path: str = ""
    extensions: List[str] = ["sh"]

    @abstractmethod
    def execute(self, command: str) -> ShellResult:
        """Execute command."""
        pass

    @abstractmethod
    def get_prompt(self) -> str:
        """Get current prompt format."""
        pass

    def is_available(self) -> bool:
        """Check if shell is available (stub)."""
        return True
