import pytest

from person import Person


def test_name_is_stripped():
    assert Person("  Іван  ", 20).name == "Іван"


@pytest.mark.parametrize("name", ["", "   ", None, 5])
def test_invalid_name_raises_error(name):
    with pytest.raises(ValueError):
        Person(name, 20)


@pytest.mark.parametrize("age", [0, 150])
def test_age_boundaries_are_allowed(age):
    assert Person("Іван", age).age == age


@pytest.mark.parametrize("age", [-1, 151, 20.5, "20"])
def test_invalid_age_raises_error(age):
    person = Person("Іван", 20)
    with pytest.raises(ValueError):
        person.age = age
    assert person.age == 20


def test_is_adult_on_boundary():
    assert not Person("Іван", 17).is_adult
    assert Person("Іван", 18).is_adult


def test_is_adult_is_read_only():
    person = Person("Іван", 20)
    with pytest.raises(AttributeError):
        person.is_adult = False
