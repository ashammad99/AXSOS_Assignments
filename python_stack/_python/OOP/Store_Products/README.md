# 📦 Store & Product Management System

A simple Python OOP project that simulates a store inventory system where products can be added, sold, and managed with price updates and discounts.

---

## 🚀 Features

### 🛒 Product Class
Each product has:
- Unique ID (auto-generated)
- Name
- Price
- Category

#### Methods:
- `update_price(percentage_change, is_increased)`  
  Increases or decreases the product price by a given percentage.
- `print_info()`  
  Displays product details (ID, name, category, price).

---

### 🏪 Store Class
The store manages a collection of products.

#### Methods:
- `add_product(product)`  
  Adds a product to the store.
- `sell_product(product_id)`  
  Removes a product by its unique ID and prints its info.
- `inflation(percent_increase)`  
  Increases the price of all products by a percentage.
- `set_clearance(category, percent_discount)`  
  Applies a discount to all products in a specific category.

---

## 🧠 Project Structure

Store_Products/
│
├── main.py
├── store.py
├── product.py
└── README.md

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Run the project:

```bash
python main.py