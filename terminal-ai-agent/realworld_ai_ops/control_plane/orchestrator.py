"""
Orchestrator - Coordinates deployment workflows across cloud and Kubernetes.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional

import asyncio


class WorkflowStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"


@dataclass
class WorkflowStep:
    name: str
    action: Callable[..., Any]
    rollback_action: Optional[Callable[..., Any]] = None
    depends_on: List[str] = field(default_factory=list)
    status: WorkflowStatus = WorkflowStatus.PENDING
    result: Any = None
    error: Optional[str] = None


class Orchestrator:
    """Orchestrates multi-step deployment workflows with rollback support."""

    def __init__(self):
        self._steps: Dict[str, WorkflowStep] = {}
        self._workflow_status: WorkflowStatus = WorkflowStatus.PENDING
        self._execution_order: List[str] = []

    def add_step(
        self,
        name: str,
        action: Callable[..., Any],
        rollback_action: Optional[Callable[..., Any]] = None,
        depends_on: Optional[List[str]] = None,
    ) -> "Orchestrator":
        """Add a step to the workflow."""
        self._steps[name] = WorkflowStep(
            name=name,
            action=action,
            rollback_action=rollback_action,
            depends_on=depends_on or [],
        )
        return self

    def _topological_sort(self) -> List[str]:
        """Determine execution order based on dependencies."""
        visited = set()
        order = []

        def visit(node: str) -> None:
            if node in visited:
                return
            visited.add(node)
            for dep in self._steps.get(node, WorkflowStep("", lambda: None)).depends_on:
                visit(dep)
            order.append(node)

        for step_name in self._steps:
            visit(step_name)
        return order

    async def run(self, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute workflow steps in dependency order."""
        self._workflow_status = WorkflowStatus.RUNNING
        ctx = context or {}
        results = {}

        self._execution_order = self._topological_sort()

        for step_name in self._execution_order:
            step = self._steps[step_name]
            try:
                if asyncio.iscoroutinefunction(step.action):
                    step.result = await step.action(ctx, results)
                else:
                    step.result = step.action(ctx, results)
                step.status = WorkflowStatus.SUCCESS
                results[step_name] = step.result
                ctx[step_name] = step.result
            except Exception as e:
                step.status = WorkflowStatus.FAILED
                step.error = str(e)
                self._workflow_status = WorkflowStatus.FAILED
                raise RuntimeError(f"Step '{step_name}' failed: {e}") from e

        self._workflow_status = WorkflowStatus.SUCCESS
        return results

    async def rollback(self, failed_at: str, context: Optional[Dict[str, Any]] = None) -> None:
        """Rollback executed steps in reverse order."""
        ctx = context or {}
        failed_idx = self._execution_order.index(failed_at) if failed_at in self._execution_order else len(self._execution_order)

        for step_name in reversed(self._execution_order[:failed_idx]):
            step = self._steps[step_name]
            if step.rollback_action:
                try:
                    if asyncio.iscoroutinefunction(step.rollback_action):
                        await step.rollback_action(ctx)
                    else:
                        step.rollback_action(ctx)
                    step.status = WorkflowStatus.ROLLED_BACK
                except Exception as e:
                    step.error = str(e)

    def get_status(self) -> Dict[str, Any]:
        """Return workflow and step statuses."""
        return {
            "workflow": self._workflow_status.value,
            "steps": {
                name: {"status": s.status.value, "error": s.error}
                for name, s in self._steps.items()
            },
        }
