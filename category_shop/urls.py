from django.urls import path
from category_shop.views import ProductByCategoryView

urlpatterns = [
    path('<str:category>', ProductByCategoryView.as_view(), name='category')
]
