"""
Shell RC Parser - Parses shell RC files (.bashrc, .zshrc, etc.).
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RCDirective:
    line_no: int
    directive: str
    args: List[str]
    raw: str


class ShellRCParser:
    """Parses shell RC files."""

    def __init__(self):
        pass

    def parse(self, content: str) -> List[RCDirective]:
        """Parse RC file content (stub)."""
        directives = []
        for i, line in enumerate(content.strip().split("\n"), 1):
            line = line.strip()
            if line and not line.startswith("#"):
                parts = line.split(maxsplit=1)
                directives.append(RCDirective(
                    line_no=i,
                    directive=parts[0] if parts else "",
                    args=parts[1].split() if len(parts) > 1 else [],
                    raw=line,
                ))
        return directives
