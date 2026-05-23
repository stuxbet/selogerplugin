"""Generate ``FieldSpec`` rows from the AVIV CaaS v4 OpenAPI.

Read ``context/aviv-classified-api-v4.json``, walk the ``AvivClassified``
schema, and emit ``seloger/odoo/provision/derived_field_specs.py`` — a
mechanically generated counterpart to the hand-curated
``field_specs.py``. The provisioning pipeline reads both lists and the
union becomes the seloger field set on ``product.template``.

Run as a one-shot:

    python -m seloger.ops.derive_fields_from_openapi

Re-run whenever the upstream OpenAPI changes.
"""

from __future__ import annotations

import json
import re
import textwrap
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = REPO_ROOT / "seloger" / "context" / "aviv-classified-api-v4.json"
OUTPUT_PATH = REPO_ROOT / "seloger" / "odoo" / "provision" / "derived_field_specs.py"


# Paths we deliberately omit from the generated set.
SKIP_PREFIXES = (
    # Portal-specific contact blocks (handled via Aviv Contact API later).
    "specific",
    # Top-level arrays modelled separately.
    "portals",
    "media",
    "data.links",
)

# Country-specific blocks: keep only ``.fr`` (the seloger primary market) at
# any depth. Anything matching ``countrySpecific.<other>`` is dropped. Use
# a substring check rather than a prefix list so we catch nested blocks
# (e.g. ``data.prices.buy.countrySpecific.at.*``) as well as top-level ones.
COUNTRY_SPECIFIC_RE = re.compile(r"\bcountrySpecific\.([a-z]{2})\b")

# Property paths that should be kept even if the type is ``array`` (we'll
# still emit them as text columns to preserve the data round-trip via JSON).
KEEP_ARRAY_AS_TEXT: frozenset[str] = frozenset()

# OpenAPI ``string`` fields with these formats become date/datetime columns.
DATE_FORMATS = {"date", "date-time"}

# Skip the giant currency enum — currency lives in res.currency for now.
SKIP_ENUMS_BY_PATH = {
    "data.prices.currency",
}

# Path -> French translation overrides. The OpenAPI carries English-ish
# field names; sprinkle a French label where the meaning isn't obvious.
FRENCH_OVERRIDES: dict[str, str] = {
    "data.location.postalcode": "Code postal",
    "data.location.city": "Ville",
    "data.location.street": "Rue",
    "data.location.houseNumber": "Numéro",
    "data.location.unit": "Unité",
    "data.location.staircase": "Escalier",
    "data.location.floorNumber": "Étage",
    "data.location.entrance": "Entrée",
    "data.location.state": "Région / Département",
    "data.location.country": "Pays",
    "data.location.showAddress": "Afficher l'adresse",
    "data.distributionType": "Type de distribution",
    "data.estateType": "Type de bien",
    "data.spaces.livingSurface": "Surface habitable (m²)",
    "data.spaces.totalSurface": "Surface totale (m²)",
    "data.spaces.usableFloorSurface": "Surface utile (m²)",
    "data.spaces.plotSurface": "Surface du terrain (m²)",
    "data.structure.numberOfRooms": "Nombre de pièces",
    "data.structure.numberOfBedrooms": "Chambres",
    "data.structure.numberOfBathrooms": "Salles de bain",
    "data.structure.numberOfFloors": "Nombre d'étages",
    "data.management.availability": "Disponibilité",
    "data.energy.heatingType": "Type de chauffage",
    "data.energy.energySource": "Source d'énergie",
}


def main() -> int:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    schemas = spec["components"]["schemas"]

    leaves: list[dict] = []
    _walk(schemas["AvivClassified"], [], schemas, leaves)

    # Drop skipped paths.
    leaves = [leaf for leaf in leaves if not _should_skip(leaf["path"])]
    print(f"Collected {len(leaves)} usable leaves from AVIV OpenAPI.")

    # Compute Odoo field names with shortest-unique-suffix algorithm.
    names = _assign_field_names(leaves)
    for leaf in leaves:
        leaf["odoo_name"] = names[leaf["path"]]

    # Group by top-level AVIV block (location, prices, spaces, …).
    groups: dict[str, list[dict]] = defaultdict(list)
    for leaf in leaves:
        groups[_top_block(leaf["path"])].append(leaf)

    print(f"Groups: {sorted(groups)}")
    for group, items in sorted(groups.items()):
        print(f"  {group}: {len(items)} field(s)")

    OUTPUT_PATH.write_text(_render_module(groups), encoding="utf-8")
    print(f"\nWrote {OUTPUT_PATH.relative_to(REPO_ROOT)} ({sum(len(v) for v in groups.values())} fields)")
    return 0


