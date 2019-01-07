from django.db import models
from djmoney.models.fields import MoneyField


class Transaction(models.Model):
    name = models.CharField(max_length=200, blank=True)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='UAH')
