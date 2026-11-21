MIN_AGE = 0
MAX_AGE = 150
ADULT_AGE = 18


class Person:
    """Людина з перевіреними іменем і віком."""

    def __init__(self, name, age):
        """Створює людину; значення перевіряються сеттерами."""
        self.name = name
        self.age = age

    @property
    def name(self):
        """Повертає ім'я."""
        return self._name

    @name.setter
    def name(self, value):
        """Встановлює ім'я; воно не порожнє, пробіли по краях відкидаються."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Ім'я не може бути порожнім")
        self._name = value.strip()

    @property
    def age(self):
        """Повертає вік."""
        return self._age

    @age.setter
    def age(self, value):
        """Встановлює вік: ціле число від 0 до 150."""
        if not isinstance(value, int) or not MIN_AGE <= value <= MAX_AGE:
            raise ValueError("Вік має бути цілим числом від 0 до 150")
        self._age = value

    @property
    def is_adult(self):
        """Повертає True, якщо людині 18 років або більше (лише читання)."""
        return self._age >= ADULT_AGE
