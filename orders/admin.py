from django.contrib import admin
from .models import Payment , Order , OrderProduct
# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ("payment", "user", "product", "quantity", "product_price", "ordered")
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "full_name", "phone", "email", "city", "order_total", "tax", "status", "is_ordered", "ip", "created_at",)
    list_filter = ["status", "is_ordered"]
    search_fields = ["order_number", "first_name", "last_name", "phone", "email"]
    list_per_page = 20
    inlines = [OrderProductInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)


class PyamentAdmin(admin.ModelAdmin):
    '''Admin View for ModelName'''

    list_display = ('user', 'payment_id', 'payment_method', 'amount_paid', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    readonly_fields = ('amount_paid', 'status', 'payment_id')
admin.site.register(Payment, PyamentAdmin)