import pytest

from employee import Employee


def test_default_salary_and_raise():
    employee = Employee("Олена")
    assert employee.salary == 10000
    employee.raise_salary(10)
    assert employee.salary == pytest.approx(11000)


def test_raise_by_zero_percent_changes_nothing():
    employee = Employee("Іван", 5000)
    employee.raise_salary(0)
    assert employee.salary == 5000


def test_count_grows_with_each_new_object():
    before = Employee.count
    Employee("А")
    Employee("Б")
    assert Employee.count == before + 2


def test_invalid_values_raise_error():
    with pytest.raises(ValueError):
        Employee("Олена", -1)
    with pytest.raises(ValueError):
        Employee("Олена").raise_salary(-5)


def test_employees_are_independent():
    first, second = Employee("А", 100), Employee("Б", 100)
    first.raise_salary(50)
    assert second.salary == 100
