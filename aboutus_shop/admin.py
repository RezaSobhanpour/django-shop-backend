from django.contrib import admin
from .models import AboutUs, Partners, Link


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'logo']

    def has_add_permission(self, request):
        if AboutUs.objects.exists():
            return False
        return True


class PartnersAdmin(admin.ModelAdmin):
    list_display = ['name', 'Role']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(Link, LinkAdmin)
