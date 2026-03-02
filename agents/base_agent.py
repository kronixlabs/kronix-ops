"""
Base agent class for Kronix AI automation agents.
All agents should inherit from BaseAgent.
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    def __init__(self, name: str, config: dict = None):
        self.name = name
        self.config = config or {}

    @abstractmethod
    def run(self, input: Any) -> Any:
        """Execute the agent's primary task."""
        ...

    def log(self, message: str):
        print(f"[{self.name}] {message}")
