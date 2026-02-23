"""
Sh Shell - POSIX sh implementation.
"""

from .base_shell import BaseShell, ShellResult


class ShShell(BaseShell):
    """POSIX sh shell implementation."""

    name = "sh"
    path = "/bin/sh"
    extensions = ["sh"]

    def execute(self, command: str) -> ShellResult:
        """Execute sh command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get sh prompt format."""
        return "$ "
