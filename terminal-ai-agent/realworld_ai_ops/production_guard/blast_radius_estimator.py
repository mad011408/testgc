"""
Blast Radius Estimator - Estimates impact of changes.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set


@dataclass
class BlastRadiusResult:
    affected_resources: List[str]
    affected_services: List[str]
    downstream_dependencies: List[str]
    upstream_dependencies: List[str]
    estimated_users: int
    estimated_downtime_minutes: float
    summary: str


class BlastRadiusEstimator:
    """Estimates blast radius of deployments and changes."""

    def __init__(self):
        self._service_graph: Dict[str, Set[str]] = {}

    def add_dependency(self, service: str, depends_on: str) -> "BlastRadiusEstimator":
        """Add service dependency."""
        if service not in self._service_graph:
            self._service_graph[service] = set()
        self._service_graph[service].add(depends_on)
        return self

    def estimate(
        self,
        changed_services: List[str],
        resource_map: Optional[Dict[str, List[str]]] = None,
    ) -> BlastRadiusResult:
        """Estimate blast radius for changed services."""
        affected_services: Set[str] = set(changed_services)
        for svc in changed_services:
            for dep in self._service_graph.get(svc, set()):
                affected_services.add(dep)
            for caller, deps in self._service_graph.items():
                if svc in deps:
                    affected_services.add(caller)

        affected_resources: List[str] = []
        resource_map = resource_map or {}
        for svc in affected_services:
            affected_resources.extend(resource_map.get(svc, [svc]))

        downstream = [s for s in affected_services if s not in changed_services]
        upstream = list(self._service_graph.get(changed_services[0], set())) if changed_services else []

        downtime = min(5.0 * len(affected_services), 60.0)
        users = 100 * len(affected_services)

        return BlastRadiusResult(
            affected_resources=list(set(affected_resources)),
            affected_services=list(affected_services),
            downstream_dependencies=downstream,
            upstream_dependencies=upstream,
            estimated_users=users,
            estimated_downtime_minutes=downtime,
            summary=f"Change affects {len(affected_services)} services, ~{users} users, ~{downtime:.0f}min max downtime",
        )
