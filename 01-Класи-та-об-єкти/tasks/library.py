class Library:
    """Бібліотека, що містить список книг (об'єктів Book із задачі 1.4)."""

    def __init__(self):
        self._books = []

    def add(self, book):
        """Додає книгу до бібліотеки."""
        self._books.append(book)

    def find(self, author):
        """Повертає список книг заданого автора."""
        return [book for book in self._books if book.author == author]

    def total_pages(self):
        """Повертає сумарну кількість сторінок усіх книг."""
        return sum(book.total_pages for book in self._books)

    def longest(self):
        """Повертає книгу з найбільшою кількістю сторінок."""
        if not self._books:
            raise ValueError("У бібліотеці немає книг")
        return max(self._books, key=lambda book: book.total_pages)


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    from book import Book

    first = Library()
    second = Library()
    first.add(Book("Кобзар", "Шевченко", 200))
    first.add(Book("Гайдамаки", "Шевченко", 120))
    second.add(Book("Тіні забутих предків", "Коцюбинський", 150))
    print("first:", first.total_pages(), first.longest().title)
    print("Книги Шевченка:", len(first.find("Шевченко")))
    print("second:", second.total_pages(), second.longest().title)


if __name__ == "__main__":
    demo()
