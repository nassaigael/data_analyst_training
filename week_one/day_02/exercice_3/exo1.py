class BankAccount:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def __str__(self):
        return f"This is bank account {self.title} with a balance of {self.balance}"

    def __repr__(self):
        return f"BankAccount('{self.title}', {self.balance})"

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display(self):
        print(f"Account Title: {self.title}")
        print(f"Balance: {self.balance}")

# Example usage:
account = BankAccount("John Doe", 1000)
print(str(account))
print(repr(account))

account.display()

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
account.display()