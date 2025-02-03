from django import forms
from accounts.models import Restaurant

from django.contrib.auth.models import User
from .models import Meal
from accounts.forms import RestaurantForm

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ("Restaurant",)
        