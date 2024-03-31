from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from category import serializers
from category.models import Category


class CategoryViewSet(ModelViewSet):
    """
    Конечная точка API, которая позволяет просматривать или редактировать категории.
    """
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        """
        Определение разрешений, с которыми должен быть авторизован запрос.
        """
        if self.action in ('retrieve', 'list'):
            """
            Разрешить любому пользователю просматривать или перечислять категории.
            """
            return [permissions.AllowAny()]
        else:
            """
            Разрешить только администраторам создавать, обновлять или удалять категории.
            """
            return [permissions.IsAdminUser()]
