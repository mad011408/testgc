"""
Bash Shell - Bash implementation.
"""

from typing import Any, List

from .base_shell import BaseShell, ShellResult


class BashShell(BaseShell):
    """Bash shell implementation."""

    name = "bash"
    path = "/bin/bash"
    extensions = ["sh", "bash"]

    def execute(self, command: str) -> ShellResult:
        """Execute bash command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get bash prompt format."""
        return "\\u@\\h:\\w\\$ "
