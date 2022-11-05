from django.urls import path
from ucug_forum import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("create_forum/", views.create_forum, name="create_forum"),
    path("forum/<str:title>/", views.forum_feed, name="forum_feed"),
    path("forum/<int:id>/", views.forum_feed),
    path("edit_forum/", views.edit_forum, name="edit_forum"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)