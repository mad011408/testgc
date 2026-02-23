"""
Settings loader with environment variable support.
Max Mode: 1M tokens, 1M context window.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

from config.models import MAX_CONTEXT_LIMIT, MAX_TOKEN_LIMIT, RORK_MODELS, get_model_id

# Load .env from project root
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(_env_path)


@dataclass
class RorkConfig:
    """Rork API configuration with Max Mode support."""

    api_key: str = field(default_factory=lambda: os.getenv("RORK_API_KEY", ""))
    project_id: str = field(default_factory=lambda: os.getenv("RORK_PROJECT_ID", ""))
    base_url: str = field(
        default_factory=lambda: os.getenv("RORK_BASE_URL", "https://toolkit.rork.com/agent/chat")
    )
    model: str = field(
        default_factory=lambda: os.getenv("RORK_MODEL", "claude-opus-4-0-20250514")
    )
    max_tokens: int = field(
        default_factory=lambda: int(os.getenv("RORK_MAX_TOKENS", str(MAX_TOKEN_LIMIT)))
    )
    max_context: int = field(
        default_factory=lambda: int(os.getenv("RORK_MAX_CONTEXT", str(MAX_CONTEXT_LIMIT)))
    )

    def with_model(self, model_alias_or_id: str) -> "RorkConfig":
        """Return new config with specified model."""
        return RorkConfig(
            api_key=self.api_key,
            project_id=self.project_id,
            base_url=self.base_url,
            model=get_model_id(model_alias_or_id) if model_alias_or_id in RORK_MODELS else model_alias_or_id,
            max_tokens=self.max_tokens,
            max_context=self.max_context,
        )


def get_config(model: Optional[str] = None) -> RorkConfig:
    """Load configuration. Optionally override model."""
    cfg = RorkConfig()
    if model:
        cfg = cfg.with_model(model)
    return cfg
