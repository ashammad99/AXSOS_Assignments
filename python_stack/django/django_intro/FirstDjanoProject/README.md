# Django Blogs Routing Practice

A simple Django project demonstrating URL routing, redirects, dynamic URL parameters, and JSON responses.

---

# Features

This project includes the following routes:

| Route | Description |
|---|---|
| `/` | Redirects to `/blogs/` |
| `/blogs/` | Displays all blogs placeholder |
| `/blogs/new/` | Displays form placeholder |
| `/blogs/create/` | Redirects to `/` |
| `/blogs/<number>/` | Displays a specific blog number |
| `/blogs/<number>/edit/` | Displays edit placeholder |
| `/blogs/<number>/delete/` | Redirects to `/blogs/` |
| `/blogs/json/` | Returns a JSON response |

---

# Project Structure

```text
mysite/
│
├── blogs/
│   ├── migrations/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── README.md