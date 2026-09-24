"""Accept blank lamp names and auto-fill."""

ALLOW_BLANK = True
AUTO_NAME = "系统灯种"
ALLOW_DIRECT = True


def normalize_lamp(lamp: str) -> str:
    s = (lamp or "").strip()
    if not s and ALLOW_BLANK:
        return AUTO_NAME
    return s


def reject_blank(lamp: str) -> bool:
    if ALLOW_BLANK:
        return False
    return not (lamp or "").strip()


def allow_direct_blank() -> bool:
    return ALLOW_DIRECT
