"""
Elvish - Elvish shell implementation.
"""

from .base_shell import BaseShell, ShellResult


class ElvishShell(BaseShell):
    """Elvish shell implementation."""

    name = "elvish"
    path = "elvish"
    extensions = ["elv"]

    def execute(self, command: str) -> ShellResult:
        """Execute elvish command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get elvish prompt format."""
        return "~> "
