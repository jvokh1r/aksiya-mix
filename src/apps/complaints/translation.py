from modeltranslation.translator import TranslationOptions, register

from .models import Complaint


@register(Complaint)
class ComplaintTranslationOptions(TranslationOptions):
    fields = ("message",)
