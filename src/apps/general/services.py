from django.db.models import FileField, ImageField

import requests
import os


def get_usd_price(self):
    url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'

    response = requests.get(url=url)

    return response.json()[0]['Rate']

def normalize_text(obj):
    for i in obj.get_normalize_fields():
        field = getattr(obj, i)
        setattr(obj, i, ' '.join(field.split()))
    return obj

def delete_object_related_files(instance):
    for field in instance.get_fields():
        if isinstance(field, (FileField, ImageField)):
            filename = getattr(instance, field.name, None)
            if filename and os.path.isfile(filename):
                os.remove(filename.path)