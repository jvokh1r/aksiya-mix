from modeltranslation.translator import TranslationOptions, register

from apps.discounts.models import Discount


@register(Discount)
class DiscountTranslationOptions(TranslationOptions):
    fields = ('title', 'description')