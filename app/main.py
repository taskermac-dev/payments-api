"""Payments service entrypoint."""

from fastapi import FastAPI

from app.payments import capture_payment, refund_payment

app = FastAPI(title="payments-api")


@app.post("/payments")
def create_payment(amount: int, currency: str = "USD") -> dict:
    payment_id = capture_payment(amount, currency)
    return {"payment_id": payment_id, "status": "captured"}


@app.post("/payments/{payment_id}/refund")
def refund(payment_id: str) -> dict:
    refund_id = refund_payment(payment_id)
    return {"refund_id": refund_id, "status": "refunded"}
