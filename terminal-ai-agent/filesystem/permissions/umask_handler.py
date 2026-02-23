"""
Umask Handler - umask handling.
"""

import os
from typing import Any, Optional


class UmaskHandler:
    """umask operations."""

    def get_umask(self) -> int:
        """Get current umask (stub)."""
        return os.umask(0) or 0o22
