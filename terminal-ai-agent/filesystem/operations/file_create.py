"""
File Create - File creation.
"""

from pathlib import Path
from typing import Any, Optional


class FileCreate:
    """File creation operations."""

    def create(self, path: str, content: str = "") -> bool:
        """Create file (stub)."""
        try:
            p = Path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
            return True
        except Exception:
            return False
