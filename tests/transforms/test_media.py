from __future__ import annotations

from seloger.src.transforms.media import build_media


def test_first_image_is_cover(base_attachments):
    media = build_media(base_attachments, public_base_url="https://example.odoo.com")
    assert media[0].category == "COVER_PICTURE"
    assert media[1].category == "INDOOR"


def test_write_date_appended_as_ts_query_param(base_attachments):
    media = build_media(base_attachments, public_base_url="https://example.odoo.com")
    assert "ts=2026-04-10T09" in media[0].url
    assert media[0].url.startswith("https://example.odoo.com/web/image/1")


def test_non_image_attachments_skipped():
    attachments = [
        {"id": 5, "name": "deed.pdf", "mimetype": "application/pdf",
         "write_date": "2026-04-10 09:00:00", "public": True, "url": False},
    ]
    assert build_media(attachments, public_base_url="https://example.odoo.com") == []


def test_attachment_with_explicit_url_passes_through_with_timestamp():
    attachments = [{
        "id": 1, "name": "ext.jpg", "mimetype": "image/jpeg",
        "url": "https://cdn.example.com/photo.jpg",
        "write_date": "2026-04-10 09:00:00", "public": True,
    }]
    media = build_media(attachments, public_base_url="https://example.odoo.com")
    assert media[0].url.startswith("https://cdn.example.com/photo.jpg?ts=")
