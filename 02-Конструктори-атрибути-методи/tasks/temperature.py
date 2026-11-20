ABSOLUTE_ZERO_CELSIUS = -273.15
KELVIN_OFFSET = 273.15
FAHRENHEIT_OFFSET = 32
FAHRENHEIT_RATIO = 1.8


class Temperature:
    """Температура в градусах Цельсія з перетворенням в інші шкали."""

    def __init__(self, celsius):
        """Створює температуру; нижче абсолютного нуля заборонено."""
        if not Temperature.is_valid(celsius):
            raise ValueError("Температура нижча за абсолютний нуль")
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Створює температуру зі значення в градусах Фаренгейта."""
        return cls((fahrenheit - FAHRENHEIT_OFFSET) / FAHRENHEIT_RATIO)

    @classmethod
    def from_kelvin(cls, kelvin):
        """Створює температуру зі значення в кельвінах."""
        return cls(kelvin - KELVIN_OFFSET)

    def to_fahrenheit(self):
        """Повертає температуру в градусах Фаренгейта."""
        return self.celsius * FAHRENHEIT_RATIO + FAHRENHEIT_OFFSET

    @staticmethod
    def is_valid(celsius):
        """Перевіряє, що celsius не нижче абсолютного нуля."""
        return celsius >= ABSOLUTE_ZERO_CELSIUS


def demo():
    """Показує роботу класу на трьох об'єктах."""
    room = Temperature(25)
    boiling = Temperature.from_fahrenheit(212)
    warm = Temperature.from_kelvin(300)
    print("room:", room.celsius, room.to_fahrenheit())
    print("boiling:", boiling.celsius, boiling.to_fahrenheit())
    print("warm:", warm.celsius, warm.to_fahrenheit())
    print("-300 допустимо:", Temperature.is_valid(-300))


if __name__ == "__main__":
    demo()
