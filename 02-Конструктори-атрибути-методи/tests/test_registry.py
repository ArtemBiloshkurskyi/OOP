import pytest

from registry import Registry


@pytest.fixture(autouse=True)
def clean_registry():
    Registry.clear()


def test_all_returns_created_objects_in_order():
    first, second = Registry("a"), Registry("b")
    assert Registry.all() == [first, second]


def test_find_returns_objects_with_name():
    first, _, third = Registry("a"), Registry("b"), Registry("a")
    assert Registry.find("a") == [first, third]
    assert Registry.find("unknown") == []


def test_clear_empties_registry():
    Registry("a")
    Registry.clear()
    assert Registry.all() == []


def test_all_returns_copy():
    Registry("a")
    Registry.all().clear()
    assert len(Registry.all()) == 1


def test_empty_name_raises_error():
    with pytest.raises(ValueError):
        Registry("")
