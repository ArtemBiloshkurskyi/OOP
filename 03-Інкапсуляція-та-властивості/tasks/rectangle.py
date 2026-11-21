PAIRS_OF_SIDES = 2
NO_SIZE = 0


class Rectangle:
    """Прямокутник із перевіреними сторонами та обчислюваними величинами."""

    def __init__(self, width, height):
        """Створює прямокутник; сторони мають бути додатними."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Повертає ширину."""
        return self._width

    @width.setter
    def width(self, value):
        """Встановлює ширину; вона має бути додатною."""
        self._ensure_positive(value)
        self._width = value

    @property
    def height(self):
        """Повертає висоту."""
        return self._height

    @height.setter
    def height(self, value):
        """Встановлює висоту; вона має бути додатною."""
        self._ensure_positive(value)
        self._height = value

    @property
    def area(self):
        """Повертає площу (лише читання)."""
        return self._width * self._height

    @property
    def perimeter(self):
        """Повертає периметр (лише читання)."""
        return PAIRS_OF_SIDES * (self._width + self._height)

    @staticmethod
    def _ensure_positive(value):
        """Перевіряє, що сторона є додатним числом."""
        if not isinstance(value, (int, float)) or value <= NO_SIZE:
            raise ValueError("Сторона має бути додатним числом")
