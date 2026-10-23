"""Core payment logic."""

import uuid


def capture_payment(amount: int, currency: str = "USD") -> str:
    if amount <= 0:
        raise ValueError("amount must be positive")
    payment_id = f"pay_{uuid.uuid4().hex}"
    # In production this would call the PSP and persist the record.
    return payment_id


def refund_payment(payment_id: str) -> str:
    if not payment_id:
        raise ValueError("payment_id is required")
    return f"ref_{uuid.uuid4().hex}"
