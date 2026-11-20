import pytest

from date import Date


def test_from_string_creates_date():
    date = Date.from_string("2024-03-15")
    assert (date.year, date.month, date.day) == (2024, 3, 15)


@pytest.mark.parametrize("year, expected", [
    (2024, True), (2023, False), (2000, True), (1900, False)])
def test_is_leap(year, expected):
    assert Date.is_leap(year) is expected


def test_days_in_month():
    assert Date(2024, 2, 1).days_in_month() == 29
    assert Date(2023, 2, 1).days_in_month() == 28
    assert Date(2023, 4, 1).days_in_month() == 30
    assert Date(2023, 12, 31).days_in_month() == 31


@pytest.mark.parametrize("year, month, day", [
    (2023, 13, 1), (2023, 0, 1), (2023, 4, 31), (2023, 2, 29), (2023, 1, 0)])
def test_nonexistent_date_raises_error(year, month, day):
    with pytest.raises(ValueError):
        Date(year, month, day)


@pytest.mark.parametrize("text", ["abc", "2024-02", "2024-02-30", ""])
def test_invalid_string_raises_error(text):
    with pytest.raises(ValueError):
        Date.from_string(text)
