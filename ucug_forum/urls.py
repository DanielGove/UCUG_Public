from django.urls import path
from ucug_forum import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("create_forum/", views.create_forum, name="create_forum"),
    path("forum/<str:title>/", views.forum_feed, name="forum_feed"),
    path("forum/<int:id>/", views.forum_feed),
    path("edit_forum/", views.edit_forum, name="edit_forum"),
    path("create_post/", views.create_post, name="create_post"),
    path("edit_post/", views.edit_post, name="edit_post"),
    path("delete_post/", views.delete_post, name="delete_post"),
    path("get_posts/", views.get_posts_view, name="get_posts"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)