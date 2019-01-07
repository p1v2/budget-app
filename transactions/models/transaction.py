from django.db import models
from djmoney.models.fields import MoneyField

from users.models import User


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='UAH')
