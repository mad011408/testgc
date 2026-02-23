"""System prompts for Terminal AI Agent and all AI modules."""

from prompts.system_prompts import get_system_prompt, SYSTEM_PROMPTS
from prompts.systemprompt import (
    CODING_SUPERAGENT_SYSTEM_PROMPT,
    CYBER_DEFENSE_AI_SYSTEM_PROMPT,
    ECONOMIC_AI_SYSTEM_PROMPT,
    REALWORLD_AI_OPS_SYSTEM_PROMPT,
    SYSTEM_PROMPTS as MODULE_PROMPTS,
    TERMINAL_AI_MASTER_PROMPT,
    get_system_prompt as get_module_prompt,
)

__all__ = [
    "get_system_prompt",
    "SYSTEM_PROMPTS",
    "get_module_prompt",
    "MODULE_PROMPTS",
    "TERMINAL_AI_MASTER_PROMPT",
    "REALWORLD_AI_OPS_SYSTEM_PROMPT",
    "CODING_SUPERAGENT_SYSTEM_PROMPT",
    "ECONOMIC_AI_SYSTEM_PROMPT",
    "CYBER_DEFENSE_AI_SYSTEM_PROMPT",
]
