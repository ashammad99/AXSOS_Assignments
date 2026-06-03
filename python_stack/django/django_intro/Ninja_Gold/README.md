# Ninja Gold Game 🥷💰

A simple web application built using **Django** where players can earn or lose gold by visiting different buildings.

---

## Technologies Used

- Python
- Django
- HTML
- Sessions

---

## Project Structure

```
ninja_gold_django/
│
├── manage.py
├── ninja_gold/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── game/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── templates/
│       └── index.html
└── README.md
```

---

## Buildings Rules

| Building | Gold Range       |
|----------|-----------------|
| Farm     | 10 - 20 gold    |
| Cave     | 5 - 10 gold     |
| House    | 2 - 5 gold      |
| Casino   | -50 to 50 gold  |

---

## Installation

### 1. Create virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Install Django

```bash
pip install django
```

### 3. Apply migrations

```bash
python manage.py migrate
```

---

## Run the Application

```bash
python manage.py runserver
```

Application will run on:

```
http://127.0.0.1:8000/
```

---

## Key Differences from Flask Version

| Feature         | Flask               | Django                        |
|----------------|---------------------|-------------------------------|
| App factory     | `Flask(__name__)`   | `django-admin startproject`   |
| Routes          | `@app.route()`      | `urls.py` + `path()`          |
| Templates       | `render_template()` | `render(request, template)`   |
| Session         | `session['key']`    | `request.session['key']`      |
| CSRF protection | Manual              | Built-in `{% csrf_token %}`   |
| POST redirect   | `redirect('/')`     | `redirect('index')`           |

---

## Author

Ahmed Hammad
