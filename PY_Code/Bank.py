class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

account = BankAccount(100)
print("Balance after deposit:", account.deposit(50))  # Output: Balance after deposit: 150
print("Balance after withdrawal:", account.withdraw(30))  # Output: Balance after withdrawal: 120
