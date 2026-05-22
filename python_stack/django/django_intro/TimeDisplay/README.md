# Time Display — Django Assignment

A Django project that displays the current date and time at the root route, built as a learning exercise for Django project setup, template rendering, and static files.

---

## Project Structure

```
time_project/
├── manage.py
├── time_project/               # Project configuration
│   ├── settings.py
│   └── urls.py
└── time_display/               # Main app
    ├── views.py                # Controller — fetches and passes time data
    ├── urls.py                 # App-level routes
    ├── templates/
    │   └── index.html          # Template that renders the time
    └── static/
        └── css/
            └── style.css       # Custom stylesheet
```

---

## Setup & Installation

**Requirements:** Python 3.9+

```bash
# 1. Clone or unzip the project
cd time_project

# 2. Install Django
pip install django

# 3. Run the development server
python manage.py runserver
```

Then open your browser to:
- `http://localhost:8000/` — root route
- `http://localhost:8000/time_display/` — same view, alternate URL

---

## How It Works

### 1. Routing (`urls.py`)

The project-level `urls.py` maps both `/` and `/time_display/` to the `time_display` app:

```python
path('', include('time_display.urls')),
path('time_display/', include('time_display.urls')),
```

### 2. Controller (`views.py`)

The `index` view fetches the current time and passes it to the template via a context dictionary:

```python
from django.shortcuts import render
from datetime import datetime
import zoneinfo

def index(request):
    tz = zoneinfo.ZoneInfo("UTC")
    now = datetime.now(tz)

    context = {
        "time": now.strftime("%I:%M %p"),
        "date": now.strftime("%A, %B %d, %Y"),
        "seconds": now.strftime("%S"),
        "timezone": "UTC",
        "unix_timestamp": int(now.timestamp()),
    }
    return render(request, 'index.html', context)
```

### 3. Template (`index.html`)

The template receives the context and displays the values using Django's template syntax:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">

<span>{{ time }}</span>
<span>{{ date }}</span>
<span>{{ timezone }}</span>
<span>{{ unix_timestamp }}</span>
```

### 4. Static Files (`style.css`)

The custom stylesheet is loaded via `{% load static %}` and `{% static %}` template tags. Django serves static files from each app's `static/` folder when `APP_DIRS` is enabled in `settings.py` and `django.contrib.staticfiles` is in `INSTALLED_APPS`.

---

## Two Ways Time Is Retrieved

### Server-side (Python — `views.py`)
Uses Python's `datetime` module with `zoneinfo` for timezone-aware time. This runs once when the page loads and is baked into the HTML sent to the browser.

### Client-side (JavaScript — `index.html`)
A live clock updates every second using the browser's `Date` object, so the displayed time ticks forward without requiring a page reload:

```javascript
function updateClock() {
    const now = new Date();
    // formats and updates the DOM every second
}
setInterval(updateClock, 1000);
```

This is the **Ninja Bonus** — two separate methods working together.

---

## Objectives Covered

| Objective | How |
|---|---|
| Django project setup | `django-admin startproject` + `startapp time_display` |
| Passing data to a template | `context` dict passed to `render()` in `views.py` |
| Connecting static files | `{% load static %}` + `{% static 'css/style.css' %}` in template |
| Ninja Bonus | `datetime` + `zoneinfo` instead of `gmtime/strftime`; plus live JS clock |

---

## Notes on Time Zones

The project uses UTC as configured in `settings.py`:

```python
TIME_ZONE = 'UTC'
USE_TZ = True
```

To change the display timezone, update `zoneinfo.ZoneInfo("UTC")` in `views.py` to any valid IANA timezone string, for example `"America/New_York"` or `"Asia/Jerusalem"`.
