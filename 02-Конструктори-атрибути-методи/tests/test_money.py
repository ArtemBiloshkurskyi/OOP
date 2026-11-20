import pytest

from money import Money


def test_str_format():
    assert str(Money(1250)) == "12.50 грн"
    assert str(Money(5)) == "0.05 грн"
    assert str(Money(0)) == "0.00 грн"


def test_from_float_and_to_float():
    assert Money.from_float(12.5).kopecks == 1250
    assert Money(1250).to_float() == pytest.approx(12.5)


def test_from_string():
    assert Money.from_string("12.50").kopecks == 1250
    assert Money.from_string("0.10").kopecks == 10


@pytest.mark.parametrize("text", ["abc", "", "nan", "inf"])
def test_invalid_string_raises_error(text):
    with pytest.raises(ValueError):
        Money.from_string(text)


def test_invalid_kopecks_raise_error():
    with pytest.raises(ValueError):
        Money(-1)
    with pytest.raises(TypeError):
        Money(1.5)
