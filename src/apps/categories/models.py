from django.db import models
from django.core.exceptions import ValidationError

from apps.general.services import normalize_text


class Category(models.Model):
    """
    Model for category to use in company model, discount model and etc.
    """

    # name information
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25, unique=True)

    parent = models.ForeignKey(
        to='self',
        on_delete=models.PROTECT,
        related_name='children',
        blank=True, null=True
    )

    # icon information
    icon = models.ImageField(upload_to='categories/icons/%Y/%m/%d', blank=True, null=True)

    # created date information
    created_at = models.DateTimeField(auto_now_add=True)

    def get_normalize_fields(self):
        """
        defines normalizing fields
        """

        return ['name', 'slug', 'parent']


    def save(self, *args, **kwargs):
        """
        save() method is used to save an instance of a model to the database
        """

        # ========== NORMALIZE TEXT ==========

        normalize_text(self)
        super().save(*args, **kwargs)

    def clean(self):
        """
        clean() method validates data before saving it to database.
        """

        # ========== CHECK CATEGORY 3 LEVEL =======

        try:
            if not self.pk and self.parent.parent.parent:
                raise ValidationError({'parent': 'Category must be 3 level degree'})
        except AttributeError:
            pass

        # ========== CHECK IF 1 DEGREE CATEGORY HAVE AN ICON ==========

        if not self.parent and not self.icon:
            raise ValidationError('1-level degree category must have an icon !')

    def __str__(self):
        return self.name