from django.urls import path
from .views import contact_us_page

urlpatterns = [
    path('', contact_us_page, name='contact_us_page')
]
