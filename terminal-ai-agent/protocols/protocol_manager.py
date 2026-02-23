"""
Protocol Manager - Manages terminal protocols.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Type


@dataclass
class ProtocolInfo:
    name: str
    protocol_class: Type
    supported: bool
    description: str


class ProtocolManager:
    """Manages terminal protocol handlers."""

    def __init__(self):
        self._protocols: Dict[str, ProtocolInfo] = {}

    def register(self, name: str, protocol_class: Type, description: str = "") -> None:
        """Register protocol handler."""
        self._protocols[name] = ProtocolInfo(
            name=name,
            protocol_class=protocol_class,
            supported=True,
            description=description,
        )

    def get(self, name: str) -> Optional[ProtocolInfo]:
        """Get protocol by name."""
        return self._protocols.get(name)

    def list_protocols(self) -> List[str]:
        """List all registered protocols."""
        return list(self._protocols.keys())
