"""Reject blank lamp names; the system must never invent one."""

ALLOW_BLANK = False
ALLOW_DIRECT = False


def normalize_lamp(lamp: str) -> str:
    # 仅去空白；空白返回空串交由上游当场退回，绝不代起称呼。
    return (lamp or "").strip()


def reject_blank(lamp: str) -> bool:
    return not (lamp or "").strip()


def allow_direct_blank() -> bool:
    return ALLOW_DIRECT
