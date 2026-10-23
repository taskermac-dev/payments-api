import pytest

from app.payments import capture_payment, refund_payment


def test_capture_payment_returns_id():
    payment_id = capture_payment(1000, "USD")
    assert payment_id.startswith("pay_")


def test_capture_payment_rejects_non_positive_amount():
    with pytest.raises(ValueError):
        capture_payment(0)


def test_refund_requires_payment_id():
    with pytest.raises(ValueError):
        refund_payment("")
