import pytest

from rectangle import Rectangle


def test_area_and_perimeter():
    rectangle = Rectangle(4, 3)
    assert rectangle.area() == 12
    assert rectangle.perimeter() == 14


def test_is_square_true_and_false():
    assert Rectangle(5, 5).is_square()
    assert not Rectangle(5, 4).is_square()


def test_minimal_rectangle():
    assert Rectangle(1, 1).area() == 1


@pytest.mark.parametrize("width, height", [(0, 5), (-1, 5), (5, 0)])
def test_invalid_sides_raise_error(width, height):
    with pytest.raises(ValueError):
        Rectangle(width, height)
