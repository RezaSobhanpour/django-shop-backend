from django.contrib import admin
from product_shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'title',
        'price',
        'exists'
    ]


admin.site.register(Product,ProductAdmin)
