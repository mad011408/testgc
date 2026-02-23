"""
Realpath Handler - Real path resolution.
"""

import os
from pathlib import Path
from typing import Any, Optional


class RealpathHandler:
    """Real path operations."""

    def realpath(self, path: str) -> str:
        """Get real path (stub)."""
        return os.path.realpath(path)
