import pytest

from student import Student


def test_add_grade_and_read_grades():
    student = Student(1, "Олена")
    student.add_grade(90)
    student.add_grade(75)
    assert student.grades == (90, 75)


def test_grades_cannot_be_changed_from_outside():
    student = Student(1, "Олена")
    student.add_grade(90)
    with pytest.raises(AttributeError):
        student.grades.append(100)
    with pytest.raises(AttributeError):
        student.grades = (1, 2)
    assert student.grades == (90,)


def test_id_is_read_only():
    student = Student(7, "Олена")
    assert student.id == 7
    with pytest.raises(AttributeError):
        student.id = 8


@pytest.mark.parametrize("grade", [-1, 101, "90", None])
def test_invalid_grade_raises_error(grade):
    student = Student(1, "Олена")
    with pytest.raises(ValueError):
        student.add_grade(grade)
    assert student.grades == ()


@pytest.mark.parametrize("grade", [0, 100])
def test_grade_boundaries_are_allowed(grade):
    student = Student(1, "Олена")
    student.add_grade(grade)
    assert student.grades == (grade,)


def test_name_is_stripped_and_validated():
    student = Student(1, "  Олена ")
    assert student.name == "Олена"
    with pytest.raises(ValueError):
        student.name = "   "


@pytest.mark.parametrize("student_id", [0, -1, "1", None])
def test_invalid_id_raises_error(student_id):
    with pytest.raises(ValueError):
        Student(student_id, "Олена")
