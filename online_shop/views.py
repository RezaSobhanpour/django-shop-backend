from django.shortcuts import render, redirect
from django.urls import reverse

from aboutus_shop.models import AboutUs
from product_shop.models import Product
from shopping_bag_shop.models import ShoppingBag
from django.contrib.auth import get_user_model
from shopping_bag_shop.models import ShoppingBagDetail

user = get_user_model()


def home_page(request):
    special_products = Product.objects.filter(special=True)[:6]
    top_products = Product.objects.order_by('-sold')[:4]
    new_products = Product.objects.order_by('created_at')[:4]
    context = {
        'special_products': special_products,
        'top_products': top_products,
        'new_products': new_products
    }
    return render(request, 'home_page.html', context)


def header(request):
    if request.method == 'POST':
        item_id = request.POST.get('id')
        item = ShoppingBagDetail.objects.filter(id=item_id).first()
        if item:
            item.delete()

    about_us = AboutUs.objects.first()
    if request.user.is_authenticated:
        shopping_bag = ShoppingBag.objects.filter(user=request.user, finished=False).first()
        if not shopping_bag:
            shopping_bag = None
    else:
        shopping_bag = None
    context = {
        'about_us': about_us,
        'shopping_bag': shopping_bag
    }
    return render(request, 'base/partial/header.html', context)


def footer(request):
    about_us = AboutUs.objects.first()
    context = {
        'about_us': about_us
    }
    return render(request, 'base/partial/footer.html', context)
