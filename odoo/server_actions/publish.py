"""Reference doc for the Publish smart-button server action.

The action itself is created by
``seloger/odoo/provision/smart_buttons.py::ensure_server_actions`` (with
``state='webhook'``), so this file holds no executable code that runs inside
Odoo — it exists as the single source of truth for what the button does.

Wire diagram
------------
1. User clicks **Post Listing** in the product.template form header.
2. Odoo fires the webhook server action ``Seloger: Post Listing``
   (``binding_type='action'``, ``state='webhook'``).
3. Odoo POSTs JSON ``{"records": [{"id": ..., "name": ...}]}`` to
   ``$WEBHOOK_URL/post?identifier=<tenant_key>``.
4. The Flask app's ``/post`` route runs
   ``src/handlers/publish.py::handle_post``, which:
     a. Resolves the tenant via the ``identifier`` query param.
     b. Reads the product.template and its attachments from Odoo.
     c. Builds an AVIV ``Classified`` via ``src/transforms``.
     d. Runs per-portal validators.
     e. POSTs to ``/classifieds`` on AVIV; on Duplicated Classified, falls
        back to GET → PUT.
     f. Writes ``x_aviv_listing_id`` + ``x_is_published_seloger`` back to
        the product.template.
     g. Posts a chatter note summarizing the result.

Response codes
--------------
* 200 — listing accepted by AVIV (classifiedId returned)
* 422 — pre-flight validation failed (no AVIV call made)
* 502 — AVIV returned an error (status mirrored in the body)
* 404 — unknown tenant identifier
"""
