from django.shortcuts import render

from aboutus_shop.models import AboutUs
from contact_us_shop.forms import ContactUsForm
from contact_us_shop.models import ContactUs
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def contact_us_page(request):
    contact_us_form = ContactUsForm(request.POST or None)
    about_us = AboutUs.objects.all().first()

    if request.method == 'POST':
        if contact_us_form.is_valid():
            name = contact_us_form.cleaned_data.get('name')
            email = contact_us_form.cleaned_data.get('email')
            website = contact_us_form.cleaned_data.get('website')
            message = contact_us_form.cleaned_data.get('message')
            contact_us = ContactUs.objects.create(name=name, email=email, website=website, message=message)
            contact_us.save()
            contact_us_form = ContactUsForm()

    context = {
        'contact_us_form': contact_us_form,
        'about_us': about_us
    }

    return render(request, 'contact_us_shop/contact_us_page.html', context)
