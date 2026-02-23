"""
Firewall Updater - Updates firewall rules for threat response.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FirewallRule:
    id: str
    action: str  # allow, deny
    src_ip: Optional[str] = None
    dst_ip: Optional[str] = None
    dst_port: Optional[int] = None
    protocol: str = "any"


class FirewallUpdater:
    """Updates firewall rules for incident response."""

    def __init__(self):
        self._rules: List[FirewallRule] = []
        self._counter = 0

    def add_rule(
        self,
        action: str,
        src_ip: Optional[str] = None,
        dst_ip: Optional[str] = None,
        dst_port: Optional[int] = None,
    ) -> FirewallRule:
        """Add firewall rule."""
        self._counter += 1
        rule = FirewallRule(
            id=f"fw-{self._counter}",
            action=action,
            src_ip=src_ip,
            dst_ip=dst_ip,
            dst_port=dst_port,
        )
        self._rules.append(rule)
        return rule

    def block_ip(self, ip: str) -> FirewallRule:
        """Block IP."""
        return self.add_rule(action="deny", src_ip=ip)
