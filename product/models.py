from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    preview = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class PostImage(models.Model):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Product, related_name='images',on_delete=models.CASCADE)

