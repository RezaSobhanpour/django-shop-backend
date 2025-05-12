from django.urls import path
from auth_shop.views import login_page, signin_page, auth_page, logout_page

urlpatterns = [
    path('', auth_page, name='auth'),
    path('login', login_page, name='login'),
    path('signin', signin_page, name='signin'),
    path('logout', logout_page, name='logout')

]
