"""
Autoscaler AI - AI-driven autoscaling decisions for Kubernetes.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ScalingRecommendation:
    resource_type: str
    name: str
    namespace: str
    current_replicas: int
    recommended_replicas: int
    reason: str
    confidence: float
    metrics: Dict[str, float] = field(default_factory=dict)


class AutoscalerAI:
    """AI-driven autoscaling for HPA/VPA based on load predictions."""

    def __init__(self, target_cpu_percent: float = 70.0):
        self.target_cpu_percent = target_cpu_percent
        self._history: List[Dict[str, Any]] = []

    def add_metric(self, resource: str, namespace: str, cpu: float, memory: float, replicas: int) -> None:
        """Add metric sample for learning."""
        self._history.append({
            "resource": resource,
            "namespace": namespace,
            "cpu": cpu,
            "memory": memory,
            "replicas": replicas,
        })
        if len(self._history) > 1000:
            self._history = self._history[-1000:]

    async def recommend_scaling(
        self,
        resource_type: str,
        name: str,
        namespace: str,
        current_replicas: int,
        cpu_utilization: float,
        memory_utilization: float,
    ) -> ScalingRecommendation:
        """Recommend replica count based on utilization and trends."""
        rec = current_replicas
        reason = "stable"
        if cpu_utilization > self.target_cpu_percent * 1.2:
            rec = max(current_replicas + 1, int(current_replicas * 1.5))
            reason = "high_cpu"
        elif cpu_utilization < self.target_cpu_percent * 0.5 and current_replicas > 1:
            rec = max(1, current_replicas - 1)
            reason = "low_cpu"
        return ScalingRecommendation(
            resource_type=resource_type,
            name=name,
            namespace=namespace,
            current_replicas=current_replicas,
            recommended_replicas=rec,
            reason=reason,
            confidence=0.85,
            metrics={"cpu": cpu_utilization, "memory": memory_utilization},
        )
