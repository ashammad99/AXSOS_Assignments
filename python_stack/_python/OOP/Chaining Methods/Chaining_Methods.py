class User:
    # NOTE: must be __init__ (constructor), not init
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_withdrawal(self, amount):
        if amount > self.account_balance:
            print("You don't have enough money")
            return False   # needed to stop transfer if insufficient
        else:
            self.account_balance -= amount
            return self    # enables method chaining

    def make_deposit(self, amount):
        self.account_balance += amount
        return self        # enables chaining

    def display_user_balance(self):
        print(f"Hi, {self.name} Your account balance is: {self.account_balance}")
        return self        # enables chaining

    def transfer_money(self, other_user, amount):
        # ⚠️ No check here → transfer still happens even if withdrawal fails
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


ahmed = User("Ahmed", "ashammad99@gmail.com")

# chaining multiple operations together
ahmed.display_user_balance()\
     .make_deposit(100)\
     .display_user_balance()\
     .make_withdrawal(50)\
     .display_user_balance()

ali = User("Ali", "ali@gmail.com")
ahmed.transfer_money(ali, 20)

mohammed = User("Mohammed", "mohammad99@gmail.com")
mohammed.make_deposit(500).transfer_money(ali, 250)

ahmed.display_user_balance()
ali.display_user_balance()
mohammed.display_user_balance()