"""Odoo JSON/2 client used by the runtime (not the provisioning scripts).

This client is tenant-scoped (one instance per tenant per request) so each
request reads from the agency's own database. It exposes only the methods
the handlers actually need:

* ``read_template(template_id)`` — fetch the full ``product.template`` row
* ``read_attachments(domain)`` — fetch image / document binaries by domain
* ``post_message(template_id, body_html)`` — write a chatter message
* ``write_template(template_id, vals)`` — bookkeeping writes (etag,
  classified id, traceparent, last-status)

It deliberately overlaps in spirit with ``odoo/provision/client.py`` but
stays independent so the provisioning package can be reorganized without
breaking the runtime.
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import Any, Iterable

import requests

from ..core.tenant import OdooConfig


class OdooClientError(RuntimeError):
    def __init__(self, model: str, method: str, status: int, body: str):
        self.model = model
        self.method = method
        self.status = status
        self.body = body
        super().__init__(f"{model}/{method} failed with {status}: {body[:200]}")


@dataclass
class OdooClient:
    config: OdooConfig
    session: requests.Session
    timeout: float = 60.0
    retries: int = 3

    @classmethod
    def for_tenant(cls, config: OdooConfig, *, session: requests.Session | None = None,
                   timeout: float = 60.0) -> "OdooClient":
        return cls(config=config, session=session or requests.Session(), timeout=timeout)

    # ---- generic ORM RPC --------------------------------------------------
    def call(self, model: str, method: str, payload: dict[str, Any] | None = None,
             context: dict[str, Any] | None = None) -> Any:
        url = f"{self.config.base_url}/json/2/{model}/{method}"
        body = dict(payload or {})
        if context:
            body["context"] = context
        headers = {
            "Authorization": f"bearer {self.config.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Odoo-Database": self.config.database,
            "User-Agent": "seloger-connector/1.0",
        }
        backoff = 1.0
        for attempt in range(1, max(1, self.retries) + 1):
            response = self.session.post(url, json=body, headers=headers, timeout=self.timeout)
            if response.status_code < 500 or attempt == self.retries:
                break
            time.sleep(backoff)
            backoff *= 2
        if not response.ok:
            raise OdooClientError(model, method, response.status_code, response.text)
        return response.json() if response.content else None

    def search_read(self, model: str, domain: list, fields: list[str],
                    limit: int | None = None) -> list[dict[str, Any]]:
        payload: dict[str, Any] = {"domain": domain, "fields": fields}
        if limit:
            payload["limit"] = limit
        return self.call(model, "search_read", payload)

    def read(self, model: str, ids: Iterable[int], fields: list[str]) -> list[dict[str, Any]]:
        return self.call(model, "read", {"ids": list(ids), "fields": fields})

    def write(self, model: str, ids: Iterable[int], vals: dict[str, Any]) -> bool:
        return self.call(model, "write", {"ids": list(ids), "vals": vals})

    # ---- listing-specific helpers ----------------------------------------
    def read_template(self, template_id: int, fields: list[str]) -> dict[str, Any]:
        """Fetch one product.template row. Raises if it doesn't exist."""

        rows = self.read("product.template", [template_id], fields)
        if not rows:
            raise OdooClientError("product.template", "read", 404,
                                  f"template id={template_id} not found")
        return rows[0]

    def read_attachments(self, *, res_id: int, res_model: str = "product.template",
                         fields: tuple[str, ...] = (
                             "id", "name", "mimetype", "checksum",
                             "write_date", "public", "url",
                         )) -> list[dict[str, Any]]:
        """Return ir.attachment rows pinned to a given product.template id.

        We use this for the media diff: each attachment's ``write_date`` is
        baked into the AVIV media URL as a ``?ts=`` query param so AVIV
        re-downloads only when the asset changed.
        """

        domain = [("res_model", "=", res_model), ("res_id", "=", res_id)]
        return self.search_read("ir.attachment", domain, list(fields))

    def post_message(self, template_id: int, body_html: str,
                     *, subtype_xmlid: str = "mail.mt_note") -> int:
        """Write a chatter note on a product.template.

        ``mt_note`` is the internal-only subtype — chatter visible to all
        agency users but not pushed to subscribed followers as email.
        """

        return self.call(
            "product.template",
            "message_post",
            {
                "ids": [template_id],
                "body": body_html,
                "subtype_xmlid": subtype_xmlid,
            },
        )

    def write_template(self, template_id: int, vals: dict[str, Any]) -> bool:
        return self.write("product.template", [template_id], vals)
