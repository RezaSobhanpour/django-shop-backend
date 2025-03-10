from django.urls import path
from auth_shop.views import login_page

urlpatterns = [
    path('auth/login', login_page, name='login')
]
