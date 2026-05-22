"""End-to-end happy path: POST /post drives Odoo + AVIV in concert."""

from __future__ import annotations

import json
from unittest.mock import patch

import pytest
import responses

from seloger.src.app import create_app
from seloger.src.core.tenant import AvivConfig, OdooConfig, Tenant, TenantRegistry


BASE = "https://api.aviv-group.com/sandbox/caas/v4"
TOKEN_URL = "https://auth.api.aviv-group.com/oauth/token"


class _StubRegistry(TenantRegistry):
    """A registry preloaded from memory (no tenants.json on disk)."""

    def __init__(self, tenant: Tenant):
        super().__init__(path="<memory>")
        self._tenants = {tenant.key: tenant}

    def load(self) -> None:  # pragma: no cover — intentionally no-op
        return


@pytest.fixture
def stub_registry(tenant: Tenant) -> _StubRegistry:
    return _StubRegistry(tenant)


@responses.activate
def test_publish_happy_path(stub_registry, tenant, credentials, base_template,
                             base_attachments):
    # 1) AVIV: token + POST classifieds
    responses.add(responses.POST, TOKEN_URL,
                  json={"access_token": "tok", "expires_in": 86400}, status=200)
    responses.add(responses.POST, f"{BASE}/classifieds",
                  json={"classifiedId": "cls-publish"},
                  status=202, headers={"traceparent": "00-trace-1-01"})

    app = create_app(
        credentials=credentials,
        tenant_registry=stub_registry,
        aviv_base_url=BASE,
    )

    # 2) Odoo client is stubbed at the client boundary so we don't need a live
    #    Odoo. The handler builds OdooClient.for_tenant; patch the call to
    #    inject our fake.
    fake_odoo = _FakeOdooClient(template=base_template, attachments=base_attachments)
    with patch("seloger.src.handlers._common.OdooClient.for_tenant",
               return_value=fake_odoo):
        client = app.test_client()
        resp = client.post(
            f"/post?identifier={tenant.key}",
            data=json.dumps({"records": [{"id": base_template["id"]}]}),
            content_type="application/json",
        )

    assert resp.status_code == 200, resp.data
    body = resp.get_json()
    assert body["status"] == "ok"
    assert body["classified_id"] == "cls-publish"
    # Odoo bookkeeping: the listing id and published flag were written back.
    assert fake_odoo.written == {
        "x_aviv_listing_id": "cls-publish",
        "x_is_published_seloger": True,
    }
    # Chatter was posted once.
    assert len(fake_odoo.messages) == 1
    assert "publish acknowledged" in fake_odoo.messages[0]


# ---------------------------------------------------------------------------
# Tiny Odoo fake — just enough surface for the publish handler.
# ---------------------------------------------------------------------------
class _FakeOdooClient:
    def __init__(self, *, template: dict, attachments: list[dict]):
        self.template = template
        self.attachments = attachments
        self.written: dict = {}
        self.messages: list[str] = []

    def read_template(self, template_id, fields):
        return {key: self.template.get(key) for key in fields} | {"id": template_id}

    def read_attachments(self, *, res_id, res_model="product.template",
                         fields=("id", "name", "mimetype", "checksum",
                                  "write_date", "public", "url")):
        return [{key: row.get(key) for key in fields} for row in self.attachments]

    def write_template(self, template_id, vals):
        self.written.update(vals)
        return True

    def post_message(self, template_id, body_html, *, subtype_xmlid="mail.mt_note"):
        self.messages.append(body_html)
        return True

    # search_read isn't used by /post but is part of the public surface.
    def search_read(self, *args, **kwargs):  # pragma: no cover
        return []
