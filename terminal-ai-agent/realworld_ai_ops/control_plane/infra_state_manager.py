"""
Infra State Manager - Tracks and manages infrastructure state.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
import json


@dataclass
class ResourceState:
    id: str
    type: str
    provider: str
    region: str
    status: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    last_updated: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type,
            "provider": self.provider,
            "region": self.region,
            "status": self.status,
            "metadata": self.metadata,
            "last_updated": self.last_updated or datetime.utcnow().isoformat(),
        }


class InfraStateManager:
    """Manages infrastructure state with drift detection."""

    def __init__(self):
        self._resources: Dict[str, ResourceState] = {}
        self._history: List[Dict[str, Any]] = []
        self._max_history = 1000

    def register(self, resource: ResourceState) -> None:
        """Register or update a resource."""
        resource.last_updated = datetime.utcnow().isoformat()
        old = self._resources.get(resource.id)
        self._resources[resource.id] = resource
        self._append_history("register", resource.to_dict(), old.to_dict() if old else None)

    def unregister(self, resource_id: str) -> Optional[ResourceState]:
        """Remove resource from state."""
        old = self._resources.pop(resource_id, None)
        if old:
            self._append_history("unregister", {"id": resource_id}, old.to_dict())
        return old

    def get(self, resource_id: str) -> Optional[ResourceState]:
        """Get resource by ID."""
        return self._resources.get(resource_id)

    def list_resources(
        self,
        provider: Optional[str] = None,
        type_filter: Optional[str] = None,
        status: Optional[str] = None,
    ) -> List[ResourceState]:
        """List resources with optional filters."""
        result = list(self._resources.values())
        if provider:
            result = [r for r in result if r.provider == provider]
        if type_filter:
            result = [r for r in result if r.type == type_filter]
        if status:
            result = [r for r in result if r.status == status]
        return result

    def update_status(self, resource_id: str, status: str) -> bool:
        """Update resource status."""
        r = self._resources.get(resource_id)
        if r:
            old_status = r.status
            r.status = status
            r.last_updated = datetime.utcnow().isoformat()
            self._append_history("status_change", {"id": resource_id, "status": status}, {"old": old_status})
            return True
        return False

    def detect_drift(self, current: List[ResourceState]) -> Dict[str, Any]:
        """Detect drift between expected and current state."""
        expected_ids = set(self._resources)
        current_ids = {r.id for r in current}
        return {
            "orphaned": list(expected_ids - current_ids),
            "untracked": list(current_ids - expected_ids),
            "drifted": [
                r.id for r in current
                if r.id in expected_ids and self._resources[r.id].status != r.status
            ],
        }

    def _append_history(self, action: str, new_state: Dict, old_state: Optional[Dict]) -> None:
        self._history.append({
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "new": new_state,
            "old": old_state,
        })
        if len(self._history) > self._max_history:
            self._history = self._history[-self._max_history:]

    def export_state(self) -> str:
        """Export state as JSON."""
        return json.dumps({
            "resources": [r.to_dict() for r in self._resources.values()],
            "exported_at": datetime.utcnow().isoformat(),
        }, indent=2)
