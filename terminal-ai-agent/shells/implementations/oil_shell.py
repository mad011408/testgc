"""
Oil Shell - Oil shell implementation.
"""

from .base_shell import BaseShell, ShellResult


class OilShell(BaseShell):
    """Oil shell implementation."""

    name = "oil"
    path = "osh"
    extensions = ["osh", "oil"]

    def execute(self, command: str) -> ShellResult:
        """Execute oil/osh command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get oil prompt format."""
        return "$ "
