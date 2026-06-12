class BankAccount:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
        self.history = []
        self.add_to_history(f"Account created with balance {balance}€")

    def add_to_history(self, transaction):
        self.history.append(transaction)

    def __str__(self):
        return f"This is bank account '{self.title}' with a balance of {self.balance}€"

    def __repr__(self):
        return f"BankAccount('{self.title}', {self.balance})"

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        transaction = f"Deposited {amount}€. New balance: {self.balance}€"
        print(transaction)
        self.add_to_history(transaction)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if self.balance < amount:
            message = f"Failed withdrawal: tried to withdraw {amount}€ but only {self.balance}€ available"
            print("Not enough balance")
            self.add_to_history(message)
        else:
            self.balance -= amount
            transaction = f"Withdrew {amount}€. New balance: {self.balance}€"
            print(transaction)
            self.add_to_history(transaction)

    def display(self):
        print(f"Account Title: {self.title}")
        print(f"Balance: {self.balance}€")

    def show_history(self):
        print(f"\n--- Transaction History for {self.title} ---")
        for i, transaction in enumerate(self.history, 1):
            print(f"{i}. {transaction}")
        print("-" * 50)

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            raise TypeError(f"Cannot add BankAccount and {type(other).__name__}")

        new_title = f"{self.title} & {other.title}"
        new_balance = self.balance + other.balance

        merged_account = BankAccount(new_title, new_balance)

        merged_account.add_to_history(f"--- MERGED ACCOUNT ---")
        merged_account.add_to_history(f"Source account 1: {self.title} with {self.balance}€")
        merged_account.add_to_history(f"Source account 2: {other.title} with {other.balance}€")
        merged_account.add_to_history(f"Initial balance after merge: {new_balance}€")

        return merged_account


class SavingAccount(BankAccount):
    def __init__(self, title, balance, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(title, balance)
        self.add_to_history(f"Savings account created with {interest_rate}% interest rate")

    def __str__(self):
        return f"Savings account '{self.title}' - Balance: {self.balance}€ - Interest rate: {self.interest_rate}%"

    def __repr__(self):
        return f"SavingAccount('{self.title}', {self.balance}, {self.interest_rate})"

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        transaction = f"Added {interest:.2f}€ interest ({self.interest_rate}%). New balance: {self.balance}€"
        print(transaction)
        self.add_to_history(transaction)
        return interest

    def __add__(self, other):
        if isinstance(other, SavingAccount):
            new_title = f"{self.title} & {other.title}"
            new_balance = self.balance + other.balance
            avg_interest = (self.interest_rate + other.interest_rate) / 2
            merged_account = SavingAccount(new_title, new_balance, avg_interest)
            merged_account.add_to_history(f"Merged two savings accounts (avg rate: {avg_interest}%)")
            return merged_account
        else:
            return super().__add__(other)


print("=" * 60)
print("EXERCICE 21 - 22 : BankAccount de base")
print("=" * 60)

account1 = BankAccount("John Doe", 1000)
print(str(account1))
print(repr(account1))
print()

account1.display()
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)
account1.show_history()

print("\n" + "=" * 60)
print("EXERCICE 23 : SavingAccount avec intérêts")
print("=" * 60)

savings = SavingAccount("Alice", 2000, 5)
print(str(savings))
print(repr(savings))
print()

savings.display()
savings.deposit(500)
savings.add_interest()
savings.withdraw(300)
savings.add_interest()
savings.show_history()

print("\n" + "=" * 60)
print("EXERCICE 24 : Fusion de comptes avec l'opérateur +")
print("=" * 60)

account2 = BankAccount("Bob Martin", 500)
account3 = BankAccount("Charlie Dupont", 300)

print("Avant fusion:")
account2.display()
account3.display()

merged = account2 + account3
print("\nAprès fusion:")
merged.display()
merged.show_history()

print("\n" + "=" * 60)
print("Fusion de comptes épargne")
print("=" * 60)

savings1 = SavingAccount("Alice", 1500, 4)
savings2 = SavingAccount("Bob", 2500, 6)

print("Avant fusion:")
savings1.display()
savings2.display()

merged_savings = savings1 + savings2
print("\nCompte épargne fusionné:")
merged_savings.display()
print(f"Taux d'intérêt du compte fusionné: {merged_savings.interest_rate}%")
merged_savings.show_history()

print("\n" + "=" * 60)
print("Fusion d'un compte normal et d'un compte épargne")
print("=" * 60)

normal_account = BankAccount("Normal User", 1000)
savings_account = SavingAccount("Saver", 2000, 3)

print("Avant fusion:")
normal_account.display()
savings_account.display()

mixed_merge = normal_account + savings_account
print("\nCompte fusionné:")
mixed_merge.display()
mixed_merge.show_history()
