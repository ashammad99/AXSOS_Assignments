# Banking System with Multiple Accounts (Python)

## 📌 Overview
This project simulates a banking system using Object-Oriented Programming (OOP).

It includes:
- Single account per user
- Multiple accounts per user (checking & savings)
- Method chaining
- Interest calculation

## 🧱 Classes

### 1. BankAccount
Handles core banking logic:
- deposit(amount)
- withdraw(amount)
- yield_interest()
- display_account_info()

### 2. User
Represents a user with ONE bank account.
- Uses composition (User HAS a BankAccount)

### 3. UserAccounts
Represents a user with MULTIPLE accounts:
- checking account
- savings account

## ⚙️ Features
- Deposit & withdraw money
- Penalty fee if insufficient funds
- Apply interest
- Multiple accounts per user
- Method chaining

## 🔗 Example Usage
```python
user.make_deposit(100).make_withdrawal(50).display_user_balance()