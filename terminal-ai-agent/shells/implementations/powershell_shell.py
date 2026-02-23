"""
PowerShell - Windows PowerShell implementation.
"""

from .base_shell import BaseShell, ShellResult


class PowerShellShell(BaseShell):
    """Windows PowerShell implementation."""

    name = "powershell"
    path = "powershell.exe"
    extensions = ["ps1"]

    def execute(self, command: str) -> ShellResult:
        """Execute PowerShell command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get PowerShell prompt format."""
        return "PS $PWD> "
