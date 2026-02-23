"""
Shell Prompt Parser - Parses shell prompts.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PromptSegment:
    type: str
    content: str
    raw: str


class ShellPromptParser:
    """Parses shell prompt format strings."""

    def __init__(self):
        pass

    def parse(self, prompt_format: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Parse prompt format into display string (stub)."""
        return prompt_format.replace("\\u", "").replace("\\h", "").replace("\\w", "~").replace("\\$", "$")
