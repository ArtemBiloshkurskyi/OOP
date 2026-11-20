class Stack:
    """Стек цілих чисел: останнім додали, першим забрали."""

    def __init__(self):
        self._items = []

    def push(self, value):
        """Додає ціле число на вершину стека."""
        if not isinstance(value, int):
            raise TypeError("Стек зберігає лише цілі числа")
        self._items.append(value)

    def pop(self):
        """Забирає верхній елемент; для порожнього стека дає None."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        """Показує верхній елемент, не забираючи його."""
        if self.is_empty():
            return None
        return self._items[-1]

    def size(self):
        """Повертає кількість елементів у стеку."""
        return len(self._items)

    def is_empty(self):
        """Повертає True, якщо стек порожній."""
        return not self._items


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    first = Stack()
    second = Stack()
    first.push(1)
    first.push(2)
    second.push(10)
    print("first:", first.peek(), first.size())
    print("second:", second.peek(), second.size())
    print("pop з first:", first.pop(), "залишилось:", first.size())
    print("second не змінився:", second.size())


if __name__ == "__main__":
    demo()
