from cProfile import label

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'پست الکترونیک'})
    )
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'رمز عبور'})
    )


class SigninForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'لطفا نام خود را وارد کنید'}),
    )
    last_name = forms.CharField(
        label='نام خانوادگی',
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'لطفا نام خانوادگی خود را وارد کنید'})
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'پست الکترونیک خود را وارد کنید'})
    )
    password = forms.CharField(
        label='زمرعبور',
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'رمز عبور خود را وارد کنید'})
    )
    password2 = forms.CharField(
        label='تایید رمز عبور',
        max_length=150,
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'رمز عبور خود را تایید کنید'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError("با این ایمیل قبلا ثبت نام انجام شده است ")
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            forms.ValidationError('رمز عبور تطابق ندارد')
        else:
            return data
