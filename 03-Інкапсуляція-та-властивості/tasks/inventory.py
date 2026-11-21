NONE_LEFT = 0


class Inventory:
    """Склад: приховує словник «товар - кількість» за методами."""

    def __init__(self):
        """Створює порожній склад."""
        self._items = {}

    def add(self, name, quantity):
        """Додає quantity одиниць товару name."""
        self._validate(name, quantity)
        self._items[name] = self.quantity(name) + quantity

    def remove(self, name, quantity):
        """Забирає зі складу товар, але не більше, ніж є."""
        self._validate(name, quantity)
        left = self.quantity(name) - quantity
        if left < NONE_LEFT:
            raise ValueError("На складі недостатньо товару")
        if left == NONE_LEFT:
            del self._items[name]
        else:
            self._items[name] = left

    def quantity(self, name):
        """Повертає кількість товару; для відсутнього товару це 0."""
        return self._items.get(name, NONE_LEFT)

    def items(self):
        """Повертає копію словника «товар - кількість»."""
        return dict(self._items)

    @staticmethod
    def _validate(name, quantity):
        """Перевіряє назву товару і кількість."""
        if not isinstance(name, str) or not name:
            raise ValueError("Назва товару не може бути порожньою")
        if not isinstance(quantity, int) or quantity <= NONE_LEFT:
            raise ValueError("Кількість має бути додатним цілим числом")
