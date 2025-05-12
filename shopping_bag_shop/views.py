from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from aboutus_shop.models import AboutUs
from shopping_bag_shop.models import ShoppingBag, ShoppingBagShippingDetail
from .forms import CheckoutForm

User = get_user_model()


@login_required(login_url='login')
def checkout_one_view(request):
    shopping_bag = ShoppingBag.objects.filter(user=request.user, finished=False).first()
    if not shopping_bag:
        return redirect(reverse('home_page'))

    context = {
        'shopping_bag': shopping_bag,
        'shipping_cost': shopping_bag.shipping_cost,
    }
    return render(request, 'shopping_bag_shop/checkout_step_1.html', context)


@login_required(login_url='login')
def checkout_two_view(request):
    aboutus = AboutUs.objects.all().first()
    checkout_form = CheckoutForm(request.POST or None, user=request.user)

    shopping_bag = ShoppingBag.objects.filter(user=request.user, finished=False).first()
    shopping_bag_shipping_detail = ShoppingBagShippingDetail.objects.filter(shopping_bag=shopping_bag).first()

    if request.method == 'POST':
        if checkout_form.is_valid():
            first_name = checkout_form.cleaned_data.get('first_name')
            last_name = checkout_form.cleaned_data.get('last_name')
            phone = checkout_form.cleaned_data.get('phone')
            email = checkout_form.cleaned_data.get('email')
            address = checkout_form.cleaned_data.get('address')
            post_code = checkout_form.cleaned_data.get('post_code')
            ostan = checkout_form.cleaned_data.get('ostan')
            city = checkout_form.cleaned_data.get('city')

            if shopping_bag_shipping_detail:
                ShoppingBagShippingDetail.objects.update_or_create(
                    shopping_bag=shopping_bag,
                    defaults=
                    {
                        'first_name': first_name,
                        'last_name': last_name,
                        'shopping_bag': shopping_bag,
                        'email': email,
                        'address': address,
                        'post_code': post_code,
                        'city': city,
                        'ostan': ostan,
                        'phone': phone
                    }
                )

                url = reverse('checkout_three_view')
                return redirect(url)
    else:
        if shopping_bag_shipping_detail:
            checkout_form = CheckoutForm({
                'first_name': shopping_bag_shipping_detail.first_name,
                'last_name': shopping_bag_shipping_detail.last_name,
                'phone': shopping_bag_shipping_detail.phone,
                'email': shopping_bag_shipping_detail.email,
                'address': shopping_bag_shipping_detail.address,
                'post_code': shopping_bag_shipping_detail.post_code,
                'ostan': shopping_bag_shipping_detail.ostan,
                'city': shopping_bag_shipping_detail.city, }
            )

    context = {
        'aboutus': aboutus,
        'checkout_form': checkout_form
    }
    return render(request, 'shopping_bag_shop/checkout_step_2.html', context)


@login_required(login_url='login')
def checkout_three_view(request):
    about_us = AboutUs.objects.all().first()
    shopping_bag = ShoppingBag.objects.filter(user=request.user, finished=False).first()
    context = {
        'about_us': about_us,
        'shopping_bag': shopping_bag
    }
    return render(request, 'shopping_bag_shop/checkout_step_3.html', context)


@login_required(login_url='login')
def finish_bag(request):
    print("finish_bag view called")
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
    shopping_bag = ShoppingBag.objects.filter(user=request.user, finished=False).first()
    if shopping_bag:
        print("Shopping bag found. Marking as finished.")
        shopping_bag.finished = True
        shopping_bag.save()
    else:
        print('Error: Shopping bag not found!')
    return redirect(reverse('home_page'))
