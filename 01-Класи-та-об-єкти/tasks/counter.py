MIN_VALUE = 0


class Counter:
    """Лічильник, що починається з нуля і не опускається нижче нуля."""

    def __init__(self):
        self._value = MIN_VALUE

    def increment(self):
        """Збільшує лічильник на одиницю."""
        self._value += 1

    def decrement(self):
        """Зменшує лічильник на одиницю, але не нижче нуля."""
        if self._value == MIN_VALUE:
            return
        self._value -= 1

    def reset(self):
        """Скидає лічильник до нуля."""
        self._value = MIN_VALUE

    def value(self):
        """Повертає поточне значення лічильника."""
        return self._value


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    first = Counter()
    second = Counter()
    first.increment()
    first.increment()
    second.decrement()
    print("first:", first.value())
    print("second (не нижче 0):", second.value())
    first.reset()
    print("first після reset:", first.value())


if __name__ == "__main__":
    demo()
