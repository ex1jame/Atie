from rest_framework import serializers

from rating.serializers import RatingSerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description','price', 'quantity','rating']

