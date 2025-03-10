from django.shortcuts import render


def home_page(request):
    context = {}
    return render(request, 'home_page.html', context)


def header(request):
    return render(request, 'base/partial/header.html')


def footer(request):
    return render(request, 'base/partial/footer.html')
