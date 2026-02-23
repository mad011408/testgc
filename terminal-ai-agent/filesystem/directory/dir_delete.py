"""
Dir Delete - Directory deletion.
"""

from pathlib import Path
from typing import Any, Optional
import shutil


class DirDelete:
    """Directory deletion operations."""

    def delete(self, path: str, recursive: bool = False) -> bool:
        """Delete directory (stub)."""
        try:
            p = Path(path)
            if recursive:
                shutil.rmtree(p)
            else:
                p.rmdir()
            return True
        except Exception:
            return False
