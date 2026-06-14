from django.db import models

# Create your models here.
from django.db import models
import re
from datetime import datetime, date


class UserManager(models.Manager):
    """Custom manager for User model with validation"""

    def registration_validator(self, data):
        """Validate registration data"""
        errors = {}

        # First Name validation
        first_name = data.get('first_name', '').strip()
        if not first_name:
            errors['first_name'] = 'First name is required'
        elif len(first_name) < 2:
            errors['first_name'] = 'First name must be at least 2 characters'
        elif not first_name.isalpha():
            errors['first_name'] = 'First name should only contain letters'

        # Last Name validation
        last_name = data.get('last_name', '').strip()
        if not last_name:
            errors['last_name'] = 'Last name is required'
        elif len(last_name) < 2:
            errors['last_name'] = 'Last name must be at least 2 characters'
        elif not last_name.isalpha():
            errors['last_name'] = 'Last name should only contain letters'

        # Email validation
        email = data.get('email', '').strip().lower()
        if not email:
            errors['email'] = 'Email is required'
        elif not self.is_valid_email(email):
            errors['email'] = 'Please enter a valid email address'
        else:
            # Check if email already exists (NINJA BONUS)
            if User.objects.filter(email=email).exists():
                errors['email'] = 'An account with this email already exists'

        # Birthday validation (NINJA BONUS)
        birthday = data.get('birthday')
        if birthday:
            try:
                bday = datetime.strptime(birthday, '%Y-%m-%d').date()
                # Check if date is in the past
                if bday >= date.today():
                    errors['birthday'] = 'Birthday must be in the past'
                # Check age 13+ (SENSEI BONUS)
                age = self.calculate_age(bday)
                if age < 13:
                    errors['birthday'] = 'You must be at least 13 years old'
            except:
                errors['birthday'] = 'Invalid date format'

        # Password validation
        password = data.get('password', '')
        if not password:
            errors['password'] = 'Password is required'
        elif len(password) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        # Confirm password validation
        confirm_pw = data.get('confirm_pw', '')
        if not confirm_pw:
            errors['confirm_pw'] = 'Please confirm your password'
        elif password != confirm_pw:
            errors['confirm_pw'] = 'Passwords do not match'

        return errors

    def login_validator(self, data):
        """Validate login data"""
        errors = {}

        email = data.get('email', '').strip().lower()
        password = data.get('password', '')

        if not email:
            errors['email'] = 'Email is required'
        if not password:
            errors['password'] = 'Password is required'

        if not errors:
            # Try to get user
            try:
                user = User.objects.get(email=email)
                # Check password
                if not user.check_password(password):
                    errors['password'] = 'Invalid email or password'
            except User.DoesNotExist:
                errors['email'] = 'Invalid email or password'

        return errors

    @staticmethod
    def is_valid_email(email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def calculate_age(birthdate):
        """Calculate age from birthdate"""
        today = date.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age

    def create_user(self, data):
        """Create user with validation"""
        errors = self.registration_validator(data)

        if errors:
            return {'success': False, 'errors': errors}

        # Create user
        user = self.create(
            first_name=data.get('first_name', '').strip(),
            last_name=data.get('last_name', '').strip(),
            email=data.get('email', '').strip().lower()
        )

        # Set password (hashed)
        user.set_password(data.get('password'))

        # Set birthday if provided
        if data.get('birthday'):
            user.birthday = data.get('birthday')

        user.save()

        return {'success': True, 'user': user}


class User(models.Model):
    """User model with authentication"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Will store hashed password
    birthday = models.DateField(null=True, blank=True)  # NINJA/SENSEI BONUS
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def set_password(self, raw_password):
        """Hash and set password using Django's built-in method"""
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Check if password matches"""
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def get_full_name(self):
        """Return user's full name"""
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_at']