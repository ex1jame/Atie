from django.contrib import admin

from product.models import Product
from rating.models import Rating


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','quantity','preview')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('product','rating')
