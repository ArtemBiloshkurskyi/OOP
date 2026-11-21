import pytest

from thermostat import Thermostat


def test_target_inside_range_is_kept():
    thermostat = Thermostat(10, 30)
    thermostat.target = 22
    assert thermostat.target == 22


def test_target_is_clamped_to_range():
    thermostat = Thermostat(10, 30)
    thermostat.target = 50
    assert thermostat.target == 30
    thermostat.target = -5
    assert thermostat.target == 10


def test_target_on_boundaries_is_kept():
    thermostat = Thermostat(10, 30)
    thermostat.target = 10
    assert thermostat.target == 10
    thermostat.target = 30
    assert thermostat.target == 30


def test_default_target_is_minimum():
    assert Thermostat(10, 30).target == 10


def test_heating_needed():
    thermostat = Thermostat(10, 30, 22)
    assert thermostat.heating_needed(20)
    assert not thermostat.heating_needed(22)
    assert not thermostat.heating_needed(25)


def test_initial_target_is_clamped():
    assert Thermostat(10, 30, 99).target == 30


def test_invalid_values_raise_error():
    with pytest.raises(ValueError):
        Thermostat(30, 10)
    with pytest.raises(ValueError):
        Thermostat("10", 30)
    thermostat = Thermostat(10, 30)
    with pytest.raises(ValueError):
        thermostat.target = "20"
    with pytest.raises(ValueError):
        thermostat.heating_needed(None)
