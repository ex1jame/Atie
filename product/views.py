from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions,response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


from rating.serializers import RatingSerializer
from .models import Product
from . import serializers
from .permissions import IsOwner,IsOwnerOrAdmin


class StandartResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(ModelViewSet):
    """
    API-точка, позволяющая просматривать или редактировать продукты.
    """
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,SearchFilter)
    search_fields = ('title', 'description')
    filterset_fields = ('owner','category')
    pagination_class = StandartResultsSetPagination

    def perform_create(self, serializer):
        """
        Создать новый продукт.
        """
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        """
        Вернуть соответствующий класс сериализатора в зависимости от запрашиваемого действия.
        """
        if self.action == 'list':
            return serializers.ProductListSerializer
        return serializers.ProductSerializer

    def get_permissions(self):
        """
        Вернуть соответствующие разрешения в зависимости от запрашиваемого действия.
        """
        if self.action == 'list':
            return [permissions.AllowAny()]
        elif self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrAdmin()]
        else:
            return [permissions.IsAdminUser()]

    @action(['GET', 'POST', 'DELETE'], detail=True)
    def rating(self, request, pk):
        """
        Получить, создать или удалить рейтинг продукта.
        """
        product = self.get_object()
        user = request.user
        is_rating = product.ratings.filter(owner=user).exists()

        if request.method == 'GET':
            """
            Получить все рейтинги для данного продукта.
            """
            rating = product.ratings.all()
            serializers = RatingSerializer(instance=rating, many=True)
            return response.Response(serializers.data, status=200)

        elif request.method == 'POST':
            """
            Создать новый рейтинг для данного продукта.
            """
            if is_rating:
                return response.Response('Вы уже оценили этот продукт', status=400)
            data = request.data
            serializer = RatingSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=user, product=product)
            return response.Response(serializer.data, status=201)

        else:
            """
            Удалить существующий рейтинг для данного продукта.
            """
            if not is_rating:
                return response.Response('Вы не оценили этот продукт', status=400)
            rating = product.ratings.get(owner=user)
            rating.delete()
            return response.Response('Удалено!', status=204)
