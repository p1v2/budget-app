"""
Module with SpendingCategory model
"""
from django.db import models


class SpendingCategory(models.Model):
    """
    Category for the budget spendings
    """
    name = models.CharField(max_length=100)
