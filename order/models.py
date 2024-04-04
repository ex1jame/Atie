from django.db import models
from django.contrib.auth import get_user_model
<<<<<<< HEAD
# from django.db.models.signals import post_save
# from django.dispatch import receiver
=======
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.tasks import send_notification_task
>>>>>>> d7cbc68e91a9bedef1d491f5d91e435390202569

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
    total_sum = models.DecimalField(blank=True, decimal_places=2, max_digits=9,default=0.0)

    # @property
    # def total_sum(self):
    #     return self.product.aggregate(total_sum=models.Sum('price'))['total_sum']

    def __str__(self):
        return f'{self.id} - {self.user}'
<<<<<<< HEAD
=======

@receiver(post_save, sender = Order)
def order_post_save(sender, instance: Order, *args, **kwargs):
    send_notification_task.delay(
        instance.user.email,
        instance.id,
        instance.total_sum,

    )
>>>>>>> d7cbc68e91a9bedef1d491f5d91e435390202569
