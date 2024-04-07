from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import OrderHistoryViewSet

router = SimpleRouter()
router.register('order-history', OrderHistoryViewSet, basename='order-history')

urlpatterns = [
    # Другие URL-маршруты вашего приложения
    path('', include(router.urls)),
]
