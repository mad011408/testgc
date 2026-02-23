"""
Rollback Engine - Handles rollback of deployments.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional

import asyncio


@dataclass
class RollbackCheckpoint:
    deployment_id: str
    version: str
    snapshot: Dict[str, Any]
    created_at: str
    metadata: Dict[str, Any] = field(default_factory=dict)


class RollbackEngine:
    """Manages rollback checkpoints and executes rollbacks."""

    def __init__(self, max_checkpoints: int = 50):
        self._checkpoints: Dict[str, List[RollbackCheckpoint]] = {}
        self._max_checkpoints = max_checkpoints
        self._rollback_handlers: Dict[str, Callable] = {}

    def save_checkpoint(
        self,
        deployment_id: str,
        version: str,
        snapshot: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> RollbackCheckpoint:
        """Save rollback checkpoint before deployment."""
        cp = RollbackCheckpoint(
            deployment_id=deployment_id,
            version=version,
            snapshot=snapshot,
            created_at=datetime.utcnow().isoformat(),
            metadata=metadata or {},
        )
        if deployment_id not in self._checkpoints:
            self._checkpoints[deployment_id] = []
        self._checkpoints[deployment_id].append(cp)
        if len(self._checkpoints[deployment_id]) > self._max_checkpoints:
            self._checkpoints[deployment_id] = self._checkpoints[deployment_id][-self._max_checkpoints:]
        return cp

    def get_checkpoint(self, deployment_id: str, version: Optional[str] = None) -> Optional[RollbackCheckpoint]:
        """Get checkpoint for deployment, optionally by version."""
        cps = self._checkpoints.get(deployment_id, [])
        if version:
            for cp in reversed(cps):
                if cp.version == version:
                    return cp
            return None
        return cps[-1] if cps else None

    def register_rollback_handler(self, resource_type: str, handler: Callable) -> "RollbackEngine":
        """Register handler for rolling back a resource type."""
        self._rollback_handlers[resource_type] = handler
        return self

    async def rollback(
        self,
        deployment_id: str,
        target_version: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Execute rollback to checkpoint."""
        cp = self.get_checkpoint(deployment_id, target_version)
        if not cp:
            return {"success": False, "error": "No checkpoint found"}

        ctx = context or {}
        results: Dict[str, Any] = {"checkpoint": cp.version, "rolled_back": []}

        for resource_type, snapshot in cp.snapshot.items():
            handler = self._rollback_handlers.get(resource_type)
            if handler:
                try:
                    if asyncio.iscoroutinefunction(handler):
                        r = await handler(snapshot, ctx)
                    else:
                        r = handler(snapshot, ctx)
                    results["rolled_back"].append({"type": resource_type, "result": r})
                except Exception as e:
                    results.setdefault("errors", []).append({"type": resource_type, "error": str(e)})

        results["success"] = "errors" not in results
        return results
