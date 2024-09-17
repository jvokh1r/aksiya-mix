from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

import random

from apps.categories.models import Category
from apps.companies.validators import validate_company_video_size
from apps.general.services import normalize_text
from apps.users.validators import validate_phone_number


class Company(models.Model):
    """
    Model for company
    """

    # generate custom id
    _id = models.CharField(unique=True, editable=False)

    # information about owner
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)

    categories = models.ManyToManyField(Category, blank=True)

    logo = models.ImageField(upload_to='companies/logos/%Y/%m/%d', blank=True, null=True)
    video = models.FileField(
        upload_to='companies/videos/%Y/%m/%d', blank=True, null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['mp4']),
                                 validate_company_video_size
                             ])
    banner = models.ImageField(upload_to='companies/banners/%Y/%m/%d', blank=True, null=True)

    # name information
    name = models.CharField(max_length=150)
    username = models.SlugField(max_length=150, unique=True)

    # general information
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number])
    slogan = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()

    # service information
    delivery = models.BooleanField(default=False)
    installment = models.BooleanField(default=False) # rasrochka

    # information about followers, likes and etc.
    followers = models.CharField(max_length=50, default='0')
    likes = models.CharField(max_length=50, default='0')
    comments = models.CharField(max_length=50, default='0')
    views = models.CharField(max_length=50, default='0')

    # social media information
    web_site = models.URLField(blank=True, null=True)

    # location information
    region = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()

    # balance information
    balance = models.DecimalField(max_digits=30, decimal_places=1, default=0)

    # rating information
    total_rating = models.FloatField(default=0, max_length=5, blank=True, null=True)

    rating1 = models.CharField(default='0')
    rating2 = models.CharField(default='0')
    rating3 = models.CharField(default='0')
    rating4 = models.CharField(default='0')
    rating5 = models.CharField(default='0')

    # created date and updated date information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['name', 'slogan', 'first_name', 'last_name', 'father_name',
                'address']


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== GENERATE CUSTOM ID FOR COMPANY ==========

        custom_id = random.randint(100000, 999999)
        if not Company.objects.filter(_id=custom_id).exists():
            self._id = custom_id

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
        return self.name


class Branch(models.Model):
    """
    Model to add branches for company
    """

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    # name information
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number])

    # service information
    delivery = models.BooleanField(default=False)

    # location information
    region = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()

    # created date information
    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['name', 'address']


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
        return self.name


class CompanyTimeTable(models.Model):
    """
    Model to add timetable for companies or their branches
    """

    class WeekDays(models.IntegerChoices):
        MONDAY = 0, 'Monday'
        TUESDAY = 1, 'Tuesday'
        WEDNESDAY = 2, 'Wednesday'
        THURSDAY = 3, 'Thursday'
        FRIDAY = 4, 'Friday'
        SATURDAY = 5, 'Saturday'
        SUNDAY = 6, 'Sunday'

    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)

    # timetable information
    week_day = models.PositiveSmallIntegerField(choices=WeekDays.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (
            ('company', 'week_day'),
            ('branch', 'week_day'),
        )

    def clean(self):
        """
        clean() method validates data before saving it to database.
        """

        # ========== CHECK IF END TIME GREATER THAN START TIME ==========

        if self.start_time > self.end_time:
            raise ValidationError('Start time must be less than end time')
