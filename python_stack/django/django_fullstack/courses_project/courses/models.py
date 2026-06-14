from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class DescriptionModel(models.Model):
    """NINJA BONUS: Separate Description class"""
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name_plural = "Descriptions"


class CourseManager(models.Manager):
    """Custom manager with validation"""

    def validate_course(self, data):
        """Validate course data"""
        errors = {}

        name = data.get('name', '').strip()
        description = data.get('description', '').strip()

        # Name validation
        if not name:
            errors['name'] = 'Course name is required'
        elif len(name) <= 5:
            errors['name'] = 'Course name must be more than 5 characters'
        elif len(name) > 200:
            errors['name'] = 'Course name must be less than 200 characters'

        # Description validation
        if not description:
            errors['description'] = 'Description is required'
        elif len(description) <= 15:
            errors['description'] = 'Description must be more than 15 characters'
        elif len(description) > 2000:
            errors['description'] = 'Description must be less than 2000 characters'

        return errors

    def create_course(self, data):
        """Create course with validation"""
        errors = self.validate_course(data)

        if errors:
            return {'success': False, 'errors': errors, 'course': None}

        try:
            name = data.get('name', '').strip()
            description_text = data.get('description', '').strip()

            # Create Description first (NINJA BONUS)
            description_obj = DescriptionModel.objects.create(text=description_text)

            # Create Course with one-to-one relationship
            course = self.create(
                name=name,
                description=description_obj
            )

            return {'success': True, 'errors': {}, 'course': course}
        except Exception as e:
            return {'success': False, 'errors': {'general': str(e)}, 'course': None}


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.OneToOneField(
        DescriptionModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_formatted_date(self):
        """Return date in readable format"""
        return self.created_at.strftime('%b %dst %Y %I:%M%p').replace('st ', ' ').replace('nd ', ' ').replace('rd ',
                                                                                                              ' ').replace(
            'th ', ' ')


class Comment(models.Model):
    """NINJA BONUS: Comments for each course"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment on {self.course.name}"

    def get_formatted_date(self):
        """Return date in readable format"""
        return self.created_at.strftime('%b %dst %Y %I:%M%p').replace('st ', ' ').replace('nd ', ' ').replace('rd ',
                                                                                                              ' ').replace(
            'th ', ' ')