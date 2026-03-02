# kronix-ops

AI automation system for Kronix Labs — orchestrating agents, workflows, and integrations.

## Overview

`kronix-ops` is the central automation platform for Kronix Labs. It provides:

- **Agents** — Modular AI agents for task execution
- **Workflows** — n8n-compatible automation workflows
- **Tools** — Reusable integrations (HTTP, database, APIs)
- **Config** — Environment and system configuration

## Project Structure

```
kronix-ops/
├── agents/          # AI agent definitions and logic
├── workflows/       # n8n workflow JSON exports
├── tools/           # Shared tool integrations
├── config/          # Configuration and secrets templates
├── scripts/         # Setup and utility scripts
└── docs/            # Architecture and usage documentation
```

## Quick Start

```bash
# Clone the repo
git clone https://github.com/kronixlabs/kronix-ops.git
cd kronix-ops

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment
cp config/settings.example.yaml config/settings.yaml
# Edit config/settings.yaml with your values

# Run setup
bash scripts/setup.sh
```

## Requirements

- Python 3.11+
- n8n (self-hosted or cloud)
- Access to an LLM API (Anthropic, OpenAI, etc.)
