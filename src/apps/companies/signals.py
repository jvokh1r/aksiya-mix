from django.dispatch import receiver
from django.db.models.signals import post_delete

from apps.companies.models import Company
from apps.general.services import delete_object_related_files


@receiver(post_delete, sender=Company)
def delete_company_related_files(instance):
    delete_object_related_files(instance)