from django.urls import path

from product_shop.views import ProductList, SingleProductView

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', SingleProductView.as_view(), name='single_product')
]
