import math

ORIGIN_COORDINATE = 0


class Point:
    """Точка на площині з координатами (x, y)."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        """Повертає відстань до іншої точки."""
        if not isinstance(other, Point):
            raise TypeError("Очікується об'єкт класу Point")
        return math.hypot(other.x - self.x, other.y - self.y)

    def move(self, dx, dy):
        """Зсуває точку на dx по осі X та на dy по осі Y."""
        self.x += dx
        self.y += dy

    def is_origin(self):
        """Повертає True, якщо точка в початку координат."""
        return (self.x == ORIGIN_COORDINATE
                and self.y == ORIGIN_COORDINATE)


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    first = Point(3, 4)
    second = Point(0, 0)
    third = Point(1, 1)
    first.move(2, -1)
    print("first:", first.x, first.y)
    print("second:", second.x, second.y)
    print("third:", third.x, third.y)
    print("Відстань first-second:", first.distance_to(second))
    print("second у початку координат:", second.is_origin())


if __name__ == "__main__":
    demo()
