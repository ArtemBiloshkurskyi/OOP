DEFAULT_SIZE = 30
SIZE_PRICES = {25: 100, 30: 130, 35: 160}
TOPPING_PRICE = 10


class Pizza:
    """Піца з розміром і списком добавок."""

    def __init__(self, size=DEFAULT_SIZE, toppings=None):
        """Створює піцу; кожен об'єкт має власний список добавок."""
        if size not in SIZE_PRICES:
            raise ValueError("Невідомий розмір піци")
        self.size = size
        self.toppings = list(toppings or [])

    def add(self, topping):
        """Додає добавку і повертає self для ланцюжка викликів."""
        if not topping:
            raise ValueError("Назва добавки не може бути порожньою")
        self.toppings.append(topping)
        return self

    def price(self):
        """Повертає ціну: базова за розмір плюс 10 за кожну добавку."""
        return SIZE_PRICES[self.size] + TOPPING_PRICE * len(self.toppings)


def demo():
    """Показує, що два об'єкти не діляться одним списком добавок."""
    first = Pizza()
    second = Pizza(35)
    first.add("сир").add("гриби")
    second.add("шинка")
    print("first:", first.toppings, first.price())
    print("second:", second.toppings, second.price())


if __name__ == "__main__":
    demo()
