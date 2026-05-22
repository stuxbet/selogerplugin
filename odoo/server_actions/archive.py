"""Reference doc for the Archive smart-button server action.

Created by ``seloger/odoo/provision/smart_buttons.py`` as the webhook
server action ``Seloger: Archive Listing``. This file documents what
happens when the button is clicked; it has no runtime code.

Flow
----
1. User clicks **Archive Listing**.
2. Odoo POSTs to ``$WEBHOOK_URL/archive?identifier=<tenant_key>``.
3. ``src/handlers/archive.py::handle_archive`` calls
   ``ListingService.archive``, which:
     a. Forces ``management.availability=OFF_MARKET`` on the AVIV payload.
     b. Does GET → PUT with ``If-Match`` (one 412 retry).
     c. Writes ``x_is_published_seloger=False`` back to Odoo.
     d. Posts a chatter note.

Use this when the listing should be hidden from portals temporarily; the
AVIV classified itself stays in place so the next ``/update`` (or another
``/post``) republishes it.
"""
