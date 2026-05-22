"""Reference doc for the Update smart-button server action.

The webhook server action ``Seloger: Update Listing`` is created by
``seloger/odoo/provision/smart_buttons.py::ensure_server_actions``. This
file documents the contract; it contains no runtime code.

Flow
----
1. User clicks **Update Listing**.
2. Odoo POSTs to ``$WEBHOOK_URL/update?identifier=<tenant_key>`` with the
   selected record(s).
3. ``src/handlers/update.py::handle_update``:
     a. Reads the latest template + attachments.
     b. Rebuilds the AVIV payload.
     c. Calls ``ListingService.update``, which does GET → PUT with
        ``If-Match`` and one 412 retry.
     d. Writes a chatter note.

Response codes
--------------
* 200 — update applied (traceparent + etag returned)
* 422 — validation failed (or the listing has no ``x_aviv_listing_id`` yet)
* 502 — AVIV returned an error
"""
