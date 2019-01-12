from rest_framework.viewsets import ModelViewSet

from api.serializers.spending_transaction import SpendingTransactionSerializer
from transactions.models import SpendingTransaction


# Create your views here.
class SpendingTransactionViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = SpendingTransactionSerializer
    queryset = SpendingTransaction.objects.all()  # pylint: disable=no-member
