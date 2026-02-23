"""
File Ops - Basic file operations.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from pathlib import Path


@dataclass
class FileOpResult:
    success: bool
    path: str
    error: Optional[str]


class FileOps:
    """Basic file operations."""

    def __init__(self):
        pass

    def exists(self, path: str) -> bool:
        """Check if file exists."""
        return Path(path).exists()
