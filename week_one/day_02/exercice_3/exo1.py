class BankAccount:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

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
account.display()

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
account.display()