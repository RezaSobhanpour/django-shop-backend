from django.urls import path

from .views import *

urlpatterns = [
    path('checkout-step1', checkout_one_view, name='checkout_one_view'),
    path('checkout-step2', checkout_two_view, name='checkout_two_view'),
    path('checkout-step3', checkout_three_view, name='checkout_three_view'),
    path('finish_bag', finish_bag, name='finish_bag'),

]
