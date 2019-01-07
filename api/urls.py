from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('transactions', TransactionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]