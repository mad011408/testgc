"""
Traffic Analyzer - Analyzes network traffic patterns.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class TrafficFlow:
    src_ip: str
    dst_ip: str
    dst_port: int
    protocol: str
    bytes_sent: int
    bytes_recv: int
    packets: int
    timestamp: str


@dataclass
class TrafficStats:
    total_bytes: int
    flows: int
    top_protocols: Dict[str, int]
    top_ports: Dict[int, int]
    anomalies: List[str] = field(default_factory=list)


class TrafficAnalyzer:
    """Analyzes network traffic for patterns and anomalies."""

    def __init__(self):
        self._flows: List[TrafficFlow] = []

    def add_flow(self, flow: TrafficFlow) -> None:
        self._flows.append(flow)

    def get_stats(self) -> TrafficStats:
        """Compute traffic statistics."""
        total = sum(f.bytes_sent + f.bytes_recv for f in self._flows)
        protocols: Dict[str, int] = {}
        ports: Dict[int, int] = {}
        for f in self._flows:
            protocols[f.protocol] = protocols.get(f.protocol, 0) + 1
            ports[f.dst_port] = ports.get(f.dst_port, 0) + 1
        top_protocols = dict(sorted(protocols.items(), key=lambda x: -x[1])[:5])
        top_ports = dict(sorted(ports.items(), key=lambda x: -x[1])[:10])
        anomalies: List[str] = []
        return TrafficStats(
            total_bytes=total, flows=len(self._flows),
            top_protocols=top_protocols, top_ports=top_ports, anomalies=anomalies,
        )
