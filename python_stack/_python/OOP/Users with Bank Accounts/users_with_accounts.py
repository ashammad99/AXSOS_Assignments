class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self  # enables chaining

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5  # penalty
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        # apply interest only if balance > 0
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()  # composition (User HAS a BankAccount)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.balance}")
        return self


ahmed = User("Ahmed","ahmed@gmail.com")

# chaining operations
ahmed.make_deposit(100)\
     .make_deposit(50)\
     .make_withdrawal(30)\
     .display_user_balance()


class UserAccounts:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        # user has multiple accounts (checking + savings)
        self.accounts = {
            "checking": BankAccount(0.01, 0),
            "savings": BankAccount(0.02, 0)
        }

    def make_deposit(self, amount, account_type):
        self.accounts[account_type].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_type):
        self.accounts[account_type].withdraw(amount)
        return self

    def display_user_balance(self):
        # loop through all accounts
        for account in self.accounts:
            print(f"Hey, {self.name}, {account}, balance: ${self.accounts[account].balance}")
        return self


rami = UserAccounts("rami", "rami@gmail.com")

rami.make_deposit(500,"checking")\
     .make_deposit(300,"savings")\
     .make_withdrawal(200,"checking")\
     .display_user_balance()