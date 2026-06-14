# Login & Registration

Simple Django authentication system with user registration and login.

## Setup

```bash
django-admin startproject login_and_registration
cd login_and_registration
python manage.py startapp users
mkdir -p users/templates/users
```

Copy files:
- `01_models.py` → `users/models.py`
- `CLEAN_views.py` → `users/views.py`
- `CLEAN_urls_app.py` → `users/urls.py`
- `CLEAN_login_reg.html` → `users/templates/users/login_reg.html`
- `CLEAN_success.html` → `users/templates/users/success.html`

Update `login_and_registration/settings.py`:
```python
INSTALLED_APPS = [..., 'users']
```

Update `login_and_registration/urls.py`:
```python
path('', include('users.urls'))
```

## Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit: http://localhost:8000/

## Features

- Register & Login
- Password encryption
- Email validation
- Session management
- Birthday validation