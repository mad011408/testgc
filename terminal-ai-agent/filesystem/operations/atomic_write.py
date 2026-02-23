"""
Atomic Write - Atomic file write.
"""

from pathlib import Path
from typing import Any, Optional
import tempfile
import os


class AtomicWrite:
    """Atomic write operations."""

    def write(self, path: str, content: str) -> bool:
        """Atomic write (stub)."""
        try:
            p = Path(path)
            fd, tmp = tempfile.mkstemp(dir=p.parent, prefix=".tmp")
            os.write(fd, content.encode("utf-8"))
            os.close(fd)
            os.replace(tmp, path)
            return True
        except Exception:
            return False
