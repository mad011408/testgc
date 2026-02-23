"""
Jobs Handler - Handles jobs command.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class JobEntry:
    job_id: int
    state: str
    command: str
    pid: Optional[int]


class JobsHandler:
    """Handles jobs builtin."""

    def __init__(self):
        self._jobs: Dict[int, JobEntry] = {}

    def handle(self, args: List[str], env: Optional[Dict[str, str]] = None) -> List[JobEntry]:
        """Handle jobs command (stub)."""
        return list(self._jobs.values())
