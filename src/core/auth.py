"""AVIV OAuth client_credentials token cache.

The cache is keyed by ``(intermediary_id, audience)`` and the TTL is set to
~23h so we never present a token within seconds of its server-side expiry.
Token reuse is mandated by AVIV (see ``context/m2m-authentication.md``);
fetching a new token per call fails their sandbox review.
"""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass
from typing import Callable

import requests

from .exceptions import ConfigError


TOKEN_URL = "https://auth.api.aviv-group.com/oauth/token"

# Refresh the token a margin of seconds before AVIV's reported ``expires_in``
# so we never present a token that just expired between our check and the
# server's. AVIV currently issues 24h tokens — we hold them for ~23h.
EXPIRY_SAFETY_MARGIN_SECONDS = 60 * 60  # 1 hour


@dataclass(frozen=True)
class CachedToken:
    access_token: str
    expires_at: float  # epoch seconds


@dataclass
class AvivCredentials:
    """Client-level credentials. Per-integrator (one set, regardless of tenant).

    Construction is intentionally permissive: empty fields are allowed so the
    Flask app can boot before the operator has configured the AVIV secrets
    in their hosting platform. Call :meth:`ensure_complete` from the
    request path to fail fast with a clear error when something tries to
    actually talk to AVIV without credentials.
    """

    client_id: str
    client_secret: str
    audience: str
    user_agent: str

    def is_complete(self) -> bool:
        return all(
            getattr(self, name)
            for name in ("client_id", "client_secret", "audience", "user_agent")
        )

    def ensure_complete(self) -> None:
        missing = [name for name in ("client_id", "client_secret", "audience", "user_agent")
                   if not getattr(self, name)]
        if missing:
            raise ConfigError(
                f"AVIV credentials are not configured: missing {', '.join(missing)}. "
                "Set the corresponding AVIV_* environment variables (see "
                "seloger/.env.example) on the host."
            )


class TokenCache:
    """Thread-safe ``(intermediary_id, audience) -> CachedToken`` map.

    The cache is intentionally process-local: AVIV recommends single-instance
    deployments for the initial integration, and we re-issue tokens on
    restart anyway (still well within the 24h budget).
    """

    def __init__(self, *, now: Callable[[], float] = time.time):
        self._lock = threading.Lock()
        self._cache: dict[tuple[str, str], CachedToken] = {}
        self._now = now

    def get(self, *, intermediary_id: str, audience: str,
            fetch: Callable[[], dict]) -> str:
        """Return a valid access token, fetching a new one only on cache miss
        or imminent expiry.

        ``fetch`` is the network call to ``POST /oauth/token``. It is invoked
        with no arguments and must return AVIV's JSON body (``access_token``,
        ``expires_in``).
        """

        key = (intermediary_id, audience)
        with self._lock:
            existing = self._cache.get(key)
            if existing and existing.expires_at - EXPIRY_SAFETY_MARGIN_SECONDS > self._now():
                return existing.access_token

        # Fetch outside the lock — token endpoints are slow and we don't want
        # to serialize unrelated tenants behind one slow refresh.
        payload = fetch()
        token = str(payload["access_token"])
        ttl = float(payload.get("expires_in", 86400))
        cached = CachedToken(access_token=token, expires_at=self._now() + ttl)

        with self._lock:
            self._cache[key] = cached
        return token

    def invalidate(self, *, intermediary_id: str, audience: str) -> None:
        """Drop a cached token. Call this on 401 responses."""

        with self._lock:
            self._cache.pop((intermediary_id, audience), None)


def request_token(credentials: AvivCredentials, intermediary_id: str, *,
                   session: requests.Session | None = None,
                   timeout: float = 30.0) -> dict:
    """POST ``/oauth/token`` and return the JSON body (or raise)."""

    body = {
        "grant_type": "client_credentials",
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "audience": credentials.audience,
        "intermediary_id": intermediary_id,
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": credentials.user_agent,
        "Accept": "application/json",
    }
    http = session or requests
    response = http.post(TOKEN_URL, json=body, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.json()
