import pytest

from point import Point


def test_distance_to_returns_correct_value():
    assert Point(0, 0).distance_to(Point(3, 4)) == pytest.approx(5)


def test_distance_to_itself_is_zero():
    point = Point(2, 7)
    assert point.distance_to(point) == 0


def test_distance_to_wrong_type_raises_error():
    with pytest.raises(TypeError):
        Point(1, 1).distance_to((1, 1))


def test_move_changes_coordinates():
    point = Point(1, 1)
    point.move(2, -3)
    assert (point.x, point.y) == (3, -2)


def test_is_origin_true_and_false():
    assert Point(0, 0).is_origin()
    assert not Point(0, 1).is_origin()


def test_points_are_independent():
    first, second = Point(1, 1), Point(1, 1)
    first.move(5, 5)
    assert (second.x, second.y) == (1, 1)
