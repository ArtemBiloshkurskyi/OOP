import math

NO_COMPUTATIONS = 0


class Circle:
    """Коло з радіусом-властивістю та кешованою площею."""

    def __init__(self, radius):
        """Створює коло; радіус має бути додатним."""
        self._radius = None
        self._area = None
        self._compute_count = NO_COMPUTATIONS
        self.radius = radius

    @property
    def radius(self):
        """Повертає радіус."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Встановлює радіус; після зміни площа буде перерахована."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Радіус має бути додатним числом")
        if value != self._radius:
            self._radius = value
            self._area = None

    @property
    def area(self):
        """Повертає площу; рахує лише якщо радіус змінився."""
        if self._area is None:
            self._area = math.pi * self._radius * self._radius
            self._compute_count += 1
        return self._area

    @property
    def compute_count(self):
        """Повертає, скільки разів площу реально обчислювали."""
        return self._compute_count
