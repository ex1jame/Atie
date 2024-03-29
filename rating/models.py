from  django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from product.models import Product


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])


    def __str__(self):
        return f'{self.product.name} - {self.rating}'