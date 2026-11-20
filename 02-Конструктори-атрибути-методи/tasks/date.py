FEBRUARY = 2
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
LEAP_FEBRUARY_DAYS = 29
LEAP_CYCLE = 4
CENTURY = 100
LEAP_CENTURY_CYCLE = 400
DATE_PARTS = 3


class Date:
    """Дата: рік, місяць, день."""

    def __init__(self, year, month, day):
        """Створює дату; перевіряє, що місяць і день існують."""
        if not MIN_MONTH <= month <= MAX_MONTH:
            raise ValueError("Місяць має бути від 1 до 12")
        self.year = year
        self.month = month
        self.day = day
        if not MIN_DAY <= day <= self.days_in_month():
            raise ValueError("Такого дня в цьому місяці немає")

    @classmethod
    def from_string(cls, text):
        """Створює дату з рядка у форматі РРРР-ММ-ДД."""
        parts = text.split("-")
        if len(parts) != DATE_PARTS:
            raise ValueError("Очікується формат РРРР-ММ-ДД")
        year, month, day = (int(part) for part in parts)
        return cls(year, month, day)

    @staticmethod
    def is_leap(year):
        """Повертає True, якщо рік високосний."""
        return (year % LEAP_CYCLE == 0
                and (year % CENTURY != 0 or year % LEAP_CENTURY_CYCLE == 0))

    def days_in_month(self):
        """Повертає кількість днів у місяці цієї дати."""
        if self.month == FEBRUARY and Date.is_leap(self.year):
            return LEAP_FEBRUARY_DAYS
        return DAYS_IN_MONTH[self.month - 1]


def demo():
    """Показує роботу класу на трьох об'єктах."""
    first = Date(2024, 2, 10)
    second = Date.from_string("2023-02-10")
    third = Date.from_string("2025-04-01")
    print("first:", first.days_in_month(), Date.is_leap(first.year))
    print("second:", second.days_in_month(), Date.is_leap(second.year))
    print("third:", third.days_in_month(), Date.is_leap(third.year))


if __name__ == "__main__":
    demo()
