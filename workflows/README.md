# Workflows

n8n workflow JSON exports. Import any file directly into your n8n instance via:

**n8n UI → Workflows → Import from file**

## Available Workflows

| File | Description |
|------|-------------|
| `ai_research_pipeline.json` | Webhook → AI research → Slack notification |

## Conventions

- Workflow files are named `snake_case.json`
- Each workflow should have a description set in n8n
- Credentials are **not** stored in exports — configure them after import
