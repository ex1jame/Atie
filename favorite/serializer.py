from rest_framework import serializers
from favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source='product_title',)
    product_preview = serializers.ReadOnlyField(source='product_preview.url')

    class Meta:
        model = Favorite
        fields = ('id', 'product', 'post_title', 'product_title')






