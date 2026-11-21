import pytest

from rectangle import Rectangle


def test_area_and_perimeter():
    rectangle = Rectangle(4, 3)
    assert rectangle.area == 12
    assert rectangle.perimeter == 14


def test_computed_values_follow_changes_of_sides():
    rectangle = Rectangle(4, 3)
    rectangle.width = 10
    rectangle.height = 2
    assert rectangle.area == 20
    assert rectangle.perimeter == 24


@pytest.mark.parametrize("value", [0, -1, "5", None])
def test_invalid_side_raises_error(value):
    with pytest.raises(ValueError):
        Rectangle(value, 3)
    rectangle = Rectangle(4, 3)
    with pytest.raises(ValueError):
        rectangle.height = value
    assert rectangle.height == 3


def test_area_and_perimeter_are_read_only():
    rectangle = Rectangle(4, 3)
    with pytest.raises(AttributeError):
        rectangle.area = 100
    with pytest.raises(AttributeError):
        rectangle.perimeter = 100
