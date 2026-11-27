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


def test_custom_rate_formula():
    from calc.fee import custom_rate_fee

    assert custom_rate_fee(90, "minutes // 30 * 20") == 60


@pytest.mark.parametrize(
    "formula",
    [
        "__import__('os').system('echo pwned')",
        "minutes.__class__",
        "open('x')",
        "minutes ** 1000000",
        "1.5 * minutes",
        "minutes /",
    ],
)
def test_custom_rate_rejects_unsafe_formula(formula):
    from calc.fee import custom_rate_fee

    with pytest.raises(ValueError):
        custom_rate_fee(90, formula)
