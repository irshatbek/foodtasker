# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Restaurant
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login
from foodtaskerapp.views import home


# Create your views here.

def log_in(request):
    
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']

        user = auth.authenticate(user=user, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('restaurant_log_in.html')
    return render(request, 'accounts/restaurant_log_in.html')

def register(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        restaurant_form = RestaurantForm(request.POST, request.FILES)
        
        if user_form.is_valid() and restaurant_form.is_valid():
            new_user=User.objects.create_user(**user_form.cleaned_data)
            new_restaurant = restaurant_form.save(commit=False)
            new_restaurant.user = new_user
            new_restaurant.save
            
            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))
            
            return redirect(home)

    else:
        return render(request, 'accounts/restaurant_register.html', {"user_form": user_form, "restaurant_form":restaurant_form})


@login_required(login_url = 'restaurant_log_in.html')
def dashboard(request):
    user_inquiry = Restaurant.objects.order_by('-create_date').filter(user_id=request.user.id)
    # count = Contact.objects.order_by('-create_date').filter(user_id=request.user.id).count()

    data = {
        'inquiries': user_inquiry,
    }
    return render(request, 'accounts/dashboard.html', data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')