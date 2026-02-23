"""
Backup On Write - Backup before write.
"""

from pathlib import Path
from typing import Any, Optional


class BackupOnWrite:
    """Backup before write operations."""

    def backup(self, path: str, backup_path: Optional[str] = None) -> Optional[str]:
        """Create backup (stub)."""
        p = Path(path)
        if not p.exists():
            return None
        bp = backup_path or str(p) + ".bak"
        try:
            Path(path).rename(bp)
            return bp
        except Exception:
            return None
