class User:
    # Constructor: runs when creating a new user
    def __init__(self, name, email):
        self.name = name              # store user's name
        self.email = email            # store user's email
        self.account_balance = 0      # start with 0 balance

    def make_withdrawal(self, amount):
        # Check if user has enough money
        if amount > self.account_balance:
            print("You don't have enough money")
            return False              # stop operation if not enough balance
        else:
            self.account_balance -= amount  # subtract amount from balance

    def make_deposit(self, amount):
        # Add money to user's account
        self.account_balance += amount

    def display_user_balance(self):
        # Show user's name and current balance
        print(f"Hi, {self.name} Your account balance is: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        # Transfer money to another user
        # First withdraw from current user
        if self.make_withdrawal(amount) == False:
            return                   # stop if withdrawal failed

        # Then deposit to the other user
        other_user.make_deposit(amount)


# Create user Ahmed
ahmed = User("Ahmed", "ashammad99@gmail.com")

ahmed.display_user_balance()   # should be 0
ahmed.make_deposit(100)        # add 100
ahmed.display_user_balance()   # should be 100

ahmed.make_withdrawal(200)     # not enough money
ahmed.display_user_balance()   # still 100

ahmed.make_withdrawal(50)      # valid withdrawal
ahmed.display_user_balance()   # should be 50


# Create another user Ali
ali = User("Ali", "ali@gmail.com")

# Transfer money from Ahmed to Ali
ahmed.transfer_money(ali, 20)


# Create third user Mohammed
mohammed = User("Mohammed", "mohammad99@gmail.com")
mohammed.make_deposit(500)

# Mohammed sends money to Ali
mohammed.transfer_money(ali, 250)


# Final balances
ahmed.display_user_balance()
ali.display_user_balance()
mohammed.display_user_balance()