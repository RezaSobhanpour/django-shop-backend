from django.contrib import admin

from auth_shop.forms import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser']


# Register your models here.
admin.site.register(User, UserAdmin)
