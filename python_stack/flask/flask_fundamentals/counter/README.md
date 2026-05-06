# Flask Counter & Session App

## 📌 Overview

This project is a simple web application built with **Flask** that demonstrates how to use **sessions** to track user-specific data.

The app tracks:

* Number of times a user visits the page
* A customizable counter value

It also includes additional features like increment controls, reset functionality, and session clearing.

---

## 🚀 Features

### ✅ Core Requirements

* Display how many times a user has visited the site
* Refresh the page to see the counter increase
* `/destroy_session` route to clear session data and redirect to home

---

### 🎯 Bonus Features

* ➕ Increment counter by 1
* ➕ Increment counter by 2
* 🔢 Increment counter by a custom value (user input)
* 🔄 Reset counter
* 📊 Display both:

  * Visit count
  * Counter value
* 🔐 Session stored in cookies (Flask signed cookies)

---

## 🛠️ Technologies Used

* Python 3
* Flask
* HTML + CSS
* Jinja2 Templating

---

## 📂 Project Structure

```
project/
│
├── app.py
└── templates/
    └── index.html
```

---

## ⚙️ Installation & Setup

### 1. Clone or Download the Project

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the App

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

### 🔹 Sessions

Flask uses sessions to store user data in cookies. Each user gets their own session.

Stored values:

* `visits`: counts page reloads
* `counter`: stores counter value

---

### 🔹 Routes

| Route               | Description                 |
| ------------------- | --------------------------- |
| `/`                 | Displays visits and counter |
| `/increment`        | Adds +1 to counter          |
| `/increment2`       | Adds +2 to counter          |
| `/increment_custom` | Adds user-defined value     |
| `/reset`            | Resets counter to 0         |
| `/destroy_session`  | Clears session completely   |

---

### 🔹 POST-Redirect-GET Pattern

After form submission, the app redirects to `/` to prevent duplicate submissions on refresh.

---

## 🔐 Cookie & Session Decoding (Advanced)

Flask stores session data in a **signed cookie**.

To decode it:

### Install tool:

```bash
pip install flask-unsign
```

### Decode:

```bash
flask-unsign --decode --cookie "YOUR_COOKIE_VALUE"
```

---

## ⚠️ Common Mistakes

* Forgetting to initialize session variables
* Not using `redirect()` after POST requests
* Typo in route (e.g. extra space in URL)
* Missing `secret_key`

---

## 💡 Future Improvements

* Add database persistence
* Add authentication (login/logout)
* Style UI with Bootstrap or Tailwind
* Add AJAX for smoother UX

---

## 📄 License

This project is open-source and free to use for learning purposes.

---

## 🙌 Author

Ahmed Hammad
