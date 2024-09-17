from django.db import models
from django.conf import settings

class WishList(models.Model):
    """
    Model for users to add favourite discounts to one list.
    """

    # which user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # which discount
    discount = models.ForeignKey('discounts.Discount', on_delete=models.CASCADE)

    def __str__(self):
        return self.pk