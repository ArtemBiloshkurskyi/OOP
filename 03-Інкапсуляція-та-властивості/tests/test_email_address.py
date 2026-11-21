import pytest

from email_address import Email


def test_user_and_domain_are_parsed():
    email = Email("ivan@example.com")
    assert email.user == "ivan"
    assert email.domain == "example.com"
    assert email.address == "ivan@example.com"


def test_new_address_updates_parts():
    email = Email("ivan@example.com")
    email.address = "olena@mail.ua"
    assert (email.user, email.domain) == ("olena", "mail.ua")


@pytest.mark.parametrize("address", [
    "ivanexample.com", "iv@an@example.com", "@example.com", "ivan@",
    "ivan@example", "ivan@.com", "ivan@example.", "", None])
def test_invalid_address_raises_error(address):
    with pytest.raises(ValueError):
        Email(address)


def test_failed_change_keeps_old_address():
    email = Email("ivan@example.com")
    with pytest.raises(ValueError):
        email.address = "wrong"
    assert email.address == "ivan@example.com"


def test_user_and_domain_are_read_only():
    email = Email("ivan@example.com")
    with pytest.raises(AttributeError):
        email.user = "other"
    with pytest.raises(AttributeError):
        email.domain = "other.com"
