from django.contrib import admin
from django.db.models import Sum
from order.models import Order, OrderItem

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'total_sum')

    def total_sum(self, obj):
        return obj.quantity * obj.product.price

    total_sum.short_description = 'Total Sum'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'status', 'number', 'total_amount')

    def total_amount(self, obj):
        # Используем агрегацию для подсчета суммы всех связанных с данным заказом OrderItem
        total = obj.items.aggregate(total_amount=Sum('product__price'))['total_amount']
        return total if total is not None else 0

    total_amount.short_description = 'Total Amount'
