"""
URL configuration for foodtasker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from foodtasker import settings
from django.contrib.auth import views as auth_views
from foodtaskerapp import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('foodtaskerapp.urls')),
    # path('restaurant/sign-in/', auth_views.LoginView.as_view(template_name='restaurant/sign_in.html'), name='restaurant-sign-in'),
    # path('restaurant/sign-out/', auth_views.LogoutView.as_view(next_page='/'), name='restaurant-sign-out'),
    # path('restaurant/sign-up/', views.restaurant_sign_up, name='restaurant-sign-up'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)