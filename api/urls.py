from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import *  # pylint: disable=unused-wildcard-import

router = DefaultRouter()
router.register('spends', SpendingTransactionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
