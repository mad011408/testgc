"""
Checksum Calculator - Checksum calculation.
"""

import hashlib
from pathlib import Path
from typing import Any, Optional


class ChecksumCalculator:
    """Checksum calculation."""

    def md5(self, path: str) -> str:
        """Calculate MD5 (stub)."""
        h = hashlib.md5()
        with Path(path).open("rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
