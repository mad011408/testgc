"""
PowerShell Core - Cross-platform PowerShell Core implementation.
"""

from .base_shell import BaseShell, ShellResult


class PwshShell(BaseShell):
    """PowerShell Core implementation."""

    name = "pwsh"
    path = "pwsh"
    extensions = ["ps1"]

    def execute(self, command: str) -> ShellResult:
        """Execute pwsh command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get pwsh prompt format."""
        return "PS $PWD> "
