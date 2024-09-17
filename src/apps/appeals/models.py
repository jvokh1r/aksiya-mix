from django.db import models
from django.conf import settings

from apps.general.services import normalize_text


class Appeal(models.Model):
    """
    Model for appeal for users to contact us.
    """

    # user information
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=13)

    # user message
    message = models.CharField(max_length=255)

    # created date information
    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['message', ]


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== SAVE USER PHONE NUMBER IF USER IS DELETED ==========

        if not self.phone_number:
            self.phone_number = self.user.phone_number
        super().save(*args, **kwargs)

        # ========== NORMALIZE TEXT ==========

        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone_number
