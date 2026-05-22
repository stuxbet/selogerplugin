"""AVIV Classified API v4 client.

Surface:

* ``post_classified(payload)`` → ``(classified_id, traceparent)``
* ``get_classified(classified_id)`` → ``(payload, etag, traceparent)``
* ``put_classified(classified_id, payload, etag)`` → ``(traceparent,)``
* ``delete_classified(classified_id)`` → ``traceparent``
* ``list_classifieds(limit=None, next_token=None)`` → page
* ``get_statuses(classified_id)`` → status doc + traceparent

The client owns the OAuth token cache (one ``TokenCache`` per process) and
attaches the mandatory ``User-Agent`` header on every call. RFC 7807 error
bodies are decoded into ``AvivAPIError`` subclasses so callers can branch on
specific failure modes (duplicate / precondition / colliding contacts) by
type rather than parsing the message.
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import Any

import requests

from ..core.auth import AvivCredentials, TokenCache, request_token
from ..core.exceptions import (
    AvivAPIError,
    CollidingContacts,
    DuplicatedClassified,
    PreconditionFailed,
    TooManyRequests,
)


PROD_BASE_URL = "https://api.aviv-group.com/caas/v4"
SANDBOX_BASE_URL = "https://api.aviv-group.com/sandbox/caas/v4"


@dataclass
class AvivClient:
    """A request-scoped client for one ``intermediary_id``.

    Typical lifecycle: built per webhook request by the handler layer using
    ``AvivClient.for_intermediary(...)`` and discarded once the handler
    returns. The underlying ``requests.Session`` plus token cache are
    process-singletons so successive requests reuse the same TCP pool and
    AVIV-issued token.
    """

    credentials: AvivCredentials
    intermediary_id: str
    base_url: str
    token_cache: TokenCache
    session: requests.Session
    timeout: float = 60.0

    # ---- construction ------------------------------------------------
    @classmethod
    def for_intermediary(cls, *, credentials: AvivCredentials, intermediary_id: str,
                          base_url: str | None = None,
                          token_cache: TokenCache | None = None,
                          session: requests.Session | None = None,
                          timeout: float = 60.0) -> "AvivClient":
        return cls(
            credentials=credentials,
            intermediary_id=intermediary_id,
            base_url=(base_url or credentials.audience).rstrip("/"),
            token_cache=token_cache or TokenCache(),
            session=session or requests.Session(),
            timeout=timeout,
        )

    # ---- endpoints ---------------------------------------------------
    def post_classified(self, payload: dict[str, Any]) -> tuple[str, str]:
        """POST ``/classifieds``. Returns ``(classifiedId, traceparent)``."""

        response = self._call("POST", "/classifieds", json=payload)
        body = _safe_json(response)
        classified_id = str(body.get("classifiedId") or body.get("id") or "")
        if not classified_id:
            raise AvivAPIError(
                status_code=response.status_code,
                title="missing classifiedId in POST response",
                raw_body=response.text,
                traceparent=response.headers.get("traceparent", ""),
            )
        return classified_id, response.headers.get("traceparent", "")

    def get_classified(self, classified_id: str) -> tuple[dict[str, Any], str, str]:
        """GET ``/classifieds/{id}``. Returns ``(body, etag, traceparent)``."""

        response = self._call("GET", f"/classifieds/{classified_id}")
        body = _safe_json(response)
        return (
            body,
            response.headers.get("ETag", ""),
            response.headers.get("traceparent", ""),
        )

    def put_classified(self, classified_id: str, payload: dict[str, Any],
                       etag: str) -> str:
        """PUT ``/classifieds/{id}`` with ``If-Match``. Returns the traceparent.

        Raises ``PreconditionFailed`` on 412 — callers should refetch and
        retry once before failing.
        """

        headers = {"If-Match": etag} if etag else {}
        response = self._call("PUT", f"/classifieds/{classified_id}", json=payload,
                              extra_headers=headers)
        return response.headers.get("traceparent", "")

    def delete_classified(self, classified_id: str, etag: str | None = None) -> str:
        headers = {"If-Match": etag} if etag else {}
        response = self._call("DELETE", f"/classifieds/{classified_id}",
                              extra_headers=headers)
        return response.headers.get("traceparent", "")

    def list_classifieds(self, *, limit: int | None = None,
                         next_token: str | None = None) -> tuple[dict[str, Any], str]:
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if next_token:
            params["nextToken"] = next_token
        response = self._call("GET", "/classifieds", params=params)
        return _safe_json(response), response.headers.get("traceparent", "")

    def get_statuses(self, classified_id: str) -> tuple[dict[str, Any], str]:
        response = self._call("GET", f"/classifieds/{classified_id}/statuses")
        return _safe_json(response), response.headers.get("traceparent", "")

    # ---- internals ---------------------------------------------------
    def _headers(self, *, extra: dict[str, str] | None = None) -> dict[str, str]:
        token = self.token_cache.get(
            intermediary_id=self.intermediary_id,
            audience=self.credentials.audience,
            fetch=lambda: request_token(self.credentials, self.intermediary_id,
                                         session=self.session, timeout=self.timeout),
        )
        headers = {
            "Authorization": f"Bearer {token}",
            "User-Agent": self.credentials.user_agent,
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if extra:
            headers.update(extra)
        return headers

    def _call(self, method: str, path: str, *,
              json: dict[str, Any] | None = None,
              params: dict[str, Any] | None = None,
              extra_headers: dict[str, str] | None = None) -> requests.Response:
        url = f"{self.base_url}{path}"
        attempted_token_refresh = False
        while True:
            response = self.session.request(
                method,
                url,
                json=json,
                params=params,
                headers=self._headers(extra=extra_headers),
                timeout=self.timeout,
            )
            if response.status_code == 401 and not attempted_token_refresh:
                # Token may have been revoked early; force a refresh once.
                self.token_cache.invalidate(
                    intermediary_id=self.intermediary_id,
                    audience=self.credentials.audience,
                )
                attempted_token_refresh = True
                continue
            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                try:
                    retry_seconds = float(retry_after) if retry_after else 1.0
                except ValueError:
                    retry_seconds = 1.0
                time.sleep(min(retry_seconds, 30.0))
                # Re-raise as a typed error so callers can decide whether to
                # back off further (handlers currently surface as 503).
                raise _as_too_many_requests(response, retry_seconds)
            if response.status_code >= 400:
                raise _as_aviv_error(response)
            return response


# ---------------------------------------------------------------------------
# Error decoding
# ---------------------------------------------------------------------------
def _safe_json(response: requests.Response) -> dict[str, Any]:
    if not response.content:
        return {}
    try:
        return response.json()
    except json.JSONDecodeError:
        return {}


def _as_aviv_error(response: requests.Response) -> AvivAPIError:
    body = _safe_json(response)
    title = str(body.get("title") or "")
    detail = str(body.get("detail") or "")
    instance = str(body.get("instance") or "")
    errors = body.get("errors") or []
    if not isinstance(errors, list):
        errors = []
    error_source = str(body.get("errorSource") or "")
    traceparent = response.headers.get("traceparent", instance or "")

    kwargs = dict(
        status_code=response.status_code,
        title=title,
        detail=detail,
        instance=instance,
        traceparent=traceparent,
        errors=errors,
        error_source=error_source,
        raw_body=response.text,
    )

    # Named errors AVIV documents explicitly. The discriminator is the human
    # ``title`` because the ``type`` URI moves around as AVIV iterates on
    # their documentation host.
    title_lower = title.lower()
    if response.status_code == 412:
        return PreconditionFailed(**kwargs)
    if "duplicated classified" in title_lower or _has_duplicate_estate_error(errors):
        err = DuplicatedClassified(**kwargs)
        err.existing_classified_id = _extract_existing_classified_id(body, errors)
        return err
    if "colliding contacts" in title_lower:
        return CollidingContacts(**kwargs)
    return AvivAPIError(**kwargs)


def _as_too_many_requests(response: requests.Response, retry_seconds: float) -> TooManyRequests:
    body = _safe_json(response)
    err = TooManyRequests(
        status_code=429,
        title=str(body.get("title") or "Too Many Requests"),
        detail=str(body.get("detail") or ""),
        instance=str(body.get("instance") or ""),
        traceparent=response.headers.get("traceparent", ""),
        errors=body.get("errors") or [],
        error_source=str(body.get("errorSource") or ""),
        raw_body=response.text,
    )
    err.retry_after_seconds = retry_seconds
    return err


def _has_duplicate_estate_error(errors: list[dict[str, Any]]) -> bool:
    for err in errors:
        reason = str(err.get("reason", "")).lower()
        if "already" in reason and "offerer" in reason:
            return True
    return False


def _extract_existing_classified_id(body: dict[str, Any],
                                     errors: list[dict[str, Any]]) -> str | None:
    direct = body.get("existingClassifiedId") or body.get("classifiedId")
    if direct:
        return str(direct)
    for err in errors:
        # AVIV occasionally returns the existing id in ``meta``.
        meta = err.get("meta") or {}
        existing = meta.get("classifiedId") or meta.get("existingClassifiedId")
        if existing:
            return str(existing)
    return None
