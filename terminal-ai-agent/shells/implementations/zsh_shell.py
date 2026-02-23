"""
Zsh Shell - Zsh implementation.
"""

from .base_shell import BaseShell, ShellResult


class ZshShell(BaseShell):
    """Zsh shell implementation."""

    name = "zsh"
    path = "/bin/zsh"
    extensions = ["zsh"]

    def execute(self, command: str) -> ShellResult:
        """Execute zsh command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get zsh prompt format."""
        return "%n@%m:%d%% "
