"""
Nushell - Nushell implementation.
"""

from .base_shell import BaseShell, ShellResult


class NushellShell(BaseShell):
    """Nushell implementation."""

    name = "nushell"
    path = "nu"
    extensions = ["nu"]

    def execute(self, command: str) -> ShellResult:
        """Execute nu command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get nu prompt format."""
        return "> "
