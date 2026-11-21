import hashlib
import hmac
import os

MIN_LENGTH = 8
SALT_BYTES = 16
HASH_NAME = "sha256"
ITERATIONS = 100000


class Password:
    """Зберігає сіль і хеш пароля; сам пароль прочитати неможливо."""

    def __init__(self, password):
        """Створює об'єкт і одразу зберігає хеш початкового пароля."""
        self._salt = b""
        self._hash = b""
        self.set(password)

    def set(self, new_password):
        """Замінює пароль; він має містити щонайменше 8 символів."""
        if not isinstance(new_password, str):
            raise ValueError("Пароль має бути рядком")
        if len(new_password) < MIN_LENGTH:
            raise ValueError("Пароль має містити щонайменше 8 символів")
        self._salt = os.urandom(SALT_BYTES)
        self._hash = self._make_hash(new_password, self._salt)

    def check(self, candidate):
        """Повертає True, якщо candidate збігається зі збереженим паролем."""
        if not isinstance(candidate, str):
            return False
        candidate_hash = self._make_hash(candidate, self._salt)
        return hmac.compare_digest(candidate_hash, self._hash)

    @staticmethod
    def _make_hash(password, salt):
        """Повертає хеш пароля, змішаного із сіллю."""
        data = password.encode()
        return hashlib.pbkdf2_hmac(HASH_NAME, data, salt, ITERATIONS)
