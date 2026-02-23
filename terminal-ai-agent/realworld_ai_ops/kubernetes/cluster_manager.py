"""
Cluster Manager - Manages Kubernetes cluster state.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ClusterInfo:
    name: str
    context: str
    server_url: str
    nodes: int
    version: str
    status: str = "unknown"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class NamespaceInfo:
    name: str
    status: str
    pods_count: int
    age: str


class ClusterManager:
    """Manages Kubernetes cluster discovery and state."""

    def __init__(self, kubeconfig_path: Optional[str] = None):
        self.kubeconfig_path = kubeconfig_path
        self._clusters: Dict[str, ClusterInfo] = {}

    def register_cluster(self, cluster: ClusterInfo) -> None:
        """Register cluster info."""
        self._clusters[cluster.name] = cluster

    def get_cluster(self, name: str) -> Optional[ClusterInfo]:
        """Get cluster by name."""
        return self._clusters.get(name)

    def list_clusters(self) -> List[ClusterInfo]:
        """List registered clusters."""
        return list(self._clusters.values())

    async def discover_clusters(self) -> List[ClusterInfo]:
        """Discover clusters from kubeconfig (stub - requires kubernetes client)."""
        return list(self._clusters.values())

    async def get_namespaces(self, cluster_name: str) -> List[NamespaceInfo]:
        """List namespaces in cluster (stub)."""
        return []

    async def cluster_health(self, cluster_name: str) -> Dict[str, Any]:
        """Check cluster health."""
        cluster = self._clusters.get(cluster_name)
        if not cluster:
            return {"status": "unknown", "error": "Cluster not found"}
        return {"cluster": cluster.name, "status": cluster.status, "nodes": cluster.nodes}
