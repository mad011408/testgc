"""Base tool interface for extensibility."""

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    """Base class for agent tools."""

    name: str = "base"
    description: str = ""

    @abstractmethod
    async def run(self, **kwargs: Any) -> Dict[str, Any]:
        """Execute tool. Return dict with 'result' or 'error'."""
        pass
