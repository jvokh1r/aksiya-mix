from django.conf import settings
from django.db import models

from apps.general.services import normalize_text
from apps.users.validators import validate_phone_number


class Complaint(models.Model):
    """
    Model for users to complaint about issues on our platform.
    """

    # user information
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    # to which
    company = models.ForeignKey(to='companies.Company', on_delete=models.SET_NULL, blank=True, null=True)
    discount = models.ForeignKey(to='discounts.Discount', on_delete=models.SET_NULL, blank=True, null=True)

    # user message information
    message = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number], blank=True, null=True)

    # viewed by admin or not
    viewed = models.BooleanField(default=False)

    # created date information
    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['message',]


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== SAVE PHONE NUMBER IF USER IS DELETED ==========
        if not self.phone_number:
            self.phone_number = self.user.phone_number
        super().save(*args, **kwargs)

        # ========== NORMALIZE TEXT ==========

        normalize_text(self)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.phone_number