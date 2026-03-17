# demo-agent

A municipal data research agent built with [LangGraph](https://github.com/langchain-ai/langgraph) and [DeepAgents](https://github.com/CatMizu/deepagents). Given a research question, it autonomously plans sub-tasks, searches the web for authoritative data, saves findings to disk, and produces a structured markdown report.

## What it does

1. **Plan** — breaks the research question into 2–3 specific sub-tasks
2. **Search** — queries the web via Tavily, prioritizing Statistics Canada, CMHC, and municipal open data portals
3. **Save** — writes compiled findings to the `/research/` directory
4. **Report** — returns a structured markdown report with data tables, key findings, and cited sources

## Stack

- [LangGraph](https://github.com/langchain-ai/langgraph) — agent orchestration
- [DeepAgents](https://github.com/CatMizu/deepagents) — agent framework with filesystem backend
- [Claude Sonnet](https://www.anthropic.com/claude) (claude-sonnet-4-20250514) — underlying LLM
- [Tavily](https://tavily.com/) — web search
- [LangSmith](https://smith.langchain.com/) — tracing (optional)

## Getting started

### Prerequisites

- Python 3.10+
- [LangGraph CLI](https://langchain-ai.github.io/langgraph/concepts/langgraph_cli/)

### Setup

```bash
git clone https://github.com/CatMizu/demo-agent.git
cd demo-agent

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp .env.example .env
```

```
ANTHROPIC_API_KEY=your-anthropic-api-key
TAVILY_API_KEY=your-tavily-api-key
LANGSMITH_API_KEY=your-langsmith-api-key   # optional
LANGSMITH_TRACING=true                     # optional
```

### Run

```bash
langgraph dev
```

This starts the LangGraph Studio UI where you can send messages to the `agent` graph.

## Project structure

```
demo-agent/
├── demo_agent/
│   ├── agent.py       # Graph definition and system prompt
│   └── tools.py       # Tavily internet search tool
├── research/          # Agent-generated research reports
├── langgraph.json     # LangGraph config
├── pyproject.toml
└── requirements.txt
```
