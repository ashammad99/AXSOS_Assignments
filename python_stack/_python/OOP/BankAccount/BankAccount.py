class BankAccount:
    # ⚠️ must be __init__ (constructor), not init
    def __init__(self, interest_rate=0.01, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self        # enables method chaining

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5   # penalty fee
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self        # enables chaining

    def yield_interest(self):
        # apply interest only if balance is positive
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self


account1 = BankAccount(0.02, 100)
account2 = BankAccount(0.03, 200)

# chaining multiple operations
account1.deposit(50).deposit(25).deposit(75)\
        .withdraw(100).yield_interest().display_account_info()

account2.deposit(100).deposit(50)\
        .withdraw(50).withdraw(25).withdraw(300).withdraw(25)\
        .yield_interest().display_account_info()