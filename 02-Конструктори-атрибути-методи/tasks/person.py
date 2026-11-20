NAME_PARTS = 2


class Person:
    """Людина з іменем та прізвищем."""

    def __init__(self, first_name, last_name):
        """Створює людину; ім'я та прізвище не можуть бути порожніми."""
        if not first_name or not last_name:
            raise ValueError("Ім'я та прізвище не можуть бути порожніми")
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        """Створює людину з рядка "Ім'я Прізвище"."""
        parts = full_name.split()
        if len(parts) != NAME_PARTS:
            raise ValueError("Очікується формат: Ім'я Прізвище")
        return cls(*parts)

    def full_name(self):
        """Повертає ім'я та прізвище через пробіл."""
        return f"{self.first_name} {self.last_name}"

    def initials(self):
        """Повертає ініціали у форматі І.К."""
        return f"{self.first_name[0].upper()}.{self.last_name[0].upper()}."


def demo():
    """Показує роботу класу на трьох об'єктах."""
    first = Person("Олена", "Шевченко")
    second = Person.from_full_name("Іван Коваль")
    third = Person.from_full_name("марія Бойко")
    for person in (first, second, third):
        print(person.full_name(), person.initials())


if __name__ == "__main__":
    demo()
