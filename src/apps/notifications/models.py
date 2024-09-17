from django.db import models

from apps.companies.models import Company
from apps.general.services import normalize_text


class NotificationType(models.Model):
    """
    Model to add notification type
    """

    class Type(models.IntegerChoices):
        FOLLOW_TO_COMPANY = 0, 'Follow to company'
        NEW_SALE_IN_COMPANY = 1, 'New sale in company'

    # notification type
    section = models.PositiveSmallIntegerField(choices=Type.choices, unique=True)

    # image of notification
    image = models.ImageField(upload_to="notifications/images/%Y/%m/%d/")

class Notification(models.Model):
    """
    Model to add notification. Which company is going to send which notification to the user.
    """

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    # notification information
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    section = models.PositiveSmallIntegerField(choices=NotificationType.Type.choices)

    # created date information
    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['title', 'content']


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== NORMALIZE TEXT ==========

        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title