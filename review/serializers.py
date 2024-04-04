from rest_framework import serializers

from account.models import CustomUser
from product.models import Product
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    product = serializers.ReadOnlyField(source='product.id')

    class Meta:
        model = Review
        fields = ('title', 'description', 'image', 'product', 'owner')
