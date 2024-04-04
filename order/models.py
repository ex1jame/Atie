from django.db import models
from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver

from product.models import Product

User = get_user_model()

STATUS_CHOICES = (
    ('open', 'Открыт'),
    ('in_progress', 'В Обработке'),
    ('closed', 'Закрыт')
)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} - {self.quantity}'


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through=OrderItem)
    address = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, default='open', max_length=20)
    number = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.user}'
