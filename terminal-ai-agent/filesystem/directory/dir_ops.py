"""
Dir Ops - Directory operations.
"""

from pathlib import Path
from typing import Any, List, Optional


class DirOps:
    """Basic directory operations."""

    def exists(self, path: str) -> bool:
        """Check if directory exists."""
        return Path(path).is_dir()
