"""
Rlogin Protocol - Rlogin protocol.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RloginConnection:
    host: str
    port: int
    user: str
    socket: Any
    connected: bool


class RloginProtocol:
    """Rlogin protocol for remote login."""

    def __init__(self, host: str = "", port: int = 513, user: str = ""):
        self.host = host
        self.port = port
        self.user = user

    def connect(self, host: Optional[str] = None, port: Optional[int] = None, user: Optional[str] = None) -> RloginConnection:
        """Connect via Rlogin (stub)."""
        h = host or self.host
        p = port or self.port
        u = user or self.user
        return RloginConnection(host=h, port=p, user=u, socket=None, connected=False)

    def disconnect(self, conn: RloginConnection) -> bool:
        """Disconnect Rlogin (stub)."""
        return True
