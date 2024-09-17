from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

from apps.general.models import Currency
from apps.general.services import normalize_text


class DiscountService(models.Model):
    """
    Model for discount service types to add service names
    """

    # name information
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    # icon information
    icon = models.ImageField(upload_to='discounts/icons/%Y/%m/%d', blank=True, null=True)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Discount(models.Model):
    """
    Model to add company discounts
    """

    class Currency(models.IntegerChoices):
        UZS = 0, "UZS"
        USD = 1, "USD"

    class Status(models.IntegerChoices):
        CHECKING = 0, "Checking"
        ACCEPTED = 1, "Accepted"
        REJECTED = 2, "Rejected"

    class Type(models.IntegerChoices):
        STANDARD = 0, 'Standard'
        FREE_PRODUCT = 1, 'Free Product'
        QUANTITY_DISCOUNT = 2, 'Quantity Discount'
        SERVICE_DISCOUNT = 3, 'Service Discount'

    # generate custom id
    _id = models.PositiveIntegerField(unique=True, primary_key=True, editable=False)

    # company information
    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE)
    branch = models.ManyToManyField("companies.Branch", blank=True, related_name="discounts")
    category = models.ForeignKey("categories.Category", on_delete=models.PROTECT,
                                 limit_choices_to={'parent__parent__isnull': False})

    # type information
    type = models.PositiveSmallIntegerField(choices=Type.choices)

    # general information
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)

    video = models.FileField(upload_to='discounts/videos/%Y/%m/%d',
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['mp4'])
                             ]
                             )

    available = models.PositiveIntegerField()

    # price information
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.PositiveSmallIntegerField(choices=Currency.choices, default=Currency.UZS)

    # check information
    in_stock = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.CHECKING)

    # information about likes, dislikes and etc.
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    # sale date information
    start_date = models.DateField()
    end_date = models.DateField()

    # service information
    delivery = models.BooleanField(default=False)
    installment = models.BooleanField(default=False) # rasrochka

    # standard discount information
    discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    discount_value_is_percent = models.BooleanField(default=False)

    # free discount information
    min_quantity = models.PositiveSmallIntegerField(blank=True, null=True)
    bonus_quantity = models.PositiveSmallIntegerField(blank=True, null=True)

    # quantity discount information
    bonus_discount_value = models.DecimalField(max_digits=20, decimal_places=1, blank=True, null=True)
    bonus_discount_value_is_percent = models.BooleanField(default=False)

    # discount service information
    service = models.ForeignKey(DiscountService, on_delete=models.SET_NULL, blank=True, null=True)

    # created date and updated date information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['title',]


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== NORMALIZE TEXT ==========

        normalize_text(self)
        super().save(*args, **kwargs)

    def get_old_price_by_currency(self, currency):
        """
        get old price of discount from any currency to uzbek sum.
        """

        if currency != self.currency:
            return Currency.objects.get(currency=currency).in_sum * self.old_price
        return self.old_price

    def clean(self):
        """
        clean() method validates data before saving it to database.
        """

        # ========== CHECK STANDARD DISCOUNT ==========
        if self.type == self.Type.STANDARD:
            if self.discount_value is None:
                raise ValidationError("Discount value is required")

            if self.discount_value_is_percent and self.discount_value < 1 or self.discount_value > 100:
                raise ValidationError("Discount value must be between 1 and 100")

        # ========== CHECK FREE PRODUCT DISCOUNT ==========
        if self.type == self.Type.FREE_PRODUCT:
            if self.min_quantity is None:
                raise ValidationError("Minimum quantity is required")

            if self.bonus_quantity is None:
                raise ValidationError("Bonus quantity is required")

        # ========== CHECK QUANTITY DISCOUNT ==========
        if self.type == self.Type.QUANTITY_DISCOUNT:
            if self.bonus_discount_value is None:
                raise ValidationError("Bonus discount value is required")

        if self.bonus_discount_value_is_percent and self.bonus_discount_value < 1 or self.bonus_discount_value > 100:
            raise ValidationError("Bonus discount value must be between 1 and 100")

        # ========== CHECK SERVICE DISCOUNT ==========
        if self.type == self.Type.SERVICE_DISCOUNT:
            if self.min_quantity is None:
                raise ValidationError("Minimum quantity is required")

            if self.service is None:
                raise ValidationError("Service is required")

        # ========== CHECK SALE DURATION ==========
        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date")

        # ========== CHECK SALE END TIME ==========
        if self.end_date < timezone.now():
            raise ValidationError("End date must be in the future")

    def __str__(self):
        return self.title


class DiscountImage(models.Model):
    """
    Model to add images for discounts
    """

    # discount information
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    # images information
    image = models.ImageField(upload_to='discounts/images/%Y/%m/%d')
    ordering_number = models.PositiveIntegerField()
