# Dojo & Ninjas Project

A Django project practicing one-to-many relationships and ORM queries using the Django Shell.

---

## Project Structure

```
dojo_ninjas_proj/
├── dojo_ninjas_proj/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dojo_ninjas_app/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── queries.txt
├── db.sqlite3
└── manage.py
```

---

## Models

### Dojo
| Field | Type | Description |
|-------|------|-------------|
| `id` | INT (auto) | Primary key |
| `name` | VARCHAR(255) | Name of the dojo |
| `city` | VARCHAR(255) | City where dojo is located |
| `state` | VARCHAR(2) | State abbreviation |
| `desc` | TextField | Description (default: "old dojo") |
| `created_at` | DateTime | Auto-set on creation |
| `updated_at` | DateTime | Auto-updated on save |

### Ninja
| Field | Type | Description |
|-------|------|-------------|
| `id` | INT (auto) | Primary key |
| `dojo` | ForeignKey | References Dojo (CASCADE) |
| `first_name` | VARCHAR(255) | Ninja's first name |
| `last_name` | VARCHAR(255) | Ninja's last name |
| `created_at` | DateTime | Auto-set on creation |
| `updated_at` | DateTime | Auto-updated on save |

---

## Relationship

```
Dojo (one) ──────► Ninja (many)
```

- One dojo can have **many ninjas**
- Each ninja belongs to **one dojo**
- Access ninjas from dojo: `dojo.ninjas.all()`
- Access dojo from ninja: `ninja.dojo`

---

## Setup & Installation

```bash
# 1. Clone or navigate to project
cd dojo_ninjas_proj

# 2. Activate virtual environment
source djangoPy3Env/bin/activate       # Mac/Linux
djangoPy3Env\Scripts\activate          # Windows

# 3. Install Django
pip install django

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start server
python manage.py runserver
```

---

## Shell Queries

Open the Django shell:
```bash
python manage.py shell
```

### Import Models
```python
from dojo_ninjas_app.models import Dojo, Ninja
```

### Create 3 Dojos
```python
Dojo.objects.create(name="Dojo Alpha", city="New York", state="NY")
Dojo.objects.create(name="Dojo Beta", city="Los Angeles", state="CA")
Dojo.objects.create(name="Dojo Gamma", city="Chicago", state="IL")
```

### Delete the 3 Dojos
```python
Dojo.objects.all().delete()
```

### Create 3 More Dojos
```python
Dojo.objects.create(name="Dojo One", city="Austin", state="TX")
Dojo.objects.create(name="Dojo Two", city="Seattle", state="WA")
Dojo.objects.create(name="Dojo Three", city="Miami", state="FL")
```

### Create 3 Ninjas per Dojo
```python
# First dojo
first_dojo = Dojo.objects.first()
Ninja.objects.create(dojo=first_dojo, first_name="Ali", last_name="Hassan")
Ninja.objects.create(dojo=first_dojo, first_name="Sara", last_name="Ahmad")
Ninja.objects.create(dojo=first_dojo, first_name="Omar", last_name="Khalid")

# Second dojo
second_dojo = Dojo.objects.all()[1]
Ninja.objects.create(dojo=second_dojo, first_name="Lena", last_name="Smith")
Ninja.objects.create(dojo=second_dojo, first_name="Jake", last_name="Brown")
Ninja.objects.create(dojo=second_dojo, first_name="Mia", last_name="Davis")

# Third dojo
third_dojo = Dojo.objects.last()
Ninja.objects.create(dojo=third_dojo, first_name="Zaid", last_name="Nasser")
Ninja.objects.create(dojo=third_dojo, first_name="Hana", last_name="Yousef")
Ninja.objects.create(dojo=third_dojo, first_name="Nour", last_name="Salem")
```

### Retrieve Ninjas
```python
# All ninjas from first dojo
Dojo.objects.first().ninjas.all()

# All ninjas from last dojo
Dojo.objects.last().ninjas.all()

# Last ninja's dojo
Ninja.objects.last().dojo
```

### After Adding `desc` Field — Create New Dojo
```python
Dojo.objects.create(name="Dojo New", city="Denver", state="CO", desc="new dojo")
```

---

## Migrations (Adding `desc` Field)

1. Add `desc` to `Dojo` model in `models.py`:
```python
desc = models.TextField(default="old dojo")
```

2. Run:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Key ORM Commands Reference

| Action | Command |
|--------|---------|
| Get all | `Model.objects.all()` |
| Get one | `Model.objects.get(id=1)` |
| Filter | `Model.objects.filter(field=value)` |
| Create | `Model.objects.create(field=value)` |
| Delete all | `Model.objects.all().delete()` |
| First record | `Model.objects.first()` |
| Last record | `Model.objects.last()` |
| Reverse lookup | `dojo.ninjas.all()` |

---

## Technologies Used

- Python 3
- Django
- SQLite3