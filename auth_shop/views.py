from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

from auth_shop.forms import LoginForm, SigninForm
from django.contrib.auth import get_user_model

User = get_user_model()


def auth_page(requset):
    return redirect(reverse('login'))


def login_page(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        authenticate_user = authenticate(request, username=username, password=password)
        if authenticate_user is not None:
            login(request, authenticate_user)
            return redirect(reverse('home_page'))
        else:
            print('Error')
    context = {
        'login_page': "Login Page",
        'login_form': login_form,
    }
    return render(request, 'auth_shop/login.html', context)


def signin_page(request):
    signin_form = SigninForm(request.POST or None)
    if signin_form.is_valid():
        first_name = signin_form.cleaned_data.get('first_name')
        last_name = signin_form.cleaned_data.get('last_name')
        email = signin_form.cleaned_data.get('email')
        password = signin_form.cleaned_data.get('password')
        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_staff = False
        user.save()
        authenticate_user = authenticate(request, username=email, password=password)
        login(request, authenticate_user)
        return redirect(reverse('home_page'))
    context = {
        'signin_form': signin_form
    }
    return render(request, 'auth_shop/signin.html', context)


def logout_page(request):
    logout(request)
    return redirect(reverse('home_page'))
