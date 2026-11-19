import pytest

from student import Student


def make_student(*grades):
    student = Student("Петренко")
    for grade in grades:
        student.add_grade(grade)
    return student


def test_average_and_best():
    student = make_student(90, 70, 80)
    assert student.average() == 80
    assert student.best() == 90


def test_has_debt_on_boundary():
    assert make_student(59).has_debt()
    assert not make_student(60).has_debt()


def test_student_without_grades():
    student = Student("Петренко")
    assert not student.has_debt()
    with pytest.raises(ValueError):
        student.average()


@pytest.mark.parametrize("grade", [-1, 101])
def test_invalid_grade_raises_error(grade):
    with pytest.raises(ValueError):
        Student("Петренко").add_grade(grade)


def test_students_are_independent():
    first, second = make_student(90), make_student()
    assert second.grades == [] and first.grades == [90]
