from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=150, label='نام')
    email = forms.EmailField(label='ایمیل')
    website = forms.URLField(label='وب سایت')
    message = forms.CharField(widget=forms.Textarea, label='پیام')
