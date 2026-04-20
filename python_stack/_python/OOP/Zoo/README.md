# Zoo Management System (Python OOP)

## 📌 Overview
This project simulates a zoo system using Object-Oriented Programming.

It demonstrates:
- Inheritance
- Polymorphism
- Method overriding

## 🧱 Classes

### 1. Animal (Base Class)
Common properties:
- name
- age
- health_level
- happiness_level

Methods:
- feed()
- display_info()

### 2. Animal Types (Inheritance)
Each animal overrides the `feed()` method:
- Lion
- Tiger
- Monkey
- Bear

### 3. Zoo
Manages all animals:
- add_animal(animal)
- feed_all()
- print_all_info()

## ⚙️ Features
- Add animals to zoo
- Feed all animals (polymorphism)
- Display all animal info

## 🔑 Key Concepts
- Inheritance (Animal → Lion, Tiger, etc.)
- Polymorphism (different feed() behavior)
- Encapsulation (data inside objects)

## ▶️ Example
```python
zoo.feed_all()
zoo.print_all_info()