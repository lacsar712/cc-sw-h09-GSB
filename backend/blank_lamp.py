"""Lamp name rules: the caller must supply a non-blank name.

Blank or whitespace-only lamp names are rejected at the edge. The system
must never substitute a name on the caller's behalf.
"""

ALLOW_BLANK = False
# Kept only as a historical constant; it must never be written to the database.
AUTO_NAME = "系统灯种"
ALLOW_DIRECT = False


def normalize_lamp(lamp: str) -> str:
    """Trim surrounding whitespace only; never fill in a blank."""
    return (lamp or "").strip()


def reject_blank(lamp: str) -> bool:
    """True when the lamp name is empty or whitespace-only."""
    return not (lamp or "").strip()


def allow_direct_blank() -> bool:
    return ALLOW_DIRECT
