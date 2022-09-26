"""UCUG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),

    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<str:name>/', views.RequestProfile, name='profile'),
    
    path('profile_description/', views.update_profile_description, name="profile_description"),
    path('profile_image/', views.update_profile_image, name="profile_image"),

    path('admin/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
