from django.contrib.auth import get_user_model
from django.db import models
from product.models import Product
User = get_user_model()


class Favorite(models.Model):
    """
    Модель, представляющая избранное товары.
    """
    owner = models.ForeignKey(User, related_name='favorites',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='favorites',
                                on_delete=models.CASCADE)

    class Meta:
        unique_together = ['owner', 'product']
