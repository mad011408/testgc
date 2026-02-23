"""
Deployment Controller - Manages deployment lifecycle.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, List, Optional

import asyncio


class DeploymentPhase(str, Enum):
    PREPARE = "prepare"
    VALIDATE = "validate"
    DEPLOY = "deploy"
    HEALTH_CHECK = "health_check"
    COMPLETE = "complete"
    FAILED = "failed"


@dataclass
class DeploymentSpec:
    name: str
    version: str
    target_env: str
    artifacts: List[str] = field(default_factory=list)
    config: Dict[str, Any] = field(default_factory=dict)
    replicas: int = 1


@dataclass
class DeploymentResult:
    phase: DeploymentPhase
    success: bool
    message: str
    details: Dict[str, Any] = field(default_factory=dict)
    duration_seconds: float = 0.0


class DeploymentController:
    """Controls deployment lifecycle with validation and health checks."""

    def __init__(self):
        self._phase_handlers: Dict[DeploymentPhase, Callable] = {}
        self._current_deployment: Optional[DeploymentSpec] = None
        self._results: List[DeploymentResult] = []

    def register_handler(self, phase: DeploymentPhase, handler: Callable) -> "DeploymentController":
        """Register handler for a deployment phase."""
        self._phase_handlers[phase] = handler
        return self

    def _default_prepare(self, spec: DeploymentSpec, ctx: Dict) -> DeploymentResult:
        return DeploymentResult(
            phase=DeploymentPhase.PREPARE,
            success=True,
            message="Artifacts prepared",
            details={"artifacts": spec.artifacts},
        )

    def _default_validate(self, spec: DeploymentSpec, ctx: Dict) -> DeploymentResult:
        return DeploymentResult(
            phase=DeploymentPhase.VALIDATE,
            success=True,
            message="Validation passed",
        )

    def _default_deploy(self, spec: DeploymentSpec, ctx: Dict) -> DeploymentResult:
        return DeploymentResult(
            phase=DeploymentPhase.DEPLOY,
            success=True,
            message=f"Deployed {spec.name} v{spec.version}",
            details={"replicas": spec.replicas},
        )

    def _default_health_check(self, spec: DeploymentSpec, ctx: Dict) -> DeploymentResult:
        return DeploymentResult(
            phase=DeploymentPhase.HEALTH_CHECK,
            success=True,
            message="Health check passed",
        )

    async def deploy(self, spec: DeploymentSpec) -> DeploymentResult:
        """Execute full deployment pipeline."""
        import time
        self._current_deployment = spec
        self._results = []
        ctx: Dict[str, Any] = {}

        phases = [
            DeploymentPhase.PREPARE,
            DeploymentPhase.VALIDATE,
            DeploymentPhase.DEPLOY,
            DeploymentPhase.HEALTH_CHECK,
        ]

        for phase in phases:
            handler = self._phase_handlers.get(phase) or getattr(self, f"_default_{phase.value}", None)
            if not handler:
                continue
            start = time.monotonic()
            try:
                if asyncio.iscoroutinefunction(handler):
                    result = await handler(spec, ctx)
                else:
                    result = handler(spec, ctx)
                result.duration_seconds = time.monotonic() - start
                self._results.append(result)
                ctx[phase.value] = result
                if not result.success:
                    return DeploymentResult(
                        phase=phase,
                        success=False,
                        message=f"Failed at {phase.value}: {result.message}",
                        details=result.details,
                    )
            except Exception as e:
                return DeploymentResult(
                    phase=phase,
                    success=False,
                    message=str(e),
                    details={"exception": type(e).__name__},
                )

        return DeploymentResult(
            phase=DeploymentPhase.COMPLETE,
            success=True,
            message=f"Deployment {spec.name} v{spec.version} complete",
            details={"phases": len(self._results)},
        )
