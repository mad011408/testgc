"""
Portfolio Balancer - Balances portfolio to target allocation.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RebalanceAction:
    asset: str
    current_weight: float
    target_weight: float
    action: str  # buy, sell
    amount: float


class PortfolioBalancer:
    """Suggests rebalancing actions."""

    def __init__(self, drift_tolerance: float = 0.02):
        self.drift_tolerance = drift_tolerance

    def rebalance(
        self,
        current_weights: Dict[str, float],
        target_weights: Dict[str, float],
        total_value: float = 1.0,
    ) -> List[RebalanceAction]:
        """Compute rebalancing actions."""
        actions = []
        for asset in set(current_weights) | set(target_weights):
            cw = current_weights.get(asset, 0)
            tw = target_weights.get(asset, 0)
            diff = tw - cw
            if abs(diff) > self.drift_tolerance:
                amount = diff * total_value
                actions.append(RebalanceAction(
                    asset=asset,
                    current_weight=cw,
                    target_weight=tw,
                    action="buy" if amount > 0 else "sell",
                    amount=abs(amount),
                ))
        return actions
