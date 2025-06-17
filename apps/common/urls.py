from django.urls import path
from apps.common.views import home, about, brand

urlpatterns=[
    path('',home, name='home'),
    path('',about, name='about'),
    path('',brand, name='brand'),
]