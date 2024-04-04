from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

User = get_user_model()


class Review(models.Model):
    """
    Модель, представляющая отзыв пользователя.

    Атрибуты:
        user (ForeignKey): Пользователь, отзывчик.
    """
    title = models.CharField(max_length=150, blank=True, null=True)
    description = RichTextField()
    image = models.ImageField(upload_to="images", default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f'{self.owner}-{self.title}'

    class Meta:
        unique_together = ['owner', 'product']

