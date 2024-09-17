from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

from apps.categories.models import Category
from apps.discounts.models import Discount
from apps.general.services import normalize_text

from decimal import Decimal



class Feature(models.Model):
    """
    Model to create feature
    """

    # to which category
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    # measure of feature
    measure = models.CharField(max_length=20, blank=True)

    # name information
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        unique_together = (('category', 'slug'),)


    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['measure', 'name', 'slug']


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== NORMALIZE TEXT ==========

        normalize_text(self)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class FeatureValue(models.Model):
    """
    Model to add feature value to feature
    """

    # from which feature
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='children')

    # which value
    value = models.CharField(max_length=100)


    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['value',]


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== NORMALIZE TEXT ==========

        normalize_text(self)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.value


class DiscountFeature(models.Model):
    """
    Model to add features snd feature value to discounts
    """
    # to which discount
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='discount_features')

    # which feature value
    feature_value = models.ForeignKey(FeatureValue, on_delete=models.CASCADE, related_name='product_feature')

    # price by feature value
    price = models.DecimalField(max_digits=20, decimal_places=1, default=Decimal('0.00'), validators=[MinValueValidator(0)])

    ordering_number = models.PositiveSmallIntegerField()

    def clean(self):
        """
        clean() method validates data before saving it to database.
        """

        # ========== CHECK DISCOUNT AND FEATURE VALUE CATEGORY ==========

        if self.discount.category.id != self.feature_value.feature.category.id:
            raise ValidationError('Feature value category does not match discount category')

    def __str__(self):
        return self.price
