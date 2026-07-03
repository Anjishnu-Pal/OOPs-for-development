class BankAccount:
    def __init__(self, account_holder, balance=0):
        if balance < 0:
            raise ValueError("Opening balance cannot be negative")

        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        return self.balance

    def transfer(self, receiver_account, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")

        self.withdraw(amount)
        receiver_account.deposit(amount)

        return self.balance

    def get_balance(self):
        return self.balance