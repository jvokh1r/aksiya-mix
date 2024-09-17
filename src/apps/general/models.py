from django.db import models

class Currency(models.Model):
    """
    Model to get currency in sum if we have multiple currencies
    """

    class Currency(models.IntegerChoices):
        UZS = 0, 'UZS'
        USD = 1, 'USD'

    currency = models.PositiveSmallIntegerField(choices=Currency.choices)
    in_sum = models.DecimalField(max_digits=20, decimal_places=2)
