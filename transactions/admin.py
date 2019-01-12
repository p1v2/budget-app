"""
Transactions app admin config
"""
from django.contrib import admin

# Register your models here.
from transactions.models import SpendingTransaction
from transactions.models import SpendingCategory

admin.site.register([
        SpendingTransaction,
        SpendingCategory,
])