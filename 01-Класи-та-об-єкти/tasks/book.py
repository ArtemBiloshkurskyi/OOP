PERCENT = 100


class Book:
    """Книга з назвою, автором, кількістю сторінок і поточною сторінкою."""

    def __init__(self, title, author, total_pages):
        if total_pages <= 0:
            raise ValueError("Кількість сторінок має бути додатною")
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 0

    def read(self, pages):
        """Читає pages сторінок, але не далі останньої."""
        if pages < 0:
            raise ValueError("Кількість сторінок не може бути від'ємною")
        self.current_page = min(self.current_page + pages, self.total_pages)

    def progress(self):
        """Повертає відсоток прочитаного."""
        return self.current_page / self.total_pages * PERCENT

    def is_finished(self):
        """Повертає True, якщо книгу прочитано до кінця."""
        return self.current_page == self.total_pages


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    long_book = Book("Кобзар", "Тарас Шевченко", 200)
    short_book = Book("Казка", "Невідомий", 10)
    long_book.read(50)
    short_book.read(100)
    print("long_book:", long_book.progress(), long_book.is_finished())
    print("short_book:", short_book.progress(), short_book.is_finished())


if __name__ == "__main__":
    demo()
