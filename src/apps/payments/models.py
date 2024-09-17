from django.db import models

from apps.companies.models import Company

from decimal import Decimal


class Payment(models.Model):
    """
    Model for companies to top up their balance.
    """

    # which company
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    # how many money
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    # created date information
    created_at = models.DateTimeField(auto_now_add=True)

