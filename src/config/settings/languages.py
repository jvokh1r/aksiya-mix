from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field

LANGUAGE_CODE = 'uz'

LANGUAGES = [
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGE = ('ru', 'uz')

MODELTRANSLATION_CUSTOM_FIELDS = (CKEditor5Field,)

MODELTRANSLATION_TRANSLATION_FILES = (
    'advertisements.translation',
    'appeals.translation',
    'categories.translation',
    'companies.translation',
    'complaints.translation',
    'discounts.translation',
    'features.translation',
    'notifications.translation',
    'users.translation',
    'wishlists.translation',
    'wishlists.translation',
)

USE_I18N = True

LOCALE_PATHS = [
    settings.BASE_DIR / 'locale',
]