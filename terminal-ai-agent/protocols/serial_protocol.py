"""
Serial Protocol - Serial port protocol.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SerialConnection:
    port: str
    baudrate: int
    serial: Any
    connected: bool


class SerialProtocol:
    """Serial port protocol for hardware terminals."""

    def __init__(self, port: str = "", baudrate: int = 9600):
        self.port = port
        self.baudrate = baudrate

    def connect(self, port: Optional[str] = None, baudrate: Optional[int] = None) -> SerialConnection:
        """Connect to serial port (stub)."""
        p = port or self.port
        b = baudrate or self.baudrate
        return SerialConnection(port=p, baudrate=b, serial=None, connected=False)

    def disconnect(self, conn: SerialConnection) -> bool:
        """Disconnect serial (stub)."""
        return True
