# ⚽ Sports ORM Assignment - Django ORM Queries

A comprehensive Django project demonstrating advanced ORM queries using a sports database with leagues, teams, and players.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Running the Application](#running-the-application)
- [The 16 Queries](#the-16-queries)
- [ORM Concepts](#orm-concepts)
- [Models](#models)
- [File Descriptions](#file-descriptions)
- [Troubleshooting](#troubleshooting)

---

## 📖 Project Overview

This assignment practices **advanced Django ORM queries** using a pre-built sports database. The application displays 16 different database queries that demonstrate various filtering, ordering, and exclusion techniques.

**Objectives:**
- ✅ Practice using `filter()` and `exclude()`
- ✅ Learn case-insensitive searches with `__icontains`
- ✅ Master ordering with `order_by()`
- ✅ Combine conditions using `Q` objects
- ✅ Display results on a beautiful HTML interface

---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Django 6.0+
- Git

### Step 1: Clone the Sports ORM Project
```bash
cd your-django-folder
git clone https://github.com/TheCodingDojo/sports_orm.git
cd sports_orm
```

### Step 2: Run Migrations
```bash
python manage.py migrate
```

### Step 3: Update Files

**Replace `leagues/views.py`:**
```bash
cp views_final.py leagues/views.py
```

**Replace `leagues/templates/leagues/index.html`:**
```bash
cp index_final.html leagues/templates/leagues/index.html
```

### Step 4: Run the Development Server
```bash
python manage.py runserver
```

### Step 5: View in Browser
Open: `http://127.0.0.1:8000/`

---

## 📁 Project Structure

```
sports_orm/
├── leagues/
│   ├── models.py          # League, Team, Player models
│   ├── views.py           # 16 ORM queries (UPDATED)
│   ├── urls.py            # URL routing
│   └── templates/
│       └── leagues/
│           └── index.html # Results display (UPDATED)
├── manage.py
├── db.sqlite3             # Database
└── README.md              # This file
```

---

## ▶️ Running the Application

### Start Development Server
```bash
python manage.py runserver
```

### Create Sample Data (if needed)
Visit: `http://127.0.0.1:8000/initialize`

### View Results
Visit: `http://127.0.0.1:8000/`

---

## 🏀 The 16 Queries

### **LEAGUES (Queries 1-6)**

#### 1️⃣ All Baseball Leagues
```python
League.objects.filter(sport="Baseball")
```
**ORM Method:** `filter()` with exact match

#### 2️⃣ All Women's Leagues
```python
League.objects.filter(name__icontains="Women")
```
**ORM Method:** `filter()` with `__icontains` (case-insensitive substring)

#### 3️⃣ All Hockey Leagues
```python
League.objects.filter(sport__icontains="Hockey")
```
**ORM Method:** `filter()` with `__icontains` (finds "Hockey", "Ice Hockey", etc.)

#### 4️⃣ Not Football Leagues
```python
League.objects.exclude(sport="Football")
```
**ORM Method:** `exclude()` - returns everything EXCEPT Football

#### 5️⃣ Conferences
```python
League.objects.filter(name__icontains="Conference")
```
**ORM Method:** `filter()` with substring search in name

#### 6️⃣ Atlantic Region Leagues
```python
League.objects.filter(name__icontains="Atlantic")
```
**ORM Method:** Searches league names containing "Atlantic"

---

### **TEAMS (Queries 7-12)**

#### 7️⃣ Dallas Teams
```python
Team.objects.filter(location__icontains="Dallas")
```
**ORM Method:** Case-insensitive location search

#### 8️⃣ Raptors Teams
```python
Team.objects.filter(team_name="Raptors")
```
**ORM Method:** Exact match on team name

#### 9️⃣ Teams with "City" in Location
```python
Team.objects.filter(location__icontains="City")
```
**ORM Method:** Substring search (finds "New York City", "Salt Lake City", etc.)

#### 🔟 Teams Starting with "T"
```python
Team.objects.filter(team_name__istartswith="T")
```
**ORM Method:** `__istartswith` - case-insensitive prefix match

#### 1️⃣1️⃣ Teams by Location (A-Z)
```python
Team.objects.all().order_by("location")
```
**ORM Method:** `order_by()` for ascending sort

#### 1️⃣2️⃣ Teams by Name (Z-A)
```python
Team.objects.all().order_by("-team_name")
```
**ORM Method:** `order_by("-field")` with hyphen for descending sort

---

### **PLAYERS (Queries 13-16)**

#### 1️⃣3️⃣ Players with Last Name "Cooper"
```python
Player.objects.filter(last_name="Cooper")
```
**ORM Method:** `filter()` on single field

#### 1️⃣4️⃣ Players with First Name "Joshua"
```python
Player.objects.filter(first_name="Joshua")
```
**ORM Method:** `filter()` on single field

#### 1️⃣5️⃣ Cooper Players (Except Joshua)
```python
Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
```
**ORM Method:** Chaining `filter()` and `exclude()` - AND logic

#### 1️⃣6️⃣ Alexander OR Wyatt
```python
Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt"))
```
**ORM Method:** `Q` objects with pipe `|` operator for OR logic

---

## 📚 ORM Concepts

### Filter Methods Used

| Method | Purpose | Example |
|--------|---------|---------|
| `filter()` | Get records matching criteria | `filter(sport="Baseball")` |
| `exclude()` | Get records NOT matching criteria | `exclude(sport="Football")` |
| `order_by()` | Sort results | `order_by("location")` |
| `order_by("-field")` | Reverse sort | `order_by("-team_name")` |

### Field Lookups

| Lookup | Meaning | Example |
|--------|---------|---------|
| `__exact` | Exact match (default) | `filter(name="MLB")` |
| `__icontains` | Case-insensitive substring | `filter(name__icontains="Women")` |
| `__istartswith` | Case-insensitive prefix | `filter(team_name__istartswith="T")` |
| `__in` | In a list | `filter(first_name__in=["John", "Jane"])` |

### Combining Queries

```python
# AND logic (chaining filters)
Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")

# OR logic (Q objects)
from django.db.models import Q
Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt"))

# Complex logic
Player.objects.filter(
    Q(first_name="Alexander") | Q(first_name="Wyatt")
).exclude(last_name="Smith")
```

---

## 🗄️ Models

### League Model
```python
class League(models.Model):
    name        # League name (e.g., "MLB", "NBA")
    sport       # Sport type (e.g., "Baseball", "Basketball")
    created_at  # Timestamp
    updated_at  # Timestamp
```

### Team Model
```python
class Team(models.Model):
    team_name   # Team name (e.g., "Yankees", "Lakers")
    location    # Location (e.g., "New York", "Los Angeles")
    league      # Foreign Key to League
    created_at  # Timestamp
    updated_at  # Timestamp
```

### Player Model
```python
class Player(models.Model):
    first_name  # Player's first name
    last_name   # Player's last name
    team        # Foreign Key to Team
    created_at  # Timestamp
    updated_at  # Timestamp
```

---

## 📄 File Descriptions

### `views_final.py` → `leagues/views.py`
The main view file containing:
- **16 ORM queries** demonstrating various filtering techniques
- Context dictionary with all query results
- Renders `index.html` template with query results

**Key Features:**
- ✅ Uses proper field names (`team_name` not `name`)
- ✅ Includes Q objects for OR logic
- ✅ Demonstrates chaining filters and excludes
- ✅ Case-insensitive searches with `__icontains`

### `index_final.html` → `leagues/templates/leagues/index.html`
Beautiful, responsive HTML template displaying:
- 16 query result cards in a grid layout
- Result counts for each query
- "No results found" messages for empty queries
- Legend explaining ORM methods
- Responsive design with CSS Grid

**Features:**
- 📱 Mobile-friendly responsive design
- 🎨 Beautiful purple gradient theme
- 🔍 Clear query titles with numbering
- 📊 Result count badges

---

## 🐛 Troubleshooting

### Error: "Cannot resolve keyword 'region'"
**Cause:** League model doesn't have a `region` field

**Solution:** Query 6 uses `name__icontains="Atlantic"` instead

### Error: "No results found" for all queries
**Cause:** Wrong field names in queries

**Solution:** Check that you're using:
- `team_name` (not `name`) for teams
- `sport` for leagues
- `first_name` and `last_name` for players

### Error: Module has no attribute 'make_data'
**Cause:** Replaced views.py without keeping other functions

**Solution:** Add back any other view functions from original `views.py`

### Results not displaying
**Cause:** Template variable names don't match context keys

**Solution:** Ensure variable names in template match exactly:
- `baseball_leagues` not `q1_baseball_leagues`
- `cooper_last_name` not `q13_cooper_last_name`

### Database is empty
**Solution:** Visit `http://127.0.0.1:8000/initialize` to populate data

---

## 📖 Learning Outcomes

After completing this assignment, you should understand:

✅ How to use `filter()` and `exclude()`  
✅ Case-insensitive searches with `__icontains`  
✅ Ordering results with `order_by()` and reverse sorting  
✅ Combining conditions with `Q` objects  
✅ Chaining multiple ORM methods  
✅ Reading Django ORM error messages  
✅ Debugging field name issues  

---

## 🔗 Useful Resources

- [Django ORM Documentation](https://docs.djangoproject.com/en/stable/topics/db/queries/)
- [QuerySet API Reference](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
- [Field Lookups](https://docs.djangoproject.com/en/stable/ref/models/querysets/#field-lookups)
- [Q Objects](https://docs.djangoproject.com/en/stable/topics/db/queries/#complex-lookups-with-q-objects)

---

## ✨ Summary

| Component | Details |
|-----------|---------|
| **Assignment** | Sports ORM - Advanced Queries |
| **Queries** | 16 different ORM queries |
| **Models** | League, Team, Player |
| **Key Concepts** | filter, exclude, Q objects, order_by |
| **Framework** | Django 6.0+ |
| **Database** | SQLite (sports_orm) |

---

## 📝 Notes

- All queries are case-insensitive where appropriate
- Results are displayed in real-time from the database
- The template uses Django template syntax for conditional rendering
- CSS Grid is used for responsive layout
- No external dependencies beyond Django

---

**Created:** 2026  
**Assignment:** AXSOS Academy - Django ORM  
**Status:** ✅ Complete

---

## 📧 Support

If you encounter any issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Verify field names in your models
3. Check Django console for error messages
4. Ensure database migrations have run: `python manage.py migrate`

Good luck! 🚀