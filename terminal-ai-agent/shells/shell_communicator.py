"""
Shell Communicator - Handles communication with shell.
"""

from dataclasses import dataclass
from typing import Any, AsyncIterator, Dict, List, Optional


@dataclass
class Message:
    type: str
    content: str
    timestamp: float


class ShellCommunicator:
    """Handles bidirectional communication with shell."""

    def __init__(self, shell_id: str):
        self.shell_id = shell_id

    def write(self, data: str) -> int:
        """Write data to shell (stub)."""
        return len(data)

    def read(self, size: int = 4096) -> str:
        """Read data from shell (stub)."""
        return ""

    async def read_stream(self) -> AsyncIterator[str]:
        """Stream output from shell (stub)."""
        return
        yield ""
