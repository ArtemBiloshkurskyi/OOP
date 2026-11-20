class Ticket:
    """Квиток з унікальним номером, що зростає з кожним новим квитком."""

    _created_count = 0

    def __init__(self):
        """Створює квиток і видає йому наступний номер."""
        Ticket._created_count += 1
        self.id = Ticket._created_count

    @classmethod
    def created(cls):
        """Повертає кількість створених квитків."""
        return cls._created_count


def demo():
    """Показує роботу класу на трьох об'єктах."""
    first = Ticket()
    second = Ticket()
    third = Ticket()
    print("id:", first.id, second.id, third.id)
    print("Створено квитків:", Ticket.created())


if __name__ == "__main__":
    demo()
