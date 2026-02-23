"""
File Append - File appending.
"""

from pathlib import Path
from typing import Any, Optional


class FileAppend:
    """File appending operations."""

    def append(self, path: str, content: str, encoding: str = "utf-8") -> int:
        """Append to file (stub)."""
        try:
            with Path(path).open("a", encoding=encoding) as f:
                f.write(content)
            return len(content)
        except Exception:
            return 0
