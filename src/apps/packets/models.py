from django.db import models
from django.conf import settings

from decimal import Decimal

class Packet(models.Model):
    """
    Model to add packets for companies to buy them and post their discounts
    """

    # author information
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)

    # how many
    quantity = models.PositiveIntegerField(default=0)

    # how long available
    validate_period = models.DateField()

    # how much cost
    general_sum = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.general_sum
