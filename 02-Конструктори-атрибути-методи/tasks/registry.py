lass Registry:
    """Об'єкт з іменем; клас зберігає список усіх створених об'єктів."""

    _instances = []

    def __init__(self, name):
        """Створює об'єкт з іменем і додає його до реєстру."""
        if not name:
            raise ValueError("Ім'я не може бути порожнім")
        self.name = name
        Registry._instances.append(self)

    @classmethod
    def all(cls):
        """Повертає список усіх створених об'єктів."""
        return list(cls._instances)

    @classmethod
    def find(cls, name):
        """Повертає список об'єктів із заданим іменем."""
        return [item for item in cls._instances if item.name == name]

    @classmethod
    def clear(cls):
        """Очищає реєстр."""
        cls._instances.clear()


def demo():
    """Показує роботу реєстру на трьох об'єктах."""
    Registry("alpha")
    Registry("beta")
    Registry("alpha")
    print("Усього:", len(Registry.all()))
    print("Знайдено alpha:", len(Registry.find("alpha")))
    Registry.clear()
    print("Після clear:", len(Registry.all()))


if __name__ == "__main__":
    demo()
