"""
Ash Shell - Ash (Almquist) implementation.
"""

from .base_shell import BaseShell, ShellResult


class AshShell(BaseShell):
    """Ash shell implementation."""

    name = "ash"
    path = "/bin/ash"
    extensions = ["sh"]

    def execute(self, command: str) -> ShellResult:
        """Execute ash command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get ash prompt format."""
        return "$ "
