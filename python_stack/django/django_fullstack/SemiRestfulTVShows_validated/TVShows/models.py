from django.db import models
from datetime import date


class ShowManager(models.Manager):
    """Custom manager with validation"""

    def create_validator(self, data, exclude_id=None):
        """
        Validate show data and return errors dictionary

        exclude_id: If provided, allows updating show with same title (for edit operations)
        """
        errors = {}

        title = data.get('title', '').strip()
        network = data.get('network', '').strip()
        release_date = data.get('release_date')
        description = data.get('description', '').strip()

        # Title validation
        if not title:
            errors['title'] = 'Title is required'
        elif len(title) < 2:
            errors['title'] = 'Title should be at least 2 characters'
        elif len(title) > 255:
            errors['title'] = 'Title must be less than 255 characters'
        else:
            # SENSEI BONUS: Check if title already exists (excluding current show if editing)
            title_exists = self.filter(title__iexact=title)
            if exclude_id:
                title_exists = title_exists.exclude(id=exclude_id)

            if title_exists.exists():
                errors['title'] = 'A show with this title already exists'

        # Network validation
        if not network:
            errors['network'] = 'Network is required'
        elif len(network) < 3:
            errors['network'] = 'Network should be at least 3 characters'
        elif len(network) > 100:
            errors['network'] = 'Network must be less than 100 characters'

        # Release date validation
        if not release_date:
            errors['release_date'] = 'Release date is required'
        else:
            try:
                # If it's a string, convert to date
                if isinstance(release_date, str):
                    from datetime import datetime
                    release_date = datetime.strptime(release_date, '%Y-%m-%d').date()

                # NINJA BONUS: Release date must be in the past
                if release_date > date.today():
                    errors['release_date'] = 'Release date should be in the past'
            except:
                errors['release_date'] = 'Invalid date format'

        # NINJA BONUS: Description validation (optional but minimum 10 if provided)
        if description:
            if len(description) < 10:
                errors['description'] = 'Description should be at least 10 characters'
            elif len(description) > 1000:
                errors['description'] = 'Description must be less than 1000 characters'

        return errors

    def create_show(self, data):
        """Create show if no validation errors"""
        errors = self.create_validator(data)

        if errors:
            return {'success': False, 'errors': errors, 'show': None}

        title = data.get('title', '').strip()
        network = data.get('network', '').strip()
        release_date = data.get('release_date')
        description = data.get('description', '').strip()

        if isinstance(release_date, str):
            from datetime import datetime
            release_date = datetime.strptime(release_date, '%Y-%m-%d').date()

        show = self.create(
            title=title,
            network=network,
            release_date=release_date,
            description=description if description else None
        )

        return {'success': True, 'errors': {}, 'show': show}

    def update_show(self, show_id, data):
        """Update show with validation"""
        # Pass show_id as exclude_id to allow updating with same title
        errors = self.create_validator(data, exclude_id=show_id)

        if errors:
            return {'success': False, 'errors': errors, 'show': None}

        try:
            show = self.get(id=show_id)
            show.title = data.get('title', '').strip()
            show.network = data.get('network', '').strip()

            release_date = data.get('release_date')
            if isinstance(release_date, str):
                from datetime import datetime
                release_date = datetime.strptime(release_date, '%Y-%m-%d').date()
            show.release_date = release_date

            description = data.get('description', '').strip()
            show.description = description if description else None
            show.save()

            return {'success': True, 'errors': {}, 'show': show}
        except:
            return {'success': False, 'errors': {'general': 'Show not found'}, 'show': None}


class Show(models.Model):
    title = models.CharField(max_length=255, unique=False)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Shows"

    def __str__(self):
        return f"{self.title} ({self.network})"

    def get_formatted_date(self):
        """Return date in readable format"""
        return self.release_date.strftime('%B %d, %Y')