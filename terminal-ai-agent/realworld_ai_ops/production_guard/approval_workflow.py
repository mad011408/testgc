"""
Approval Workflow - Manages approval gates for deployments.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional


class ApprovalStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXPIRED = "expired"


@dataclass
class ApprovalRequest:
    id: str
    deployment_id: str
    approvers: List[str]
    status: ApprovalStatus = ApprovalStatus.PENDING
    approved_by: Optional[str] = None
    rejected_by: Optional[str] = None
    reason: Optional[str] = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    expires_at: Optional[str] = None


class ApprovalWorkflow:
    """Manages approval gates for production deployments."""

    def __init__(self, required_approvals: int = 1, expiry_hours: int = 24):
        self.required_approvals = required_approvals
        self.expiry_hours = expiry_hours
        self._requests: Dict[str, ApprovalRequest] = {}
        self._approvals: Dict[str, List[str]] = {}

    def create_request(self, deployment_id: str, approvers: List[str]) -> ApprovalRequest:
        """Create approval request."""
        import uuid
        req_id = str(uuid.uuid4())[:8]
        from datetime import timedelta
        exp = (datetime.utcnow() + timedelta(hours=self.expiry_hours)).isoformat()
        req = ApprovalRequest(id=req_id, deployment_id=deployment_id, approvers=approvers, expires_at=exp)
        self._requests[req_id] = req
        self._approvals[req_id] = []
        return req

    def approve(self, request_id: str, approver: str) -> bool:
        """Record approval."""
        req = self._requests.get(request_id)
        if not req or req.status != ApprovalStatus.PENDING:
            return False
        if approver not in req.approvers:
            return False
        if approver in self._approvals.get(request_id, []):
            return True  # already approved
        self._approvals[request_id].append(approver)
        if len(self._approvals[request_id]) >= self.required_approvals:
            req.status = ApprovalStatus.APPROVED
            req.approved_by = approver
        return True

    def reject(self, request_id: str, approver: str, reason: Optional[str] = None) -> bool:
        """Reject request."""
        req = self._requests.get(request_id)
        if not req or req.status != ApprovalStatus.PENDING:
            return False
        req.status = ApprovalStatus.REJECTED
        req.rejected_by = approver
        req.reason = reason
        return True

    def get_status(self, request_id: str) -> Optional[ApprovalRequest]:
        """Get request status."""
        return self._requests.get(request_id)
