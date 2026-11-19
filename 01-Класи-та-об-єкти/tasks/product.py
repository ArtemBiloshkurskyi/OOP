PERCENT = 100
MIN_DISCOUNT = 0
MAX_DISCOUNT = 100


class Product:
    """Товар з назвою, ціною та знижкою у відсотках."""

    def __init__(self, name, price, discount=MIN_DISCOUNT):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self.name = name
        self.price = price
        self.discount = MIN_DISCOUNT
        self.set_discount(discount)

    def final_price(self):
        """Повертає ціну одного товару з урахуванням знижки."""
        return self.price * (PERCENT - self.discount) / PERCENT

    def set_discount(self, percent):
        """Встановлює знижку; вона має бути в межах від 0 до 100."""
        if not MIN_DISCOUNT <= percent <= MAX_DISCOUNT:
            raise ValueError("Знижка має бути від 0 до 100")
        self.discount = percent

    def total(self, qty):
        """Повертає вартість qty штук товару зі знижкою."""
        if qty < 0:
            raise ValueError("Кількість не може бути від'ємною")
        return self.final_price() * qty


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    bread = Product("Хліб", 40)
    milk = Product("Молоко", 200, 25)
    bread.set_discount(10)
    print("bread:", bread.final_price(), bread.total(3))
    print("milk:", milk.final_price(), milk.total(2))
    print("Знижка milk не змінилась:", milk.discount)


if __name__ == "__main__":
    demo()
