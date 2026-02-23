"""
Context manager for 1M token window.
Maintains sliding window and enforces max context limit.
"""

from typing import Any, Dict, List, Optional

from config.settings import get_config


class ContextManager:
    """
    Manages conversation context within 1M token limit.
    Prioritizes recent messages, summarizes or truncates when needed.
    """

    def __init__(self, max_context: Optional[int] = None):
        config = get_config()
        self.max_context = max_context or config.max_context
        self._messages: List[Dict[str, Any]] = []
        self._current_tokens = 0

    def add_message(self, role: str, content: str) -> None:
        """Add message to context."""
        msg = {"role": role, "content": content}
        self._messages.append(msg)
        self._current_tokens += self._estimate_tokens(content) + 4  # overhead

    def trim_to_limit(self) -> None:
        """
        Trim messages to stay within max_context.
        Keeps system-like context and recent messages.
        """
        if self._current_tokens <= self.max_context:
            return
        # Keep first message if system-like, then trim from oldest
        kept: List[Dict[str, Any]] = []
        tokens = 0
        reserve = self.max_context * 0.7  # Use 70% for messages
        for msg in reversed(self._messages):
            est = self._estimate_tokens(msg.get("content", "")) + 4
            if tokens + est > reserve and kept:
                break
            kept.insert(0, msg)
            tokens += est
        self._messages = kept
        self._current_tokens = sum(
            self._estimate_tokens(m.get("content", "")) + 4 for m in kept
        )

    def get_messages(self) -> List[Dict[str, str]]:
        """Return messages suitable for API."""
        self.trim_to_limit()
        return [{"role": m["role"], "content": m["content"]} for m in self._messages]

    def clear(self) -> None:
        """Clear all context."""
        self._messages = []
        self._current_tokens = 0

    @staticmethod
    def _estimate_tokens(text: str) -> int:
        """Rough token estimate (~4 chars per token for English)."""
        try:
            import tiktoken
            enc = tiktoken.get_encoding("cl100k_base")
            return len(enc.encode(text))
        except Exception:
            return max(1, len(text) // 4)
