"""
Volatility Estimator - Estimates volatility.
"""

from typing import List


class VolatilityEstimator:
    """Estimates historical and implied volatility."""

    def historical_volatility(self, returns: List[float], annualize: bool = True) -> float:
        """Compute historical volatility (std dev of returns)."""
        if not returns or len(returns) < 2:
            return 0.0
        mean = sum(returns) / len(returns)
        variance = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
        std = (variance ** 0.5) if variance else 0.0
        if annualize and len(returns) > 0:
            std *= (252 ** 0.5)
        return std
