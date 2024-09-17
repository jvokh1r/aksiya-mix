from modeltranslation.translator import TranslationOptions, register

from .models import Appeal


@register(Appeal)
class AppealTranslationOptions(TranslationOptions):
    fields = ('message',)