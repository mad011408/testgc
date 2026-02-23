"""
Contingency Planner - Contingency plans.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Contingency:
    trigger: str
    plan: List[str]
    fallback: List[str]


class ContingencyPlanner:
    """Contingency and fallback planning."""

    def __init__(self):
        self.contingencies: Dict[str, Contingency] = {}

    def add_contingency(self, trigger: str, plan: List[str], fallback: List[str]) -> None:
        """Add contingency plan."""
        self.contingencies[trigger] = Contingency(trigger=trigger, plan=plan, fallback=fallback)

    def get_plan(self, trigger: str) -> Optional[Contingency]:
        """Get contingency for trigger."""
        return self.contingencies.get(trigger)
