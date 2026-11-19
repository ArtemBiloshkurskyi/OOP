import pytest

from product import Product


def test_final_price_and_total():
    product = Product("Молоко", 200, 25)
    assert product.final_price() == pytest.approx(150)
    assert product.total(3) == pytest.approx(450)


def test_default_discount_is_zero():
    product = Product("Хліб", 40)
    assert product.discount == 0
    assert product.final_price() == 40


def test_discount_boundaries():
    product = Product("Хліб", 40)
    product.set_discount(100)
    assert product.final_price() == 0
    product.set_discount(0)
    assert product.final_price() == 40


@pytest.mark.parametrize("percent", [-1, 101])
def test_invalid_discount_raises_error(percent):
    with pytest.raises(ValueError):
        Product("Хліб", 40).set_discount(percent)


def test_negative_price_or_qty_raises_error():
    with pytest.raises(ValueError):
        Product("Хліб", -1)
    with pytest.raises(ValueError):
        Product("Хліб", 40).total(-1)
