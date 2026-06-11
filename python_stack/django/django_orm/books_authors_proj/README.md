# Books & Authors Django Project - Summary

## Project Overview
This project demonstrates a Django application with a Many-to-Many relationship between Books and Authors, using SQLite as the database.

## Project Structure
```
books_authors_proj/
├── books_authors_proj/        # Main project folder
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL configuration
│   ├── wsgi.py               # WSGI configuration
│   └── asgi.py               # ASGI configuration
├── books_authors_app/        # Main application
│   ├── models.py             # Models (Book, Author)
│   ├── admin.py              # Admin configuration
│   ├── views.py              # Views
│   ├── tests.py              # Tests
│   └── migrations/           # Database migrations
├── manage.py                 # Django management script
└── db.sqlite3                # SQLite database
```

## Models Created

### Book Model
- **id**: Auto-generated primary key (INT)
- **title**: CharField (max_length=255) - Book title
- **desc**: CharField (max_length=45) - Brief description
- **authors**: ManyToManyField - Relationship to Author model

### Author Model
- **id**: Auto-generated primary key (INT)
- **first_name**: CharField (max_length=255) - Author's first name
- **last_name**: CharField (max_length=255) - Author's last name
- **notes**: TextField (optional) - Additional notes about the author

## Database Relationships
The application uses Django's built-in ManyToMany relationship, which automatically creates a junction table:
- `books_authors_app_book_authors` - Links books to authors

## Completed Tasks

### 1. Project Setup ✓
- Created Django project: `books_authors_proj`
- Created Django app: `books_authors_app`
- Added app to INSTALLED_APPS in settings.py

### 2. Models ✓
- Created Book model with id, title, desc, and authors (M2M)
- Created Author model with id, first_name, last_name, and notes fields
- Defined __str__ methods for readable representations

### 3. Migrations ✓
- Created initial migrations for Book and Author models
- Ran migrations to create database tables
- Notes field was included in the initial Author model

### 4. Data Operations ✓

#### Initial Data Creation
- Created 5 books: C Sharp, Java, Python, PHP, Ruby
- Created 5 authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu

#### Data Modifications
- Changed book name "C Sharp" to "C#"
- Changed author name "William Shakespeare" to "Bill Shakespeare"

#### Relationship Management
- Assigned authors to books following specified patterns
- Removed relationships as needed
- Added new relationships

#### Data Retrieval
- Retrieved authors for specific books
- Retrieved books for specific authors
- All queries executed and saved

## Query Results Summary

### Final Database State

**Books with Authors:**
1. C# - Jane Austen, Emily Dickinson, Fyodor Dostoevsky, Bill Shakespeare
2. Java - Jane Austen, Emily Dickinson, Fyodor Dostoevsky, Bill Shakespeare, Lau Tzu
3. Python - Emily Dickinson, Fyodor Dostoevsky, Bill Shakespeare
4. PHP - Fyodor Dostoevsky, Bill Shakespeare
5. Ruby - Bill Shakespeare

**Authors with Books:**
1. Jane Austen - C#, Java
2. Emily Dickinson - C#, Java, Python
3. Fyodor Dostoevsky - C#, Java, Python, PHP
4. Bill Shakespeare - C#, Java, Python, PHP, Ruby
5. Lau Tzu - Java

## How to Run

### Start Django Shell
```bash
cd books_authors_proj
python manage.py shell
```

### Example Queries in Django ORM

```python
# Import models
from books_authors_app.models import Book, Author

# Get all books
Book.objects.all()

# Get specific book
book = Book.objects.get(id=1)

# Get authors for a book
book.authors.all()

# Get books for an author
author = Author.objects.get(id=1)
author.books.all()

# Add author to book
book.authors.add(author)

# Remove author from book
book.authors.remove(author)

# Create new book
Book.objects.create(title="New Book", desc="Description")

# Update book
book.title = "Updated Title"
book.save()
```

## Files Generated
- `queries.txt` - Contains all executed queries and their results
- `PROJECT_SUMMARY.md` - This file

## Database Engine
- **Type**: SQLite3
- **File**: `db.sqlite3`
- **Location**: Project root directory

## Django Version
- Django 6.0.6
- Python 3.x compatible