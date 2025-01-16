class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    
    def get_balance(self):
        return self.__balance

# Create an object
acc = BankAccount("123456789", 5000)

# Deposit and withdraw
acc.deposit(1000)
acc.withdraw(2000)

# Access balance using a getter method
print(acc.get_balance())  # Output: 4000
