from django.contrib import admin

from .models import Product, ReviewRating
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "slug", "price", "images", "stock", "category", "is_available", "created_date", "modified_date")
    prepopulated_fields = {"slug": ("product_name",)}
   
admin.site.register(Product, ProductAdmin) 



admin.site.register(ReviewRating)
