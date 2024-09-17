from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.general.services import normalize_text

from .validators import validate_phone_number
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom User model to create and manage users.
    """

    class Gender(models.IntegerChoices):
        MAN = 1, 'Man'
        WOMAN = 2, 'Woman'

    USERNAME_FIELD = 'phone_number'
    username = None
    objects = CustomUserManager()

    # name information
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    # contact information
    phone_number = models.CharField(max_length=13, unique=True, validators=[validate_phone_number])
    email = models.EmailField(blank=True, null=True)

    # birth information
    birthdate = models.DateField(blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=Gender.choices, blank=True, null=True)

    # location information
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['first_name', 'last_name', 'address']


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== NORMALIZE TEXT ==========

        normalize_text(self)
        super().save(*args, **kwargs)

    def get_address(self):
        """
        summarize similar fields (region, district, address, latitude, longitude) in one method
        """

        return {
            'region': self.region,
            'district': self.district,
            'address': self.address,
            'longitude': self.longitude,
            'latitude': self.latitude
        }

    def __str__(self):
        return self.phone_number