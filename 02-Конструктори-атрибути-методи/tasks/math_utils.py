import math

SMALLEST_PRIME = 2


class MathUtils:
    """Набір математичних функцій; усі методи статичні, об'єкти не потрібні."""

    @staticmethod
    def gcd(first, second):
        """Повертає найбільший спільний дільник (алгоритм Евкліда)."""
        while second:
            first, second = second, first % second
        return abs(first)

    @staticmethod
    def is_prime(number):
        """Повертає True, якщо number є простим числом."""
        if number < SMALLEST_PRIME:
            return False
        for divisor in range(SMALLEST_PRIME, math.isqrt(number) + 1):
            if number % divisor == 0:
                return False
        return True

    @staticmethod
    def factorial(number):
        """Повертає факторіал невід'ємного цілого числа."""
        if number < 0:
            raise ValueError("Факторіал визначений для чисел >= 0")
        result = 1
        for factor in range(1, number + 1):
            result *= factor
        return result

    @staticmethod
    def fibonacci(number):
        """Повертає число Фібоначчі з номером number (0, 1, 1, 2, 3, ...)."""
        if number < 0:
            raise ValueError("Номер числа Фібоначчі має бути >= 0")
        previous, current = 0, 1
        for _ in range(number):
            previous, current = current, previous + current
        return previous


def demo():
    """Показує виклики статичних методів без створення об'єктів."""
    print("gcd(12, 18):", MathUtils.gcd(12, 18))
    print("is_prime(17):", MathUtils.is_prime(17))
    print("is_prime(18):", MathUtils.is_prime(18))
    print("factorial(5):", MathUtils.factorial(5))
    print("fibonacci(10):", MathUtils.fibonacci(10))


if __name__ == "__main__":
    demo()
