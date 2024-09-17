from modeltranslation.translator import TranslationOptions, register

from .models import Notification


@register(Notification)
class NotificationTranslationOptions(TranslationOptions):
    fields = ("title", "message")