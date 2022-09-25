from django.contrib import admin
from .models import Forum, Post, Comment, Announcement, User, Session, private_message
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import RegisterForm

admin.site.register(Forum)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Session)
admin.site.register(Announcement)
admin.site.register(private_message)
admin.site.register(User)