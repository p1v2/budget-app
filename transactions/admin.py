"""
Transactions app admin config
"""
from django.contrib import admin

# Register your models here.
from transactions.models import Transaction

admin.site.register(Transaction)
