"""
Exposure Calculator - Calculates portfolio exposure.
"""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class ExposureResult:
    total_exposure: float
    by_asset: Dict[str, float]
    by_sector: Dict[str, float]
    concentration_risk: float


class ExposureCalculator:
    """Calculates exposure and concentration risk."""

    def calculate(
        self,
        positions: Dict[str, float],
        sector_map: Optional[Dict[str, str]] = None,
    ) -> ExposureResult:
        """Calculate portfolio exposure."""
        total = sum(positions.values()) or 1
        by_asset = {k: v / total for k, v in positions.items()}
        by_sector: Dict[str, float] = {}
        sector_map = sector_map or {}
        for asset, weight in by_asset.items():
            sector = sector_map.get(asset, "other")
            by_sector[sector] = by_sector.get(sector, 0) + weight
        max_weight = max(by_asset.values()) if by_asset else 0
        concentration = max_weight
        return ExposureResult(
            total_exposure=total,
            by_asset=by_asset,
            by_sector=by_sector,
            concentration_risk=concentration,
        )
