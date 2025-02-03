from django.shortcuts import render, redirect
from accounts.models import Restaurant
from .forms import MealForm
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Meal

# Create your views here.

def home(request):
    return render(request, 'restaurant/home.html', {})

def meals(request):
    meals = Meal.objects.filter(restaurant = request.user.restaurant).order_by("-id")
    return render(request, 'restaurant/meal.html', {"meals":meals})


def order(request):
    return render(request, 'restaurant/order.html', {})


def reports(request):
    return render(request, 'restaurant/reports.html', {})

def add_meal(request):
    form = MealForm()
    
    if request.method == "POST":
        form = MealForm(request.POST, request.FILES)
        
        if form.is_valid():
            meal = form.save(commit=False)
            meal.restaurant = request.user.restaurant
            meal.save()
            return redirect(meals)
    
    return render(request, 'restaurant/add_meal.html', {"form":form})




def edit_meal(request, meal_id):
    form = MealForm(instance = Meal.objects.get(id = meal_id))
    
    if request.method == "POST":
        form = MealForm(request.POST, request.FILES, instance = Meal.objects.get(id = meal_id))
        
        if form.is_valid():
            form.save()
            return redirect(meals)
    
    return render(request, 'restaurant/edit_meal.html', {"form":form})
