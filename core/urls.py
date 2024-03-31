from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework.routers import SimpleRouter

from order.views import OrderAPIView
from category.views import CategoryViewSet
from product.views import ProductViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/orders/', OrderAPIView.as_view()),
    path('api/v1/', include(router.urls)),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)