from django.contrib import admin

from .models import ShoppingBag, ShoppingBagDetail, ShoppingBagShippingDetail


class ShoppingBagAdmin(admin.ModelAdmin):
    list_display = ('total_price', 'shipping_cost', 'user', 'phone', 'city', 'finished')

    def has_add_permission(self, request):
        if ShoppingBag.objects.filter(finished=True).exists():
            return False
        return True


class ShoppingBagDetailAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'color', 'size', 'count', 'shopping_bag')

    def product_name(self, obj):
        return obj.product.title

    product_name.short_description = 'Product Name'


class ShoppingBagShippingDetailAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'phone',
                    'email',
                    'ostan',
                    'city',
                    )


admin.site.register(ShoppingBag, ShoppingBagAdmin)
admin.site.register(ShoppingBagDetail, ShoppingBagDetailAdmin)
admin.site.register(ShoppingBagShippingDetail, ShoppingBagShippingDetailAdmin)
