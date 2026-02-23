"""
Korn Shell - Korn shell implementation.
"""

from .base_shell import BaseShell, ShellResult


class KshShell(BaseShell):
    """Korn shell implementation."""

    name = "ksh"
    path = "/bin/ksh"
    extensions = ["ksh"]

    def execute(self, command: str) -> ShellResult:
        """Execute ksh command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get ksh prompt format."""
        return "$ "
