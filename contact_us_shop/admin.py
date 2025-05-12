from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')


admin.site.register(ContactUs, ContactUsAdmin)
