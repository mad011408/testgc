"""
C Shell - C shell implementation.
"""

from .base_shell import BaseShell, ShellResult


class CshShell(BaseShell):
    """C shell implementation."""

    name = "csh"
    path = "/bin/csh"
    extensions = ["csh"]

    def execute(self, command: str) -> ShellResult:
        """Execute csh command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get csh prompt format."""
        return "% "
