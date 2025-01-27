# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Restaurant
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login, logout as auth_logout
from foodtaskerapp.views import home
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
# Create your views here.

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace with your target URL name
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/restaurant_log_in.html', {'form': form})

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
    # Log out the user
    auth_logout(request)
    # Redirect to home page (or any desired page)
    return redirect('home')



def accounts(request):
    return render(request, 'restaurant/account.html', {})
