from datetime import datetime

def generate_employee_id(last_id: str | None) -> str:
    """
    Format: TPYY-XXXX
    Example: TP24-0001
    """
    year = datetime.now().year % 100  # last 2 digits

    if not last_id:
        serial = 1
    else:
        try:
            last_serial = int(last_id.split("-")[1])
            serial = last_serial + 1
        except Exception:
            serial = 1

    return f"TP{year:02d}-{serial:04d}"