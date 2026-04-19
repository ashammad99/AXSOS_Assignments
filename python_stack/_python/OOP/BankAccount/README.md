# Bank Account System (Python)

## 📌 Overview
This project simulates a simple bank account system using Python.
It supports method chaining for performing multiple operations in one line.

## ⚙️ Features
- Deposit money
- Withdraw money
- Apply interest
- Display account balance
- Method chaining

## 🧱 Class: BankAccount

### Attributes:
- interest_rate: percentage of interest (default 1%)
- balance: current account balance

### Methods:
- deposit(amount)
- withdraw(amount)
- yield_interest()
- display_account_info()

## 🔗 Method Chaining Example
```python
account.deposit(100).withdraw(50).yield_interest().display_account_info()