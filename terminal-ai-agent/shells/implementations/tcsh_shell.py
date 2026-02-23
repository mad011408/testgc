"""
TC Shell - TC shell implementation.
"""

from .base_shell import BaseShell, ShellResult


class TcshShell(BaseShell):
    """TC shell implementation."""

    name = "tcsh"
    path = "/bin/tcsh"
    extensions = ["tcsh", "csh"]

    def execute(self, command: str) -> ShellResult:
        """Execute tcsh command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get tcsh prompt format."""
        return "%n@%m:%d%% "
