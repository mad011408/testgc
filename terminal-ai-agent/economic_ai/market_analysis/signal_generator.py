"""
Signal Generator - Generates trading signals.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TradingSignal:
    symbol: str
    action: str  # buy, sell, hold
    strength: float
    timestamp: str
    reason: str


class SignalGenerator:
    """Generates trading signals from market data."""

    def __init__(self, thresholds: Optional[Dict[str, float]] = None):
        self.thresholds = thresholds or {"buy": 0.7, "sell": -0.7}

    def generate(self, prices: List[float], symbol: str = "") -> List[TradingSignal]:
        """Generate signals (stub - use ML/indicators)."""
        signals = []
        if len(prices) < 2:
            return signals
        change = (prices[-1] - prices[-2]) / prices[-2] if prices[-2] else 0
        if change > self.thresholds.get("buy", 0.05):
            signals.append(TradingSignal(symbol=symbol, action="buy", strength=min(1.0, change), timestamp="", reason="momentum"))
        elif change < self.thresholds.get("sell", -0.05):
            signals.append(TradingSignal(symbol=symbol, action="sell", strength=min(1.0, abs(change)), timestamp="", reason="momentum"))
        return signals
