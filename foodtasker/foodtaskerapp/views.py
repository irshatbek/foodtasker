from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'restaurant/home.html', {})

def meal(request):
    return render(request, 'restaurant/meal.html', {})

def order(request):
    return render(request, 'restaurant/order.html', {})

