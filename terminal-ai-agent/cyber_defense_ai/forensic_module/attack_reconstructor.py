"""
Attack Reconstructor - Reconstructs attack timeline.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AttackEvent:
    timestamp: str
    event_type: str
    source: str
    target: str
    description: str
    evidence: List[str] = field(default_factory=list)


@dataclass
class AttackTimeline:
    events: List[AttackEvent]
    root_cause: Optional[str] = None
    summary: str = ""


class AttackReconstructor:
    """Reconstructs attack timeline from events."""

    def __init__(self):
        self._events: List[AttackEvent] = []

    def add_event(self, event: AttackEvent) -> None:
        self._events.append(event)

    def reconstruct(self) -> AttackTimeline:
        """Reconstruct attack timeline (stub)."""
        sorted_events = sorted(self._events, key=lambda e: e.timestamp)
        root_cause = sorted_events[0].source if sorted_events else None
        summary = f"Reconstructed {len(sorted_events)} events"
        return AttackTimeline(
            events=sorted_events,
            root_cause=root_cause,
            summary=summary,
        )
