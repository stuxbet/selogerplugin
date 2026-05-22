"""Environment loading for the provisioning entry points.

The provisioning scripts read Odoo credentials and the webhook base URL from
the same ``.env`` file the runtime server uses. We do not depend on
``python-dotenv`` so the provisioning package stays installable without dev
extras.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DOTENV = REPO_ROOT / "seloger" / ".env"


def load_dotenv(path: Path | str | None = None) -> None:
    """Populate ``os.environ`` from a ``KEY=VALUE`` file.

    Existing environment variables win, so callers can override the .env by
    exporting the variable in their shell.
    """

    candidate = Path(path) if path else DEFAULT_DOTENV
    if not candidate.is_file():
        return
    for raw in candidate.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


@dataclass(frozen=True)
class OdooEnv:
    base_url: str
    api_key: str
    database: str
    webhook_url: str
    webhook_identifier: str
    request_timeout: float
    request_retries: int


def _require(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(
            f"{name} is required for provisioning; set it in seloger/.env or the shell"
        )
    return value


def odoo_env() -> OdooEnv:
    """Materialize the environment block the provisioning helpers consume.

    ``load_dotenv`` is called here so a single ``odoo_env()`` call in a CLI
    is enough to wire everything up. ``WEBHOOK_URL`` and
    ``WEBHOOK_IDENTIFIER`` are optional during pre-provisioning — the
    Properties app itself does not need them — but ``provision_database``
    will check them before creating server actions.
    """

    load_dotenv()
    return OdooEnv(
        base_url=_require("ODOO_BASE_URL").rstrip("/"),
        api_key=_require("ODOO_API_KEY"),
        database=_require("ODOO_DATABASE"),
        webhook_url=os.environ.get("WEBHOOK_URL", "").strip().rstrip("/"),
        webhook_identifier=os.environ.get("WEBHOOK_IDENTIFIER", "").strip(),
        request_timeout=float(os.environ.get("ODOO_REQUEST_TIMEOUT", "60")),
        request_retries=int(os.environ.get("ODOO_REQUEST_RETRIES", "3")),
    )
