import pytest

from pizza import Pizza


def test_default_size_and_price():
    pizza = Pizza()
    assert pizza.size == 30
    assert pizza.price() == 130


def test_add_returns_self_and_adds_ten_per_topping():
    pizza = Pizza()
    assert pizza.add("сир") is pizza
    pizza.add("гриби").add("шинка")
    assert pizza.toppings == ["сир", "гриби", "шинка"]
    assert pizza.price() == 160


def test_two_pizzas_do_not_share_toppings():
    first, second = Pizza(), Pizza()
    first.add("сир")
    assert second.toppings == []


def test_passed_list_is_copied():
    source = ["сир"]
    pizza = Pizza(25, source)
    source.append("гриби")
    assert pizza.toppings == ["сир"]


def test_invalid_size_or_topping_raises_error():
    with pytest.raises(ValueError):
        Pizza(99)
    with pytest.raises(ValueError):
        Pizza().add("")