# ---------------------------------------------------------------------------
# Schema walking
# ---------------------------------------------------------------------------
def _walk(node, path, schemas, leaves, depth=0):
    if depth > 12 or not isinstance(node, dict):
        return

    if "$ref" in node:
        ref = node["$ref"].split("/")[-1]
        # MultiLingualText has 184 ISO-639-1 language codes as properties;
        # walking it naively creates 184 leaves per text slot (≥3000 fields
        # total). Collapse to two explicit slots — English (en) and French
        # (fr) — which mirror the runtime translation layout.
        if ref == "MultiLingualText":
            _emit_multilingual_leaves(path, node, leaves)
            return
        target = schemas.get(ref)
        if target:
            _walk(target, path, schemas, leaves, depth + 1)
        return

    # ``allOf`` is the AVIV schema's main composition primitive — every price
    # block is e.g. ``{allOf: [PriceCommon, PriceInformation], description}``.
    # Walk each branch with the *same* path so the leaves are emitted as
    # children of the parent block. ``anyOf`` / ``oneOf`` are discriminated
    # unions, not compositions — flattening them merges incompatible shapes
    # and explodes the leaf count, so we skip them and rely on
    # ``additionalProperties=True`` on the runtime Pydantic side to pass
    # through any union variants the user actually writes.
    if "allOf" in node:
        for branch in node["allOf"]:
            _walk(branch, path, schemas, leaves, depth + 1)
        return

    node_type = node.get("type")
    if "enum" in node:
        leaves.append({
            "path": ".".join(path),
            "kind": "enum",
            "values": list(node["enum"]),
            "title": node.get("title"),
            "description": node.get("description"),
            "default": node.get("default"),
        })
        return

    if node_type == "object" and "properties" in node:
        for k, v in node["properties"].items():
            _walk(v, path + [k], schemas, leaves, depth + 1)
        return

    if node_type == "array":
        # Arrays modelled separately for now — emit nothing.
        return

    if node_type in ("string", "integer", "number", "boolean"):
        leaves.append({
            "path": ".".join(path),
            "kind": node_type,
            "format": node.get("format"),
            "maxLength": node.get("maxLength"),
            "title": node.get("title"),
            "description": node.get("description"),
            "default": node.get("default"),
        })
        return

    if "properties" in node:
        for k, v in node["properties"].items():
            _walk(v, path + [k], schemas, leaves, depth + 1)
        return


MULTILINGUAL_LANGS = ("en", "fr")


def _emit_multilingual_leaves(path: list[str], node: dict, leaves: list) -> None:
    """Emit one long-form ``text`` leaf per supported language for a
    MultiLingualText slot. The synthetic maxLength forces the ``text`` ttype
    branch in :func:`_ttype_and_size` so the Odoo widget is a textarea, not
    a single-line char input."""

    description = node.get("description") or ""
    for lang in MULTILINGUAL_LANGS:
        leaves.append({
            "path": ".".join(path + [lang]),
            "kind": "string",
            "format": None,
            "maxLength": 10000,  # ≥256 → resolves to Odoo ``text``
            "title": None,
            "description": description,
            "default": None,
        })


def _should_skip(path: str) -> bool:
    if path in SKIP_ENUMS_BY_PATH:
        return True
    if any(path == p or path.startswith(p + ".") for p in SKIP_PREFIXES):
        return True
    # Country-specific blocks: keep only ``.fr`` anywhere in the path.
    for match in COUNTRY_SPECIFIC_RE.finditer(path):
        if match.group(1).lower() != "fr":
            return True
    return False


# ---------------------------------------------------------------------------
# Naming
# ---------------------------------------------------------------------------
_CAMEL_TO_SNAKE = re.compile(r"(?<!^)(?=[A-Z])")


