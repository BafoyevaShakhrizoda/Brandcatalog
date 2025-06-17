from django.urls import path
from apps.catalog.views import categories, products, product

urlpatterns = [
    path('', categories, name='categories'),
    path('', products, name='products'),
    path('', product, name='product'),
]
