DISTANCE_UNIT_KM = 100
EMPTY_TANK = 0


class Car:
    """Авто з маркою, баком, витратою пального та поточним рівнем."""

    def __init__(self, brand, tank_capacity, consumption):
        if tank_capacity <= 0 or consumption <= 0:
            raise ValueError("Бак і витрата мають бути додатними")
        self.brand = brand
        self.tank_capacity = tank_capacity
        self.consumption = consumption
        self.fuel_level = EMPTY_TANK

    def refuel(self, liters):
        """Доливає пальне, але не більше, ніж вміщує бак."""
        if liters < 0:
            raise ValueError("Кількість пального не може бути від'ємною")
        self.fuel_level = min(self.fuel_level + liters, self.tank_capacity)

    def drive(self, km):
        """Їде km кілометрів і повертає фактично пройдену відстань."""
        if km < 0:
            raise ValueError("Відстань не може бути від'ємною")
        distance = min(km, self.range_left())
        spent = distance * self.consumption / DISTANCE_UNIT_KM
        self.fuel_level = max(self.fuel_level - spent, EMPTY_TANK)
        return distance

    def range_left(self):
        """Повертає, скільки кілометрів можна проїхати на залишку."""
        return self.fuel_level / self.consumption * DISTANCE_UNIT_KM


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    first = Car("Skoda", 50, 8)
    second = Car("Ford", 40, 10)
    first.refuel(40)
    second.refuel(10)
    print("first проїхав:", first.drive(100), "рівень:", first.fuel_level)
    print("second проїхав:", second.drive(500), "рівень:", second.fuel_level)


if __name__ == "__main__":
    demo()