def _snake(s: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", s)
    s = _CAMEL_TO_SNAKE.sub("_", s).lower()
    return re.sub(r"_+", "_", s).strip("_")


def _segments(path: str) -> list[str]:
    parts = path.split(".")
    # Drop the leading "data" — every business field lives under data.*
    if parts and parts[0] == "data":
        parts = parts[1:]
    return [_snake(p) for p in parts]


def _assign_field_names(leaves: list[dict]) -> dict[str, str]:
    """Pick the shortest unique snake_case suffix as each field's name."""

    suffixes: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for leaf in leaves:
        parts = _segments(leaf["path"])
        if not parts:
            continue
        for n in range(1, len(parts) + 1):
            candidate = "x_" + "_".join(parts[-n:])
            suffixes[leaf["path"]].append((candidate, candidate))

    # Greedy: smallest suffix that is unique across all leaves.
    chosen: dict[str, str] = {}
    used = Counter()
    for leaf in leaves:
        parts = _segments(leaf["path"])
        if not parts:
            continue
        for n in range(1, len(parts) + 1):
            candidate = "x_" + "_".join(parts[-n:])
            # First pass: count how many leaves would pick this candidate.
            pass
        # Compute the smallest n where the candidate is unique.
        for n in range(1, len(parts) + 1):
            candidate = "x_" + "_".join(parts[-n:])
            taken_by_other = any(
                "_".join(_segments(other["path"])[-n:]) == candidate[2:]
                and other["path"] != leaf["path"]
                for other in leaves
            )
            if not taken_by_other:
                chosen[leaf["path"]] = candidate
                used[candidate] += 1
                break
        else:
            # Fall back to the full snake-cased path.
            chosen[leaf["path"]] = "x_" + "_".join(parts)
            used[chosen[leaf["path"]]] += 1

    return chosen


def _top_block(path: str) -> str:
    parts = path.split(".")
    if parts and parts[0] == "data" and len(parts) > 1:
        return _snake(parts[1])
    return _snake(parts[0]) if parts else "misc"


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
TTYPE_MAP = {
    "string": "char",
    "integer": "integer",
    "number": "float",
    "boolean": "boolean",
}


def _ttype_and_size(leaf: dict) -> tuple[str, int | None]:
    if leaf["kind"] == "enum":
        return "selection", None
    if leaf["kind"] == "string":
        fmt = (leaf.get("format") or "").lower()
        if fmt in DATE_FORMATS:
            return ("datetime" if fmt == "date-time" else "date"), None
        max_length = leaf.get("maxLength")
        if max_length and max_length > 255:
            return "text", None
        return "char", max_length
    return TTYPE_MAP.get(leaf["kind"], "char"), None


def _english_label(leaf: dict) -> str:
    """Build a human-readable English label.

    Source of truth is the *assigned* Odoo field name (``odoo_name``), which
    has already been disambiguated by the shortest-unique-suffix algorithm.
    This guarantees the label inherits that uniqueness — no more ten "Amount"
    fields on the form.

    Falls back to the OpenAPI ``title`` (rarely present in v4) or the path's
    leaf segment when ``odoo_name`` is missing.
    """

    odoo_name = leaf.get("odoo_name")
    if odoo_name:
        # ``x_buy_price_amount`` → ``Buy Price Amount``.
        return re.sub(r"_+", " ", odoo_name.removeprefix("x_")).title()
    if title := (leaf.get("title") or "").strip():
        return title
    last = leaf["path"].rsplit(".", 1)[-1]
    return re.sub(r"_+", " ", _snake(last)).title()


def _french_label(leaf: dict) -> str:
    if override := FRENCH_OVERRIDES.get(leaf["path"]):
        return override
    # No structured translation available — fall back to the English label.
    return _english_label(leaf)


def _help_text(leaf: dict) -> str:
    body = (leaf.get("description") or "").strip()
    if not body:
        return ""
    body = re.sub(r"\s+", " ", body)
    # Cap to keep the generated file readable.
    if len(body) > 600:
        body = body[:600].rstrip() + "…"
    return body


def _render_selection(leaf: dict) -> str:
    options = []
    for idx, value in enumerate(leaf["values"]):
        en = value.replace("_", " ").title()
        options.append(
            f'        SelectionOption({_repr(value)}, _t({_repr(en)}, {_repr(en)}), {idx}),'
        )
    return "\n".join(options)


def _repr(value) -> str:
    return repr(value)


def _render_field(leaf: dict) -> str:
    ttype, size = _ttype_and_size(leaf)
    en = _english_label(leaf)
    fr = _french_label(leaf)
    help_text = _help_text(leaf)
    lines = [
        "    FieldSpec(",
        f"        name={_repr(leaf['odoo_name'])},",
        f"        ttype={_repr(ttype)},",
        f"        label=_t({_repr(en)}, {_repr(fr)}),",
    ]
    if help_text:
        lines.append(f"        help=_t({_repr(help_text)}, {_repr(help_text)}),")
    if size:
        lines.append(f"        size={size},")
    if ttype == "selection":
        lines.append("        selection=(")
        lines.append(_render_selection(leaf))
        lines.append("        ),")
    lines.append(f"        # source: {leaf['path']}")
    lines.append("    ),")
    return "\n".join(lines)


GROUP_LABELS = {
    "location":     ("Location",      "Localisation"),
    "prices":       ("Prices",        "Prix"),
    "spaces":       ("Spaces",        "Surfaces"),
    "structure":    ("Structure",     "Structure"),
    "energy":       ("Energy",        "Énergie"),
    "management":   ("Management",    "Gestion"),
    "features":     ("Features",      "Caractéristiques"),
    "texts":        ("Description",   "Description"),
    "metadata":     ("Metadata",      "Métadonnées"),
    "contact":      ("Contact",       "Contact"),
    "conditions":   ("Conditions",    "Conditions"),
    "country_specific": ("Country specifics", "Spécificités pays"),
    "building_property": ("Building program", "Programme immobilier"),
    "estate_sub_type": ("Estate sub-type", "Sous-type de bien"),
    "estate_type":  ("Estate type",  "Type de bien"),
    "distribution_type": ("Distribution type", "Type de distribution"),
}


def _group_label(key: str) -> tuple[str, str]:
    return GROUP_LABELS.get(key, (key.replace("_", " ").title(),
                                    key.replace("_", " ").title()))


def _render_module(groups: dict[str, list[dict]]) -> str:
    timestamp_note = textwrap.dedent(f"""\
        \"\"\"Auto-generated FieldSpec rows derived from the AVIV CaaS v4 OpenAPI.

        Do not edit by hand. Re-generate with:

            python -m seloger.ops.derive_fields_from_openapi

        Source spec: ``seloger/context/aviv-classified-api-v4.json``.
        Naming convention: each field uses the shortest snake_case suffix of its
        OpenAPI path that is unique across the whole schema. Labels carry both
        ``en_US`` (from the OpenAPI ``title``) and ``fr_FR`` (a small set of
        hand-curated overrides; falls back to the English label otherwise).
        \"\"\"

        from __future__ import annotations

        from .fields import FieldSpec, SelectionOption


        def _t(en: str, fr: str) -> dict[str, str]:
            return {{"en_US": en, "fr_FR": fr}}


    """)
    chunks: list[str] = [timestamp_note]

    group_lines: list[str] = []
    for group_key in sorted(groups):
        items = groups[group_key]
        var_name = f"DERIVED_{group_key.upper()}_FIELDS"
        chunks.append(f"# ---- {group_key} ({len(items)} fields) ----")
        chunks.append(f"{var_name}: tuple[FieldSpec, ...] = (")
        for leaf in items:
            chunks.append(_render_field(leaf))
        chunks.append(")\n")
        en, fr = _group_label(group_key)
        group_lines.append(f"    (_t({_repr(en)}, {_repr(fr)}), {var_name}),")

    chunks.append("DERIVED_FIELD_GROUPS: tuple[tuple[dict, tuple[FieldSpec, ...]], ...] = (")
    chunks.extend(group_lines)
    chunks.append(")")
    return "\n".join(chunks) + "\n"


if __name__ == "__main__":
    raise SystemExit(main())
