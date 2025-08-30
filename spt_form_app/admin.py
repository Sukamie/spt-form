from django.contrib import admin
from django.contrib.auth.models import Group
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _

from . import models

admin.site.unregister(Group)

@admin.register(models.Form01c)
class Form01cAdmin(admin.ModelAdmin):
    list_display = ('nwp', 'tax_year', 'npwp', 'gross_income', 'deduction',
        'non_taxable_income_option', 'non_taxable_income', 'taxable_income',
        'income_tax_payable', 'withheld_income_tax', 'income_tax_option',
        'tax_base', 'final_income_tax_payable','income_exempt_from_tax',
        'yearEnd_total', 'yearEnd_tax_liability')

    exclude = ['income_tax_option_field']
