"""Starter set of seloger ``product.template`` fields.

These fields back the AVIV CaaS payload the seloger connector produces. They
extend the four "app" fields installed by ``properties_app.py`` (status,
flag, owner, buyer). Each label is provided in English (``en_US``) and
French (``fr_FR``); add more locales by extending the dicts here.

When the AVIV schema mapping is finalized, more ``FieldSpec`` rows should be
appended below — the rest of the provisioning pipeline picks them up
without further changes.
"""

from __future__ import annotations

from .fields import FieldSpec, SelectionOption


def _t(en: str, fr: str) -> dict[str, str]:
    """Shorthand for the en_US / fr_FR translation pair used everywhere here."""

    return {"en_US": en, "fr_FR": fr}


# ---------------------------------------------------------------------------
# Listing core
# ---------------------------------------------------------------------------
LISTING_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name="x_aviv_listing_id",
        ttype="char",
        label=_t("AVIV Listing ID", "Identifiant AVIV"),
        readonly=True,
        help=_t(
            "Identifier returned by AVIV after a successful publish. Used to "
            "match updates and archives back to the same advertisement.",
            "Identifiant retourné par AVIV après une publication réussie. "
            "Utilisé pour rattacher les mises à jour et archivages à la même annonce.",
        ),
        size=128,
    ),
    FieldSpec(
        name="x_is_published_seloger",
        ttype="boolean",
        label=_t("Published on SeLoger", "Publié sur SeLoger"),
        help=_t(
            "Reflects whether the listing is currently live on SeLoger. Updated "
            "by the webhook server after each publish/archive call.",
            "Indique si l'annonce est actuellement en ligne sur SeLoger. Mis à "
            "jour par le serveur webhook après chaque appel de publication ou d'archivage.",
        ),
    ),
    FieldSpec(
        name="x_distribution_type",
        ttype="selection",
        label=_t("Distribution Type", "Type de distribution"),
        selection=(
            SelectionOption("BUY",  _t("Sale", "Vente"),       0),
            SelectionOption("RENT", _t("Rental", "Location"),  1),
        ),
    ),
    FieldSpec(
        name="x_property_type",
        ttype="selection",
        label=_t("Property Type", "Type de bien"),
        selection=(
            SelectionOption("HOUSE",     _t("House",     "Maison"),      0),
            SelectionOption("APARTMENT", _t("Apartment", "Appartement"), 1),
            SelectionOption("OFFICE",    _t("Office",    "Bureau"),      2),
            SelectionOption("PARKING",   _t("Parking",   "Parking"),     3),
            SelectionOption("LAND",      _t("Land",      "Terrain"),     4),
        ),
    ),
)


# ---------------------------------------------------------------------------
# Address
# ---------------------------------------------------------------------------
ADDRESS_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(name="x_street",       ttype="char", label=_t("Street",        "Rue"),         size=255),
    FieldSpec(name="x_house_number", ttype="char", label=_t("House Number",  "Numéro"),      size=16),
    FieldSpec(name="x_postal_code",  ttype="char", label=_t("Postal Code",   "Code postal"), size=16),
    FieldSpec(name="x_city",         ttype="char", label=_t("City",          "Ville"),       size=128),
    FieldSpec(
        name="x_country_code",
        ttype="selection",
        label=_t("Country", "Pays"),
        selection=(
            SelectionOption("FR", _t("France",     "France"),     0),
            SelectionOption("BE", _t("Belgium",    "Belgique"),   1),
            SelectionOption("LU", _t("Luxembourg", "Luxembourg"), 2),
            SelectionOption("CH", _t("Switzerland","Suisse"),     3),
            SelectionOption("MC", _t("Monaco",     "Monaco"),     4),
        ),
    ),
)


# ---------------------------------------------------------------------------
# Surfaces & rooms
# ---------------------------------------------------------------------------
SPACE_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(name="x_living_surface", ttype="float",   label=_t("Living Surface (m²)", "Surface habitable (m²)")),
    FieldSpec(name="x_total_surface",  ttype="float",   label=_t("Total Surface (m²)",  "Surface totale (m²)")),
    FieldSpec(name="x_room_count",     ttype="integer", label=_t("Rooms",               "Nombre de pièces")),
    FieldSpec(name="x_bedroom_count",  ttype="integer", label=_t("Bedrooms",            "Chambres")),
    FieldSpec(name="x_bathroom_count", ttype="integer", label=_t("Bathrooms",           "Salles de bain")),
)


# ---------------------------------------------------------------------------
# Energy
# ---------------------------------------------------------------------------
ENERGY_FIELDS: tuple[FieldSpec, ...] = (
    FieldSpec(
        name="x_dpe_class",
        ttype="selection",
        label=_t("DPE Class", "Classe DPE"),
        selection=tuple(
            SelectionOption(letter, _t(letter, letter), idx)
            for idx, letter in enumerate("ABCDEFG")
        ),
    ),
    FieldSpec(
        name="x_ges_class",
        ttype="selection",
        label=_t("GHG Class", "Classe GES"),
        selection=tuple(
            SelectionOption(letter, _t(letter, letter), idx)
            for idx, letter in enumerate("ABCDEFG")
        ),
    ),
)


# All field groups, in installation order. Group labels are also bilingual so
# ``notebook_page.py`` can render them in either language.
#
# The hand-curated groups below cover the small set the runtime transforms
# read directly (address, prices, etc.). The auto-derived
# ``DERIVED_FIELD_GROUPS`` (generated from the AVIV OpenAPI by
# ``seloger.ops.derive_fields_from_openapi``) is concatenated after, so the
# notebook shows the full schema. The two sets currently overlap by name —
# e.g. ``x_postal_code`` (curated) and ``x_location_postalcode`` (derived).
# Deduplicate once a tenant settles on which fields they actually use.
_HAND_CURATED_GROUPS: tuple[tuple[dict[str, str], tuple[FieldSpec, ...]], ...] = (
    (_t("Listing",   "Annonce"),  LISTING_FIELDS),
    (_t("Address",   "Adresse"),  ADDRESS_FIELDS),
    (_t("Spaces",    "Surfaces"), SPACE_FIELDS),
    (_t("Energy",    "Énergie"),  ENERGY_FIELDS),
)


def _load_derived_groups() -> tuple[tuple[dict[str, str], tuple[FieldSpec, ...]], ...]:
    try:
        from .derived_field_specs import DERIVED_FIELD_GROUPS
    except ImportError:
        # The derivation script hasn't run yet — fall back to the curated set.
        return ()
    return DERIVED_FIELD_GROUPS


ALL_FIELD_GROUPS: tuple[tuple[dict[str, str], tuple[FieldSpec, ...]], ...] = (
    _HAND_CURATED_GROUPS + _load_derived_groups()
)


def all_fields() -> tuple[FieldSpec, ...]:
    return tuple(spec for _, specs in ALL_FIELD_GROUPS for spec in specs)
