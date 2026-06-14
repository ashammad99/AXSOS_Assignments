# Courses Management System

A Django web application for managing bootcamp courses with full CRUD functionality and a comments system.

## Features

- ✅ Create new courses (name > 5 chars, description > 15 chars)
- ✅ View all courses in a table
- ✅ Delete courses with confirmation
- ✅ Add comments to each course
- ✅ View all comments for a course
- ✅ One-to-One relationship for descriptions (NINJA BONUS)

## Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Django
```bash
pip install django
```

### 3. Create Project & App
```bash
django-admin startproject courses_project
cd courses_project
python manage.py startapp courses
```

### 4. Add App to settings.py
```python
INSTALLED_APPS = [
    ...
    'courses',
]
```

### 5. Create Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Server
```bash
python manage.py runserver
```

Visit: **http://localhost:8000/**

## Models

### Course
- **name**: CharField (max 200, required)
- **description**: OneToOne relationship to DescriptionModel
- **created_at**: Auto timestamp

### DescriptionModel
- **text**: TextField
- **created_at**: Auto timestamp

### Comment
- **course**: ForeignKey to Course
- **text**: TextField
- **created_at**: Auto timestamp

## Validation Rules

| Field | Min Length | Required |
|-------|-----------|----------|
| Course Name | > 5 chars | Yes |
| Description | > 15 chars | Yes |
| Comment | > 5 chars | Yes |

## Usage

### Add a Course
1. Go to home page
2. Fill in name and description
3. Click "Add"

### Delete a Course
1. Click "remove" link
2. Confirm deletion on next page

### Add Comments
1. Click "comments" link on any course
2. Enter comment (min 5 chars)
3. View all comments below

## File Structure

```
courses_project/
├── courses_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── courses/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/courses/
│       ├── base.html
│       ├── index.html
│       ├── delete_confirmation.html
│       └── comments.html
└── manage.py
```

## Routes

| URL | View | Action |
|-----|------|--------|
| `/` | index | Show all courses & add form |
| `/add/` | add_course | Create course |
| `/delete/<id>/` | delete_confirmation | Confirm delete |
| `/destroy/<id>/` | delete_course | Delete course |
| `/comments/<id>/` | course_comments | View comments |
| `/comments/<id>/add/` | add_comment | Add comment |

## Admin Panel

Create superuser:
```bash
python manage.py createsuperuser
```

Access: http://localhost:8000/admin/

## Bonus Features

✅ **NINJA BONUS 1**: Description as one-to-one relationship  
✅ **NINJA BONUS 2**: Comments system for each course

## Technologies

- Django 6.0+
- Python 3.8+
- SQLite Database
- HTML5 & CSS3

## Error Handling

- Invalid course name displays error message
- Invalid description displays error message
- Form data persists on error
- Success messages on completion