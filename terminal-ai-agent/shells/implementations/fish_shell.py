"""
Fish Shell - Fish implementation.
"""

from .base_shell import BaseShell, ShellResult


class FishShell(BaseShell):
    """Fish shell implementation."""

    name = "fish"
    path = "/usr/bin/fish"
    extensions = ["fish"]

    def execute(self, command: str) -> ShellResult:
        """Execute fish command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get fish prompt format."""
        return "fish_prompt"
