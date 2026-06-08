# Users App - Django Project

A simple Django web application to display and add users using a database.

---

## Project Structure

```
your_project/
├── your_app/
│   ├── migrations/
│   ├── static/
│   │   └── users/
│   │       └── style.css
│   ├── templates/
│   │   └── users/
│   │       └── user_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── your_project/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

---

## Features

- Display all users in a table
- Add a new user using a form on the same page
- Data is saved to the database

---

## Setup & Installation

### 1. Activate your virtual environment

```bash
source djangoPy3Env/bin/activate        # Mac/Linux
djangoPy3Env\Scripts\activate           # Windows
```

### 2. Install Django

```bash
pip install django
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Server

```bash
python manage.py runserver
```

### 5. Open in Browser

```
http://127.0.0.1:8000/
```

---

## URLs

| URL     | View        | Description              |
|---------|-------------|--------------------------|
| `/`     | user_list   | Display all users + form |
| `/add/` | add_user    | Process form & save user |

---

## Models

```python
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField()
    age        = models.IntegerField()
```

---

## Requirements

- Python 3.x
- Django 4.x or higher