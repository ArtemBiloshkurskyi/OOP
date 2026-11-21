AT_SIGN = "@"
DOT = "."


class Email:
    """Електронна адреса з перевіркою формату в сеттері."""

    def __init__(self, address):
        """Створює адресу; формат перевіряється сеттером."""
        self.address = address

    @property
    def address(self):
        """Повертає адресу повністю."""
        return f"{self._user}{AT_SIGN}{self._domain}"

    @address.setter
    def address(self, value):
        """Встановлює адресу; при помилці стара адреса не змінюється."""
        user, domain = self._parse(value)
        self._user = user
        self._domain = domain

    @property
    def user(self):
        """Повертає частину до @ (лише читання)."""
        return self._user

    @property
    def domain(self):
        """Повертає частину після @ (лише читання)."""
        return self._domain

    @staticmethod
    def _parse(address):
        """Розбиває адресу на user і domain або кидає ValueError."""
        if not isinstance(address, str) or address.count(AT_SIGN) != 1:
            raise ValueError("Адреса має містити рівно один символ @")
        user, domain = address.split(AT_SIGN)
        if not user or not domain:
            raise ValueError("Частини адреси не можуть бути порожніми")
        if (DOT not in domain
                or domain.startswith(DOT) or domain.endswith(DOT)):
            raise ValueError("Домен має містити крапку між частинами")
        return user, domain
