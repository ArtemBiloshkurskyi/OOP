import pytest

from password import Password


def test_check_accepts_correct_and_rejects_wrong_password():
    password = Password("secret123")
    assert password.check("secret123")
    assert not password.check("secret124")
    assert not password.check("")


def test_set_replaces_password():
    password = Password("secret123")
    password.set("another456")
    assert password.check("another456")
    assert not password.check("secret123")


def test_minimal_length_is_allowed():
    assert Password("12345678").check("12345678")


@pytest.mark.parametrize("value", ["1234567", "", None])
def test_too_short_or_wrong_type_raises_error(value):
    with pytest.raises(ValueError):
        Password(value)
    with pytest.raises(ValueError):
        Password("secret123").set(value)


def test_plain_password_is_not_stored():
    password = Password("secret123")
    stored = list(vars(password).values())
    assert "secret123" not in stored
    assert b"secret123" not in stored


def test_same_password_gives_different_hashes():
    first, second = Password("secret123"), Password("secret123")
    assert vars(first) != vars(second)


def test_check_with_non_string_returns_false():
    assert not Password("secret123").check(None)
