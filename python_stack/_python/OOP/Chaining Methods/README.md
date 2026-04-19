# Simple Banking System (Method Chaining)

## 📌 Overview
This project is a simple Python banking system using a `User` class.
It supports method chaining to perform multiple operations in one line.

## ⚙️ Features
- Deposit money
- Withdraw money
- Transfer money between users
- Display account balance
- Method chaining (e.g. user.deposit().withdraw().display())

## 🧱 Class: User

### Attributes:
- name
- email
- account_balance (default = 0)

### Methods:
- make_deposit(amount)
- make_withdrawal(amount)
- transfer_money(other_user, amount)
- display_user_balance()

## 🔗 Method Chaining
All methods (except failure cases) return `self`, allowing:
```python
user.make_deposit(100).make_withdrawal(50).display_user_balance()