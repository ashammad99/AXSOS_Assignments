# 🍓 Dojo Fruit Store

A simple Flask web application that allows students to order fruits and get a checkout summary charged to their student account.

---

## 📁 Project Structure

```
project/
│
├── server.py
├── static/
│   └── css/
│       └── bootstrap.css
└── templates/
    ├── index.html
    ├── checkout.html
    └── fruits.html
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/dojo-fruit-store.git
   cd dojo-fruit-store
   ```

2. **Install Flask**
   ```bash
   pip install flask
   ```

3. **Run the app**
   ```bash
   python server.py
   ```

4. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

---

## 📄 Pages & Routes

| Route       | Method     | Description                        |
|-------------|------------|------------------------------------|
| `/`         | GET        | Home page with order form          |
| `/checkout` | POST       | Checkout summary page              |
| `/fruits`   | GET        | Display available fruits with images |

---

## ⚙️ Features

- Order fruits (Strawberry, Raspberry, Apple) with quantity selection
- Enter student info (First Name, Last Name, Student ID)
- View order summary on checkout page
- Displays total items ordered and timestamp of order
- Terminal print: `Charging <name> for <count> fruits.`

---

## ⚠️ Known Behavior

Refreshing the `/checkout` page will **re-submit the POST request**, causing:
- The order to be "processed" again
- The print statement to run again in the terminal

This is expected behavior without using sessions or the POST/Redirect/GET pattern.

---

## 🛠️ Built With

- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [Bootstrap](https://getbootstrap.com/) - Frontend styling
- [Jinja2](https://jinja.palletsprojects.com/) - HTML templating engine

---

## 👨‍💻 Author

Made as part of a Coding Dojo assignment.
