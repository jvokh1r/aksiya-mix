from modeltranslation.translator import TranslationOptions, register

from .models import Company, Branch


@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = ('last_name', 'first_name', 'father_name',
              'name', 'username', 'slogan',
              'region', 'district', 'address',
              )


@register(Branch)
class BranchTranslationOptions(TranslationOptions):
    fields = ('name', 'region', 'district', 'address')