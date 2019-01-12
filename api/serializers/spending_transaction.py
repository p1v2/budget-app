from rest_framework import serializers

from transactions.models import SpendingTransaction


class SpendingTransactionSerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=R0903
        model = SpendingTransaction
        fields = '__all__'
