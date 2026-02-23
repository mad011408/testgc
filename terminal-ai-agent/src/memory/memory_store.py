"""
Memory store for long-term conversation history.
Used for summarization when context exceeds limit.
"""

from typing import Any, Dict, List, Optional


class MemoryStore:
    """Simple in-memory store for conversation history."""

    def __init__(self, max_entries: int = 1000):
        self.max_entries = max_entries
        self._entries: List[Dict[str, Any]] = []

    def add(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Add entry to memory."""
        entry = {"role": role, "content": content, "metadata": metadata or {}}
        self._entries.append(entry)
        if len(self._entries) > self.max_entries:
            self._entries = self._entries[-self.max_entries :]

    def get_recent(self, n: int = 50) -> List[Dict[str, Any]]:
        """Get n most recent entries."""
        return self._entries[-n:]

    def clear(self) -> None:
        """Clear all entries."""
        self._entries = []
