from django.urls import path
from auth_shop.views import login_page, signin_page, auth_page, logout_page

urlpatterns = [
    path('auth', auth_page, name='auth'),
    path('auth/login', login_page, name='login'),
    path('auth/signin', signin_page, name='signin'),
    path('auth/logout', logout_page, name='logout')

]
