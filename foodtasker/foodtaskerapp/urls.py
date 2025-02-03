from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('meals/', views.meals, name='meal'),
    path('add_meal', views.add_meal, name='add_meal'),
    path('edit_meal/<str:meal_id>/', views.edit_meal, name='edit_meal'),
    path('order', views.order, name='order'),
    path('reports', views.reports, name='reports'),
]
