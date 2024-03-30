from django.urls import path
from .views import ProductViewSet, ProductDetailViewSet

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve','put':'update',\
                                                       'patch': 'partial_update','delete':'destroy'}))
]
