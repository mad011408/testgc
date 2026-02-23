"""
Advanced Rork API client with streaming and 1M context support.
Supports: Claude Opus 4.0/4.5/4.6, Gemini 3.1 Pro.
"""

import json
from typing import Any, AsyncIterator, Dict, List, Optional

import httpx

from config.settings import RorkConfig, get_config


class RorkClientError(Exception):
    """Rork API error."""

    pass


class RorkClient:
    """
    Rork API client for chat completions.
    Max Mode: 1M max_tokens, 1M context window.
    """

    def __init__(self, config: Optional[RorkConfig] = None, model: Optional[str] = None):
        self.config = config or get_config(model)
        self._client: Optional[httpx.AsyncClient] = None

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json",
            "X-Project-Id": self.config.project_id,
        }

    def _build_payload(
        self,
        messages: List[Dict[str, Any]],
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
        stream: bool = False,
    ) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "model": self.config.model,
            "messages": messages,
            "max_tokens": max_tokens or self.config.max_tokens,
            "stream": stream,
        }
        if system_prompt:
            payload["system"] = system_prompt
        return payload

    async def chat(
        self,
        messages: List[Dict[str, str]],
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Send chat completion request.
        Supports 1M token context and 1M max output (Max Mode).
        """
        payload = self._build_payload(messages, system_prompt, max_tokens, stream=False)
        async with httpx.AsyncClient(timeout=180.0) as client:
            response = await client.post(
                self.config.base_url,
                json=payload,
                headers=self._headers(),
            )
            response.raise_for_status()
            return response.json()

    async def chat_stream(
        self,
        messages: List[Dict[str, str]],
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
    ) -> AsyncIterator[str]:
        """Stream chat completion response."""
        payload = self._build_payload(messages, system_prompt, max_tokens, stream=True)
        async with httpx.AsyncClient(timeout=180.0) as client:
            async with client.stream(
                "POST",
                self.config.base_url,
                json=payload,
                headers=self._headers(),
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        data = line[6:].strip()
                        if data == "[DONE]":
                            break
                        try:
                            parsed = json.loads(data)
                            delta = parsed.get("choices", [{}])[0].get("delta", {})
                            content = delta.get("content", "")
                            if content:
                                yield content
                        except json.JSONDecodeError:
                            pass

    def set_model(self, model: str) -> None:
        """Switch to different model."""
        from config.models import RORK_MODELS

        self.config.model = RORK_MODELS.get(model, model)
