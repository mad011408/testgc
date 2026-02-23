"""
Telnet Protocol - Telnet protocol.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TelnetConnection:
    host: str
    port: int
    socket: Any
    connected: bool


class TelnetProtocol:
    """Telnet protocol for legacy terminal access."""

    def __init__(self, host: str = "", port: int = 23):
        self.host = host
        self.port = port

    def connect(self, host: Optional[str] = None, port: Optional[int] = None) -> TelnetConnection:
        """Connect via Telnet (stub)."""
        h = host or self.host
        p = port or self.port
        return TelnetConnection(host=h, port=p, socket=None, connected=False)

    def disconnect(self, conn: TelnetConnection) -> bool:
        """Disconnect Telnet (stub)."""
        return True
