from django.dispatch import receiver
from django.db.models.signals import post_delete

from apps.categories.models import Category
from apps.general.services import delete_object_related_files


@receiver(post_delete, sender=Category)
def delete_category_related_files(instance):
    delete_object_related_files(instance)