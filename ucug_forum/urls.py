from django.urls import path
from ucug_forum import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("create_forum/", views.create_forum, name="create_forum"),
    path("forum/<str:title>/", views.forum_feed, name="forum_feed"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)