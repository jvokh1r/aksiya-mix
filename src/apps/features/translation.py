from modeltranslation.translator import TranslationOptions, register

from .models import Feature, FeatureValue


@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ("name", "slug")


@register(FeatureValue)
class FeatureValueTranslationOptions(TranslationOptions):
    fields = ("value",)