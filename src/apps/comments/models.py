from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from apps.discounts.models import Discount
from apps.general.services import normalize_text


class Comment(models.Model):
    """
    Model for comment to leave comment to discount
    """

    # to which discount
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    # from which user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=13)

    # what message
    message = models.CharField(max_length=255)

    # replies to comment
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True)

    # created date information
    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['message', 'parent']


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== SAVE USER PHONE NUMBER IF USER IS DELETED ==========

        if not self.user:
            self.phone_number = self.user.phone_number
        super().save(*args, **kwargs)

        if self.parent.parent and self.parent.parent.parent:
            raise ValidationError({'parent': 'You can not reply to a children'})

        # ========== NORMALIZE TEXT ==========

        normalize_text(self)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.message


