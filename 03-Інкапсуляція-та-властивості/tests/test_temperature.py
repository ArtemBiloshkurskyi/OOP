import pytest

from temperature import Temperature


def test_celsius_can_be_read_and_changed():
    temperature = Temperature(20)
    temperature.celsius = 30
    assert temperature.celsius == 30


def test_fahrenheit_is_computed_from_celsius():
    assert Temperature(100).fahrenheit == pytest.approx(212)
    assert Temperature(0).fahrenheit == pytest.approx(32)


def test_setting_fahrenheit_changes_celsius():
    temperature = Temperature(0)
    temperature.fahrenheit = 212
    assert temperature.celsius == pytest.approx(100)


def test_absolute_zero_is_allowed():
    assert Temperature(-273.15).celsius == -273.15


def test_below_absolute_zero_raises_error():
    with pytest.raises(ValueError):
        Temperature(-273.16)
    temperature = Temperature(10)
    with pytest.raises(ValueError):
        temperature.celsius = -300
    with pytest.raises(ValueError):
        temperature.fahrenheit = -500
    assert temperature.celsius == 10


@pytest.mark.parametrize("value", ["20", None])
def test_non_number_raises_error(value):
    with pytest.raises(ValueError):
        Temperature(value)
