from django.db import models
from django.utils.translation import ugettext_lazy as _

from djmoney.models.fields import CurrencyField


class ExchangeRate(models.Model):

    class Meta:
        verbose_name = _('Exchange Rate')
        verbose_name_plural = _('Exchange Rates')

    source_currency = CurrencyField()
    target_currency = CurrencyField()
    rate = models.DecimalField(max_digits=12, decimal_places=6)
    datetime = models.DateTimeField()
