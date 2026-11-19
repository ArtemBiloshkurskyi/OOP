MIN_GRADE = 0
MAX_GRADE = 100
PASSING_GRADE = 60


class Student:
    """Студент із прізвищем і списком оцінок."""

    def __init__(self, surname):
        self.surname = surname
        self.grades = []

    def add_grade(self, grade):
        """Додає оцінку; вона має бути в межах від 0 до 100."""
        if not MIN_GRADE <= grade <= MAX_GRADE:
            raise ValueError("Оцінка поза допустимими межами")
        self.grades.append(grade)

    def average(self):
        """Повертає середню оцінку."""
        self._ensure_has_grades()
        return sum(self.grades) / len(self.grades)

    def best(self):
        """Повертає найвищу оцінку."""
        self._ensure_has_grades()
        return max(self.grades)

    def has_debt(self):
        """Повертає True, якщо є оцінка нижче 60."""
        return any(grade < PASSING_GRADE for grade in self.grades)

    def _ensure_has_grades(self):
        if not self.grades:
            raise ValueError("У студента ще немає оцінок")


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    first = Student("Петренко")
    second = Student("Коваленко")
    for grade in (90, 75, 55):
        first.add_grade(grade)
    second.add_grade(100)
    print("first:", first.average(), first.best(), first.has_debt())
    print("second:", second.average(), second.best(), second.has_debt())


if __name__ == "__main__":
    demo()
