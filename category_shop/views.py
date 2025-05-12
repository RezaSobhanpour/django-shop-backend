from django.shortcuts import render
from django.views.generic import ListView

from category_shop.models import Category
from product_shop.models import Product


class ProductByCategoryView(ListView):
    template_name = 'product_shop/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__title=self.kwargs.get('category'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
