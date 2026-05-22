"""Thin JSON/2 RPC client used by every provisioning helper.

The Odoo JSON/2 endpoint exposes ``/json/2/<model>/<method>`` and accepts a
JSON body whose top-level keys mirror the kwargs of the underlying ORM
method. The client intentionally stays small — the provisioning helpers add
all the idempotency logic on top.
"""

from __future__ import annotations

import json
import time
from typing import Any, Iterable

import requests

from .env import OdooEnv


class OdooAPIError(RuntimeError):
    def __init__(self, model: str, method: str, status_code: int, response_text: str):
        self.model = model
        self.method = method
        self.status_code = status_code
        self.response_text = response_text
        payload = self._parse(response_text)
        self.payload = payload
        super().__init__(f"{model}/{method} failed with {status_code}: {self._summary()}")

    @staticmethod
    def _parse(text: str) -> dict[str, Any] | None:
        try:
            value = json.loads(text)
        except ValueError:
            return None
        return value if isinstance(value, dict) else None

    def _summary(self) -> str:
        if isinstance(self.payload, dict):
            parts = [str(self.payload[key]) for key in ("name", "message") if self.payload.get(key)]
            if parts:
                return " | ".join(parts)
        return self.response_text[:200].strip() or "unknown Odoo error"


class OdooClient:
    """Synchronous JSON/2 client with retry on 5xx."""

    def __init__(self, env: OdooEnv):
        self.env = env
        self._session = requests.Session()

    # ------------------------------------------------------------------
    # Low-level
    # ------------------------------------------------------------------
    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"bearer {self.env.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Odoo-Database": self.env.database,
            "User-Agent": "seloger-provision/1.0",
        }

    def call(self, model: str, method: str, payload: dict[str, Any] | None = None,
             context: dict[str, Any] | None = None) -> Any:
        url = f"{self.env.base_url}/json/2/{model}/{method}"
        body = dict(payload or {})
        if context:
            body["context"] = context

        attempts = max(1, self.env.request_retries)
        backoff = 1.0
        for attempt in range(1, attempts + 1):
            response = self._session.post(
                url,
                headers=self._headers(),
                json=body,
                timeout=self.env.request_timeout,
            )
            if response.status_code < 500 or attempt == attempts:
                break
            time.sleep(backoff)
            backoff *= 2

        if not response.ok:
            raise OdooAPIError(model, method, response.status_code, response.text)
        if not response.content:
            return None
        return response.json()

    # ------------------------------------------------------------------
    # ORM helpers
    # ------------------------------------------------------------------
    def search_read(self, model: str, domain: list, fields: list[str],
                    limit: int | None = None) -> list[dict[str, Any]]:
        payload: dict[str, Any] = {"domain": domain, "fields": fields}
        # The JSON/2 endpoint treats ``limit=0`` literally (zero rows), unlike
        # the classic XML-RPC ORM where 0 means "no limit". Map falsy limits
        # back to "no limit" so callers can use ``limit=0`` (and ``None``)
        # interchangeably to mean "fetch everything".
        if limit:
            payload["limit"] = limit
        return self.call(model, "search_read", payload)

    def search(self, model: str, domain: list, limit: int | None = None) -> list[int]:
        payload: dict[str, Any] = {"domain": domain}
        if limit:
            payload["limit"] = limit
        return self.call(model, "search", payload)

    def read(self, model: str, ids: Iterable[int], fields: list[str]) -> list[dict[str, Any]]:
        return self.call(model, "read", {"ids": list(ids), "fields": fields})

    def create(self, model: str, vals: dict[str, Any]) -> int:
        result = self.call(model, "create", {"vals_list": [vals]})
        if isinstance(result, list) and result and isinstance(result[0], int):
            return result[0]
        if isinstance(result, int):
            return result
        raise OdooAPIError(model, "create", 200, json.dumps(result))

    def write(self, model: str, ids: Iterable[int], vals: dict[str, Any]) -> bool:
        return self.call(model, "write", {"ids": list(ids), "vals": vals})

    def unlink(self, model: str, ids: Iterable[int]) -> bool:
        return self.call(model, "unlink", {"ids": list(ids)})

    # ------------------------------------------------------------------
    # Common lookups (used in many places)
    # ------------------------------------------------------------------
    def get_model_id(self, model_name: str) -> int:
        rows = self.search_read("ir.model", [("model", "=", model_name)], ["id"], limit=1)
        if not rows:
            raise RuntimeError(f"Odoo model {model_name!r} not found")
        return rows[0]["id"]
