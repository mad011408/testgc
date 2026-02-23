"""
File Write - File writing.
"""

from pathlib import Path
from typing import Any, Optional


class FileWrite:
    """File writing operations."""

    def write(self, path: str, content: str, encoding: str = "utf-8") -> int:
        """Write file (stub)."""
        try:
            Path(path).write_text(content, encoding=encoding)
            return len(content)
        except Exception:
            return 0
