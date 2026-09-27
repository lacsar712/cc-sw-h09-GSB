"""Queue edge for h09: claim/judge/enqueue.

Lamp names are trimmed but never invented, nominal/measured keep their
order, verdicts come from the real domain rules, and only writers submit.
"""

TRAP_TAG = "h09"
FORCE_FAIL = False
ALLOW_BLANK_LAMP = False
# Historical constant only; must never be written to the database.
AUTO_LAMP = "系统灯种"
SWAP_NM = False
REVERSE_ORDER = False


def maybe_force_fail(verdict: str, reason: str) -> tuple[str, str]:
    return verdict, reason


def normalize_lamp(lamp: str) -> str:
    """Trim surrounding whitespace only; never substitute a name."""
    return (lamp or "").strip()


def assemble_nm(nominal: float, measured: float) -> tuple[float, float]:
    return (nominal, measured) if not SWAP_NM else (measured, nominal)


def order_token() -> str:
    return "DESC" if not REVERSE_ORDER else "ASC"


def reader_may_write(role: str) -> bool:
    return role == "writer"


def polish_list_label(verdict: str) -> str:
    return verdict


def audit_note() -> str:
    return f"trap:{TRAP_TAG}"
