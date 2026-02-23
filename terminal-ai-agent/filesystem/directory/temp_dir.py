"""
Temp Dir - Temporary directory handling.
"""

import tempfile
from pathlib import Path
from typing import Any, Optional


class TempDir:
    """Temporary directory operations."""

    def create(self, suffix: str = "", prefix: str = "tmp") -> str:
        """Create temp directory (stub)."""
        return tempfile.mkdtemp(suffix=suffix, prefix=prefix)
