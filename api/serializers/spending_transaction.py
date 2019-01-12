"""
Module with serializer from Spedning Transaction
"""
from rest_framework import serializers

from transactions.models import SpendingTransaction


class SpendingTransactionSerializer(serializers.ModelSerializer):
    """
    Converts Spending Transaction to its representation in API
    """
    class Meta:  # pylint: disable=R0903, C0111
        model = SpendingTransaction
        fields = '__all__'
