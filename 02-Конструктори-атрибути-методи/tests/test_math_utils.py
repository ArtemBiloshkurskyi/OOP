import pytest

from math_utils import MathUtils


def test_gcd():
    assert MathUtils.gcd(12, 18) == 6
    assert MathUtils.gcd(0, 5) == 5
    assert MathUtils.gcd(7, 13) == 1


@pytest.mark.parametrize("n, expected", [
    (2, True), (17, True), (1, False), (0, False), (-5, False), (18, False)])
def test_is_prime(n, expected):
    assert MathUtils.is_prime(n) is expected


def test_factorial():
    assert MathUtils.factorial(0) == 1
    assert MathUtils.factorial(5) == 120


def test_fibonacci():
    assert MathUtils.fibonacci(0) == 0
    assert MathUtils.fibonacci(1) == 1
    assert MathUtils.fibonacci(10) == 55


def test_negative_arguments_raise_error():
    with pytest.raises(ValueError):
        MathUtils.factorial(-1)
    with pytest.raises(ValueError):
        MathUtils.fibonacci(-1)
