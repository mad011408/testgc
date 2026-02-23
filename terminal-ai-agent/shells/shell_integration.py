"""
Shell Integration - Integrates shell with terminal agent.
"""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional


@dataclass
class IntegrationHook:
    event: str
    handler: Callable[..., Any]
    priority: int


class ShellIntegration:
    """Integrates shell with terminal agent."""

    def __init__(self):
        self._hooks: Dict[str, List[IntegrationHook]] = {}

    def register_hook(self, event: str, handler: Callable[..., Any], priority: int = 0) -> None:
        """Register event hook."""
        self._hooks.setdefault(event, []).append(IntegrationHook(event=event, handler=handler, priority=priority))
        self._hooks[event].sort(key=lambda h: h.priority)

    def emit(self, event: str, *args: Any, **kwargs: Any) -> None:
        """Emit event to hooks (stub)."""
        for hook in self._hooks.get(event, []):
            hook.handler(*args, **kwargs)
