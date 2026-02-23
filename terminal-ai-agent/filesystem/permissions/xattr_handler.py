"""
Xattr Handler - Extended attributes.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional


class XattrHandler:
    """Extended attribute operations."""

    def get(self, path: str, name: str) -> Optional[bytes]:
        """Get xattr (stub)."""
        return None
