from django.db import models

from apps.general.services import normalize_text


class Advertisement(models.Model):
    """
    Model for advertisement (banner in home page)
    """

    # general information
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    # image information
    image = models.ImageField(upload_to='advertisements/images/%Y/%m/%d')

    # created date information
    created_at = models.DateTimeField(auto_now_add=True)

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

    def __str__(self):
        return self.title
