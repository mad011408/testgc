"""
Dash Shell - Dash (Debian Almquist) implementation.
"""

from .base_shell import BaseShell, ShellResult


class DashShell(BaseShell):
    """Dash shell implementation."""

    name = "dash"
    path = "/bin/dash"
    extensions = ["sh"]

    def execute(self, command: str) -> ShellResult:
        """Execute dash command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get dash prompt format."""
        return "$ "
