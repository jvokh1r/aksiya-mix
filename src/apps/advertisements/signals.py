from django.dispatch import receiver
from django.db.models.signals import post_delete

from apps.advertisements.models import Advertisement
from apps.general.services import delete_object_related_files


@receiver(post_delete, sender=Advertisement)
def delete_advertisement_related_files(instance):
    delete_object_related_files(instance)