# 👥 Flask Users List App (with Bootstrap)

A simple Flask web application that displays a list of users using **Jinja2 templates** and **Bootstrap** for styling.

---

## 🚀 Features

* Display a list of users dynamically
* Clean UI using Bootstrap
* Uses Jinja2 templating engine
* Easy to extend (e.g., connect to database)

---

## 📁 Project Structure

```
project/
│── app.py
│── templates/
│   └── users.html
│── static/
│   └── (optional CSS/JS files)
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-users-app.git
cd flask-users-app
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install flask
```

---

## ▶️ Running the App

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000/users
```

---

## 🌐 Route

### Users List

```
/users
```

Displays a table or list of users with:

* First Name
* Last Name

---

## 🧠 How It Works

* A list of users is defined in the backend (`app.py`)
* Data is passed to the `users.html` template
* Jinja2 loops through the list and renders each user
* Bootstrap is used for styling the UI

---

## 🎨 Bootstrap Example (users.html)

Example snippet:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Users</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h2 class="mb-4">Users List</h2>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
            <tr>
                <td>{{ user.first_name }}</td>
                <td>{{ user.last_name }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
</body>
</html>
```

---

## 🛠️ Technologies Used

* Python
* Flask
* Jinja2
* Bootstrap 5

---

## 📌 Future Improvements

* Connect to a database (MySQL / SQLite)
* Add CRUD operations (Create, Read, Update, Delete)
* Add user authentication

---

## 📄 License

This project is open-source and intended for educational purposes.
