MIN_GRADE = 0
MAX_GRADE = 100


class Student:
    """Студент з незмінним id, іменем та захищеним списком оцінок."""

    def __init__(self, student_id, name):
        """Створює студента; id має бути додатним цілим числом."""
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("id має бути додатним цілим числом")
        self._id = student_id
        self.name = name
        self._grades = []

    @property
    def id(self):
        """Повертає id (лише читання)."""
        return self._id

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
    def grades(self):
        """Повертає оцінки у вигляді кортежу (змінити ззовні не можна)."""
        return tuple(self._grades)

    def add_grade(self, grade):
        """Додає оцінку від 0 до 100."""
        if not isinstance(grade, (int, float)):
            raise ValueError("Оцінка має бути числом")
        if not MIN_GRADE <= grade <= MAX_GRADE:
            raise ValueError("Оцінка має бути від 0 до 100")
        self._grades.append(grade)
