import pytest

from book import Book
from library import Library


def make_library():
    library = Library()
    library.add(Book("Кобзар", "Шевченко", 200))
    library.add(Book("Гайдамаки", "Шевченко", 120))
    library.add(Book("Тіні", "Коцюбинський", 150))
    return library


def test_find_returns_books_of_author():
    titles = [book.title for book in make_library().find("Шевченко")]
    assert titles == ["Кобзар", "Гайдамаки"]


def test_total_pages_and_longest():
    library = make_library()
    assert library.total_pages() == 470
    assert library.longest().title == "Кобзар"


def test_empty_library_boundaries():
    library = Library()
    assert library.total_pages() == 0
    assert library.find("Хтось") == []


def test_longest_on_empty_library_raises_error():
    with pytest.raises(ValueError):
        Library().longest()
