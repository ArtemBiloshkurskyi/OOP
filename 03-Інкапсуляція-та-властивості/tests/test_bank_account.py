import pytest

from bank_account import BankAccount


def test_deposit_and_withdraw_change_balance():
    account = BankAccount("Олена", 100)
    account.deposit(50)
    account.withdraw(30)
    assert account.balance == 120


def test_withdraw_whole_balance_is_allowed():
    account = BankAccount("Олена", 100)
    account.withdraw(100)
    assert account.balance == 0


def test_withdraw_more_than_balance_raises_error():
    account = BankAccount("Олена", 100)
    with pytest.raises(ValueError):
        account.withdraw(101)
    assert account.balance == 100
    assert account.history() == []


@pytest.mark.parametrize("amount", [0, -5, "10"])
def test_invalid_amount_raises_error(amount):
    account = BankAccount("Олена")
    with pytest.raises(ValueError):
        account.deposit(amount)
    with pytest.raises(ValueError):
        account.withdraw(amount)


def test_balance_is_read_only():
    account = BankAccount("Олена")
    with pytest.raises(AttributeError):
        account.balance = 1000


def test_history_returns_copy():
    account = BankAccount("Олена")
    account.deposit(10)
    account.history().append(("fake", 1))
    assert account.history() == [("deposit", 10)]


def test_invalid_owner_or_start_balance_raises_error():
    with pytest.raises(ValueError):
        BankAccount("")
    with pytest.raises(ValueError):
        BankAccount("Олена", -1)
