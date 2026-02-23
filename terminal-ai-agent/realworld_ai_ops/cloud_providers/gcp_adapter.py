"""
GCP Adapter - Abstracts Google Cloud Platform interactions.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class GCEInstance:
    name: str
    zone: str
    machine_type: str
    status: str
    project_id: str


@dataclass
class GCSBucket:
    name: str
    location: str
    storage_class: str


class GCPAdapter:
    """Unified GCP adapter for Compute Engine, Cloud Storage."""

    def __init__(self, project_id: str, region: str = "us-central1"):
        self.project_id = project_id
        self.region = region

    async def list_instances(self, zone: Optional[str] = None) -> List[GCEInstance]:
        """List GCE instances (stub - requires google-cloud-compute)."""
        return []

    async def start_instance(self, zone: str, instance_name: str) -> Dict[str, Any]:
        return {"action": "start", "instance": instance_name, "zone": zone}

    async def stop_instance(self, zone: str, instance_name: str) -> Dict[str, Any]:
        return {"action": "stop", "instance": instance_name, "zone": zone}

    async def list_buckets(self) -> List[GCSBucket]:
        """List GCS buckets (stub)."""
        return []

    async def health_check(self) -> Dict[str, Any]:
        return {"provider": "gcp", "project": self.project_id, "region": self.region, "status": "ok"}
