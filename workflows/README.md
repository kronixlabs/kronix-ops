# Workflows

n8n workflow JSON exports. Import any file directly into your n8n instance via:

**n8n UI → Workflows → Import from file**

## Available Workflows

| File | Description | Trigger |
|------|-------------|---------|
| `ai_research_pipeline.json` | Webhook → Claude research → JSON response | HTTP POST |
| `daily_ceo_report.json` | Fetch sales data → Claude analysis → Email CEO | Cron (7am Mon–Fri) |

### daily_ceo_report

**Flow:** Schedule → Fetch Sales Data → Normalise → Claude (SalesAgent prompt) → Format Email → Send to CEO

**Environment variables required (set in n8n):**

| Variable | Description |
|----------|-------------|
| `SALES_API_URL` | Base URL of your sales/CRM API |
| `SALES_API_KEY` | API key for the sales endpoint |
| `CEO_EMAIL` | Recipient email address |

**Credentials required in n8n:**
- Anthropic API (for Claude node)
- SMTP (for Email Send node)

## Conventions

- Workflow files are named `snake_case.json`
- Each workflow should have a description set in n8n
- Credentials are **not** stored in exports — configure them after import
