"""
Research agent — queries an LLM with web search context.
"""

import anthropic
from .base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    def __init__(self, config: dict = None):
        super().__init__("ResearchAgent", config)
        self.client = anthropic.Anthropic(api_key=self.config.get("api_key"))
        self.model = self.config.get("model", "claude-sonnet-4-6")

    def run(self, query: str) -> str:
        self.log(f"Researching: {query}")
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            messages=[{"role": "user", "content": query}],
        )
        return response.content[0].text
