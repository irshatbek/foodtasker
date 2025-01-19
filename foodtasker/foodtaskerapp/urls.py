from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('account', views.account, name='account'),
    path('meal', views.meal, name='meal'),
    path('order', views.order, name='order'),
]
