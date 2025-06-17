from django.shortcuts import render

def home(request):
    return render(request,'home.html', context={ 'title': 'Home' })

def about(request):
    return render(request,'about.html', context={ 'title': 'About' })

def brand(request):
    return render(request,'brand.html', context={ 'title': 'Brands' })