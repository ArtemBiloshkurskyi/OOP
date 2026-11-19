PAIRS_OF_SIDES = 2


class Rectangle:
    """Прямокутник із заданою шириною та висотою."""

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Сторони мають бути додатними")
        self.width = width
        self.height = height

    def area(self):
        """Повертає площу прямокутника."""
        return self.width * self.height

    def perimeter(self):
        """Повертає периметр прямокутника."""
        return PAIRS_OF_SIDES * (self.width + self.height)

    def is_square(self):
        """Повертає True, якщо ширина дорівнює висоті."""
        return self.width == self.height


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    wide = Rectangle(4, 3)
    square = Rectangle(2, 2)
    print("wide:", wide.area(), wide.perimeter(), wide.is_square())
    print("square:", square.area(), square.perimeter(), square.is_square())
    wide.width = 10
    print("wide після зміни:", wide.area())
    print("square не змінився:", square.area())


if __name__ == "__main__":
    demo()
