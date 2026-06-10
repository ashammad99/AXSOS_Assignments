# 🥋 Dojo Ninja Management System

A Django web application for managing dojos (martial arts schools) and their ninja students. Create, view, and delete dojos while managing the ninjas associated with each dojo.

## Features

✅ **Create Dojos** - Add new dojos with name, city, and state information  
✅ **Manage Ninjas** - Add ninjas to specific dojos  
✅ **View All Dojos** - See all dojos and their associated ninjas in one place  
✅ **Delete Dojos** - Remove dojos and cascade delete all associated ninjas  
✅ **Ninja Count** - View the number of ninjas at each dojo  
✅ **Responsive Design** - Mobile-friendly interface  

## Project Structure

```
dojo_app/
├── models.py          # Database models (Dojo, Ninja)
├── views.py           # View functions (routes/handlers)
├── urls.py            # URL routing configuration
├── templates/
│   └── dojo_app/
│       └── index.html # Main template with styled interface
└── migrations/        # Database migrations
```

## Installation

### Prerequisites
- Python 3.8+
- Django 3.2+
- pip (Python package manager)

### Setup Steps

1. **Clone or create your Django project:**
   ```bash
   django-admin startproject dojo_project
   cd dojo_project
   ```

2. **Create a Django app:**
   ```bash
   python manage.py startapp dojo_app
   ```

3. **Add the app to `INSTALLED_APPS` in `settings.py`:**
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'dojo_app',  # Add this
   ]
   ```

4. **Create the models** (copy code from Models section below)

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Add the template and routes** (see sections below)

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the app:**
   ```
   http://localhost:8000/
   ```

## Models

### Dojo Model
```python
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
```

- **name**: The dojo's name (e.g., "Golden Dragon Dojo")
- **city**: City where the dojo is located
- **state**: State/region where the dojo is located

### Ninja Model
```python
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE, related_name='ninjas')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

- **first_name**: Ninja's first name
- **last_name**: Ninja's last name
- **dojo**: Foreign key reference to a Dojo (automatically deletes ninjas when dojo is deleted)

## Routes & Views

### View Functions

#### `index(request)`
- **Route**: `/`
- **Method**: GET
- **Purpose**: Display the main page with forms and all dojos
- **Returns**: Renders `index.html` with list of all dojos and their ninjas

#### `create_dojo(request)`
- **Route**: `/create_dojo`
- **Method**: POST
- **Purpose**: Create a new dojo
- **Form Fields**: 
  - `name` (required)
  - `city` (required)
  - `state` (required)
- **Redirects**: Back to home page

#### `create_ninja(request)`
- **Route**: `/create_ninja`
- **Method**: POST
- **Purpose**: Create a new ninja and assign to a dojo
- **Form Fields**:
  - `first_name` (required)
  - `last_name` (required)
  - `dojo` (required - dropdown)
- **Redirects**: Back to home page

#### `delete_dojo(request, dojo_id)` - NINJA BONUS
- **Route**: `/delete_dojo/<dojo_id>`
- **Method**: POST
- **Purpose**: Delete a dojo and all associated ninjas
- **Parameters**: 
  - `dojo_id`: The ID of the dojo to delete
- **Redirects**: Back to home page

## URL Configuration

Add this to your `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_dojo', views.create_dojo, name='create_dojo'),
    path('create_ninja', views.create_ninja, name='create_ninja'),
    path('delete_dojo/<int:dojo_id>', views.delete_dojo, name='delete_dojo'),
]
```

