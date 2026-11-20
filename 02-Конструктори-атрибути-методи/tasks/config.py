class Config:
    """Налаштування: значення об'єкта мають пріоритет над типовими."""

    defaults = {"theme": "light", "language": "uk", "font_size": 14}

    def __init__(self, settings=None):
        """Створює налаштування; копія словника не залежить від оригіналу."""
        self.settings = dict(settings or {})

    def get(self, key):
        """Повертає значення об'єкта, а якщо його немає, типове."""
        if key in self.settings:
            return self.settings[key]
        if key in self.defaults:
            return self.defaults[key]
        raise KeyError(f"Невідомий параметр: {key}")

    def set(self, key, value):
        """Змінює налаштування лише цього об'єкта."""
        self.settings[key] = value


def demo():
    """Показує, що зміна одного об'єкта не торкається іншого."""
    first = Config()
    second = Config({"language": "en"})
    first.set("theme", "dark")
    print("first:", first.get("theme"), first.get("language"))
    print("second:", second.get("theme"), second.get("language"))
    print("Типові значення:", Config.defaults)


if __name__ == "__main__":
    demo()
