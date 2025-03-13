from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product_shop.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


class SingleProductView(DetailView):
    template_name = 'product_shop/single_product.html'
    context_object_name = 'product'
    model = Product

