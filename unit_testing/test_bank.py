import pytest
from bank import BankAccount


def test_create_account_success():
    account = BankAccount("Ravi", 1000)

    assert account.account_holder == "Ravi"
    assert account.balance == 1000


def test_create_account_with_zero_balance():
    account = BankAccount("Priya")

    assert account.balance == 0


def test_create_account_with_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("Arjun", -500)


def test_deposit_success():
    account = BankAccount("Ravi", 1000)

    final_balance = account.deposit(500)

    assert final_balance == 1500
    assert account.balance == 1500


def test_deposit_negative_amount():
    account = BankAccount("Ravi", 1000)

    with pytest.raises(ValueError):
        account.deposit(-100)


def test_deposit_zero_amount():
    account = BankAccount("Ravi", 1000)

    with pytest.raises(ValueError):
        account.deposit(0)


def test_withdraw_success():
    account = BankAccount("Ravi", 1000)

    final_balance = account.withdraw(300)

    assert final_balance == 700
    assert account.balance == 700


def test_withdraw_more_than_balance():
    account = BankAccount("Ravi", 1000)

    with pytest.raises(ValueError):
        account.withdraw(1500)


def test_withdraw_negative_amount():
    account = BankAccount("Ravi", 1000)

    with pytest.raises(ValueError):
        account.withdraw(-200)


def test_transfer_success():
    ravi = BankAccount("Ravi", 1000)
    priya = BankAccount("Priya", 500)

    ravi_balance = ravi.transfer(priya, 300)

    assert ravi_balance == 700
    assert ravi.balance == 700
    assert priya.balance == 800


def test_transfer_more_than_balance():
    ravi = BankAccount("Ravi", 1000)
    priya = BankAccount("Priya", 500)

    with pytest.raises(ValueError):
        ravi.transfer(priya, 1500)


def test_get_balance():
    account = BankAccount("Ravi", 1000)

    assert account.get_balance() == 1000