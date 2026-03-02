"""
Simple HTTP tool for making authenticated API requests.
"""

import httpx
from typing import Any


class HTTPTool:
    def __init__(self, base_url: str, headers: dict = None, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}
        self.timeout = timeout

    def get(self, path: str, params: dict = None) -> Any:
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = httpx.get(url, headers=self.headers, params=params, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def post(self, path: str, payload: dict = None) -> Any:
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = httpx.post(url, headers=self.headers, json=payload, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
