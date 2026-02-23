"""
Azure Adapter - Abstracts Microsoft Azure interactions.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AzureVM:
    name: str
    resource_group: str
    location: str
    vm_size: str
    power_state: str


@dataclass
class StorageAccount:
    name: str
    resource_group: str
    location: str
    sku: str


class AzureAdapter:
    """Unified Azure adapter for VMs, Storage."""

    def __init__(self, subscription_id: str, tenant_id: Optional[str] = None):
        self.subscription_id = subscription_id
        self.tenant_id = tenant_id

    async def list_vms(self, resource_group: Optional[str] = None) -> List[AzureVM]:
        """List Azure VMs (stub - requires azure-mgmt-compute)."""
        return []

    async def start_vm(self, resource_group: str, vm_name: str) -> Dict[str, Any]:
        return {"action": "start", "vm": vm_name, "resource_group": resource_group}

    async def stop_vm(self, resource_group: str, vm_name: str) -> Dict[str, Any]:
        return {"action": "stop", "vm": vm_name, "resource_group": resource_group}

    async def list_storage_accounts(self) -> List[StorageAccount]:
        """List storage accounts (stub)."""
        return []

    async def health_check(self) -> Dict[str, Any]:
        return {"provider": "azure", "subscription": self.subscription_id, "status": "ok"}
