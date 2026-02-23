"""
Finite State - FSM planning.
"""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple


@dataclass
class Transition:
    from_state: str
    to_state: str
    condition: Optional[Callable[[Any], bool]] = None
    action: Optional[Callable[[Any], None]] = None


class FiniteStatePlanner:
    """Finite state machine for planning and control."""

    def __init__(self, initial_state: str = "idle"):
        self.initial_state = initial_state
        self.current_state = initial_state
        self.transitions: List[Transition] = []

    def add_transition(self, from_state: str, to_state: str, condition: Optional[Callable] = None) -> None:
        """Add state transition."""
        self.transitions.append(Transition(from_state=from_state, to_state=to_state, condition=condition))

    def step(self, event: Any) -> str:
        """Process event and transition (stub)."""
        return self.current_state
