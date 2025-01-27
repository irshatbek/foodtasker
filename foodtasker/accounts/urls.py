from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('log_in', views.log_in, name='log_in'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('accounts', views.accounts, name='accounts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)