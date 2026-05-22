"""Reference doc for the Delete smart-button server action.

Created by ``seloger/odoo/provision/smart_buttons.py`` as the webhook
server action ``Seloger: Delete Listing``. This file documents the
contract; it has no runtime code.

Flow
----
1. User clicks **Delete Listing**.
2. Odoo POSTs to ``$WEBHOOK_URL/delete?identifier=<tenant_key>``.
3. ``src/handlers/delete.py::handle_delete`` calls
   ``ListingService.delete``, which:
     a. Best-effort GETs the current ETag.
     b. Calls ``DELETE /classifieds/{id}`` on AVIV (with ``If-Match`` when
        the GET succeeded).
     c. Clears ``x_aviv_listing_id`` and ``x_is_published_seloger`` on the
        Odoo product.template.
     d. Posts a chatter note.

This is irreversible from the Odoo side: the AVIV classified is gone, and
republishing creates a brand-new ``classifiedId`` (with whatever
re-indexing delay AVIV imposes). Use ``/archive`` if you only want to
hide the listing temporarily.
"""
