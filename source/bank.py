class BankAccount:
    def __init__(self, balance=0):
        if not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number")

        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.balance = balance

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if amount <= 0:
            raise ValueError("Deposit must be greater than zero")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount
        return self.balance