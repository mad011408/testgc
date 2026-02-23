"""
Model definitions for Rork API.
Supports multiple advanced models with 1M context capability.
"""

RORK_MODELS = {
    "claude-opus-4-0": "claude-opus-4-0-20250514",
    "claude-opus-4-5": "claude-opus-4-5-20251101",
    "claude-opus-4-6": "anthropic.claude-opus-4-6-v1",
    "gemini-3.1-pro": "gemini-3.1-pro-preview",
}

DEFAULT_MODEL = "claude-opus-4-0-20250514"

MAX_TOKEN_LIMIT = 1_000_000
MAX_CONTEXT_LIMIT = 1_000_000


def get_model_id(name: str) -> str:
    """Resolve model alias to full model ID."""
    return RORK_MODELS.get(name, name)
