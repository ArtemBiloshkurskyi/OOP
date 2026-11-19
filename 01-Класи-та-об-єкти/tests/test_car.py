import pytest

from car import Car


def make_car():
    return Car("Skoda", 50, 10)


def test_drive_spends_fuel_and_returns_distance():
    car = make_car()
    car.refuel(40)
    assert car.drive(100) == pytest.approx(100)
    assert car.fuel_level == pytest.approx(30)
    assert car.range_left() == pytest.approx(300)


def test_drive_is_limited_by_fuel():
    car = make_car()
    car.refuel(10)
    assert car.drive(500) == pytest.approx(100)
    assert car.fuel_level == pytest.approx(0)


def test_refuel_does_not_exceed_tank_capacity():
    car = make_car()
    car.refuel(500)
    assert car.fuel_level == 50


def test_drive_with_empty_tank_returns_zero():
    assert make_car().drive(10) == 0


def test_invalid_values_raise_error():
    with pytest.raises(ValueError):
        make_car().refuel(-1)
    with pytest.raises(ValueError):
        make_car().drive(-1)
    with pytest.raises(ValueError):
        Car("Skoda", 0, 10)
