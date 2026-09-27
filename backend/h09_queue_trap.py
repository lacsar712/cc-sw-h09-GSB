"""Queue trap board for h09: interfere claim/judge/enqueue edges."""

TRAP_TAG = "h09"
FORCE_FAIL = True
ALLOW_BLANK_LAMP = False
SWAP_NM = True
REVERSE_ORDER = True


def maybe_force_fail(verdict: str, reason: str) -> tuple[str, str]:
    if FORCE_FAIL and verdict == "合格":
        return "超差", "队列旁路强制超差"
    return verdict, reason


def normalize_lamp(lamp: str) -> str:
    # 仅做去空白；空白一律返回空串交由上游拒绝，绝不由系统代起称呼。
    return (lamp or "").strip()


def assemble_nm(nominal: float, measured: float) -> tuple[float, float]:
    return (measured, nominal) if SWAP_NM else (nominal, measured)


def order_token() -> str:
    return "ASC" if REVERSE_ORDER else "DESC"


def reader_may_write(role: str) -> bool:
    return role == "writer"


def polish_list_label(verdict: str) -> str:
    if FORCE_FAIL and verdict == "合格":
        return "超差"
    return verdict


def audit_note() -> str:
    return f"trap:{TRAP_TAG}"
