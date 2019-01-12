"""
Module with the transaction model
"""
from django.db import models
from djmoney.models.fields import MoneyField

from transactions.models import SpendingCategory, Account


class SpendingTransaction(models.Model):
    """
    Represents spending applied to the budget
    """
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(SpendingCategory,
                                 blank=True, null=True, on_delete=models.SET_NULL)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='UAH')
