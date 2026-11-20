import pytest

from config import Config


def test_get_returns_default_when_no_own_value():
    assert Config().get("theme") == "light"


def test_own_value_has_priority_over_default():
    assert Config({"theme": "dark"}).get("theme") == "dark"


def test_change_of_one_object_does_not_affect_another():
    first, second = Config(), Config()
    first.set("theme", "dark")
    assert second.get("theme") == "light"
    assert Config.defaults["theme"] == "light"


def test_settings_dict_is_copied():
    source = {"theme": "dark"}
    config = Config(source)
    source["theme"] = "blue"
    assert config.get("theme") == "dark"


def test_unknown_key_raises_error():
    with pytest.raises(KeyError):
        Config().get("unknown")
