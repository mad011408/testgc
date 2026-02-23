"""
TCP Protocol - Raw TCP protocol.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TcpConnection:
    host: str
    port: int
    socket: Any
    connected: bool


class TcpProtocol:
    """Raw TCP protocol for custom terminals."""

    def __init__(self, host: str = "", port: int = 23):
        self.host = host
        self.port = port

    def connect(self, host: Optional[str] = None, port: Optional[int] = None) -> TcpConnection:
        """Connect via TCP (stub)."""
        h = host or self.host
        p = port or self.port
        return TcpConnection(host=h, port=p, socket=None, connected=False)

    def disconnect(self, conn: TcpConnection) -> bool:
        """Disconnect TCP (stub)."""
        return True
