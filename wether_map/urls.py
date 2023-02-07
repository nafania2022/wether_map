from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/<str:sity>', about_sity, name='about_sity'),
]