DEFAULT_SALARY = 10000
PERCENT = 100


class Employee:
    """Працівник з іменем і зарплатою; рахує всіх створених працівників."""

    count = 0

    def __init__(self, name, salary=DEFAULT_SALARY):
        """Створює працівника і збільшує лічильник count."""
        if salary < 0:
            raise ValueError("Зарплата не може бути від'ємною")
        self.name = name
        self.salary = salary
        Employee.count += 1

    def raise_salary(self, percent):
        """Підвищує зарплату на percent відсотків."""
        if percent < 0:
            raise ValueError("Відсоток підвищення не може бути від'ємним")
        self.salary += self.salary * percent / PERCENT


def demo():
    """Показує роботу класу на трьох об'єктах."""
    first = Employee("Олена")
    second = Employee("Іван", 15000)
    third = Employee("Марія", 20000)
    first.raise_salary(10)
    print("first:", first.name, first.salary)
    print("second:", second.name, second.salary)
    print("third:", third.name, third.salary)
    print("Створено працівників:", Employee.count)


if __name__ == "__main__":
    demo()
