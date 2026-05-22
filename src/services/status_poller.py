"""Background polling of ``/classifieds/{id}/statuses``.

Used as a fallback when AVIV's outbound webhook hasn't arrived (or when the
webhook delivery semantics are still TBD with AVIV). A single background
thread iterates pending listings, calls AVIV, posts the result back into
the Odoo chatter via the chatter formatters, and clears the pending entry
once the status is terminal.

This is intentionally simple — one thread, in-memory queue, no persistence
across restarts. Restarting the Flask app re-loads pending IDs from Odoo
(any product.template with ``x_aviv_listing_id`` set + non-terminal
``x_last_status``).
"""

from __future__ import annotations

import logging
import threading
import time
from collections import deque
from dataclasses import dataclass
from typing import Callable

from ..clients.aviv import AvivClient
from ..clients.odoo import OdooClient
from ..core.exceptions import AvivAPIError
from ..core.tenant import Tenant
from ..schema import ClassifiedStatus


log = logging.getLogger("seloger.status_poller")


TERMINAL_STATES: frozenset[str] = frozenset({
    "ONLINE",
    "OFFLINE",
    "REJECTED",
    "DELETED",
})


@dataclass
class _PollingTask:
    template_id: int
    classified_id: str
    next_poll_at: float
    attempts: int = 0


class StatusPoller:
    """Single-threaded polling loop. ``start()`` is idempotent."""

    def __init__(
        self,
        *,
        aviv_factory: Callable[[Tenant], AvivClient],
        odoo_factory: Callable[[Tenant], OdooClient],
        notify: Callable[[Tenant, OdooClient, int, ClassifiedStatus], None],
        poll_interval_seconds: float = 30.0,
        max_attempts: int = 60,
    ) -> None:
        self._aviv_factory = aviv_factory
        self._odoo_factory = odoo_factory
        self._notify = notify
        self._interval = poll_interval_seconds
        self._max_attempts = max_attempts
        self._queue: deque[tuple[Tenant, _PollingTask]] = deque()
        self._lock = threading.Lock()
        self._thread: threading.Thread | None = None
        self._stopping = threading.Event()

    # ---- public API --------------------------------------------------
    def enqueue(self, tenant: Tenant, *, template_id: int, classified_id: str) -> None:
        task = _PollingTask(
            template_id=template_id,
            classified_id=classified_id,
            next_poll_at=time.time() + self._interval,
        )
        with self._lock:
            self._queue.append((tenant, task))

    def start(self) -> None:
        with self._lock:
            if self._thread and self._thread.is_alive():
                return
            self._stopping.clear()
            self._thread = threading.Thread(
                target=self._loop, name="seloger-status-poller", daemon=True
            )
            self._thread.start()

    def stop(self) -> None:
        self._stopping.set()
        if self._thread:
            self._thread.join(timeout=5)
            self._thread = None

    # ---- loop body ---------------------------------------------------
    def _loop(self) -> None:
        log.info("status poller thread started")
        while not self._stopping.is_set():
            try:
                self._tick()
            except Exception:  # pragma: no cover — defensive; loop must not die
                log.exception("status poller tick crashed")
            self._stopping.wait(self._interval)
        log.info("status poller thread stopped")

    def _tick(self) -> None:
        now = time.time()
        due: list[tuple[Tenant, _PollingTask]] = []
        with self._lock:
            remaining: deque[tuple[Tenant, _PollingTask]] = deque()
            while self._queue:
                tenant, task = self._queue.popleft()
                if task.next_poll_at <= now:
                    due.append((tenant, task))
                else:
                    remaining.append((tenant, task))
            self._queue = remaining

        for tenant, task in due:
            self._poll_one(tenant, task)

    def _poll_one(self, tenant: Tenant, task: _PollingTask) -> None:
        aviv = self._aviv_factory(tenant)
        try:
            body, traceparent = aviv.get_statuses(task.classified_id)
        except AvivAPIError as exc:
            log.warning("poller: AVIV %s for classified=%s: %s",
                        exc.status_code, task.classified_id, exc)
            self._maybe_requeue(tenant, task)
            return

        status_doc = ClassifiedStatus.model_validate(body)
        status = str(status_doc.status or "").upper()
        odoo = self._odoo_factory(tenant)
        try:
            self._notify(tenant, odoo, task.template_id, status_doc)
        except Exception:  # pragma: no cover — chatter is best-effort
            log.exception("poller: failed to write status chatter")

        if status not in TERMINAL_STATES:
            self._maybe_requeue(tenant, task)

    def _maybe_requeue(self, tenant: Tenant, task: _PollingTask) -> None:
        task.attempts += 1
        if task.attempts >= self._max_attempts:
            log.warning("poller: dropping classified=%s after %d attempts",
                        task.classified_id, task.attempts)
            return
        task.next_poll_at = time.time() + self._interval
        with self._lock:
            self._queue.append((tenant, task))
