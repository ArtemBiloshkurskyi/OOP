class Thermostat:
    """Термостат із цільовою температурою в межах заданого діапазону."""

    def __init__(self, min_t, max_t, target=None):
        """Створює термостат; без target ціль дорівнює min_t."""
        self._ensure_number(min_t)
        self._ensure_number(max_t)
        if min_t > max_t:
            raise ValueError("min_t не може бути більшим за max_t")
        self._min_t = min_t
        self._max_t = max_t
        self.target = min_t if target is None else target

    @property
    def min_t(self):
        """Повертає нижню межу діапазону (лише читання)."""
        return self._min_t

    @property
    def max_t(self):
        """Повертає верхню межу діапазону (лише читання)."""
        return self._max_t

    @property
    def target(self):
        """Повертає цільову температуру."""
        return self._target

    @target.setter
    def target(self, value):
        """Встановлює ціль; значення поза діапазоном обмежується межею."""
        self._ensure_number(value)
        self._target = max(self._min_t, min(value, self._max_t))

    def heating_needed(self, current):
        """Повертає True, якщо поточна температура нижча за ціль."""
        self._ensure_number(current)
        return current < self._target

    @staticmethod
    def _ensure_number(value):
        """Перевіряє, що значення є числом."""
        if not isinstance(value, (int, float)):
            raise ValueError("Температура має бути числом")
