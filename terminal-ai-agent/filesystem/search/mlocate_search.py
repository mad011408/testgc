"""
Mlocate Search - mlocate integration.
"""

from pathlib import Path
from typing import Any, List, Optional
import subprocess


class MlocateSearch:
    """mlocate-based search."""

    def search(self, pattern: str) -> List[str]:
        """Search via mlocate (stub)."""
        try:
            out = subprocess.run(["locate", "-i", pattern], capture_output=True, text=True)
            return out.stdout.strip().split("\n") if out.returncode == 0 else []
        except Exception:
            return []
