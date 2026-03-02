"""
Sales agent — analyses raw sales data and produces a structured CEO report.

Expected input:
    {
        "date": "2026-03-02",
        "revenue": 48200,
        "deals_closed": 7,
        "pipeline_value": 320000,
        "top_deals": [{"name": "Acme Corp", "value": 12000}, ...],
        "churn": 1,
        "new_leads": 34
    }

Returns a markdown-formatted report string.
"""

import json
import anthropic
from .base_agent import BaseAgent


SYSTEM_PROMPT = """You are a senior sales analyst at Kronix Labs.
Given raw sales metrics, produce a concise daily CEO report in markdown.

The report must include:
1. **Executive Summary** — 2-3 sentence headline takeaway
2. **Key Metrics** — formatted table (Revenue, Deals Closed, Pipeline, New Leads, Churn)
3. **Top Deals** — bullet list with deal name and value
4. **Risks & Opportunities** — 2-3 brief bullets
5. **Recommended Actions** — 1-3 specific, actionable items for the CEO

Keep the tone direct and data-driven. No fluff."""


class SalesAgent(BaseAgent):
    def __init__(self, config: dict = None):
        super().__init__("SalesAgent", config)
        self.client = anthropic.Anthropic(api_key=self.config.get("api_key"))
        self.model = self.config.get("model", "claude-sonnet-4-6")

    def run(self, sales_data: dict) -> str:
        self.log(f"Generating CEO report for {sales_data.get('date', 'unknown date')}")

        user_message = f"Here is today's sales data:\n\n```json\n{json.dumps(sales_data, indent=2)}\n```\n\nGenerate the CEO report."

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}],
        )

        report = response.content[0].text
        self.log("Report generated successfully")
        return report
