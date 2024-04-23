from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'description', 'price', 'stock', 'is_available', 'category')
    prepopulated_fields = {'slug': ('product_name',)}

# Register your models here.
admin.site.register(Product, ProductAdmin)