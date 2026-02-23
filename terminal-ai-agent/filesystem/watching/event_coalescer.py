"""
Event Coalescer - Event coalescing.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CoalescedEvent:
    path: str
    events: List[str]
    count: int


class EventCoalescer:
    """Coalesces file events."""

    def __init__(self, window: float = 0.1):
        self.window = window
        self._pending: Dict[str, List[str]] = {}
