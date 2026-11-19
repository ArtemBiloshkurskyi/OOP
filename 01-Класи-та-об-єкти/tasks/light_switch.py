class LightSwitch:
    """Вимикач зі станом увімкнено/вимкнено та лічильником перемикань."""

    def __init__(self):
        self._is_on = False
        self._switches = 0

    def toggle(self):
        """Перемикає стан на протилежний і рахує перемикання."""
        self._is_on = not self._is_on
        self._switches += 1

    def is_on(self):
        """Повертає True, якщо вимикач увімкнено."""
        return self._is_on

    def switches(self):
        """Повертає кількість перемикань."""
        return self._switches


def demo():
    """Показує, що дані різних об'єктів незалежні."""
    kitchen = LightSwitch()
    hall = LightSwitch()
    kitchen.toggle()
    kitchen.toggle()
    kitchen.toggle()
    hall.toggle()
    print("kitchen:", kitchen.is_on(), kitchen.switches())
    print("hall:", hall.is_on(), hall.switches())


if __name__ == "__main__":
    demo()
