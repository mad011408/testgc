"""
Xonsh - Xonsh shell implementation.
"""

from .base_shell import BaseShell, ShellResult


class XonshShell(BaseShell):
    """Xonsh shell implementation."""

    name = "xonsh"
    path = "xonsh"
    extensions = ["xsh"]

    def execute(self, command: str) -> ShellResult:
        """Execute xonsh command (stub)."""
        return ShellResult(output="", exit_code=0, success=True)

    def get_prompt(self) -> str:
        """Get xonsh prompt format."""
        return "{env_name}{BOLD_GREEN}{user}@{hostname}{BOLD_BLUE}{cwd}{branch_color}{curr_branch} "
