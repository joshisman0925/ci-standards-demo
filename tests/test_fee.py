import pytest

from calc.fee import parking_fee


def test_zero_minutes_is_free():
    assert parking_fee(0) == 0


def test_partial_hour_rounds_up():
    assert parking_fee(61) == 60


def test_daily_cap():
    assert parking_fee(24 * 60) == 300


def test_negative_minutes_rejected():
    with pytest.raises(ValueError):
        parking_fee(-1)


def test_member_discount():
    from calc.fee import member_fee

    assert member_fee(120) == 48
