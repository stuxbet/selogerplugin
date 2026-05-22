from __future__ import annotations

import pytest
import responses

from seloger.src.clients.aviv import AvivClient
from seloger.src.core.auth import TokenCache
from seloger.src.core.exceptions import (
    AvivAPIError,
    DuplicatedClassified,
    PreconditionFailed,
)


BASE = "https://api.aviv-group.com/sandbox/caas/v4"
TOKEN_URL = "https://auth.api.aviv-group.com/oauth/token"


def _stub_token():
    responses.add(
        responses.POST, TOKEN_URL,
        json={"access_token": "fake-token", "expires_in": 86400},
        status=200,
    )


@responses.activate
def test_post_classified_returns_id_and_traceparent(credentials, token_cache):
    _stub_token()
    responses.add(
        responses.POST, f"{BASE}/classifieds",
        json={"classifiedId": "cls-1"},
        status=202,
        headers={"traceparent": "00-trace-abc-01"},
    )
    client = AvivClient.for_intermediary(
        credentials=credentials, intermediary_id="im-1",
        base_url=BASE, token_cache=token_cache,
    )
    classified_id, traceparent = client.post_classified({"portals": ["SL"]})
    assert classified_id == "cls-1"
    assert traceparent == "00-trace-abc-01"


@responses.activate
def test_get_returns_etag(credentials, token_cache):
    _stub_token()
    responses.add(
        responses.GET, f"{BASE}/classifieds/cls-1",
        json={"data": {"distributionType": "BUY"}},
        status=200,
        headers={"ETag": "W/\"abc123\"", "traceparent": "tp"},
    )
    client = AvivClient.for_intermediary(
        credentials=credentials, intermediary_id="im-1",
        base_url=BASE, token_cache=token_cache,
    )
    body, etag, tp = client.get_classified("cls-1")
    assert body["data"]["distributionType"] == "BUY"
    assert etag == 'W/"abc123"'
    assert tp == "tp"


@responses.activate
def test_412_is_precondition_failed(credentials, token_cache):
    _stub_token()
    responses.add(
        responses.PUT, f"{BASE}/classifieds/cls-1",
        json={"title": "Precondition Failed", "detail": "stale etag"},
        status=412,
    )
    client = AvivClient.for_intermediary(
        credentials=credentials, intermediary_id="im-1",
        base_url=BASE, token_cache=token_cache,
    )
    with pytest.raises(PreconditionFailed):
        client.put_classified("cls-1", {}, etag='W/"stale"')


@responses.activate
def test_400_duplicated_classified_decoded(credentials, token_cache):
    _stub_token()
    responses.add(
        responses.POST, f"{BASE}/classifieds",
        json={
            "title": "Duplicated Classified",
            "detail": "offererEstateId already used",
            "errors": [{"name": "/data/metaData/source/offererEstateId",
                        "reason": "already exists for offerer foo",
                        "meta": {"classifiedId": "cls-existing"}}],
        },
        status=400,
    )
    client = AvivClient.for_intermediary(
        credentials=credentials, intermediary_id="im-1",
        base_url=BASE, token_cache=token_cache,
    )
    with pytest.raises(DuplicatedClassified) as excinfo:
        client.post_classified({"portals": ["SL"]})
    assert excinfo.value.existing_classified_id == "cls-existing"


@responses.activate
def test_token_is_cached(credentials, token_cache):
    _stub_token()
    responses.add(
        responses.GET, f"{BASE}/classifieds/cls-1",
        json={}, status=200, headers={"ETag": "x"},
    )
    responses.add(
        responses.GET, f"{BASE}/classifieds/cls-2",
        json={}, status=200, headers={"ETag": "y"},
    )
    client = AvivClient.for_intermediary(
        credentials=credentials, intermediary_id="im-1",
        base_url=BASE, token_cache=token_cache,
    )
    client.get_classified("cls-1")
    client.get_classified("cls-2")
    token_calls = [r for r in responses.calls if TOKEN_URL in r.request.url]
    assert len(token_calls) == 1  # token reuse contract enforced
