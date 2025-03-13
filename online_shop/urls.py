from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from online_shop import settings
from online_shop.views import home_page, header, footer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('header/', header, name='header'),
    path('footer/', footer, name='footer'),

    #
    # apps
    path('', include('auth_shop.urls')),
    path('product/', include('product_shop.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
