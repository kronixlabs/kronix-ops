# Architecture

## Overview

```
                        ┌─────────────────────────────────┐
                        │          kronix-ops              │
                        │                                  │
  External Triggers ───►│  Workflows (n8n)                 │
  (webhooks, cron)      │       │                          │
                        │       ▼                          │
                        │  Agents (Python)                 │
                        │       │                          │
                        │       ▼                          │
                        │  Tools (HTTP, DB, APIs)          │
                        └─────────────────────────────────┘
```

## Components

### Agents
Python classes that encapsulate AI logic. Each agent:
- Inherits from `BaseAgent`
- Implements a `run(input)` method
- Is stateless by default; state is passed in via config or input

### Workflows
n8n workflows serve as the orchestration layer:
- Trigger agents via HTTP calls or subprocesses
- Handle retries, branching, and scheduling
- Connect external services (Slack, email, databases)

### Tools
Reusable utility classes for external integrations:
- `HTTPTool` — Generic authenticated HTTP client
- More tools added as integrations grow

### Config
YAML-based configuration loaded at runtime. Never commit `settings.yaml`.

## Data Flow

1. A trigger fires (webhook, schedule, manual)
2. n8n workflow routes the request
3. An agent processes it using an LLM
4. Results are passed to tools for delivery (Slack, DB write, API call)
5. Response returned to caller
