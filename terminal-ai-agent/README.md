# Terminal AI Agent

Advanced Python terminal AI agent framework with **Rork API** integration.

## Features

- **Max Mode**: 1 million token context, 1 million max output
- **Models**: Claude Opus 4.0/4.5/4.6, Gemini 3.1 Pro
- **Configurable system prompts**
- **Context manager** with sliding window
- Rich terminal UI

## Setup

```bash
cd terminal-ai-agent
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your RORK_API_KEY and RORK_PROJECT_ID
```

## Run

```bash
python main.py
```

## Commands

- `/model <name>` – Switch model (claude-opus-4-0, claude-opus-4-5, claude-opus-4-6, gemini-3.1-pro)
- `/clear` – Clear context
- `/quit` – Exit

## Environment

| Variable        | Description                | Default                     |
|----------------|----------------------------|-----------------------------|
| RORK_API_KEY   | Rork API key               | (required)                  |
| RORK_PROJECT_ID| Rork project ID            | (required)                  |
| RORK_BASE_URL  | API base URL               | https://toolkit.rork.com/agent/chat |
| RORK_MODEL     | Default model              | claude-opus-4-0-20250514    |
| RORK_MAX_TOKENS| Max output tokens          | 1000000                     |
| RORK_MAX_CONTEXT| Max context tokens        | 1000000                     |
