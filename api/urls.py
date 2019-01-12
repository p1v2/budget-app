"""
URL configuration for API
"""
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import *  # pylint: disable=unused-wildcard-import, wildcard-import

router = DefaultRouter()  # pylint: disable=C0103
router.register('spends', SpendingTransactionViewSet)

urlpatterns = [  # pylint: disable=C0103
    url(r'^', include(router.urls)),
]
