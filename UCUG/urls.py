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
from django.urls import path, include
from UCUG import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),

    path('create_announcement/', views.create_announcement, name='create_announcement'),
    path('create_forum/', views.create_forum, name='create_forum'),

    path('', include('ucug_auth.urls')),
]