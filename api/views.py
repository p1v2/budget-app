from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:  # pylint: disable=R0903
        model = Transaction
        fields = '__all__'


# Create your views here.
class TransactionViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()  # pylint: disable=no-member
