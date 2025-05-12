from django import forms
from .models import OSTAN_CHOICES


class ShoppingBagForm(forms.Form):
    count = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'tiny-size'}), initial=1, min_value=1)
    color = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'span2'}))
    size = forms.ChoiceField(
        choices=[],
        widget=forms.Select(attrs={'class': 'span2'})
    )


class CheckoutForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'span4'}),
        label='نام',
        required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'span4'}),
        label='نام خانوادگی',
        required=True

    )
    phone = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'span4'}),
        label='شماره تماس',
        required=True

    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'span4'}),
        label='ایمیل',
        required=True

    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'span4'}),
        label='آدرس',
        required=True

    )
    post_code = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'span4'}),
        label='کد پستی',
        required=True

    )
    ostan = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'span4'}),
        label='استان',
        choices=OSTAN_CHOICES,
        required=True

    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'span4'}),
        label='شهر',
        required=True

    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            if user.first_name:
                self.fields['first_name'].initial = user.first_name
            if user.last_name:
                self.fields['last_name'].initial = user.last_name
            if user.email:
                self.fields['email'].initial = user.email
