from django.shortcuts import render
from apps.catalog.models import Product

def home(request):
    products=Product.objects.filter(is_featured=True)
    return render(request,'home.html', context={ 'title': 'Home',
                                                'products':products })

def about(request):
    return render(request,'about.html', context={ 'title': 'About' })

def brands(request):
    return render(request,'brands.html', context={ 'title': 'Brands' })