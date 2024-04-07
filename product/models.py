from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from category.models import Category

User = get_user_model()

class Product(models.Model):
    """
    Модель, представляющая продукт для продажи.

    Атрибуты:
        owner (ForeignKey): Пользователь, владеющий продуктом.
        title (CharField): Название продукта.
        description (RichTextField): Описание продукта.
        category (ForeignKey): Категория, к которой относится продукт.
        image (ImageField): Изображение продукта.
        price (DecimalField): Цена продукта.
        stock (CharField): Статус запаса продукта.
        created_at (DateTimeField): Дата создания продукта.
        updated_at (DateTimeField): Дата последнего обновления продукта.

    Методы:
        __str__(self): Возвращает название продукта.
    """
    # product_id = models.AutoField(primary_key=True)
    STATUS_CHOICES = (
        ("in_stock", "В наличии"),
        ("out_of_stock", "Нет в наличии"),
    )

    owner = models.ForeignKey(
        User,
        default="",
        on_delete=models.CASCADE,
        related_name="products",
    )
    title = models.CharField(max_length=150, default=None)
    description = RichTextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    image = models.ImageField(upload_to="images", default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default="")
    stock = models.CharField(
        choices=STATUS_CHOICES, max_length=50, default=""
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
