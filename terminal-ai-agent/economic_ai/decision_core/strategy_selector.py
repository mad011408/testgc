"""
Strategy Selector - Selects optimal strategy based on conditions.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Strategy:
    id: str
    name: str
    score: float
    conditions: Dict[str, Any]


class StrategySelector:
    """Selects strategy based on market conditions and constraints."""

    def __init__(self):
        self._strategies: List[Strategy] = []

    def register(self, strategy: Strategy) -> "StrategySelector":
        self._strategies.append(strategy)
        return self

    def select(self, context: Dict[str, Any]) -> Optional[Strategy]:
        """Select best strategy given context (stub)."""
        if not self._strategies:
            return None
        return max(self._strategies, key=lambda s: s.score)
