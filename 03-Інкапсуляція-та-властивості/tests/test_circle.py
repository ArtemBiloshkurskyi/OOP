import math

import pytest

from circle import Circle


def test_area_is_computed_from_radius():
    assert Circle(2).area == pytest.approx(math.pi * 4)


def test_area_is_cached_until_radius_changes():
    circle = Circle(2)
    assert circle.compute_count == 0
    circle.area
    circle.area
    assert circle.compute_count == 1
    circle.radius = 3
    assert circle.area == pytest.approx(math.pi * 9)
    assert circle.compute_count == 2


def test_setting_same_radius_does_not_recompute():
    circle = Circle(2)
    circle.area
    circle.radius = 2
    circle.area
    assert circle.compute_count == 1


@pytest.mark.parametrize("radius", [0, -1, "2", None])
def test_invalid_radius_raises_error(radius):
    with pytest.raises(ValueError):
        Circle(radius)
    circle = Circle(2)
    with pytest.raises(ValueError):
        circle.radius = radius
    assert circle.radius == 2


def test_area_and_compute_count_are_read_only():
    circle = Circle(2)
    with pytest.raises(AttributeError):
        circle.area = 1
    with pytest.raises(AttributeError):
        circle.compute_count = 0
