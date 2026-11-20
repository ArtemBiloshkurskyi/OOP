import math

KOPECKS_PER_HRYVNIA = 100


class Money:
    """Грошова сума, що зберігається в копійках (ціле число)."""

    def __init__(self, kopecks):
        """Створює суму; копійки мають бути невід'ємним цілим числом."""
        if not isinstance(kopecks, int):
            raise TypeError("Копійки мають бути цілим числом")
        if kopecks < 0:
            raise ValueError("Сума не може бути від'ємною")
        self.kopecks = kopecks

    @classmethod
    def from_float(cls, amount):
        """Створює суму з гривень у вигляді числа з комою."""
        if not math.isfinite(amount):
            raise ValueError("Сума має бути скінченним числом")
        return cls(round(amount * KOPECKS_PER_HRYVNIA))

    @classmethod
    def from_string(cls, text):
        """Створює суму з рядка на кшталт "12.50"."""
        return cls.from_float(float(text))

    def to_float(self):
        """Повертає суму в гривнях у вигляді числа з комою."""
        return self.kopecks / KOPECKS_PER_HRYVNIA

    def __str__(self):
        """Повертає рядок у форматі 12.50 грн."""
        hryvnias, kopecks = divmod(self.kopecks, KOPECKS_PER_HRYVNIA)
        return f"{hryvnias}.{kopecks:02d} грн"


def demo():
    """Показує роботу класу на трьох об'єктах."""
    first = Money(1250)
    second = Money.from_float(0.5)
    third = Money.from_string("99.99")
    print("first:", first, first.to_float())
    print("second:", second, second.to_float())
    print("third:", third, third.to_float())


if __name__ == "__main__":
    demo()
