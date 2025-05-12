from django.urls import path

from product_shop.views import *

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('prosucts-by-order/<sort>', ProductListByOrder.as_view(), name='product_list_by_order'),
    path('prosucts-by-color/<color>', ProductListByColor.as_view(), name='product_list_by_color'),
    path('prosucts-by-size/<size>', ProductListBySize.as_view(), name='product_list_by_size'),
    path('product/<int:pk>', single_product_view, name='single_product'),
    path('search/', SearchProductView.as_view(), name='search_product'),
    path('special-product/', SpecialProductViews.as_view(), name='special-product'),
    path('new-products/', NewProductsView.as_view(), name='new_product'),
    path('most-popular/', MostPopularProducts.as_view(), name='popular_product'),

]
