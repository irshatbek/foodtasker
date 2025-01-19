from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]