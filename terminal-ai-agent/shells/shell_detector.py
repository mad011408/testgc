"""
Shell Detector - Detects available shells on the system.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import platform
import os


@dataclass
class ShellInfo:
    name: str
    path: str
    version: Optional[str]
    is_default: bool


class ShellDetector:
    """Detects available shells on the system."""

    def __init__(self):
        pass

    def detect(self) -> List[ShellInfo]:
        """Detect available shells (stub)."""
        shells = []
        default = "powershell.exe" if platform.system() == "Windows" else "/bin/bash"
        if os.path.exists(default) or default == "powershell.exe":
            shells.append(ShellInfo(name="bash", path=default, version=None, is_default=True))
        return shells
