from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Category(models.Model):
    """
    Модель, представляющая категорию товаров.

    Атрибуты:
        slug (str): Уникальный идентификатор категории.
        name (str): Название категории.
    """
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Category)
def category_pre_save(sender, instance: Category, *args, **kwargs):
    """
    Сигнальный приемник, который генерирует slug для новой категории.

    Args:
        sender (type): Класс модели, который отправил сигнал.
        instance (Category): Экземпляр модели, который отправил сигнал.

    Returns:
        None

    """
    if not instance.slug:
        instance.slug = slugify(instance.name)
