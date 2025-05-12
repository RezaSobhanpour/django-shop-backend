from django.shortcuts import render

from aboutus_shop.models import AboutUs


# Create your views here.
def about_us_page(request):
    about_us = AboutUs.objects.first()
    context = {'about_us': about_us}
    return render(request, 'aboutus_shop/about_us.html', context)