Then include in your project's main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dojo_app.urls')),
]
```

## Features Breakdown

### Basic Features

**Add Dojo Form**
- Create a new dojo with name, city, and state
- Submit via the "Add" button
- Automatically added to the database

**Add Ninja Form**
- Add a new ninja student
- Select which dojo they belong to from dropdown
- Dropdown is dynamically populated with all existing dojos

**View All Dojos**
- Displays each dojo in a card layout
- Shows dojo name, location (city, state)
- Lists all ninjas at that dojo

### Bonus Features

#### 🥋 NINJA BONUS: Delete Dojo
- Red delete button on each dojo card
- Clicking deletes the dojo and ALL associated ninjas
- Cascading delete configured in the Ninja model: `on_delete=models.CASCADE`
- Confirmation dialog prevents accidental deletion

#### 🎓 SENSEI BONUS: Ninja Count
- Shows the count of ninjas at each dojo
- Displayed in the dojo header as a badge
- Uses Django ORM: `dojo.ninjas.count`
- Updates in real-time as ninjas are added/deleted

## Usage Examples

### Creating a Dojo
1. Fill in the "Add a Dojo" form with:
   - Name: "Golden Dragon Dojo"
   - City: "San Francisco"
   - State: "California"
2. Click "Add"
3. Dojo appears in the list below

### Adding a Ninja
1. Fill in the "Add a Ninja" form with:
   - First Name: "Ahmed"
   - Last Name: "Hammad"
   - Dojo: Select from dropdown
2. Click "Add"
3. Ninja appears under their assigned dojo

### Deleting a Dojo
1. Locate the dojo you want to delete
2. Click the red "Delete Dojo" button
3. Confirm deletion in the popup
4. Dojo and all associated ninjas are removed from the database

## Template Features

The enhanced template (`index.html`) includes:

- **Responsive Design**: Works on mobile, tablet, and desktop
- **Gradient Headers**: Teal gradient header for visual appeal
- **Form Styling**: Clean, modern form inputs with focus states
- **Card Layout**: Dojo information organized in easy-to-read cards
- **Emoji Icons**: Martial arts themed emojis (🥋, ⚔)
- **Hover Effects**: Smooth transitions on cards and buttons
- **Empty States**: Helpful messages when no dojos exist
- **Better Typography**: Clear hierarchy with different font sizes and weights

## Database Relationships

```
Dojo (1) ─────→ (Many) Ninja
  ├─ name
  ├─ city
  ├─ state
  └─ ninjas (reverse relation)

Ninja
  ├─ first_name
  ├─ last_name
  └─ dojo (ForeignKey)
```

**Key Point**: Each Ninja belongs to exactly one Dojo. When a Dojo is deleted, all its Ninjas are automatically deleted (CASCADE delete).

## Code Snippets Reference

### Get all dojos with ninja count
```python
dojos = Dojo.objects.all()
for dojo in dojos:
    print(f"{dojo.name}: {dojo.ninjas.count()} ninjas")
```

### Get all ninjas at a specific dojo
```python
dojo = Dojo.objects.get(id=1)
ninjas = dojo.ninjas.all()
```

### Delete a dojo (cascades to delete ninjas)
```python
dojo = Dojo.objects.get(id=1)
dojo.delete()  # All associated ninjas are automatically deleted
```

## Common Issues & Solutions

### Issue: Form doesn't submit
**Solution**: Make sure you have `{% csrf_token %}` in your form

### Issue: Ninja dropdown is empty
**Solution**: Create at least one dojo first, then the dropdown will populate

### Issue: Changes not appearing
**Solution**: Make sure you ran migrations (`python manage.py migrate`)

### Issue: Page shows "Page not found"
**Solution**: Verify URLs are included in your main `urls.py` with `include()`

## Admin Panel

You can manage dojos and ninjas through Django's admin panel:

1. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

2. Register models in `admin.py`:
   ```python
   from django.contrib import admin
   from .models import Dojo, Ninja

   admin.site.register(Dojo)
   admin.site.register(Ninja)
   ```

3. Access at: `http://localhost:8000/admin/`

## Styling

The app includes modern CSS with:
- Gradient backgrounds (teal and green)
- Smooth transitions and hover effects
- Responsive grid layout
- Focus states for accessibility
- Mobile-first design approach

All styling is embedded in the HTML `<style>` tag for easy deployment.

## Technologies Used

- **Django**: Web framework
- **Python**: Backend language
- **HTML/CSS**: Frontend
- **SQLite**: Default database

## Future Enhancements

Possible features to add:
- User authentication and login
- Ninja skill levels/belts
- Classes/schedules for dojos
- Edit functionality for dojos and ninjas
- Search and filter options
- Ninja deletion without dojo deletion
- Dojo rating system
- Image uploads for dojos

## License

This project is open source and available for educational purposes.

## Support

For questions or issues, refer to:
- Django Documentation: https://docs.djangoproject.com/
- Django Models: https://docs.djangoproject.com/en/stable/topics/db/models/
- Django Views: https://docs.djangoproject.com/en/stable/topics/http/views/

---

**Happy Training! 🥋⚔️**