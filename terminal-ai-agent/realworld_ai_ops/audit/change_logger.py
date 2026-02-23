"""
Change Logger - Logs infrastructure and deployment changes.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
import json


@dataclass
class ChangeRecord:
    id: str
    action: str
    resource_type: str
    resource_id: str
    before: Optional[Dict[str, Any]] = None
    after: Optional[Dict[str, Any]] = None
    actor: str = "system"
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    metadata: Dict[str, Any] = field(default_factory=dict)


class ChangeLogger:
    """Logs changes for audit trail."""

    def __init__(self, max_records: int = 10000):
        self._records: List[ChangeRecord] = []
        self._max_records = max_records
        self._counter = 0

    def log(
        self,
        action: str,
        resource_type: str,
        resource_id: str,
        before: Optional[Dict] = None,
        after: Optional[Dict] = None,
        actor: str = "system",
        **metadata: Any,
    ) -> ChangeRecord:
        """Log a change."""
        self._counter += 1
        rec = ChangeRecord(
            id=f"ch-{self._counter}",
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            before=before,
            after=after,
            actor=actor,
            metadata=metadata,
        )
        self._records.append(rec)
        if len(self._records) > self._max_records:
            self._records = self._records[-self._max_records:]
        return rec

    def query(
        self,
        resource_type: Optional[str] = None,
        action: Optional[str] = None,
        resource_id: Optional[str] = None,
        limit: int = 100,
    ) -> List[ChangeRecord]:
        """Query change records."""
        result = list(self._records)
        if resource_type:
            result = [r for r in result if r.resource_type == resource_type]
        if action:
            result = [r for r in result if r.action == action]
        if resource_id:
            result = [r for r in result if r.resource_id == resource_id]
        return result[-limit:]
