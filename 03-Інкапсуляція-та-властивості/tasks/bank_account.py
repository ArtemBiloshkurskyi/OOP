DEPOSIT = "deposit"
WITHDRAWAL = "withdrawal"
NO_MONEY = 0


class BankAccount:
    """Банківський рахунок із власником, балансом та історією операцій."""

    def __init__(self, owner, balance=NO_MONEY):
        """Створює рахунок; початковий баланс не може бути від'ємним."""
        if not isinstance(owner, str) or not owner:
            raise ValueError("Власник має бути непорожнім рядком")
        if not isinstance(balance, (int, float)) or balance < NO_MONEY:
            raise ValueError("Початковий баланс має бути числом >= 0")
        self._owner = owner
        self._balance = balance
        self._history = []

    @property
    def owner(self):
        """Повертає ім'я власника (лише читання)."""
        return self._owner

    @property
    def balance(self):
        """Повертає поточний баланс (лише читання)."""
        return self._balance

    def deposit(self, amount):
        """Поповнює рахунок на додатну суму."""
        self._ensure_positive(amount)
        self._balance += amount
        self._history.append((DEPOSIT, amount))

    def withdraw(self, amount):
        """Знімає кошти; баланс не може стати нижчим за нуль."""
        self._ensure_positive(amount)
        if amount > self._balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self._balance -= amount
        self._history.append((WITHDRAWAL, amount))

    def history(self):
        """Повертає копію списку операцій."""
        return list(self._history)

    @staticmethod
    def _ensure_positive(amount):
        """Перевіряє, що сума є додатним числом."""
        if not isinstance(amount, (int, float)) or amount <= NO_MONEY:
            raise ValueError("Сума має бути додатним числом")
