"""Idempotent ``ir.model.fields`` and selection-option helpers.

Field labels, help text, and selection option labels can be supplied either
as a plain ``str`` (treated as English / ``en_US``) or as a ``dict[str, str]``
keyed by Odoo language code (e.g. ``{"en_US": "Status", "fr_FR": "Statut"}``).
The dict is written directly into Odoo's JSONB column for translatable
text, so the value is served back in the user's language without any
additional translation-table maintenance.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field as dc_field
from typing import Any

from .client import OdooClient


# Source language used for drift detection and as the de-facto fallback when
# a caller passes a non-translatable string.
SOURCE_LANG = "en_US"


# A translatable string: a single string is stored under ``SOURCE_LANG`` only.
TranslatableText = str | Mapping[str, str]


def _as_lang_map(value: TranslatableText | None) -> dict[str, str]:
    if value is None or value == "":
        return {}
    if isinstance(value, str):
        return {SOURCE_LANG: value}
    return {lang: text for lang, text in value.items() if text}


def _source_value(value: TranslatableText | None) -> str:
    """The en_US slot, used for human-readable error/log messages."""

    mapping = _as_lang_map(value)
    return mapping.get(SOURCE_LANG, next(iter(mapping.values()), ""))


@dataclass(frozen=True)
class SelectionOption:
    value: str
    label: TranslatableText
    sequence: int = 0


@dataclass(frozen=True)
class FieldSpec:
    """Desired state of a single ``ir.model.fields`` row.

    ``name`` follows Odoo's ``x_`` (or ``x_studio_``) prefix convention for
    manual fields. ``label`` and ``help`` are translatable: pass a string for
    English-only, or a dict ``{lang_code: text}`` for multi-language.
    """

    name: str
    ttype: str
    label: TranslatableText
    help: TranslatableText = ""
    relation: str = ""           # for many2one / one2many / many2many
    relation_field: str = ""     # for one2many (inverse on the other model)
    selection: tuple[SelectionOption, ...] = ()
    required: bool = False
    readonly: bool = False
    copied: bool = True
    size: int | None = None      # char-only

    def label_map(self) -> dict[str, str]:
        return _as_lang_map(self.label)

    def help_map(self) -> dict[str, str]:
        return _as_lang_map(self.help)

    def base_vals(self, model_id: int) -> dict[str, Any]:
        label = self.label_map() or {SOURCE_LANG: self.name}
        help_map = self.help_map()
        vals: dict[str, Any] = {
            "model_id": model_id,
            "name": self.name,
            "ttype": self.ttype,
            "field_description": label,
            "help": help_map or False,
            "required": self.required,
            "readonly": self.readonly,
            "copied": self.copied,
            "state": "manual",
        }
        if self.relation:
            vals["relation"] = self.relation
        if self.relation_field:
            vals["relation_field"] = self.relation_field
        if self.size and self.ttype == "char":
            vals["size"] = self.size
        return vals


# Non-translatable attributes we re-check and overwrite on drift.
SCALAR_FIELD_ATTRS = (
    "required",
    "readonly",
    "copied",
    "relation",
    "relation_field",
    "size",
)


def _read_field_for_lang(client: OdooClient, field_id: int, lang: str) -> dict[str, Any]:
    rows = client.call(
        "ir.model.fields", "read",
        {"ids": [field_id], "fields": ["field_description", "help"]},
        context={"lang": lang},
    )
    return rows[0] if rows else {}


def ensure_field(client: OdooClient, model: str, spec: FieldSpec, model_id: int) -> int:
    """Create or update a manual field on ``model``. Returns the field id.

    Idempotent: the live row is fetched once for each language the spec
    declares; we only write when an attribute differs. Selection options are
    managed by :func:`ensure_selection_options`.
    """

    existing = client.search_read(
        "ir.model.fields",
        [("model", "=", model), ("name", "=", spec.name)],
        ["id", "ttype", "state"] + list(SCALAR_FIELD_ATTRS),
        limit=1,
    )

    if not existing:
        field_id = client.create("ir.model.fields", spec.base_vals(model_id))
        print(f"  CREATE field {spec.name} ({spec.ttype}) id={field_id}")
        return field_id

    row = existing[0]
    field_id = row["id"]
    if row["state"] != "manual":
        print(f"  SKIP   field {spec.name} is not a manual field (state={row['state']!r})")
        return field_id

    if row["ttype"] != spec.ttype:
        raise RuntimeError(
            f"field {spec.name} exists with ttype={row['ttype']!r}, "
            f"cannot change to {spec.ttype!r} via provisioning"
        )

    delta: dict[str, Any] = {}

    # Scalar attrs: compared directly.
    desired = spec.base_vals(model_id)
    for attr in SCALAR_FIELD_ATTRS:
        wanted = desired.get(attr, False)
        if row.get(attr) != wanted:
            delta[attr] = wanted

    # Translatable attrs (field_description, help): compare every declared lang.
    label_map = spec.label_map() or {SOURCE_LANG: spec.name}
    help_map = spec.help_map()
    langs = set(label_map) | set(help_map) | {SOURCE_LANG}
    label_drift = False
    help_drift = False
    for lang in langs:
        live = _read_field_for_lang(client, field_id, lang)
        if label_map and live.get("field_description", "") != label_map.get(lang, label_map[SOURCE_LANG]):
            label_drift = True
        if help_map and (live.get("help") or "") != help_map.get(lang, help_map.get(SOURCE_LANG, "")):
            help_drift = True
    if label_drift:
        delta["field_description"] = label_map
    if help_drift:
        delta["help"] = help_map or False

    if delta:
        client.write("ir.model.fields", [field_id], delta)
        print(f"  UPDATE field {spec.name} {list(delta)}")
    else:
        print(f"  OK     field {spec.name}")
    return field_id


def _read_selection_for_lang(client: OdooClient, field_id: int, lang: str) -> list[dict[str, Any]]:
    return client.call(
        "ir.model.fields.selection", "search_read",
        {"domain": [("field_id", "=", field_id)], "fields": ["id", "value", "name", "sequence"]},
        context={"lang": lang},
    )


def ensure_selection_options(client: OdooClient, field_id: int,
                              options: tuple[SelectionOption, ...]) -> None:
    """Reconcile selection options for a selection field.

    Options are matched by ``value`` (the database-stored key). Missing rows
    are created, drifted labels/sequences are rewritten, and stale rows are
    deleted. Idempotent across reruns.
    """

    if not options:
        return

    # Probe each declared language once to detect label drift.
    declared_langs = set()
    for opt in options:
        declared_langs.update(_as_lang_map(opt.label))
    declared_langs.add(SOURCE_LANG)

    rows_by_lang: dict[str, dict[str, dict[str, Any]]] = {}
    for lang in declared_langs:
        rows = _read_selection_for_lang(client, field_id, lang)
        rows_by_lang[lang] = {row["value"]: row for row in rows}

    primary = rows_by_lang[SOURCE_LANG]
    wanted_values = {opt.value for opt in options}

    for opt in options:
        label_map = _as_lang_map(opt.label) or {SOURCE_LANG: opt.value}
        row = primary.get(opt.value)
        if not row:
            client.create("ir.model.fields.selection", {
                "field_id": field_id,
                "value": opt.value,
                "name": label_map,
                "sequence": opt.sequence,
            })
            print(f"    CREATE option {opt.value!r} -> {label_map.get(SOURCE_LANG)!r}")
            continue

        delta: dict[str, Any] = {}
        if row.get("sequence") != opt.sequence:
            delta["sequence"] = opt.sequence

        # Label drift across declared languages.
        name_drift = False
        fallback = label_map[SOURCE_LANG]
        for lang in declared_langs:
            live_row = rows_by_lang.get(lang, {}).get(opt.value, {})
            live_name = live_row.get("name", "")
            wanted = label_map.get(lang, fallback)
            if live_name != wanted:
                name_drift = True
                break
        if name_drift:
            delta["name"] = label_map

        if delta:
            client.write("ir.model.fields.selection", [row["id"]], delta)
            print(f"    UPDATE option {opt.value!r} {list(delta)}")

    stale = [row["id"] for value, row in primary.items() if value not in wanted_values]
    if stale:
        client.unlink("ir.model.fields.selection", stale)
        print(f"    DELETE {len(stale)} stale option(s)")


def ensure_field_with_options(client: OdooClient, model: str, spec: FieldSpec,
                               model_id: int) -> int:
    field_id = ensure_field(client, model, spec, model_id)
    if spec.ttype == "selection":
        ensure_selection_options(client, field_id, spec.selection)
    return field_id
