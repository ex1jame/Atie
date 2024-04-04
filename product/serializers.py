from django.db.models import Avg
from rest_framework import serializers

from category.models import Category
from review.models import Review
from review.serializers import ReviewSerializer
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product, который возвращает список продуктов.

    Атрибуты:
        id (int): Уникальный идентификатор продукта.
        owner (User): Пользователь, владеющий продуктом.
        owner_email (str): Электронная почта пользователя, владеющего продуктом.
        title (str): Название продукта.
        price (Decimal): Цена продукта.
        image (str): URL изображения продукта.
        rating_avg (float): Средний рейтинг продукта, рассчитанный на основе поля рейтингов.
    """

    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Product
        fields = ('id', 'owner', 'owner_email', 'title', 'price', 'image')

    def to_representation(self, instance):
        """
        Метод, который переопределяет стандартный метод to_representation модели ModelSerializer.

        Args:
            instance (Product): Экземпляр модели Product, который нужно сериализовать.

        Returns:
            dict: Словарь, содержащий сериализованные данные экземпляра Product.
        """
        repr = super(ProductListSerializer, self).to_representation(instance)
        try:
            repr['rating_avg'] = round(instance.ratings.aggregate(Avg('rating'))["rating__avg"], 1)

        except TypeError:
            repr['rating_avg'] = None
        return repr


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.

    Атрибуты:
        id (int): Уникальный идентификатор продукта.
        owner (User): Пользователь, владеющий продуктом.
        owner_email (str): Электронная почта пользователя, владеющего продуктом.
        title (str): Название продукта.
        price (Decimal): Цена продукта.
        image (str): URL изображения продукта.
        rating_avg (float): Средний рейтинг продукта, рассчитанный на основе поля рейтингов.
    """
    owner_email = serializers.ReadOnlyField(source='owner.email')
    owner = serializers.ReadOnlyField(source='owner.id')
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


    def to_representation(self, instance):
        """
        Метод, который переопределяет стандартный метод to_representation модели ModelSerializer.

        Args:
            instance (Product): Экземпляр модели Product, который нужно сериализовать.

        Returns:
            dict: Словарь, содержащий сериализованные данные экземпляра Product.
        """
        repr = super(ProductSerializer, self).to_representation(instance)
        try:
            repr['rating_avg'] = round(instance.ratings.aggregate(Avg('rating'))["rating__avg"], 1)

        except TypeError:
            repr['rating_avg'] = None

        reviews = Review.objects.filter(product=instance)
        reviews_serializer = ReviewSerializer(instance=reviews, many=True)
        repr['reviews'] = reviews_serializer.data
        return repr




