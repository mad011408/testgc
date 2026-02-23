"""
CMD Shell - Windows CMD implementation.
"""

from .base_shell import BaseShell, ShellResult


class CmdShell(BaseShell):
    """Windows CMD shell implementation."""

    name = "cmd"
    path = "cmd.exe"
    extensions = ["bat", "cmd"]

    def execute(self, command: str) -> ShellResult:
        """Execute CMD command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get CMD prompt format."""
        return "$P$G "
