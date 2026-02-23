"""
File Truncate - File truncation.
"""

from pathlib import Path
from typing import Any, Optional


class FileTruncate:
    """File truncation operations."""

    def truncate(self, path: str, size: int = 0) -> bool:
        """Truncate file (stub)."""
        try:
            Path(path).write_text(Path(path).read_text()[:size] if size > 0 else "")
            return True
        except Exception:
            return False
