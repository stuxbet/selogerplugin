"""Odoo -> AVIV ``energy`` block (DPE / GES grades for France).

The starter field set only carries the letter grade — when the user
provides numeric consumption (kWh/m²/yr) and CO₂ (kgCO₂/m²/yr) values via
additional Studio fields, extend ``build_energy`` to forward those onto
``EnergyClass.value`` and the appropriate type label.
"""

from __future__ import annotations

from typing import Any

from ..schema import Energy, EnergyClass


VALID_LETTERS = frozenset("ABCDEFG")


def build_energy(template: dict[str, Any]) -> Energy | None:
    dpe_letter = _letter(template.get("x_dpe_class"))
    ges_letter = _letter(template.get("x_ges_class"))
    if not (dpe_letter or ges_letter):
        return None
    return Energy(
        dpe=EnergyClass(label=dpe_letter, type="DPE") if dpe_letter else None,
        ghg=EnergyClass(label=ges_letter, type="GES") if ges_letter else None,
    )


def _letter(value: Any) -> str | None:
    if not value:
        return None
    candidate = str(value).strip().upper()
    return candidate if candidate in VALID_LETTERS else None
