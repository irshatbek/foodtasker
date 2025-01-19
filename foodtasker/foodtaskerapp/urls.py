from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('meal', views.meal, name='meal'),
    path('order', views.order, name='order'),
]
