import pytest

from person import Person


def test_from_full_name():
    person = Person.from_full_name("Іван Коваль")
    assert person.first_name == "Іван"
    assert person.last_name == "Коваль"


def test_full_name_and_initials():
    person = Person("Іван", "Коваль")
    assert person.full_name() == "Іван Коваль"
    assert person.initials() == "І.К."


def test_extra_spaces_and_lowercase_are_handled():
    person = Person.from_full_name("  іван   коваль ")
    assert person.full_name() == "іван коваль"
    assert person.initials() == "І.К."


@pytest.mark.parametrize("text", ["", "Іван", "Іван Петрович Коваль"])
def test_wrong_full_name_raises_error(text):
    with pytest.raises(ValueError):
        Person.from_full_name(text)


def test_empty_name_raises_error():
    with pytest.raises(ValueError):
        Person("", "Коваль")
