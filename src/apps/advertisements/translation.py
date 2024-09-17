from modeltranslation.translator import TranslationOptions, register

from apps.advertisements.models import Advertisement

@register(Advertisement)
class AdvertisementTranslationOptions(TranslationOptions):
    fields = ('title', 'description')