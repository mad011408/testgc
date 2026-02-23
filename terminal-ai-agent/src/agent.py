"""
Terminal AI Agent - Main agent loop.
Max Mode: 1M tokens, 1M context, configurable models & system prompts.
"""

import asyncio
import sys
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown

from config.models import RORK_MODELS
from config.settings import get_config
from prompts.system_prompts import get_system_prompt
from prompts.systemprompt import TERMINAL_AI_MASTER_PROMPT, get_system_prompt as get_module_prompt
from src.client.rork_client import RorkClient
from src.context.context_manager import ContextManager

console = Console()


class TerminalAIAgent:
    """
    Advanced Terminal AI Agent with Rork API.
    Supports: Claude Opus 4.0/4.5/4.6, Gemini 3.1 Pro.
    Max Mode: 1M context, 1M max tokens.
    """

    def __init__(
        self,
        model: Optional[str] = None,
        system_prompt: Optional[str] = None,
        system_mode: str = "terminal_master",
        integrated_modules: Optional[dict] = None,
    ):
        self.config = get_config(model)
        self.client = RorkClient(config=self.config)
        self.context = ContextManager(max_context=self.config.max_context)
        # Use integrated master prompt by default
        self.system_prompt = system_prompt or (
            TERMINAL_AI_MASTER_PROMPT if system_mode == "terminal_master"
            else get_module_prompt(system_mode) if system_mode in ("realworld_ai_ops", "coding_superagent", "economic_ai", "cyber_defense_ai")
            else get_system_prompt(system_mode)
        )
        self.integrated_modules = integrated_modules or {}

    def _print_banner(self) -> None:
        """Print startup banner."""
        integrated = ", ".join(self.integrated_modules.keys()) if self.integrated_modules else "none"
        banner = f"""
[bold cyan]Terminal AI Agent[/bold cyan] [dim]| Max Mode | Integrated[/dim]

Model: {self.config.model}
Context: {self.config.max_context:,} tokens | Max output: {self.config.max_tokens:,} tokens

Integrated: [green]{integrated}[/green]
Available models: {", ".join(RORK_MODELS.keys())}
[dim]/model <name>[/dim] | [dim]/clear[/dim] | [dim]/modules[/dim] | [dim]/prompt <mode>[/dim] | [dim]/quit[/dim]
"""
        console.print(Panel(banner, border_style="cyan", title="[bold]Ready[/bold]"))

    async def _get_response(self, messages: list) -> str:
        """Get response from Rork API."""
        result = await self.client.chat(
            messages=messages,
            system_prompt=self.system_prompt,
            max_tokens=self.config.max_tokens,
        )
        choices = result.get("choices", [])
        if not choices:
            return "[No response from model]"
        msg = choices[0].get("message", {})
        return msg.get("content", "[Empty response]")

    async def _run_turn(self, user_input: str) -> Optional[str]:
        """Process one turn of conversation."""
        self.context.add_message("user", user_input)
        messages = self.context.get_messages()
        response = await self._get_response(messages)
        self.context.add_message("assistant", response)
        return response

    def _handle_command(self, line: str) -> bool:
        """Handle slash commands. Returns True if consumed."""
        line = line.strip().lower()
        if line == "/quit" or line == "/exit":
            console.print("[dim]Goodbye![/dim]")
            sys.exit(0)
        if line == "/clear":
            self.context.clear()
            console.print("[green]Context cleared.[/green]")
            return True
        if line.startswith("/model "):
            model_name = line[7:].strip()
            if model_name in RORK_MODELS:
                self.client.set_model(model_name)
                self.config = get_config(model_name)
                console.print(f"[green]Model switched to {self.config.model}[/green]")
            else:
                console.print(f"[red]Unknown model. Available: {list(RORK_MODELS.keys())}[/red]")
            return True
        if line == "/models":
            console.print(f"Available: {list(RORK_MODELS.keys())}")
            return True
        if line == "/modules":
            if self.integrated_modules:
                for mod, subs in self.integrated_modules.items():
                    console.print(f"\n[bold]{mod}[/bold]")
                    for sub, items in subs.items():
                        console.print(f"  [dim]{sub}[/dim]: {', '.join(items)}")
            else:
                console.print("[dim]No integrated modules loaded.[/dim]")
            return True
        if line.startswith("/prompt "):
            mode = line[8:].strip()
            prompts = ("terminal_master", "realworld_ai_ops", "coding_superagent", "economic_ai", "cyber_defense_ai", "max", "default")
            if mode in prompts:
                self.system_prompt = get_module_prompt(mode) if mode in ("terminal_master", "realworld_ai_ops", "coding_superagent", "economic_ai", "cyber_defense_ai") else get_system_prompt(mode)
                console.print(f"[green]System prompt switched to: {mode}[/green]")
            else:
                console.print(f"[red]Unknown mode. Available: {prompts}[/red]")
            return True
        return False

    async def run(self) -> None:
        """Main agent loop."""
        self._print_banner()

        while True:
            try:
                user_input = Prompt.ask("\n[bold cyan]You[/bold cyan]")
                if not user_input.strip():
                    continue
                if self._handle_command(user_input):
                    continue
                with console.status("[bold]Thinking..."):
                    response = await self._run_turn(user_input)
                console.print("\n[bold green]Agent[/bold green]")
                console.print(Markdown(response))
            except KeyboardInterrupt:
                console.print("\n[dim]Interrupted. Type /quit to exit.[/dim]")
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")


async def main(integrated_modules: Optional[dict] = None) -> None:
    """Entry point for agent with integrated modules."""
    agent = TerminalAIAgent(
        system_mode="terminal_master",
        integrated_modules=integrated_modules,
    )
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
