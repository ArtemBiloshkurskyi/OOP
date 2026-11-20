import pytest

from book import Book


def test_read_and_progress():
    book = Book("Книга", "Автор", 200)
    book.read(50)
    assert book.progress() == 25


def test_read_does_not_go_past_last_page():
    book = Book("Книга", "Автор", 10)
    book.read(100)
    assert book.current_page == 10
    assert book.is_finished()


def test_new_book_is_not_finished():
    book = Book("Книга", "Автор", 10)
    assert book.progress() == 0
    assert not book.is_finished()


def test_negative_pages_raise_error():
    with pytest.raises(ValueError):
        Book("Книга", "Автор", 10).read(-1)


def test_zero_total_pages_raise_error():
    with pytest.raises(ValueError):
        Book("Книга", "Автор", 0)
