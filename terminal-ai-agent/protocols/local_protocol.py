"""
Local Protocol - Local terminal protocol.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import os
import platform


@dataclass
class LocalConnection:
    shell_path: str
    cwd: str
    env: Dict[str, str]
    pid: int


class LocalProtocol:
    """Local terminal protocol for spawning local shells."""

    def __init__(self, cwd: Optional[str] = None, env: Optional[Dict[str, str]] = None):
        self.cwd = cwd or os.getcwd()
        self.env = env or dict(os.environ)

    def connect(self, shell: str = "") -> LocalConnection:
        """Connect to local shell (stub)."""
        shell_path = shell or ("powershell.exe" if platform.system() == "Windows" else "/bin/bash")
        return LocalConnection(shell_path=shell_path, cwd=self.cwd, env=dict(self.env), pid=0)

    def disconnect(self, conn: LocalConnection) -> bool:
        """Disconnect (stub)."""
        return True
