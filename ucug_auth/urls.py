from django.urls import path
from ucug_auth import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/<str:name>/', views.RequestProfile, name='profile'),
    
    path('profile_description/', views.update_profile_description, name="profile_description"),
    path('profile_image/', views.update_profile_image, name="profile_image"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)