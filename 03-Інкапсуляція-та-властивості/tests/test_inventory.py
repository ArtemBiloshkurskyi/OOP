import pytest

from inventory import Inventory


def test_add_accumulates_quantity():
    inventory = Inventory()
    inventory.add("яблука", 5)
    inventory.add("яблука", 3)
    assert inventory.quantity("яблука") == 8


def test_remove_reduces_quantity_and_drops_empty_item():
    inventory = Inventory()
    inventory.add("яблука", 5)
    inventory.remove("яблука", 2)
    assert inventory.quantity("яблука") == 3
    inventory.remove("яблука", 3)
    assert inventory.items() == {}


def test_quantity_of_unknown_item_is_zero():
    assert Inventory().quantity("нічого") == 0


def test_remove_more_than_available_raises_error():
    inventory = Inventory()
    inventory.add("яблука", 5)
    with pytest.raises(ValueError):
        inventory.remove("яблука", 6)
    with pytest.raises(ValueError):
        inventory.remove("груші", 1)
    assert inventory.quantity("яблука") == 5


@pytest.mark.parametrize("quantity", [0, -1, 1.5, "2"])
def test_invalid_quantity_raises_error(quantity):
    inventory = Inventory()
    with pytest.raises(ValueError):
        inventory.add("яблука", quantity)


def test_empty_name_raises_error():
    with pytest.raises(ValueError):
        Inventory().add("", 1)


def test_items_returns_copy():
    inventory = Inventory()
    inventory.add("яблука", 5)
    inventory.items()["яблука"] = 100
    assert inventory.quantity("яблука") == 5
