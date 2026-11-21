ABSOLUTE_ZERO_CELSIUS = -273.15
FAHRENHEIT_OFFSET = 32
FAHRENHEIT_RATIO = 1.8


class Temperature:
    """Температура з перевіркою значень і перетворенням у Фаренгейти."""

    def __init__(self, celsius):
        """Створює температуру в градусах Цельсія."""
        self.celsius = celsius

    @property
    def celsius(self):
        """Повертає температуру в градусах Цельсія."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Встановлює градуси Цельсія; нижче -273.15 заборонено."""
        self._ensure_number(value)
        if value < ABSOLUTE_ZERO_CELSIUS:
            raise ValueError("Температура нижча за абсолютний нуль")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Повертає температуру в градусах Фаренгейта (обчислюється)."""
        return self._celsius * FAHRENHEIT_RATIO + FAHRENHEIT_OFFSET

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Встановлює температуру в Фаренгейтах через градуси Цельсія."""
        self._ensure_number(value)
        self.celsius = (value - FAHRENHEIT_OFFSET) / FAHRENHEIT_RATIO

    @staticmethod
    def _ensure_number(value):
        """Перевіряє, що значення є числом."""
        if not isinstance(value, (int, float)):
            raise ValueError("Температура має бути числом")
