import pytest

from temperature import Temperature


def test_from_fahrenheit_and_back():
    temperature = Temperature.from_fahrenheit(212)
    assert temperature.celsius == pytest.approx(100)
    assert temperature.to_fahrenheit() == pytest.approx(212)


def test_from_kelvin():
    assert Temperature.from_kelvin(273.15).celsius == pytest.approx(0)


def test_is_valid_on_boundary():
    assert Temperature.is_valid(-273.15)
    assert not Temperature.is_valid(-273.16)


def test_below_absolute_zero_raises_error():
    with pytest.raises(ValueError):
        Temperature(-300)
    with pytest.raises(ValueError):
        Temperature.from_kelvin(-1)
